import random

word_list = ['apple', 'giraffe', 'america', 'college', 'orange']

word = random.choice(word_list)
# print(word)

print("Guess the word!!")

blank_word = '_' * len(word)
print(blank_word)

list_word = list(word) 
list_blank_word = list(blank_word)  

def replace_func(x):
    for i in range(len(list_word)): 
        if list_word[i] == x:  
            list_blank_word[i] = x  
    
    string_blank_word = ''.join(list_blank_word) 
    print(string_blank_word)

tries = 5

while tries > 0:
    guess = input("Guess a letter: ")
    user_guess = guess.lower()

    if user_guess in word:
        replace_func(user_guess)

    elif user_guess not in word:
        print("This letter is not in the word")
        tries -= 1
        print(f"ONLY {tries} ATTEMPTS ARE LEFT!!!")

    if '_' not in list_blank_word: 
        print("Congratulations! You've guessed the word!")
        break

if tries == 0:
    print("Game over\nYou used all of your attempts")
    print(word)
