# string manipulation

# print method and declare a Variable
print("\n>>>>>> Task1 <<<<<<\n")

city = "London"
print(city)

print("_____________________________________________")

# print tow Variable and separate them by a given char
print("\n>>>>>> Task2 <<<<<<\n")

city = "berlin"
population = "3645000"

print (city.capitalize() + population , sep=": ")


print("_____________________________________________")

#  check if the content of the `city` is a text
print("\n>>>>>> Task3 <<<<<<\n")

city = "london"
population = "9000000"

# F-String
print(f"City: {(city.capitalize())} ({city.isalpha()})" )

#print ("City: "+ city, city.isalpha() + "\nPopulation: " + population)

print("_____________________________________________")


# print the index of the location inside the `text` string
print("\n>>>>>> Task4 <<<<<<\n")

text = "Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital."

print("capital: ",text.index("capital"))
print("_____________________________________________")

#Your task is to split the content of the `text` variable and store it in a list.
print("\n>>>>>> Task5 <<<<<<\n")

text = "Berlin straddles the banks of the Spree, which flows into the Havel (a tributary of the Elbe) in the western borough of Spandau."

print(text.split())

print("_____________________________________________")


# Your task is to replace the word `capital` with the phrase  `capital of Germany
print("\n>>>>>> Task6 <<<<<<\n")

text = "Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital."

print(text.replace("capital","capital of Germany"))

print("_____________________________________________")