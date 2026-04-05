s=input() #take the input string
vowels='aeiouAEIOU' # a string containing all the vowels
count=0 # a variable to store the count of vowels
for char in s: # iterate through each character in the input string
    if char in vowels: # if the character is a vowel, increment the count
        count+=1
print(count) # print the count of vowels in the input string
