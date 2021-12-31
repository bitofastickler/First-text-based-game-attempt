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
        if (c1.upper() == "STAY"):
            print("Egwene decides to stay in the room and go back to sleep. THE END.")
            ans = 'correct'
        elif(c1.uPPER()=="EVALUATE"):
            print("Egwene exits the room silently and enters the main hall.")
            ans='correct'
            scene2()
        else:
            print("ENTER: Stay or Evaluate")
            c1 = input()
