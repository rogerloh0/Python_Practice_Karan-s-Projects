word = input("Please enter the word: ")
eachAlp = list(word)
vowelCnt = 0
#print(eachAlp)
for i in eachAlp:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        vowelCnt += 1
    elif i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U':
        vowelCnt += 1
print("The word has " + str(vowelCnt) + " vowel(s)")
