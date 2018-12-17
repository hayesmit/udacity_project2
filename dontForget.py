
import json
import random
import string

import httplib2
import requests
from flask import Flask, render_template, request, flash, redirect, jsonify, url_for
from flask import make_response
from flask import session as login_session
from oauth2client.client import FlowExchangeError
from oauth2client.client import flow_from_clientsecrets
from sqlalchemy import create_engine #posibly add ', asc import as well. it was in his code
from sqlalchemy.orm import sessionmaker
from database_setup import Base, User, Event

client_secret_json = 'client_secret.json'
CLIENT_ID = json.loads(
    open(client_secret_json, 'r').read())['web']['client_id']
APPLICATION_NAME = "dontForget"


# from database_setup import Base, user, event
app = Flask(__name__)

engine = create_engine('sqlite:///dontForget.db')
# Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

#route to the main page
@app.route('/')
@app.route('/dontForget')
def allEvents():
    return render_template('dontForget.html')


#Create a token called state
#store token in session for validation
@app.route('/login')
def showLogin():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in xrange(32))
    login_session['state'] = state
    return render_template('login.html', STATE=state)


@app.route('/gconnect', methods=['Post'])
def gconnect():
        if request.args.get('state') != login_session['state']:
            response = make_response(json.dumps('Invalid state parameter.'), 401)
            response.headers['Content-Type'] = 'application/json'
            return response
        # Obtain authorization code
        code = request.data

        try:
            # Upgrade the authorization code into a credentials object
            oauth_flow = flow_from_clientsecrets(client_secret_json, scope='')
            oauth_flow.redirect_uri = 'postmessage'
            credentials = oauth_flow.step2_exchange(code)
        except FlowExchangeError:
            response = make_response(
                json.dumps('Failed to upgrade the authorization code.'), 401)
            response.headers['Content-Type'] = 'application/json'
            return response

        # Check that the access token is valid.
        access_token = credentials.access_token
        print(str(access_token))
        url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
               % access_token)
        h = httplib2.Http()
        result = json.loads(h.request(url, 'GET')[1])
        # If there was an error in the access token info, abort.
        if result.get('error') is not None:
            response = make_response(json.dumps(result.get('error')), 500)
            response.headers['Content-Type'] = 'application/json'
            return response

        # Verify that the access token is used for the intended user.
        gplus_id = credentials.id_token['sub']
        if result['user_id'] != gplus_id:
            response = make_response(
                json.dumps("Token's user ID doesn't match given user ID."), 401)
            response.headers['Content-Type'] = 'application/json'
            return response

        # Verify that the access token is valid for this app.
        if result['issued_to'] != CLIENT_ID:
            response = make_response(
                json.dumps("Token's client ID does not match app's."), 401)
            print
            'Token\'s client ID does not match app\'s.'
            response.headers['Content-Type'] = 'application/json'
            return response

        stored_access_token = login_session.get('access_token')
        stored_gplus_id = login_session.get('gplus_id')
        if stored_access_token is not None and gplus_id == stored_gplus_id:
            response = make_response(json.dumps('Current user is already connected.'),
                                     200)
            response.headers['Content-Type'] = 'application/json'
            return response

        # Store the access token in the session for later use.
        login_session['access_token'] = credentials.access_token
        login_session['gplus_id'] = gplus_id

        # Get user info
        userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
        params = {'access_token': credentials.access_token, 'alt': 'json'}
        answer = requests.get(userinfo_url, params=params)

        data = answer.json()
        print(data)

        login_session['email'] = data['email']

        output = ''
        output += '<h1>Welcome, '
        output += login_session['email']
        output += '!</h1>'
        output += '<img src="'
        output += ' " style = "width: 300px; height: 300px;border-radius: 150px;-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '
        flash("you are now logged in as %s" % login_session['email'])
        print
        "done!"
        return output


@app.route('/gdisconnect')
def gdisconnect():
    access_token = login_session.get('access_token')
    if access_token is None:
        print 'Access Token is None'
        response = make_response(json.dumps('Current user not connected.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    print 'In gdisconnect access token is %s', access_token
    print 'User name is: '
    print login_session['username']
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % login_session['access_token']
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    print 'result is '
    print result
    if result['status'] == '200':
        del login_session['access_token']
        del login_session['gplus_id']
        del login_session['username']
        del login_session['email']
        del login_session['picture']
        response = make_response(json.dumps('Successfully disconnected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response
    else:
        response = make_response(json.dumps('Failed to revoke token for given user.', 400))
        response.headers['Content-Type'] = 'application/json'
        return response


@app.route('/dontForget/<int:user_id>/myEvents')
def myEvents(user_id):
    if 'email' not in login_session:
        return  redirect('/login')
    else:
        return render_template('myEvents.html')


@app.route('/dontForget/<int:user_id>/newEvent')
def newEvent(user_id):
    return render_template('newEvent.html')


@app.route('/dontForget/<int:user_id>/<int:event_id>/editEvent')
def editEvent(user_id, event_id):
    return render_template('editEvent.html')


@app.route('/dontForget/<int:user_id>/<int:items_id>/editItems')
def editItems(user_id, items_id):
    return render_template('editItems.html')


@app.route('/dontForget/<int:user_id>/<int:event_id>/deleteEvent')
def deleteEvent(user_id, event_id):
    return render_template('deleteEvent.html')


@app.route('/dontForget/<int:user_id>/<int:items_id>/deleteItems')
def deleteItems(user_id, items_id):
    return render_template('deleteItems.html')

# checks to see if user already exists
def getUserID(email):
    try:
        user = session.query(User).filter_by(email = email).one()
        return user.id
    except:
        return None

# finds users unique id number
def getUserInfo(user_id):
    user = session.query(User).filter_by(id = user_id).one()
    return user

# creates a new user in our database
def createUser(login_session):
    newUser = User(email = login_session['email'])
    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(email = login_session['email']).one()
    return user.id


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8000)



""""@app.route('/restaurants/<int:restaurant_id>/')
def restaurantMenu(restaurant_id):
    restaurant = session.query(Resataurant).filter_by(id = restaurant_id).one()
    items = session.query(MenuItems).filter_by(restaurant_id = restaurant_id)
    return render_template('menu.html', restaurant = restaurant, items = items)
    i still need to incorperate the restaurant = restaurant and items = items part
    which can be referenced on lesson 3-10"""