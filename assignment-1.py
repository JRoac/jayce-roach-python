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
age = int(2026) - int(birthyear)
print(f"Hi, {name_1.title()}! You are approximately {age} years old.")
print()

price = float(input("How much is a soda? "))
drinks = float(input("How many sodas did you order? "))
total = price * drinks
print(f"Total:${total:.2f}")
print()

print("=============================")
print("          Receipt            ")
print("Item:              Soda      ")
print("Price:            $",price, "")
print("Quantity:          ",drinks,"")
print("-----------------------------")
print("Total:""          $",total," ")
print("=============================")
print()

hometown = input("Where are you from? ")
hobby = input("What do you do for fun? ")
fact = input("What is a fun fact about yourself? ")
print()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Profile Card:", name_1.title(),)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Hometown:",hometown.title())
print("Hobby:",hobby.title())
print("Fun fact:", fact.capitalize())
print("Age:",age)
