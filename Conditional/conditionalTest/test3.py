# Write a Python program that takes a character as input and checks 
# if it is a vowel or a consonant. If it is a vowel,
# print "Vowel", otherwise print "Consonant".

tex=input("Enter a character ")
vowel=['a','e','i','o','u']
if tex.lower() in vowel:
    print("VOWEL")
else:
    print("CONSONANT")