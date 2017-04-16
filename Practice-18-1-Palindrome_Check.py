word = input("Please enter the word for Palindrome check: ")
revWord = word[::-1]
if word == revWord:
    print("The word is a Palinedrome")
else:
    print("The word is not a Palindrome")
