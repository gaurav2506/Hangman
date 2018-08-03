import random

def get_word():
    words =['Umbrella','pug','dog','food','Harley','Labrador','Voldemort','Dumbledore','Wine','Drink','Husky','woodstock']
           
    return random.choice(words).upper() 


def check (word,guesses,guess):
    guess = guess.upper()
    status = ''
    i = 0
    matches = 0
    for letter in word:
        if letter in guesses:
            status = status + letter
        else:
            status = status + '*'
        if letter == guess:
            matches = matches + 1

def main():
    word = get_word()
    guesses = []
    guessed =False
    print('The word contains',len(word),'letters.')
    while not guessed:
        text = 'Please enter one letter or {} letter word.' .format(len(word))
        guess = input(text)
        guess = guess.upper()
        if guess in guesses:
            print('You already guessed"' + guess + '"')
        elif len(guess) == len(word):
            guesses.append(guess)
            if guess == word:
                guessed = True
            else:
                print ("That is incorrect")
        elif len(guess) == 1:
                guesses.append(guess)
                result = check(word,guesses,guess)
                if result == word:
                    guessed = True
                    
                else:
                    print(result)
        else:
                print('invalid entry.')
                
    print('Yes,the word is',word + '!You got it in',len(guesses),'tries.')
main()


