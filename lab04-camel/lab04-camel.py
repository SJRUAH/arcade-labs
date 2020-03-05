import random

Initial_Text = """Welcome to Camel!
You have stolen a camel to make your way across the great Mobi desert.
The natives want their camel back and are chasing you down! Survive your
desert trek and out run the natives"""


def main():
    print(Initial_Text)
    done = False
    print("What is your choice?")
    while not done:
        print("""A. Drink from your canteen.
            B. Ahead moderate speed.
            C. Ahead full speed.
            D. Stop for the night.
            E. Status check.
            Q. Quit.""")
        Letra =input().upper()
        if Letra == "A":
            pass
        elif Letra == "B":
            pass
        elif Letra == "C":
            pass
        elif Letra == "D":
            pass
        elif Letra == "E":
            pass
        elif Letra == "Q":
            done = True
            print("Turning off the game")



main()
