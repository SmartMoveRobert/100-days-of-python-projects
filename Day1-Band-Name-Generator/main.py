#100DaysofPython - Day 1 Project - Band Name Generator

#1. Create a greeting for your program.

user_name = input("Hello, What is your name? ")

#2. Ask the user for the city that they grew up in.

city_name = input("Hi" + " " + user_name + ", what city did you grow up in? ")

#3. Ask the user for the name of a pet.

pet_name = input("Thank you" + " " + user_name +
                 ", secondly, what is the name of your pet? ")

#4. Combine the name of their city and pet and show them their band name.

print(user_name + ",your band name is: " + city_name + " " + pet_name)