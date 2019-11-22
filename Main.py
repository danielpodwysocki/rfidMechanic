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
from Reader import Reader
import threading
from bottle import route,run,HTTPResponse,static_file,post
from time import sleep
import json
import sys
from math import floor

LARGE_FONT = 10
MEDIUM_FONT = 5
class App():
    cards=[1,15,32,12,44,52,10]
    
    def __init__(self,*args,**kwargs):

        self.readerEnabled = False #tells us whether or not the reader is running
        self.root = sys.path[0]+'/webMechanic' #web server root
        
        threading.Thread(target=self.startServer).start()
    
    def startReader(self):
        self.enabled = True
        self.readerEnabled = Reader()

        threading.Thread(target=self.getCards).start()

    
    def getCards(self):
        self.cards.append(self.reader.lastRead())
        print(self.cards)
        self.getCards()
    
    def clearCards(self):
        self.cards.clear()
    

    def startServer(self):
        @route("/get_cards")
        def getcards():
            return HTTPResponse(json.dumps(self.cards))
        
        @route("/")
        def index():
            if self.readerEnabled:
                return static_file('index.html',root=self.root)
            else:
                return static_file('startup.html',root=self.root)
        
        @route("/main.css")
        def css():
            return static_file('main.css',root=self.root)
        
        @route("/nav.js")
        def nav():
            return static_file('nav.js',root=self.root)
        
        @route("/mechanic.js")
        def mechanic():
            return static_file('mechanic.js',root=self.root)
        
        @route("/switcher.js")
        def switcher():
            return static_file('switcher.js',root=self.root)
        
        
        @post("/clear_cards")
        def clearCards():
            self.clearCards()
            return HTTPResponse()
        
            
            
        run(host='0.0.0.0',port=8080)
        while True:
            time.sleep(1)
    
    
myApp = App()






