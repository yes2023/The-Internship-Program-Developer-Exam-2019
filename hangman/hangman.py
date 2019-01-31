import sys
import os
import json
import random

class Player :
    def __init__(self, name):
        self.name = name
        self.health = 10
        self.score = 0
    def reset(self):
        self.health = 10
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
quiz = []
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
            quiz.clear()
            file = open(quizPath + fileName,"r")
            Data = json.load(file)
            quiz.append(Data['quiz'])
            allQuiz.append(quiz)
            listedQuiz.append(Data['Category'])
            #print(Category["Category"])
        file.close()
    return 1

def FindCorrectAlp(game,player,alp) :
    length = len(game.answer)
    checkGuess = 0
    for x in range(0,length) :
        if(game.guess[x] == "_" and game.answer[x] == alp) :
            game.guess = AlpReplace(game.guess,alp,x)
            player.score = player.score + 10
            game.remain = game.remain - 1
            checkGuess = 1
    if(checkGuess == 1) :
        return True
    else :
        player.health = player.health - 1
        return False

def InGame(selectCategory,player) :
    randomQuiz = random.randint(0,len(allQuiz[selectCategory-1][0])) -1 
    print("Hint: " + allQuiz[selectCategory-1][0][randomQuiz]['hint'])
    answer = allQuiz[selectCategory-1][0][randomQuiz]['answer']
    game = Game(answer)
    print(game.guess)
    win = 0
    wrongGuess = []
    while win == 0 and player.health > 0 :
        for x in range(0,len(game.guess)) :
            print(game.guess[x] + " ",end="")
        print("score " + str(player.score) + ", remaining word guess " + str(player.health))
        for x in wrongGuess :
            print(x + " ",end="")
        if(len(wrongGuess) > 0) :
            print("\n")
        alp = input('Enter Guess Alphabet: ')
        while alp in wrongGuess or alp in game.guess or not alp.isalpha():
            if alp.isalpha() :
                alp = input('Already guess this alphabet, guess the other: ')
            else :
                alp = input('Enter Only alphabet: ')
        if not FindCorrectAlp(game,player,alp) :
            wrongGuess.append(alp)
        if(game.remain == 0) :
            win = 1
            for x in range(0,len(game.guess)) :
                print(game.guess[x] + " ",end="")
            print("You Win") 

        
    

def StartGame() :
    name = input('Enter Player Name: ')
    player = Player(name)
    status = 1
    listedFile=LoadQuiz()   #load .json quiz file
    ListQuiz(listedFile)   
    while status == 1 :
        print("\n--Category--")
        for x in listedQuiz :
            print(x)
        while True :
            try :
                selectCategory = int(input('Select Category(-1 to Exit Game): '))
                if(selectCategory > len(listedQuiz) ) :
                    print("Input Only 1 to " + str(len(listedQuiz)) + "Or -1 to Exit Game")
                    continue
            except ValueError:
                print("Input number only")
                continue
            else :
                break
        if(selectCategory == -1) :
            status = 0
        else :
            os.system('cls')
            InGame(selectCategory-1,player)
        


StartGame()