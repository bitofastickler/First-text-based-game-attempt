def scene1():
    import time
    print("""WELCOME TO THE ADVENTURE GAME!
        Let's start the action!

        Egwene wakes up in her bedroom in the middle of the night.
        A loud bang reverberates through the night from outside of the house.
        Now, she has to make a choice.
        Does Egwene stay inside or go outside to investigate the noise?

        Type your choice: Stay or Investigate?
    """)

    c1 = input()
    time.sleep(2)
    ans = 'incorrect'
    while (ans == 'incorrect'):
        if (c1.upper() == "STAY"):               #currently the game ends and shows 'end of chapter 1' screen
            print("\nEgwene decides to stay in the room and go back to sleep. THE END.")
            ans = 'correct'
        elif (c1.upper() == "INVESTIGATE"):
            print("\nEgwene exits the room silently and enters the main hall.")
            ans = 'correct'
            scene2()
        else:
            print("ENTER: Stay or Investigate")
            c1 = input()

def scene2():
    import time
    print("""
        In the hallway, she finds a cute blue teddy bear she has never seen before.
        Strangely, it's sitting up as if purposely placed in her path.
        And there's something about the eyes...

        Type your choice: Pickup or Ignore?
    """)

    c1 = input()
    time.sleep(2)
    ans = 'incorrect'
    while (ans == 'incorrect'):
        if (c1.upper() == "PICKUP"):
            print("""\nThe moment Egwene picks up the bear, it starts TALKING!
            The bear tells her that a monster is in the house and that
            she is in grave danger.
            The monster already has her parents, but she must be brave.""")
            time.sleep(5)
            print("""\nThe bear hands Egwene a small glass vile.
            Inside the vile there is a small amount of
            what appears to be a thin liquid.
            The liquid seems to flow within the vile under its own power
            and its color constantly shifts.
            The mysterious bear tells Egwene the potion
            is the key to defeating the monster.
            As soon as the words are out of his mouth,
            the bear fades into myst.
            Egwene's skin tingles with icey cold
            and she begins to feel as if she is in a dream.""")
            ans = 'correct'
            pickup = "True"
        elif (c1.upper() == "IGNORE"):
            print("""\nEgwene carefully sidesteps around the creepy stuffed
            teddy bear and exits the hallway.""")
            ans = 'correct'
            pickup = "False"
        else:
            print("Enter Pickup or Ignore")
            c1 = input()
    time.sleep(7)
    scene3(pickup)

def scene3(pickup_value):
    import time
    print("""\nUpon entering the dining room,
    a huge horned creature stands leering at Egwene.
    It's eyes are glowing red and it steps toward her,
    menace oozing from it's every muscle.
    """)
    time.sleep(5)
    if(pickup_value == "True"):
        time.sleep(5)
        print("""\nAlmost without thinking, Egwene flings the glass vial
        at the horned monster!""")
        time.sleep(5)
        print("""\nScreaming in pain the monster learches forward and grabs Egwene.
        The world spins around her as she clenches her eys shut.
        When the world stops spinning, she opens her eyes.
        Egwene realizes she is now standing the middle of a glade
        and her home is nowhere to be seen.
        Her arm aches from where the beast grabbed her,
        but the monster is gone.""")

scene1()
print("\n\n")
print("========================END OF CHAPTER 1======================")

