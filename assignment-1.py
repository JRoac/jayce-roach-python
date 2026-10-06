from datetime import datetime
name = "Angel"
age = 24
height = 6.4
is_basketballplayer = True

print(name, type(name))
print(age, type(age))
print(height, type(height))
print(is_basketballplayer, type(is_basketballplayer))
print()

name_1 = input("What is your name? ")
birthyear = input("What year were you born? ")
age = int(datetime.now().year ) - int(birthyear)
print(f"Hi, {name_1.title()}! You are approximately {age} years old.")
print()

price = float(input("How much is a soda? "))
drinks = float(input("How many sodas did you order? "))
total = price * drinks
print(f"Total:${total:.2f}")
print()

item = "soda"
soda_price = 2.79
how_many = 3
total = float(soda_price * how_many)
print("=============================")
print("          Receipt            ")
print("Item:            ", item.title()," ")
print("Price:            $",soda_price, "")
print("Quantity:          ",how_many,"")
print("-----------------------------")
print(f"Total:             ${total:.2f}", "" )
print("=============================")
print()

hometown = input("Where are you from? ")
hobby = input("What do you do for fun? ")
fact = input("What is a fun fact about yourself? ")
print()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(f"Profile Card: {name_1.title()}")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(f"Hometown:{hometown.title()}")
print(f"Hobby:{hobby.title()}")
print(f"Fun fact: {fact.capitalize()}")
print(f"Age:{age}")
