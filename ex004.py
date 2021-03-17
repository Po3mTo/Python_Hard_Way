cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

# the quantity of cars is 100 so...
print("There are", cars, "cars available.")
# the number of drivers is 30...
print("There are only", drivers, "drivers available.")
# cars_not_driven = cars - drivers (100 - 30)
print("There will be", cars_not_driven, "empty cars today.")
# carpool_capacity tells us how much free space we have have multiple by cars_driven
print("We can transport", carpool_capacity, "people today.")
# how many passengers we need to transport (90)
print("We have", passengers, "to carpool today.")
# we need to determine the average number of passengerers per (passengers / cars_driven)
print("we need to put about", average_passengers_per_car, "in each car.")
