# Darren | Lab 4 | Intro to Python

# Ticket 1
ages = [17, 11, 25, 13, 9]

for age in ages:
    if age >= 13:
     print(f"{age} — Access granted ✅")
    else:
        print(f"{age} — Too young ❌")
#PREDICT 11,9 is too young and 13,17,25 is granted
# The variable age holds one age from the "ages list" at a time.

# Ticket 2
# Set up a control variable
keep_checking = "yes"

while keep_checking == "yes":
   # Ask the user to enter an age
   age = int(input("Enter an age: "))

   # Check if age is 13 or older and print the result
   if age >= 13:
      print("Access granted ✅")
   else:
      print("Too young ❌")
   # Ask if they want to check another page
   # Store their answer in keep_checking
   keep_checking = input("Check another page? (Yes/no): ")
#PREDICT if the user types "no", the loop runs once, then stops because keep_checking becomes a "no"
# A while loop is the right choice because you don't know how many times the user wants to check their ages

# Ticket 3
while True:
   # Ask the user: enter an age or type "stop"
   entry = input("Enter an age or type 'stop': ")

   # If they typed "stop", break out of the loop
   if entry == "stop":
      break
   
   # Otherwise check the age and print the result
   age = int(entry)

   if age >= 13:
      print("Access granted ✅")
   else:
      print("Too young ❌")
#PREDICT If I forgot the break statement the loop would never end
# Ticket 2 uses a control variable (keep_checking), while ticket 3 uses while True, creating an endless loop

# Ticket 4
def can_access(age):
   if age >= 13:
      return True
   else:
      return False

ages = [17, 11, 25, 13, 9]

for age in ages:
    if can_access(age):
        print(age, "Access granted ✅")
    else:
        print(age, "Too young ❌")
#PREDICT the age check is inside the can_access() function and the loop calls the function instead of checking if age >= 13 directly
# You only write the age checking code once and if the rule changes later, you only need to update the function instead of changing every if/else statement

# Ticket 5
def can_access(age):
    return age >= 13


def signup_report(ages):
    approved = 0

    print("--- StreamPass Signup Report ---")

    for num, age in enumerate(ages, start=1):
        if can_access(age):
            print(f"Signup #{num} | Age {age} — Access granted ✅")
            approved += 1
        else:
            print(f"Signup #{num} | Age {age} — Too young ❌")

    print(f"Approved: {approved} out of {len(ages)}")

signups = [22, 10, 15, 8, 19, 13]
signup_report(signups)
#PREDICT full output of approved users are: 22,15,19,13 (Approved 4 out of 6)
# I used def signup_report and can_access, parameters, for loops, enumerate(), conditonals (if/else), return values, counter variable, lists, and f-strings
