# String Basics 2


# Counting characters in the text
print("\n>>>>>> Task1 <<<<<<\n")

text = "Berlin is a world city of culture, politics, media and science."

print(len(str(text)))

print("\n_____________________________________________\n")

# Slicing strings
print("\n>>>>>> Task2 <<<<<<\n")

print(text [0] , text [-1])

print("\n_____________________________________________\n")


# Slicing strings
print("\n>>>>>> Task3 <<<<<<\n")

print(text.upper() [0:3] )

print("\n_____________________________________________\n")


# Count Method
print("\n>>>>>> Task4 <<<<<<\n")

text = "Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital"

print("B appears: " + str(text.count("B")) + " times")


print("\n_____________________________________________\n")

# Slicing strings
print("\n>>>>>> Task5 <<<<<<\n")

text = "Berlin straddles the banks of the Spree, which flows into the Havel (a tributary of the Elbe) in the western borough of Spandau."

print(text [-10::])

print("\n_____________________________________________\n")

# Replace Method
print("\n>>>>>> Task6 <<<<<<\n")

text = "---Python programming---"

print (text.replace("-",""))

print("\n_____________________________________________\n")

# concatenate variables
print("\n>>>>>> Task7 <<<<<<\n")

firstname = "Mary" 
lastname = "Mat"

print("Firstname: " + firstname + "\nLastname: " + lastname)

# F-string Method
#print (f"Firstname: {firstname} \nLastname: {lastname}")
