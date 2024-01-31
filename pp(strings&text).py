from email.utils import encode_rfc2231


types_of_people=10 #we've created a variable 
x = f"There are {types_of_people} types of people." #a string inside a string
binary = "binary" #variable
do_not = "don't" #variable
y = f"Those who know {binary} and those who {do_not}" #string inside a string
print(x) #print a string
print(y) #print a string
 
print(f"I said: {x}") #string inside a string
print(f"I also said: '{y}'") #string inside a string
hilarious = False #booleanvariable
joke_evaluation = "Isn't that joke funny?! {}" #variable
print(joke_evaluation.format(hilarious)) #print two strings. format works to insert a string or variable where there are curly braces

w = "This is the left of..." #variable
e = "a string with a right side." #variable
print(w+e) #two strings together

print("Mary had a little lamb.")
print("It's fleece was white as {}".format("snow"))
print("And everywhere it went.")
print("."*10) #prints the dot 10 times

end1 = "C" #use single quotes for short strings
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')#removing the comma causes error in the code. it stops the endline process and prints the next line on the same line
print(end7 + end8 + end9 + end10 + end11 + end12)
print(" ")
formatter = "{} {} {} {}"
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four")) #format replaces the curly braces with the four variables
print(formatter.format(True, False, True, False))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format("Try your", "Own text here", "Maybe a poem", "Or a song about fear"))

print(" ")
days = " Mon Tue Wed Thur Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJune\nJuly\nAug" #\n starts a new line
print("Here are the days", days)
print("Here are the months", months)
print(""" 
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even the four lines of we want, or 5, or 6.
""")#do not put any spaces between """
print(" ")
tabby_cat = "\tI'm tabbed in." #horizontal tab function
backslash_cat = "I'm \\ a \\ cat." #double backlashes allow us to use it
persian_cat = "I'm split\non a line." #\n is for a new line after it
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

