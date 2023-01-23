"""Knock Knock Joke With Conditionals"""

inter_cow: str = input("Do you want an interrupting cow? ")

print("Knock Knock")
if (inter_cow == "yes"):
    print("...Who's there?")
    print("interrupting cow.")
    print("...interrupting cow wh--")
    print("MOO!!!")
else:
    print("Oh... Okay.. :((((")
    if (inter_cow == "you're not funny"):
        print("that hurts my feelings")