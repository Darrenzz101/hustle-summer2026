# ============================================================
# LAB 7  -  MY OWN ORDERING APP
# Week 7  -  Hack the Hood
# ============================================================
# Name: ______Darren____________
#
# This is YOUR app. YOU write the code.
# Do the tickets IN ORDER from the Lab 7 sheet.
# Run this file after EVERY ticket to check your work.
#
# My store sells: ____Chips + Drinks_____________________________________
# ============================================================


# ============================================================
# DAY 1  -  BUILD YOUR ITEMS
# ============================================================

# TICKET 1: My item blueprint
#   A class for your item. Every item has a name and a price.
#   Write your class below.

class Snack:
    def __init__(self, name, price):
        self.name = name
        self.price = price  

    def set_price(self, new_price):
        if new_price < 0:
            print("Error: Price cannot be negative!")
        else:
            self.price = new_price

# TICKET 3: The price guard
#   Add a set_price method INSIDE your class above.
#   It should say no to a price below zero.
#   BREAK ON PURPOSE: after you build it, try item1.set_price(-5)
#   PREDICT what happens: __It will check if -5 is less than 0, trigger the print statement, and leave the original price unchanged.____________
#   Paste the message you see here: _____Error: Price cannot be negative!_________



# TICKET 4: A second kind of item
#   A new class that copies (inherits from) your first class.
#   Write it below.

class Drink(Snack):
     pass # copies everything from Snack


# TICKET 5: Each item's own action
#   Give each class its own method (deliver, serve, play...).
#   Same method name, different message.
#   EXPLAIN why the same name can do two things: ____Polymorphism allows different classes to have methods with the exact same name__________

class Snack: # Updated base class with serve action
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def set_price(self, new_price):
        if new_price < 0:
            print("Error: Price cannot be negative!")
        else:
            self.price = new_price

    def serve(self):
        print(f"Bagging up your crispy {self.name}!")


class Drink(Snack):
    def serve(self):
        print(f"Pouring your icy cold {self.name}!")

# TICKET 2: Make your real items
#   Make 2 or 3 real items with YOUR OWN names and prices.
#   PREDICT what print(item1.name) shows: __Doritos____________

item1 = Snack("Doritos", 2.99)
item2 = Drink("Gatorade", 1.99)


# ============================================================
# DAY 2  -  BUILD YOUR STORE
# ============================================================

# TICKET 6: My cart
#   A class that holds items in a list and can check out.
#   Write your Cart class below.

class Cart:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def checkout(self):
        print("\n--- Checking Out ---")
        total = 0
        for item in self.items:
            item.serve()
            total += item.price
        print(f"Total: ${total:.2f}")


# TICKET 9: Checkout  (add this method INSIDE your Cart class)
#   Deliver every item and add up the total.



# TICKET 7: My menu and my cart
#   A dictionary that gives each item a number, and one empty cart.

store = { "1": item1,"2": item2}

cart = Cart()

# TICKET 8: Let customers shop
#   Use input() and a loop to keep adding picks until "done".
#   PREDICT what happens when you pick 1: __Doritos will be added to the cart and served__

print("Welcome to the Snack Shack!")
print("Menu:")
print("1: Doritos ($2.99)")
print("2: Gatorade ($1.99)")

while True:
    choice = input("Pick 1, 2, or 'done': ").strip()
    
    if choice.lower() == "done":
        break
    elif choice in store:
        picked_item = store[choice]
        cart.add(picked_item)
        print(f"{picked_item.name} added!")
    else:
        print("Invalid pick, try again.")

# TICKET 10: Test the whole app
#   Run it start to finish. PREDICT the full output first,
#   then check it against what really prints.

# PREDICT full output:
# Pick 1, 2, or 'done': 1
# Doritos added!
# Pick 1, 2, or 'done': 2
# Gatorade added!
# Pick 1, 2, or 'done': done
# --- Checking Out ---
# Bagging up your crispy Doritos!
# Pouring your icy cold Gatorade!
# Total: $4.98

# Triggers checkout method at the end of shopping loop
cart.checkout()

# ============================================================
# CHALLENGE: add a THIRD kind of item, or your own feature!
# ============================================================