#Define a function which counts vowels and consonant in a word

def count(word):
    vow = 0
    con = 0
    for i in range(len(word)):
        if word[i] in ['a','e','i','o','u']:
            vow += 1
        else:
            con += 1

    print('vowel in word',vow)
    print('consonant in word',con)

word = input('enter the word')
count(word)