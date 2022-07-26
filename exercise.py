#Task1

city = "London"

print (city)

#Task2
city1 = "berlin"
population = "3645000"


print (city1.capitalize() +" : "+ population )

#Task3

city2 = "London"
population1 = "9000000"

print ("City:" , city2.isalpha() , "\nPopulation: " ,population1)

#Task4

text = "Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital."


print ("Capital: ", text.find("capital"))

#Task5

text1 = "Berlin straddles the banks of the Spree, which flows into the Havel (a tributary of the Elbe) in the western borough of Spandau"

x = text1.split ()

print (x)


#Task6


text2 = "Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital."

y = text2.replace("capital" , "capital of Germany")

print (y)

#String Basics 2

#Task 1

text3 = "Berlin is a world city of culture, politics, media and science."

z = len ( text3)

print (z)

#Task2

z = slice (0,63,62)

print (text3 [z])

#Task3 

e = slice (0,3)

print(text3.upper()[e])

#Text4

text4 = "Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital"

print (text4.count("B"))

#Test5

text5 = "Berlin straddles the banks of the Spree, which flows into the Havel (a tributary of the Elbe) in the western borough of Spandau."

f = len (text5)
g = slice(-10,f)
print(text5[g])

#test6

text6 ="---Python programming---"

a = text6.replace("-","")

print (a)

#test7

fn = "Mary"
ln = "Mat"

print ("Firstname:",fn + "\nLastname:",ln)

#length() in Python

text7 = "hello world"
text8 = "hello planet"
text9 = ""

length1 = len(text7) 

if length1 %2 == 0:
     print (text7 + " -->" , "even") 
else :
    print  (text7 + " -->" , "odd")
    

    
    