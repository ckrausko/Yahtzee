"""
ckrausko
Yahtzee game
6/25/14
CSI 230
GUI enabled two player game of the classic, Yahtzee
"""

from Tkinter import *
import tkMessageBox

import math
import random
numDice = 5
diceValue = [0] * numDice
keeper = [False] * numDice

values = ("Ones", "Twos", "Threes", "Fours", "Fives", "Sixes", "3 of a kind", "4 of a kind", "Full House", "Small Straight", "Large Straight", "Yahtzee", "Chance")
nextTurn = True

class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        #set app state
        self.state = "A"
        self.headerFont = ("Helvetica", "16", "bold italic")
        Label(self, text = "Yahtzee",
            font = self.headerFont).grid(columnspan = 2)
        #adds players
        self.addPlayers()

        #adds switch button
        self.btnSwitch = Button(self, text = "Play", command = self.switch)
        self.btnSwitch.grid()
        #creates new frame but doesn't load it
        self.gameWindow = NewFrame(self)

        self.mainloop()



        #creates main game window
    def switch(self):
        #switches frames
        if self.state == "A":
                 self.state = "B"
                 self.btnNewGame = Button(self,  text = "New Game", command = self.switch)
                 self.btnNewGame.grid()
                 self.btnSwitch.grid_remove()




                 self.lbl1.grid_remove()
                 self.txt1.grid_remove()
                 self.lbl2.grid_remove()
                 self.txt2.grid_remove()

                 playerOne.name = self.txt1.get()
                 playerTwo.name = self.txt2.get()
                 playerOne.resetScore()
                 playerTwo.resetScore()




                 self.gameWindow.grid(row = 1, column = 0)
        #switches frames
        else:
                 self.state = "A"
                 self.gameWindow.grid_remove()
                 self.addPlayers()
                 self.btnSwitch.grid()
                 self.btnNewGame.grid_remove()
        self.gameWindow.setup()








        #adds player name text boxes to window
    def addPlayers(self):

        #user 1
        self.lbl1 = Label(self, text = "Player %s Name:" % 1)
        self.lbl1.grid(row = 1, column = 0)
        self.txt1 = Entry(self)
        self.txt1.grid(row = 1, column = 1)
        #user 2
        self.lbl2 = Label(self, text = "Player %s Name:" % 2)
        self.lbl2.grid(row = 2, column = 0)
        self.txt2 = Entry(self)
        self.txt2.grid(row = 2, column = 1)


class NewFrame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.txtName = StringVar()
        self.txtName.set(playerOne.name)
        self.lblName = Label (self, textvariable = self.txtName).grid(row=1, column =1, sticky="w")
        self.txtScore = StringVar()
        self.txtScore.set(playerOne.score)
        Label (self,text ="Turn:").grid(row=1, column = 0)
        Label(self, text="Score:").grid(row=1, column =2)
        self.lblScore = Label(self, textvariable = self.txtScore).grid(row=1, column =3)
        self.rollCount = 0
        #sets which players turn
        self.turn = 1
        #game counter to know when game is over
        self.gameCounter = 1



        self.btnScore = Button(self, text="Add Score to:", command = self.score)
        self.btnScore.grid(row = 3, column = 0)
        self.spnSpin = Spinbox(self, values = ("Ones", "Twos", "Threes", "Fours", "Fives", "Sixes", "3 of a kind", "4 of a kind", "Full House", "Small Straight", "Large Straight", "Yahtzee", "Chance"))
        self.spnSpin.grid(row = 3, column = 1)
        self.btnRoll = Button(self, text="Roll Dice", command = self.roll)
        self.btnRoll.grid(row = 4, column = 0)
        Label(self,text="Check box to keep die").grid(row = 6, column =1)
        #dice 1 reroll?
        self.diceOne = IntVar()
        self.dice1 = Checkbutton(self, text = "",
        variable = self.diceOne)
        self.dice1.grid(row = 6, column = 2)
        #dice 2 reroll?
        self.diceTwo = IntVar()
        self.dice2 = Checkbutton(self, text = "",
        variable = self.diceTwo)
        self.dice2.grid(row = 6, column = 3)
        #dice 3 reroll?
        self.diceThree = IntVar()
        self.dice3 = Checkbutton(self, text = "",
        variable = self.diceThree)
        self.dice3.grid(row = 6, column = 4)
        #dice 4 reroll?
        self.diceFour = IntVar()
        self.dice4 = Checkbutton(self, text = "",
        variable = self.diceFour)
        self.dice4.grid(row = 6, column = 5)
        #dice 5 reroll?
        self.diceFive = IntVar()
        self.dice5 = Checkbutton(self, text = "",
        variable = self.diceFive)
        self.dice5.grid(row = 6, column = 6)


    #loads the score and name into labels on window
    def setup(self):
        self.txtName.set(playerOne.name)
        self.txtScore.set("0")
        #game counter to know when game is over
        self.gameCounter = 1



    #rolls dice if they aren't "keepers"
    def roll(self):
        if self.rollCount >=3:
            showinfo("Info", "You've rolled 3 times, please score a category")
        else:
            self.rollCount += 1

            if self.diceOne.get() == 1:
                keeper[0] = True
            else:
                keeper[0] = False
            if self.diceTwo.get() == 1:
                keeper[1] = True
            else:
                keeper[1] = False

            if self.diceThree.get() == 1:
                keeper[2] = True
            else:
                keeper[2] = False
            if self.diceFour.get() == 1:
                keeper[3] = True
            else:
                keeper[3] = False
            if self.diceFive.get() == 1:
                keeper[4] = True
            else:
                keeper[4] = False

            counter = 0
            #if not keeper reroll and update label
            for i in keeper:
                if i ==False:
                    dice = random.randint(1,6)
                    diceValue[counter] = dice
                    Label(self, text =diceValue[counter]).grid(row=7, column =counter+2)


                counter += 1
         #resets dice check boxes, labels, and values for next players turn
    def reset(self):
        self.diceOne.set(0)
        self.diceTwo.set(0)
        self.diceThree.set(0)
        self.diceFour.set(0)
        self.diceFive.set(0)
        diceValue = [0] * numDice
        Label(self, text =0).grid(row=7, column =2)
        Label(self, text =0).grid(row=7, column =3)
        Label(self, text =0).grid(row=7, column =4)
        Label(self, text =0).grid(row=7, column =5)
        Label(self, text =0).grid(row=7, column =6)


    #scores the players dice
    def score(self):


        self.rollCount = 0
        self.scoreValue = self.spnSpin.get()
        scoreCounter = 0
        scorePosition = 0
        for i in values:

            if self.scoreValue == i:
                scorePosition = scoreCounter

            scoreCounter += 1

        #which player to score
        #set score for first player set name to second player
        if self.turn == 1:
            playerOne.score= scorePosition
            if nextTurn == True:
                self.txtName.set(playerTwo.name)
                self.txtScore.set(playerTwo.score)

                self.turn = 2
                self.reset()


        #score second player set name to first player
        elif self.turn == 2:
            playerTwo.score = scorePosition
            if nextTurn == True:
                self.txtName.set(playerOne.name)
                self.txtScore.set(playerOne.score)
                self.turn = 1
                self.gameCounter += 1
                self.reset()

            #end game info box
            if self.gameCounter >= 14:
                final = "Here are the scores: " + '\n'  +  playerOne.name + ": " + str(playerOne.score)  + '\n' + playerTwo.name + ": " +str(playerTwo.score)
                tkMessageBox.showinfo(title="Game Over", message=final)











#player class contains score card and name
#allows to set the player name
#allows to set the player score
class Player(object):
    def __init__(self, playerName ):
        self.__playerName = playerName
        self.__scoreCard = [-1] * 13
        self.__categories = ("Aces", "Twos", "Threes", "Fours", "Fives", "Sixes", "3 of a Kind",
                                "4 of a Kind", "Full House", "Small Straight", "Large Straight", "YAHTZEE", "Chance")
    def resetScore(self):
        self.__scoreCard = [-1] * 13
    #returns returns player name
    def getName(self):
        return self.__playerName
    #set player name
    def setName(self, name):
        self.__playerName = name
    #returns players score
    def getScore(self):
        total = 0
        for i in self.__scoreCard:
            if i >= 0:
                total += i

        return total
    #sets the score for persons turn
    def setTurnScore(self, pointRow):
        global diceValue
        rows = (1,2,3,4,5,6)
        total = 0
        global nextTurn
        nextTurn = True

        #send user a message if they try to score a category they've already used
        if self.__scoreCard[pointRow] != -1:
            alert = self.__categories[pointRow]
            alert += " category has already been used"
            tkMessageBox.showinfo(title="Pick New Category", message= alert)

            nextTurn = False
            #adds score for aces thru sixes
        if pointRow <= 5 and self.__scoreCard[pointRow] == -1:
            pointRow += 1
            for z in rows:
                if pointRow == z:


                    for i in diceValue:
                        if i == z:
                            total += i

                    self.__scoreCard[pointRow-1] = total
        #3 of a kind thru yahtzee scoring
        elif pointRow <= 12 and self.__scoreCard[pointRow] == -1 :
            ones = 0
            twos = 0
            threes = 0
            fours = 0
            fives = 0
            sixes = 0
            for i in diceValue:
                total += i
                if i == 1:
                    ones+=1
                elif i == 2:
                    twos+=1
                elif i ==3:
                    threes+=1
                elif i ==4:
                    fours +=1
                elif i == 5:
                    fives +=1
                elif i == 6:
                    sixes +=1
            #scores for 3 of a kind
            if pointRow == 6:

                if ones >= 3  or twos >= 3 or threes >= 3 or fours >= 3 or  fives >= 3 or sixes   >= 3:
                    self.__scoreCard[pointRow] = total
                else:
                    self.__scoreCard[pointRow] = 0
                #scores for 4 of a kind
            elif pointRow == 7:

                if ones >= 4  or twos >= 4 or threes >= 4 or fours >= 4 or  fives >= 4 or sixes   >= 4:
                    self.__scoreCard[pointRow] = total
                else:
                    self.__scoreCard[pointRow] = 0
            #scores for full house
            elif pointRow == 8:

                if(ones == 2  or twos == 2 or threes == 2 or fours == 2 or  fives == 2 or sixes   == 2) and (ones == 3  or twos == 3 or threes == 3 or fours == 3 or  fives == 3 or sixes   == 3) :
                    self.__scoreCard[pointRow] = 25
                else:
                    self.__scoreCard[pointRow] = 0
                #scores for small straight
            elif pointRow == 9:

                if (ones >= 1 and twos >= 1 and threes >= 1 and fours >= 1) or (fives >= 1 and twos >= 1 and threes >= 1 and fours >= 1) or (sixes >= 1 and twos >= 1 and threes >= 1 and fours >= 1):
                    self.__scoreCard[pointRow] = 30
                else:
                    self.__scoreCard[pointRow] = 0
                    #scores for a large straight
            elif pointRow == 10:

                if (ones >= 1 and twos >= 1 and threes >= 1 and fours >= 1 and fives >= 1) or (fives >= 1 and twos >= 1 and threes >= 1 and fours >= 1 and sixes >= 1) :
                    self.__scoreCard[pointRow] = 40
                else:
                    self.__scoreCard[pointRow] = 0
                #scores for YAHTZEE
            elif pointRow == 11:

                if ones == 5 or twos == 5 or threes == 5 or fours == 5 or fives == 5 or sixes == 5:
                    self.__scoreCard[pointRow] = 50
                else:
                    self.__scoreCard[pointRow] = 0

            #scoring for chance
            elif pointRow ==12 :
                self.__scoreCard[pointRow] = total




    score = property(fset = setTurnScore, fget = getScore)
    name = property(fset = setName, fget = getName)




















#set up player variables
playerOne = Player("")
playerTwo = Player("")
def main():

    app = App()

if __name__ == "__main__":
    main()