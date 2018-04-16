users = {'name': 'John', 'age': 23}
print("My name is {name}, and I'm {age} years old.".format(**users))
print(f"My name is {users['name']}, and I'm {users['age']} years old.")
