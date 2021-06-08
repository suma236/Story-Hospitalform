while True:
    i = input("Press S to continue and Press X key to exit = ")
    if i == "S" :
        print("1.Moral Story ")
        print("2.Hospital form")
        g=input("enter 1 or 2 = ")
        if g == '1':
            title= input("NEVER MAKE YOUR EGO WIN")
            character1= input("Enter your story character1 = ")
            character2= input("Enter your story character2 = ")
            character3= input("Enter your story character3 = ")
            place= input("Enter the name of the island")


            print(" ",title)
            print("*************")
            print("once upon a time there was an ISLAND called",place)
            print("In that island many people were lived named as ",character1,",",character2,",",character3)
            print("Two lovers were also there",character1,"and",character2)
            print("one bad day heavy floods came all made a boat and they about to leave the island,except the love pair.")
            print("Remaining people ask them to get into the boat but",character1,"wasn't agreed because of his Ego(he is thinking why i have to take their help in his mind).So remaining people left the island leaving the two lovers.")
            print("And the very next day they both died.")
            print("MORAL:IF EGO WINS LOVE DIES")
            print("*********************")



        elif g == '2':
            name = input("Enter your Name =")
            age = input("age = ")
            print(" ", name, "AND ",age)
            c = input("enter your category")
            if (c== "HC") :
                print("Health checkup")
                print("FEE = 500,contact=9696969696")
            else :
                print("DOCTOR consultant")
                print("FEE = 1000,contact=2020202020")


        else:
            print("INVALID INPUT")

    else:
        exit()
