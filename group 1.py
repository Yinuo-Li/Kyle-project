import time

name = input("Enter your name: ")

print(f"\nHello {name}, you find yourself in a cage, with no way to escape.")
print("The air is damp, and the only sound you hear is the slow dripping of water echoing in the distance.")
print("Suddenly, a shadowy figure approaches. His face is hidden under a hood.")
print("He leans in and whispers, 'I can set you free... but you must do something for me in return.'")

print("\nWhat will you do?")
print("1: Accept his offer")
print("2: Refuse and stay in the cage")
print("3: Try to escape on your own")

choice = input("Choose an option (Type 1, 2, or 3): ")

if choice == "1":
    print("\nThe stranger suddenly rips the cage apart with inhuman strength.")
    print("He beckons you to follow, his cold, piercing eyes barely visible under the hood.")

    print("\nWhat will you do?")
    print("1: Follow him")
    print("2: Ask him who he is before following")
    print("3: Run away")

    choice = input("Choose an option (Type 1, 2, or 3): ")

    if choice == "1":
        print("\nYour hands are shaking, but you follow.")
        print("The man leads you through dark tunnels until you finally reach the surface.")
        print("He removes his hood… and to your horror, it’s your long-lost brother—the one you nearly killed years ago.")
        
        print("\nWhat will you do?")
        print("1: Apologize and beg for mercy")
        print("2: Attack him first")
        print("3: Try to reason with him")

        choice = input("Choose an option (Type 1, 2, or 3): ")

        if choice == "1":
            print("\nHe glares at you, unmoved by your words.")
            print("'Mercy?' he spits. 'Did you show ME mercy back then?'")
            print("Before you can respond, everything goes black. The last thing you feel is the cold blade against your throat.")
            print("\n--- BAD ENDING")

        elif choice == "2":
            print("\nYou lunge at him, grabbing a rusty pipe from the ground.")
            print("You swing wildly, but he dodges effortlessly.")
            print("With a smirk, he says, 'You never were a good fighter.'")
            print("He disappears into the shadows, leaving you alone.")
            print("You have escaped… but something tells you he will return.")
            print("\n--- NEUTRAL ENDING ---")

        else:
            print("\nYou raise your hands. 'We don’t have to do this. We’re family.'")
            print("He hesitates. 'Prove it,' he says.")
            print("You recall an old memory from childhood—one only he would remember.")
            print("His grip on the knife loosens, and he drops it.")
            print("'Maybe... I was wrong about you,' he mutters before vanishing into the night.")
            print("\n--- GOOD ENDING---")

    elif choice == "2":
        print("\nThe man pauses for a moment, as if considering whether to answer.")
        print("Finally, he says, 'I am someone you forgot... but I never forgot you.'")
        print("Before you can respond, he vanishes in a cloud of black smoke.")
        print("The cage is gone, but so is he. You are free… but left with more questions than answers.")
        print("\n--- MYSTERY ENDING ---")

    else:
        print("\nYou turn and run as fast as you can.")
        print("But before you can escape, the stranger stretches out his hand.")
        print("Dark tendrils wrap around your body, pulling you back.")
        print("The last thing you hear is his whisper: 'You should have chosen wisely.'")
        print("\n--- BAD ENDING:---")

elif choice == "2":
    print("\nYou refuse the offer and stay in the cage.")
    print("Days pass. Then weeks. No one comes for you.")
    print("The walls of the cage seem to close in, and eventually, darkness takes over.")
    print("\n--- BAD ENDING ---")

elif choice == "3":
    print("\nYou grip the bars, looking for weakness.")
    print("After hours of effort, you manage to loosen one of them and squeeze through.")
    print("You dash into the night, free but with no idea where you are.")
    
    print("\nWhat will you do?")
    print("1: Search for civilization")
    print("2: Hide and observe your surroundings")
    print("3: Go back and try to learn more about the stranger")

    choice = input("Choose an option (Type 1, 2, or 3): ")

    if choice == "1":
        print("\nYou wander for hours until you find an abandoned village.")
        print("The place is eerily silent, as if frozen in time.")
        print("Suddenly, you hear a voice whisper your name…")
        print("\n--- MYSTERY ENDING ---")

    elif choice == "2":
        print("\nYou hide in the shadows and watch as the stranger walks past your empty cage.")
        print("He seems confused, as if expecting you to still be there.")
        print("A wicked smile forms on his lips. 'No matter... I always find them.'")
        print("\nYou realize now—he was never offering freedom.")
        print("\n--- HORROR ENDING ---")

    else:
        print("\nYou decide to return and learn the truth.")
        print("But as you step forward, the ground beneath you crumbles.")
        print("You fall into darkness… and awaken somewhere else entirely.")
        print("\n--- SECRET ENDING---")

else:
    print("\nInvalid choice. The world around you fades into nothingness.")
    print("\n--- ERROR ENDING ---")

print("\nThank you for playing!")
