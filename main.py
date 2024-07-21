import operations

def main():
    print("\n")
    print("\t\t\t\t\t\t  SUJITA'S RENTAL SHOP\n")
    print("\t\t\t\t\tAddress : Kalanki | Contact : 9846645224\n")
    print("\t\t\t\t       ",("=")*40)
    print("\t\t\t\t\t      Welcome to the Rental Shop!!")
    print(("=")*120+"\n")
    print("Please choose the option you want to continue.")
    

    loop=True
    while loop==True:
        print("\n")
        print("Press 1 to rent equipment. ")
        print("Press 2 to return equipment. ")
        print("Press 3 to exit the system. ")
        print("\n")
        try:
            user_input = int(input("Choose the operation you want to continue: "))
            print(("-")*120)
            if user_input==1:
                operations.rent()
                print("Thank you for shopping from SUJITA'S RENTAL SHOP.")
            elif user_input==2:
                operations.return_equipment()
                print("Thank you for shopping from SUJITA'S RENTAL SHOP.")
            elif user_input==3:
                print("Exit")
                print("Thank you for shopping from SUJITA'S RENTAL SHOP.")
                break
            else:
                print("Please enter a number from 1 to 3 and try again.")
        except ValueError:
            print("Non-numerical values are invalid! Please enter a number from 1 to 3 and try again.")

main()
