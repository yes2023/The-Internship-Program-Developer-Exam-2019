import sys
import os
import json
import random

class Player : 
    def __init__(self, name):
        self.name = name
        self.health = 5
        self.score = 0
    def reset(self):
        self.health = 5
        self.score = 0

class Game :
    def __init__(self, answer):
        temp = []
        count = 0
        self.answer = answer
        for x in range (0,len(answer)) :
            if(answer[x].isalpha()) :
                temp.append("_")
            else :
                count = count + 1       # Count ammout of alphabet that user need to answer
                temp.append(answer[x])
        self.guess = ''.join(temp)      # Convert list to string
        self.remain = len(answer) - count


listedQuiz = []         # use to collect list of quiz
quizPath = "./Quiz/"    # quiz dir
allQuiz = []            # use to collect all quiz

def LoadQuiz() :        # Use to load json quiz file and return list of file
    fileList = []
    dirs = os.listdir(quizPath)
    for file in dirs :
        if(file.endswith(".json")) :
            #print(file)
            fileList.append(file)
    return fileList

def AlpReplace(text,alp,index) :    # Use to replace text in game
    temp = text[:index] + alp + text[index + 1:]
    return temp

def ListQuiz(fileList) :            # Use to get quiz list and quiz from file
    if(len(fileList) == 0) :
        print("Need Quiz File\n")
        exit()
    else :
        for fileName in fileList :
            file = open(quizPath + fileName,"r")
            Data = json.load(file)
            allQuiz.append(Data['quiz'])
            listedQuiz.append(Data['Category'])
            #print(Category["Category"])
        file.close()
    

def FindCorrectAlp(game,player,alp) :   # Use to check answer from user
    length = len(game.answer)
    checkGuess = 0                      # To check if there are correct guess
    for x in range(0,length) :          
        if(game.guess[x] == "_" and game.answer[x].casefold() == alp.casefold()) :      # If there are avarible to guess and true
            game.guess = AlpReplace(game.guess,game.answer[x],x)
            player.score = player.score + 10
            game.remain = game.remain - 1
            checkGuess = 1
    if(checkGuess == 1) :
        return True
    else :                              # If payer guess wrong
        player.health = player.health - 1
        return False

def InGame(selectCategory,player) :     # Use for play the game
    randomQuiz = random.randint(0,len(allQuiz[selectCategory]) -1 )
    answer = allQuiz[selectCategory][randomQuiz]['answer']
    game = Game(answer)
    win = 0
    wrongGuess = []
    while win == 0 and player.health > 0 :  #continue play while player not win and have remain guess
        os.system('cls')
        print("\nHint: " + allQuiz[selectCategory][randomQuiz]['hint'])
        for x in range(0,len(game.guess)) : #loop for print guess word
            print(game.guess[x] + " ",end="")
        print("\n" + player.name + " got score " + str(player.score) + ", remaining word guess " + str(player.health))
        if(len(wrongGuess) > 0) :           #if player have been guess wrong
            print("\nwrong guessed: ")
            for x in wrongGuess :           #print wrong alphabet
                print(x + " ",end="")
            print("\n")
        alp = input('Enter Guess Alphabet: ')   
        while alp in wrongGuess or alp in game.guess or not alp.isalpha() or len(alp) != 1:
            if len(alp)!=1 or not alp.isalpha():        #Wrong format
                alp = input('Enter Only alphabet: ')
            else :                                      #if there are correct format but already guess
                alp = input('Already guess this alphabet, guess the other: ')
        alp = alp.casefold()                            #ignore case sensitive
        if not FindCorrectAlp(game,player,alp) :        #if player guess wrong
            wrongGuess.append(alp)
        if(game.remain == 0) :                          #if player can guess all alphabet
            win = 1
            print("You Win!!")
        if(game.remain == 0 or player.health == 0) :    #if game end
            print("Answer is \" ",end="")
            for x in range(0,len(game.guess)) :
                print(game.answer[x],end="")
                if(game.answer[x] != " ") :
                    print(" ",end="")
            print("\"\n")

        
    

def StartGame() : # Use to start the game(main)
    name = input('Enter Player Name: ')
    player = Player(name)
    status = 1
    listedFile=LoadQuiz()   #load .json quiz file
    ListQuiz(listedFile)   
    while status == 1 :
        print(player.name + " have score " + str(player.score))
        print("\n----Category----")
        count = 1
        for x in listedQuiz :
            print(str(count) + "." + x)
            count = count + 1
        while True :                    #validate player select category
            try :
                selectCategory = int(input('Select Category(-1 to Exit Game): '))
                if(selectCategory > len(listedQuiz) or selectCategory == 0) :
                    print("Input Only 1 to " + str(len(listedQuiz)) + " Or -1 to Exit Game")
                    continue
            except ValueError:          #if player input character
                print("Input number only")
                continue
            else :                      #Correct format
                break
        if(selectCategory == -1) :      #player want to exit
            status = 0
        else :
            InGame(selectCategory - 1,player)           #ingame play
            if player.health == 0 :                     #if player die
                play = input('\nYou lose!! Want to play again?(Y/N): ')
                play=play.casefold()                    #ignore case sensitive
                while(play != "y" and play != "n") :    #while incorrect input
                    play = input('Enter only Y/N: ')
                if(play == 'y') :
                    player.reset()                      #reset health
                else :
                    status = 0                          #exit game


StartGame()