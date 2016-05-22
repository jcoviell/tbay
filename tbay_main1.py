from tbay import Item, User, Bid, session

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


baseball = Item()
baseball.name='1986 World Series Baseball'
baseball.description='A baseball signed by the 1986 NY Mets'
baseball.user=jp
session.add(baseball)
session.commit()

shirt = Item()
shirt.name='U2 World Tour'
shirt.description='A T-Shirt from the U2 1989 World Tour'
shirt.user=jenna
session.add(shirt)
session.commit()

"""
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
bid1.auction_item=baseball
session.add(bid1)
session.commit()

bid2 = Bid()
bid2.price=85.00
bid2.bidder=jaimie
bid2.auction_item=baseball
session.add(bid2)
session.commit()

bid3 = Bid()
bid3.price=90.00
bid3.bidder=jenna
bid3.auction_item=baseball
session.add(bid3)
session.commit()

bid4 = Bid()
bid4.price=95.00
bid4.bidder=jaimie
bid4.auction_item=baseball
session.add(bid4)
session.commit()

"""