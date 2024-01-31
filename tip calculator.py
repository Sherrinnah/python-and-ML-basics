
total_bill=float(input("Enter the total food bill: "))

option1='1. Great service'
option2='2. Good service'
option3='3. Terrible service'
print('Please choose your customer satisfaction rating (1/2/3)','\n', option1, '\n', option2, '\n', option3)

rating = input()

if rating=='1':
    tip=total_bill*0.2
elif rating=='2':
    tip = total_bill*0.15
elif rating=='3':
    tip = total_bill*0
else:
   print("Invalid option")

    

sum=total_bill+tip
print('You will pay:', sum, '\n(Your tip is:',tip,')')