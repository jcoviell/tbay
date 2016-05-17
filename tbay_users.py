from tbay import Item, User, Bid, session

jp = User()
jp.username = "jpc"
jp.password = "jpjpjp"
session.add(jp)
session.commit()

jenna = User()
jenna.username = "jhershey"
jenna.password = "jhjhjh"
session.add(jenna)
session.commit()

toy = Item()
toy.name = "boat"
toy.user = jp
session.add(toy)
session.commit()

user_jp = session.query(User).filter(User.username == "jpc").first()
print(user_jp)
print(user_jp.username)
print(jp.items)

find_users = session.query(User).all()
print(find_users)