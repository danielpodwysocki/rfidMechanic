# '''
# Created on Jul 24, 2019
#      
# @author: daniel
# '''

from Reader import Reader
import threading
from bottle import route,run,HTTPResponse,static_file,post, redirect, request
import json
import sys
from math import floor

LARGE_FONT = 10
MEDIUM_FONT = 5
class App():
    cards=[]
    
    def __init__(self,*args,**kwargs):

        self.readerEnabled = False #tells us whether or not the reader is running
        self.root = sys.path[0]+'/webMechanic' #web server root
        self.reader=None
        
        
        threading.Thread(target=self.startServer).start()
    
    def startReader(self,name): #pass reader dictionary name
        readers = {'arduino': Reader}
        self.readerEnabled = True
        
        self.reader = readers[name]()
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
#                 return static_file('startup.html',root=self.root)
                redirect("/startup")
        
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
        
        @route("/probability.js")
        def probability():
            return static_file('probability.js', root=self.root)
            
        @post("/clear_cards")
        def clearCards():
            self.clearCards()
            return HTTPResponse()
        @post("/start_reader")
        def start_reader():
            data = request.body.read()
            reader = request.forms.get("reader")
            self.startReader(reader)
            redirect('/')
        @route("/startup")
        def startup():
            return static_file('startup.html',root=self.root)

            
        run(host='0.0.0.0',port=8080)

    
    
myApp = App()






