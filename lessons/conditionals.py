"""If it is raining, tell me to pack umbrella"""

weather: str = input("what is the weather like? ")

if (weather ==  "rain"):
    print("Pack and umbrella!")
    print("But splash in the puddles, have some fun! ")
else:
    if(weather == "snow"):
        print("pack a jacket")
    print("you don't need and umbrella! ")
print("have a lovely day")
