#print("Enter your name:") #or name = input("Enter your name")
#name= input()
#print("Welcome,", name)
#print(int(5/2)) or print(5//2)

#time = input()
#class_time = 5
#if int(time) < class_time:
#   print("It is too early for class")
#elif int(time) > class_time:
#    print(" You're already late for class")
#else:
#    print(" It is exactly class time")

def Factorial(n):
    if (n == 0) or (n == 1):
        return 1
    else:
        return n * Factorial(n-1) 

num = int(input())
print("The factorial of", num, "is", Factorial(num))

