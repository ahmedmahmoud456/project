#Author: Ahmed Mahmoud Ibrahim Mahmoud(ID:20230650)
#get number from user and convert it to decimal or binary or octal or hexadecimal
while True:
    print("\n**numbering system converter**")
    print("A) insert a new number")
    print("B) Exit program")
# if true one of  choices will be done
    choice_menu1 = input("Please select an option: ")

    if choice_menu1 == "A":
       number = input("please insert a number: ")

       print("\n** please select the base you want to convert a number from**")
       print("A) Decimal")
       print("B) Binary")
       print("C) Octal")
       print("D) Hexadecimal")

       from_base = input("please select an option:")

       print("\n** please select the base you want to convert a number from**")
       print("A) Decimal")
       print("B) Binary")
       print("C) Octal")
       print("D) Hexadecimal")

       to_base = input("please select an option: ")

       if from_base == "A":  # choice to number be decimal
           num_decimal = int(number)
       elif from_base == "B" :  # choice to number be binary
           num_decimal = int(number, 2)
       elif from_base == "C" : # choice to number be octal
           num_decimal = int(number, 8)
       elif from_base == "D" : # choice to number be hexadecimal
           num_decimal = int(number, 16)
       else:
           print("please select a valid choice")
           continue

       if to_base == "A" :  # convert to decimal
           result = num_decimal
       elif to_base == "B" :  # convert to binary
           result = bin(num_decimal)[2:]
       elif to_base == "C" :  # convert to octal
           result = oct(num_decimal)[2:]
       elif to_base == "D" :   # convert to hexadecimal
           result = hex(num_decimal)[2:].upper()
       else:
           print("please select a valid choice.")
           continue

       print(f"\nResult: {result}")

    elif choice_menu1 =="B" :
       print("Exiting program.")
       break

    else:
       print("Please select a valid choice.")