import random, sys, time

class user_class:
    ''' class contain all info about curent game '''
    def __init__(self):
        self.life = 0
        self.capital = ''
        self.time = 0
        self.count = 0

    def ass_life(self,life): #assing life
        self.life = life

    
    def ass_capital(self, capital):
        self.capital = capital
    
    def ass_time(self, time_of_try):
        self.time = time_of_try


    def ass_count(self): #increse number of try
        self.count += 1

    def losse_life(self): #decrese user life
        self.life = self.life - 1


user = user_class()


def chosse_capitol(capitols):
    ''' random capitol from list and make word with "_" '''
    word = ''
    list_len = len(capitols) - 1
    number = random.randint(0,list_len)
    user.ass_capital(capitols[number].upper())
    for lenght_capitol in range(len(user.capital)):
        if user.capital[lenght_capitol] != ' ':
            word += '_'
        else:
            word += ' '
    return word


def letter_or_word():
    ''' check what user wanna to input letter or word '''
    while True:
        l_or_w = input('You wanna enter letter(l) or word(w): ')
        if l_or_w == 'l':
            break
        elif l_or_w == 'w':
            break   
        else:
            print('Wrong input')
    return l_or_w
       

def letter(word):
    ''' check what letter user input checks whether there is in the word'''
    letter_match = 0
    letter = input('Enter the letter: ')
    letter = letter.upper()
    for position in range(len(user.capital)):
        if user.capital[position] == letter:
            word = switch(position, letter, word)
            letter_match += 1
    if letter_match == 0:
        print('Wrong letter')
        user.losse_life()
    return word


def switch(position, letter, word):
    ''' switch '_' with correct letter'''
    temporary = list(word)
    temporary[position] = letter
    word = ''.join(temporary)
    return word


def enter_word(word):
    ''' check user word '''
    user_word = input('Enter your word: ').upper()
    if user_word == user.capital:
        word = user_word
    else:
        print('Not this time')
        user.losse_life()
        user.losse_life()
    return word


def new_game():
    ''' restart game '''
    restart = input('Wanna play again ? (y to yes, anything else to exit: )')
    if restart == 'y':
        main()
    else:
        sys.exit()


def main():
    user.ass_life(5) # set life to 5
    victory = False
    capitols = []
    file = open('capitals.txt', 'r+')
    capitols = [line.strip() for line in file.readlines()] #take capitols list from file
    file.close()
    word = chosse_capitol(capitols) #random capitol
    time_start = time.time() # take time of start game
    while user.life > 0 or victory == True: # game loop
        user.ass_count() #increse number of attempts
        print('\nYou have %s lifes' % (user.life))
        print('Here it is your word')
        print(word)
        choice = letter_or_word()
        if choice == 'l':
            word = letter(word)
        else:
            word = enter_word(word)
        if '_' not in word: #if user enter all letters one by one  he win 
            victory = True
            break
    time_end = time.time() - time_start # check how long user play
    user.ass_time(time_end) #assing game time to class
    if victory == True:
        print('\nGreat job you win in %d tries and in %d seconds' % (user.count, user.time))
        new_game()
    else:
        print('\nSory you losse maybe next time. The correct word was: %s' % (user.capital))
        new_game()

if __name__ == '__main__': 
    main()