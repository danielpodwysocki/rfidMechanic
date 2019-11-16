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

from math import floor

LARGE_FONT = 10
MEDIUM_FONT = 5
class App():
    cards=[]
    reader = Reader()
    
    def __init__(self,*args,**kwargs):
        
        
        
        threading.Thread(target=self.getCards).start()
        threading.Thread(target=self.startServer).start()
        
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
            return static_file('index.html',root='webMechanic')
        
        @route("/main.css")
        def css():
            return static_file('main.css',root='webMechanic')
        
        @route("/nav.js")
        def nav():
            return static_file('nav.js',root='webMechanic')
        
        @route("/mechanic.js")
        def mechanic():
            return static_file('mechanic.js',root='webMechanic')
        
        @post("/clear_cards")
        def clearCards():
            self.clearCards()
            return HTTPResponse()
            
            
        run(host='172.16.1.12',port=8080)
        while True:
            time.sleep(1)
    
    
myApp = App()






