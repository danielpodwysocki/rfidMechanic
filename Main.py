# '''
# Created on Jul 24, 2019
#      
# @author: daniel
# '''

# class Main(App):
#     '''
#     This class has methods for printing the output of the Reader class 
#     '''
#     read = Reader()
#      
#     def build(self):
#         self.screen = GameScreen(players=10)
#         self.screen.test(1) #we can use that principle to create labels for cards AND change em every update, yaaay
#         return self.screen
#          
#     def toWords(self,card):
#         cards=['ace','two','three','four','five','six','seven','eight','nine','ten','jack','queen','king']
#         colors = ['clubs','hearts','spades','diamonds']
#         colorIndex = ceil(card/13)-1
#         cardIndex = card - colorIndex*13 -1
#         return (cards[cardIndex]+" of " +colors[colorIndex])
#          
#     def display(self):
#         return self.toWords(self.read.lastRead())
#      
#          
# t = Main()
# t.run()
import tkinter as tk
from views.EqualDeal import EqualDeal
from Reader import Reader
import threading
from bottle import route,run,HTTPResponse,static_file
from time import sleep
import json

from math import floor

LARGE_FONT = 10
MEDIUM_FONT = 5
class App(tk.Tk):
    frames={}
    cards=[]
    reader = Reader()
    
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        
        container.pack(side="top", fill="both", expand = True)
        
#         container.grid_rowconfigure(0,weight=1) #0 - min size, weight = 1 - priority
#         container.grid_columnconfigure(0, weight=1)
#         container.grid()
        frame = EqualDeal(container,self,2) #set start frame
        
        self.frames[EqualDeal] = frame # the key is the id(EqualDeal) of the class apparently (according to stack overflow). 
        #pretty cool and i guess i'll stick with it
        
        
        frame.grid(row=0,column=0, sticky="nsew") #set the grid INSIDE of the frame
        
        threading.Thread(target=self.getCards).start()
        threading.Thread(target=self.startServer).start()
        
        self.cardsUpdate()
        self.changeFrame(EqualDeal)
#         self.proc = Process(target=self.getCards)
#         self.proc.start()
    def changeFrame(self, controller):
        frame = self.frames[controller]
        frame.tkraise()
    def getCards(self):
        self.cards.append(self.reader.lastRead())
        print(self.cards)
        self.getCards()
    def cardsUpdate(self):

        frame = self.frames[EqualDeal]
        frame.updateCards(self.cards)
        print(self.cards)
        self.after(500,self.cardsUpdate)
    
    def clearCards(self):
        self.cards.clear()
    def toNames(self, number):
        '''
        this method turns a card number into the card symbol + first letter of the suit format (AC - ace of clubs)
        '''
        suits = ['c','h','s','d']
#         suits = ['clubs, hearts, spades','diamonds']
        cards = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        suit = floor((number-1)/13.0) # 13 cards in a suite, king of clubs is 13, ace of hearts is 14, so we subtract one to make the logic work
        card = number-1 - suit*13 #again, cards are in the "human" form, so we subtract one from the card number
        return cards[card]+suits[suit]
    def startServer(self):
        @route("/getcards")
        def getcards():
            return HTTPResponse(json.dumps(self.cards))
        
        @route("/")
        def index():
            return static_file('index.html',root='webMechanic')
        
        @route("/main.css")
        def css():
            return static_file('main.css',root='webMechanic')
        
        @route("/mechanic.js")
        def mechanic():
            return static_file('mechanic.js',root='webMechanic')
            
            
        run(host='localhost',port=8080)
        while True:
            time.sleep(1)
    
    
myApp = App()
myApp.mainloop()





