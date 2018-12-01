from flask import Flask, render_template
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# from database_setup import Base, user, event
app = Flask(__name__)

engine = create_engine('sqlite:///dontForget.db')
# Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
@app.route('/dontForget')
def allEvents():
    return render_template('dontForget.html')


@app.route('/dontForget/<int:user_id>/myEvents')
def myEvents(user_id):
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


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000)



""""@app.route('/restaurants/<int:restaurant_id>/')
def restaurantMenu(restaurant_id):
    restaurant = session.query(Resataurant).filter_by(id = restaurant_id).one()
    items = session.query(MenuItems).filter_by(restaurant_id = restaurant_id)
    return render_template('menu.html', restaurant = restaurant, items = items)
    i still need to incorperate the restaurant = restaurant and items = items part
    which can be referenced on lesson 3-10"""