#name = input("Please enter your name: ")
#print (f"Hello {name}!")
#prompt = "If you tell us who you are we can personalise your messages. \nWhat is your first name? "
#prompt = "If you tell us who you are we can personalise your messages."
#adding a string onto another string
#prompt += "\nWhat is your first name? "
#name = input(prompt)
#print(f"Hello {name.title()}")


#guests = int (input("How many people are in your dinner group?"))
#if guests > 8:
#    print("Sorry, you have to wait for a table.")
#elif guests <= 8:
#    print("Your table is ready!")    


#guess = int(input("Enter any number to check whether it is a multiple of ten.\n NUMBER: "))
#if guess % 10==0:
#    print("This is a multiple of 10!")
#else:
#    print("This is not a multiple of 10!")    


#toppings = ""
#while toppings !=("quit"):
#    toppings= input("Add your pizza toppings.Enter 'quit' to stop.\nTopping: ")
    
#    if toppings != 'quit':
#       print (f"We are adding {toppings} to your pizza\n")



while True:
    age = input("Please enter the age or else 'q'.\nAGE: ")

    if age == "q":
        break  
    elif int (age)<3:
        print("The ticket is free")
    elif int (age)<13:
        print("The ticket is 10$")
    elif int (age)>=13:
        print("The ticket is 15$")
    else:
        print('Invalid input. Try again!')
    