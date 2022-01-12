from main import Parent,Child,session



parent_to_delete=session.query(Parent).filter(Parent.id==1).first()

session.delete(parent_to_delete)
session.commit()


print(f"Parents {session.query(Parent).all()}")

print(f"Children {session.query(Child).all()}")