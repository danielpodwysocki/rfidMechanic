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
        
        #container.grid_rowconfigure(0,weight=1) #0 - min size, weight = 1 - priority
        #container.grid_columnconfigure(0, weight=1)
        
        frame = EqualDeal(container,self,2) #set start frame
        
        self.frames[EqualDeal] = frame # the key is the id(EqualDeal) of the class apparently (according to stack overflow). 
        #pretty cool and i guess i'll stick with it
        
        
        frame.grid(row=0,column=0, sticky="nsew") #set the grid INSIDE of the frame
        print('lol')
        threading.Thread(target=self.getCards).start()
        print('xdd')
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

        
myApp = App()
myApp.mainloop()





