from sqlalchemy.orm import sessionmaker
from database_setup import Base, User, Event
from sqlalchemy import create_engine

APPLICATION_NAME = "dontForget"


engine = create_engine('sqlite:///dontForget.db')
# Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()



def getid(emailhere):
    emailtogetid = session.query(User).filter_by(email=emailhere).one()
    for x in emailtogetid:
        return x.id

for x in range(7):
    startingusers= User(email=('email'+x))
    session.add(startingusers)
    session.commit()


newevent = Event(name='softball', category='day trip', items= 'water bottle, shoes, t-shirt, shorts, glove, sunglasses, hat, bat', user_id=getid('email1'))
session.add(newevent)
session.commit()


newevent = Event(name='swimming', category='day trip', items= 'water bottle, towel, sunscreen, sunglasses, swim shorts', user_id=getid('email1'))
session.add(newevent)
session.commit()


newevent = Event(name='mushroom hunting', category='day trip', items= 'water bottle, knife, paint brush, basket, boots, weather appropriate clothing', user_id=getid('email1'))
session.add(newevent)
session.commit()


newevent = Event(name='camping', category='overnight', items= 'water bottle, food, tent, sleeping bag, chainsaw, sleeping pad, camp supplies bin, matches or a lighter, head lamp', user_id=getid('email1'))
session.add(newevent)
session.commit()


newevent = Event(name='tropical vacation', category='overnight', items= 'water bottle, backpack, travel snack, snorkel, book, appropriate clothing, sunglasses, phone, id, headphones', user_id=getid('email1'))
session.add(newevent)
session.commit()


newevent = Event(name='snowshoeing', category='day trip', items= 'water bottle, backpack, poles, snowshoes, goggles, gloves, beany, jacket, snacks', user_id=getid('email2'))
session.add(newevent)
session.commit()


newevent = Event(name='backpacking', category='overnight', items= 'water bottle, food, tent, bag, pad, sunglasses, water filter, head lamp', user_id=getid('email2'))
session.add(newevent)
session.commit()


newevent = Event(name='camping', category='overnight', items= 'water bottle, dog food, bowls for dog, snacks, binoculars, tent, sleeping bag and pad, more, more, more', user_id=getid('email2'))
session.add(newevent)
session.commit()


newevent = Event(name='shopping', category='day trip', items= 'list, reusable bags, return items', user_id=getid('email3'))
session.add(newevent)
session.commit()


newevent = Event(name='lasagna', category='recipe', items='fat noodles, 1.5lb ground chuck, 1lb ground italian sausage, 1 onion, 2 cloves garlic, 2 tsp ground oregano, 1 tsp ground basil,1 can diced tomatoes, 1/4 tsp salt and same for pepper, 2 cans tomato sauce, 1 can tomato pase, 1.5 cups cottage cheese, 5oz grated parm, 2 eggs, 16 oz shredded mazzarella', user_id=getid('email1'))
session.add(newevent)
session.commit()


newevent = Event(name='salad dressing', category='recipe', items='.25 cup red wine vinegar, 2tbsp djon mustard, .5 cup olive oil, zest and juice of one lemon, 1 clove garlic, 1 tbsp honey, 1 tsp salt, .25 tsp pepper', user_id=getid('email2'))
session.add(newevent)
session.commit()


newevent = Event(name='apple pie', category='recipe', items='.25 cup white sugar, .5 cup brown sugar, pinch of salt, .25 tsp ground cinnamon, .25 cup water, 15 oz ready to use pie crust', user_id=getid('email4'))
session.add(newevent)
session.commit()


newevent = Event(name='kale beet salad', category='recipe', items= '1 buch kale, 6 beets, .5 tsp dried rosemery, .5 tsp garlic poowder, salt and pepper to tase, olive oil, .25 medium red onion sliced thin, 1-2 tbsp slivered almonds', user_id=getid('email1'))
session.add(newevent)
session.commit()


newevent = Event(name='Dunkle beer', category='recipe', items= '7lbs munich malt, 2 lb pilsner malt, 12oz melanoidin malt, 4 oz carafa special III malt, 1 oz perle hops', user_id=getid('email1'))
session.add(newevent)
session.commit()


newevent = Event(name='hiking', category='day trip', items= 'water bottle, leash, backpack, snacks, sunglasses', user_id=getid('email2'))
session.add(newevent)
session.commit()


newevent = Event(name='hunting', category='overnight', items='gun, boots, camo, tent, knife, bugle, towel, food, water, toiletries, sleeping bag and pad', user_id=getid('email3'))
session.add(newevent)
session.commit()


newevent = Event(name='chicken soup', category='recipe', items= 'chicken, garlic, termaric, carrots, broth, onion ', user_id=getid('email6'))
session.add(newevent)
session.commit()


newevent = Event(name='chocolate chip cookies', category='recipe', items= 'flour, chocolate chips, milk, eggs, sugar', user_id=getid('email6'))
session.add(newevent)
session.commit()


newevent = Event(name='bowling', category='day trip', items= 'bowling balls, shoes, new skin, tape, rag', user_id=getid('email6'))
session.add(newevent)
session.commit()

message = "struggl"


