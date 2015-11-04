from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Shop, Base, MenuItem, User

engine = create_engine('sqlite:///database.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create dummy user
User1 = User(name="Hagrid", email="hxw130430@utdallas",
             picture='https://upload.wikimedia.org/wikipedia/en/1/10/RubeusHagrid.jpg')
session.add(User1)
session.commit()


# Menu for Super Stir Fry
restaurant1 = Shop(user_id=1, name="Apple")

session.add(restaurant1)
session.commit()


menuItem1 = MenuItem(user_id=1, name="TECHO Universal Professional HD Camera Lens Kit for iPhone 6s / 6s Plus / 6 / 5s", 
					 description="0.45x Super Wide Angle Lens + 12.5x Super Macro Lens + 37mm Thread Clip Holder",
                     price="$24.99", course="Camera", restaurant=restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name="Apple MacBook Pro 15.4-Inch Laptop",
                     description="Retina Display and Force Touch - Intel Quad-Core i7 2.8GHz, 1TB Flash Storage, 16GB DDR3 Memory, AMD Radeon R9 M370X Graphics with 2GB Memory (Mid 2015 VERSION) 3 Year AppleCare included", 
                     price="$3,599", course="Laptop", restaurant=restaurant1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1, name="Apple MacBook Pro 13.3", description="nch Laptop 2.4GHz / 16GB DDR3 Memory / 1TB SSHD (Solid State Hybrid) Drive / OS X 10.10 Yosemite / DVD Burner",
                     price="$899.00", course="Laptop", restaurant=restaurant1)
session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user_id=1, name="Microsoft Office Home and Student 2016 for Mac", description="Office 2016 for Mac versions of Word, Excel, PowerPoint, and OneNote",
                     price="$129.98", course="Software", restaurant=restaurant1)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(user_id=1, name="Apple EarPods with Remote and Mic", description="Headphone",
                     price="30.99", course="Headphone", restaurant=restaurant1)
session.add(menuItem5)
session.commit()



restaurant2 = Shop(user_id=1, name="Lenovo")

session.add(restaurant2)
session.commit()


menuItem1 = MenuItem(user_id=1, name="MSI GT70 DOMINATOR DRAGON-1886 17.3-Inch Laptop", 
					 description="Intel Core i7-4810MQ 2.7 GHz Processor 8 GB DDR3L RAM 1 TB 7200 rpm Hard Drive 17.3-Inch Screen; NVIDIA Geforce GTX870M Graphics with 3GB GDDR5 VRAM Windows 8.1; DVD-Super Multi (No Blu-Ray)",
                     price="$7,171.68", course="Laptop", restaurant=restaurant2)

session.add(menuItem1)
session.commit()


menuItem2 = MenuItem(user_id=1, name="Lenovo Headset for PC and Mac", description=" ",
                     price="27.99", course="Headphone", restaurant=restaurant2)
session.add(menuItem2)
session.commit()


print "added menu items!"
