# Darren|Lab 3|Intro to Python

# Ticket 1
username = "i9Darrenn"
print(len(username)) 
#PREDICT #9
# Yes! len() counted every character

# Ticket 2
print(username[0])
print(username[len(username)-1])
#PREDICT i and n
# The last index len(username) is -1 because Python starts counting at 0, so the final character is before the length of the string.

# Ticket 3
username = "i9Darrenn"

welcome = "Welcome to Loop, @" + username + "!"
welcome2 = f"Welcome to Loop, @{username}!"
print(welcome)
print(welcome2)
#PREDICT Yes, both lines will look identical
# f-string is easier than concatenation because I dont have to add the +, instead I add an f and {}

# Ticket 4
# username[0] = "X" # run this, it breaks on purpose
#PREDICT my username would be X9Darrenn
# TypeError: 'str' object does not support item assignment
print(username.upper())
# Immutable means that the string can't be changed

# Ticket 5
feed = ["Can't wait to wake up", "Going thrifting with my friends", "Summer is really boring"]
print(len(feed))
print(feed[0])
#PREDICT 3 prints for the count and the caption that comes first is "Can't wait to wake up"
# I used index 0 because in Python, lists starts counting at 0 not 1

# Ticket 6
feed.append ("Doing Hack the Hood in the middle of summer!")
print(feed)
#PREDICT the index of the fourth post is 3
# Again, Python's indexing starts at 0, so the fourth post is 3. For example, (0,1,2,3)

# Ticket 7
feed.pop(0)
feed.sort()
print(feed)
#PREDICT my first post gets removed and the rest of the order would end up in alphabetical order
# .pop removed my 1st post since its index(0) and it moved my other posts to the left and .sort rearranged my posts in alphabetical order

# Ticket 8
profile = {"username": "i9Darrenn", "followers": 200, "verified": True}
print(profile["followers"])
# profile[0] # run this, it breaks on purpose
#PREDICT follower count is 200 and profile[0] is my whole feed
# Dictonaries use keys instead of numbers because each value is labeled with a name, so you can look up data by definition rather than position

# Ticket 9
profile["followers"] = profile["followers"] + 50
profile["bio"] = "Finishing Hack the Hood and graduating"
print(profile)
print(profile.get("age"))
#PREDICT .get("age") will print nothing because it doesn't exist in the dictionary
# .get() is safer than profile["age"] because it won't crash my program and profile["age"] would cause a KeyError

# Ticket 10
print(f"@{profile['username']} has {profile['followers']} followers and {len(feed)} posts. Top post: {feed[0]}")
#PREDICT @i9Darrenn has 250 followers and 3 posts. Top post: Can't wait to wake up
# I used my dictionary for my profile/followers, list for my feeds/posts, and functions like lens() to count items on my lists and f-string to combine everything into one line of code