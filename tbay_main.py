from tbay import Item, User, Bid, session
from sqlalchemy import desc

#add three users to the database
"""
jp = User(username="jpc", password="jpcjpc")
jenna = User(username="jsh", password="jshjsh")
jaimie = User(username="jec", password="jecjec")
"""

jp = User()
jp.username = "jpc"
jp.password = "jpcjpc"
session.add(jp)
session.commit()

jenna = User()
jenna.username = "jsh"
jenna.password = "jshjsh"
session.add(jenna)
session.commit()

jaimie = User()
jaimie.username = "jec"
jaimie.password = "jecjec"
session.add(jaimie)
session.commit()

#make one user auction a baseball
'''
baseball = Item(name='1986 World Series Baseball', description='A baseball signed by the 1986 NY Mets', start_time='', owner=jp)
'''

baseball = Item()
baseball.name='1986 World Series Baseball'
baseball.description='A baseball signed by the 1986 NY Mets'
baseball.user=jp
session.add(baseball)
session.commit()

#Have each other user place two bids on the baseball
'''
bid1 = Bid(price=75.00, bidder=jenna, auction_item=baseball)
'''

bid1 = Bid()
bid1.price=75.00
bid1.bidder=jenna
bid1.item=baseball
session.add(bid1)
session.commit()

bid2 = Bid()
bid2.price=85.00
bid2.bidder=jaimie
bid2.item=baseball
session.add(bid2)
session.commit()

bid3 = Bid()
bid3.price=90.00
bid3.bidder=jenna
bid3.item=baseball
session.add(bid3)
session.commit()

bid4 = Bid()
bid4.price=95.00
bid4.bidder=jaimie
bid4.item=baseball
session.add(bid4)
session.commit()


item_list = session.query(Item).all()
print(item_list[0].bids)

for bid in item_list[0].bids:
    print(bid.price)

bids = session.query(Bid).filter(Bid.item == item_list[0]).order_by(desc(Bid.price)).all()

for x in bids:
    print(x.price)
    print(x.bidder.username)

print("The winner is: ")
print(bids[0].bidder.username)

"""
printing the price and username properties of the Bid object
ordering bids in descending order, find the highest bid, print the username of 
the highest bidder. 
"""
    