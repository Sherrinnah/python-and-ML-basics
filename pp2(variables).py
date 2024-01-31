cars=100
space_in_a_car =4.0
drivers=30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers/cars_driven

print("There are",cars,"cars available.")
print("There are only",drivers,"drivers available.")
print('There will be',cars_not_driven,"empty cars today.")
print("We can trasnport",carpool_capacity,"people today.")
print("We have",passengers,"to carpool today.")
print("We need to put about",average_passengers_per_car,"in each car.")

print("")
#string variables
my_name = 'Sherry Were'
my_age = 20
my_height = 70
my_weight = 180
eyes = 'Black'
my_teeth = 'White'
my_hair = "Black"

print(f"Let's talk about {my_name}.")
print(f"She's {my_height} inches tall")
print(f"She's {my_weight} pound heavy")
print(f"Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {my_hair} hair")
print(f"His teeth are usually {my_teeth} depending on what she's eaten")

#this line is tricky, try to get it exactly right
total= my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}")