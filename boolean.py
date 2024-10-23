# EXERCISE 1
variable = input('what is your favorite programming?').lower()
if variable == 'python':
    print('YOU LOVE PYTHON!')
else:
    print('no match')
if variable == 'different choice':
    print('different choice')

# EXERCISE 2

grade = int(input("What is your grade 0-100 "))
if grade >= 90:
    print("You have an A")
elif grade >= 80:
    print("You have a B")
elif grade >= 70:
    print("You have a C")
elif grade >= 60:
    print("You have a D")
else:
    print("You have a F")

# EXERCISE 3

username = input("What position are you? ")
logged_in = input("Are you logged in? ")
if username == "Admin" and logged_in == "yes":
    print("Welcome Admin!")
else:
    print("Log in")

# EXERCISE 4

list = input('Give me a number')
list_one = input("give me that same number again")
listid_two = id(list)
listid_three = id(list_one)
if listid_two is listid_three: 
    print("They're the same in memory!")
else: 
    print("They're different!")


print(listid_two)
print(listid_three)