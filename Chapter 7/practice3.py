# Write a function that takes a string and returns the count of vowels and
# consonants separately.

def func(userinput):
    vowels= "aeiouAEIOU"

    Countvowels= 0
    CountConsonants= 0
    for eachchar in userinput:
        if(eachchar.isalpha()):
            if(eachchar in vowels):
                Countvowels+= 1
            else:
                CountConsonants+= 1
    return Countvowels,CountConsonants
vowels, Consonants = func("Laiba Khan")           
print(vowels,Consonants)


# Define a function convert_to_upper(word) that returns the uppercase
# version of the strvbvfdr  
def convert_to_upper(word):
    return word.upper
=
print(convert_to_upper("i am an ideal and powerful women:"))

    