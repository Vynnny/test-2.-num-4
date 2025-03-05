#Adventya type shi

def adventure_game():

    print("Welcome Adventurer!")
    print("You are on the way to a mysterious forest.")
    print("You stand in front of a dark forest. Do you 'enter' or 'turn back'?")
    choice1 = input("Enter your choice: ").lower()

    if choice1 == "enter":
        print("You encounter a mysterious path. Do you go 'left' or 'right'?")
        choice2 = input("Enter your choice: ").lower()
        if choice2 == "left":
            print("You fall into a Goth girls basement and die.")
        else:
            print("You are surrounded by Furries. Do you 'fight' or 'flee'?")
            choice3 = input("Enter your choice: ").lower()
            if choice3 == "fight":
                print("You fight bravely but are overwhelmed and die.")
            else:
                print("You flee into Shrek's swamp. Do you 'explore' or 'climb a tree'?")
                choice4 = input("Enter your choice: ").lower()
                if choice4 == "explore":
                    print("You are eaten by a Shrek.")
                else:
                    print("You climb a tree but fall and break your neck and Shrek eats you.")
    else:
        print("You turn back and live a long, uneventful life for now.")

    print("The end or is it?.")

adventure_game()

#Jose Diego