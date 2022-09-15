# Andrew Janedy Project 1

# declaring and assigning variables
my_birth_year = 1988
current_year = 2022
my_name = "Andrew Janedy"
my_age = current_year - my_birth_year

# Output concatenating assigned variables and string literals
print(f"\n{my_name} will turn {my_age} this year\n")

# Asking user for input
user_birth_year = input("What year were you born?: ")

# Declaring and assigning a variable by converting user input to an integer
user_age = current_year - int(user_birth_year)

# Output concatenating assigned variables and string literals
print(f"\nYou will turn {user_age} this year")

# if/elif statements to output appropriate message depending on user input
if (user_age == my_age):
    print("We are the same age!")
elif (user_age > my_age):
    print(f"You are {user_age - my_age} year(s) older than me")
elif (user_age < my_age):
    print(f"You are {my_age - user_age} year(s) younger than me")

