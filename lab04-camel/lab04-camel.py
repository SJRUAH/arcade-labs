import random

Initial_Text = """Welcome to Camel!
You have stolen a camel to make your way across the great Mobi desert.
The natives want their camel back and are chasing you down! Survive your
desert trek and out run the natives"""


def main():
    thirst = 0
    miles_Travelled = 0
    camel_tiredness = 0
    milles_travelled_by_natives = -20
    Drinks_available = 3
    print(Initial_Text)
    done = False
    print("What is your choice?")
    while not done:
        print("""
A. Drink from your canteen.
B. Ahead moderate speed.
C. Ahead full speed.
D. Stop for the night.
E. Status check.
Q. Quit.""")
        print("What is your choice?")
        Letra =input().upper()
        AvanceNativos = random.randint(7, 14)
        AvanceCamello = random.randint(10, 20)
        AvanceCamelloModerado = random.randint(5,12)
        Cansancio = random.randint(1,3)
        if Letra == "A":
            if Drinks_available <1:
                    print("You dont have any water")
            if Drinks_available >= 1:
                thirst = 0
                Drinks_available -= 1
        elif Letra == "B":
            miles_Travelled += AvanceCamelloModerado
            milles_travelled_by_natives += AvanceNativos
            thirst += 1
            camel_tiredness += 1
        elif Letra == "C":
            miles_Travelled +=  AvanceCamello
            print("Milles travelled:", miles_Travelled)
            thirst += 1
            camel_tiredness += Cansancio
            milles_travelled_by_natives += AvanceNativos
        elif Letra == "D":
            print("The camel is happy and full of energy!")
            camel_tiredness = 0
            milles_travelled_by_natives += AvanceNativos
        elif Letra == "E":
            print("Miles travelled:", miles_Travelled)
            print("Drinks in canteen:", Drinks_available)
            print("The natives are", miles_Travelled - milles_travelled_by_natives, "miles behind you")
        elif Letra == "Q":
            done = True
            print("Turning off the game")



main()
