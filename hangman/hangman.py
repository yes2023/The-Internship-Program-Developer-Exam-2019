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
                count = count + 1
                temp.append(answer[x])
        self.guess = ''.join(temp)
        self.remain = len(answer) - count


listedQuiz = []
quizPath = "./Quiz/"
allQuiz = []

def LoadQuiz() :
    fileList = []
    dirs = os.listdir(quizPath)
    for file in dirs :
        if(file.endswith(".json")) :
            #print(file)
            fileList.append(file)
    return fileList

def AlpReplace(text,alp,index) :
    temp = text[:index] + alp + text[index + 1:]
    return temp

def ListQuiz(fileList) :
    if(len(fileList) == 0) :
        print("Need Quiz File\n")
        exit()
        return 0
    else :
        for fileName in fileList :
            file = open(quizPath + fileName,"r")
            Data = json.load(file)
            allQuiz.append(Data['quiz'])
            listedQuiz.append(Data['Category'])
            #print(Category["Category"])
        file.close()
    return 1

def FindCorrectAlp(game,player,alp) :
    length = len(game.answer)
    checkGuess = 0
    for x in range(0,length) :
        if(game.guess[x] == "_" and game.answer[x].casefold() == alp.casefold()) :
            game.guess = AlpReplace(game.guess,game.answer[x],x)
            player.score = player.score + 10
            game.remain = game.remain - 1
            checkGuess = 1
    if(checkGuess == 1) :
        return True
    else :
        player.health = player.health - 1
        return False

def InGame(selectCategory,player) :
    #print(len(allQuiz[selectCategory-1][0]))
    #print(">>" + allQuiz[0][0]['hint'])
    #print(len( allQuiz[selectCategory-1] ))
    #input()
    randomQuiz = random.randint(0,len(allQuiz[selectCategory]) -1 )
    answer = allQuiz[selectCategory][randomQuiz]['answer']
    game = Game(answer)
    win = 0
    wrongGuess = []
    while win == 0 and player.health > 0 :
        os.system('cls')
        print("\nHint: " + allQuiz[selectCategory][randomQuiz]['hint'])
        for x in range(0,len(game.guess)) :
            print(game.guess[x] + " ",end="")
        print("\n" + player.name + " got score " + str(player.score) + ", remaining word guess " + str(player.health))
        if(len(wrongGuess) > 0) :
            print("\nwrong guessed: ")
            for x in wrongGuess :
                print(x + " ",end="")
            print("\n")
        alp = input('Enter Guess Alphabet: ')
        while alp in wrongGuess or alp in game.guess or not alp.isalpha() or len(alp) != 1:
            if len(alp)!=1 or not alp.isalpha():
                alp = input('Enter Only alphabet: ')
            elif alp.isalpha() :
                alp = input('Already guess this alphabet, guess the other: ')
        alp = alp.casefold()
        if not FindCorrectAlp(game,player,alp) :
            wrongGuess.append(alp)
        if(game.remain == 0) :
            win = 1
            print("You Win!!")
        if(game.remain == 0 or player.health == 0) :
            print("Answer is \" ",end="")
            for x in range(0,len(game.guess)) :
                print(game.answer[x],end="")
                if(game.answer[x] != " ") :
                    print(" ",end="")
            print("\"\n")

        
    

def StartGame() :
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
        while True :
            try :
                selectCategory = int(input('Select Category(-1 to Exit Game): '))
                if(selectCategory > len(listedQuiz) or selectCategory == 0) :
                    print("Input Only 1 to " + str(len(listedQuiz)) + " Or -1 to Exit Game")
                    continue
            except ValueError:
                print("Input number only")
                continue
            else :
                break
        if(selectCategory == -1) :
            status = 0
        else :
            InGame(selectCategory - 1,player)
            if player.health == 0 :
                play = input('\nYou lose!! Want to play again?(Y/N): ')
                play=play.casefold()
                while(play != "y" and play != "n") :
                    play = input('Enter only Y/N: ')
                if(play == 'y') :
                    player.reset()
                else :
                    status = 0


StartGame()