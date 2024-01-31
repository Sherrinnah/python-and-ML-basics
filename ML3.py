
def give_options(x,y,z):
    print ("a):", x)
    print ("b):", y)
    print ("c):", z)
    
print("Hello!, Welcome to my quiz\n" "Every answer is worth 10 points")
answer = (input("Are you ready to play the game: Yes or No?"))

disc = ("Note: Write the actual answer, NOT the option")
#print (disc)

score = 0
total_questions = 5

if answer.lower() == "yes": #if the previous answer is yes
    print(disc)
    print("1). What is the best programming language?")
    give_options("Python","C++","Java")
    ans = input("My answer is:")
    if ans.lower() == "python": #if answer to previous question given is Python
        score += 1 #or score = score + 1
        print("Yaay! Correct\n")
    else:
        print("Oops! Incorrect\n")
        
    print(disc)
    print("2). Who is the founder of apple")
    give_options("Mark Zuckerburg","Bill Gates","Steve Jobs")
    ans = input("My answer is:")
    if ans.lower() == "steve jobs": #if answer to previous question given is Python
        score += 1 #or score = score + 1
        print("Yaay! Correct\n")
    else:
        print("Oops! Incorrect\n")
        
i=score*10
print("Your score is", i,"/50\n")
if i<=20:
    print("Better luck next time!")
elif i==30 or i==40:
    print("Good trial!")
else:
    print ("Perfect. You are a genius!")