from sunau import AUDIO_FILE_ENCODING_MULAW_8
from unicodedata import name


myString= "This is a string"
print(myString)
print(type(myString))
print(myString + " is of the data type " + str(type(myString)))

firstString= "water"
secondString= "fall"
thirdString= firstString + secondString
print(thirdString)

name= input("What is your name? ")
print(name)

color = input("what is your favorite color? :")
animal = input("what is your favorite animal? :")
print("{}, you like a {} {}!" .format(name,color,animal))