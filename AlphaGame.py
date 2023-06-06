print("Alpha Game")
print("""
Welcome to Alpha Game!

It was a sunny day. I was working at the office and I decided to grab a lunch. When I was on my way to my favorite cafe 
something strange started to happen - people running helter skelter...some are fainting on the street. 

That moment I received a message from Government:

"Dear citizens, we are sorry to inform you that we have been attacked by aliens. Please, stay calm and follow the instructions."
Instructions were simple: Try staying indoors and lock your doors."

Your options are:
1.Take a train back home  2. Fight   3. Run and find the next place to hide"


What option do you choose?
1. Take a train back home
2. Fight alongside the Army
3. Run and find the next place to hide
(Enter 1, 2 or 3)
""")
      
choice1 = int(input("Enter your choice: "))

if choice1 == 1:
    print("""You are checking for the next available train back home. You take the train back home, but unfortunately train crashes and...

    You are dead!
    RIP
          """)
elif choice1 == 2:
    print("""You come onboard and join forces with Army to fight the enemy. Later in the day you die in combat.

    But you die as a hero!""")
elif choice1 == 3:
    print("""You gotta save your life somehow and decide where to hide:
    1. Hide in the church
    2. Hide in the school
    3. Hide in the hospital
          """)
    choice2 = int(input("Where you want to hide: your choice: "))
    if choice2 == 1:
        print("""You thought you are safe coz you are hiding in the church. But the church is getting attacked by aliens.
        And Oops....
        You are dead!!!""")
    elif choice2 == 2:
        print("""You are hiding in the school. You gotta decide where in school to hide:
        1. Hide in the classroom
        2. Hide in the gym
        3. Hide in the library
        """)
        
        choice3 = int(input("Enter your choice: "))
        if choice3 == 1:
            print("You hide in the classroom which is way out visible, and you are dead.")
        elif choice3 == 2:
            print("You are dead. There were aliens rampaging the gym.")
        elif choice3 == 3:
            print("Library is the last place where aliens will come looking coz they don't know what a book is and what reading means!!! congrats you saved your life for now! .") 
    else:
        print("You are hiding in the hospital. There are so many people there, its chaotic. You are dead, because noise attracts the aliens.") 
    
else:
    print("You are dead. You didn't get to choose any of the options.")