'''
Created on Aug 9, 2019

@author: daniel
'''

class Predictor():
    '''
    This class is all about predicting which player wins, or which player has what cards based on the input
    It can tell you how many players there are and what do they have based on the game that is being played
    
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
    def normalDeal(self, cards, players):
        '''
        This function is for games where all players get an equal amount of cards
        '''
        cardsPerPlayer = int(len(cards)/players)
        retArr = []
        for p in range(players):
            pArr=[] # array of player no p cards
            for c in range(cardsPerPlayer):
                print(c)
                pArr.append(cards[players*c+p]) #amount of players times which card is it plus number of the seat
                #that way we know from which deal around the table it is (players*c) and we just add the seat number counting from 0
            
            retArr.append(pArr)
        return retArr
        
        
pred = Predictor()
cards = ['ace','two','three','four','five','six','seven','eight']
print(Predictor.normalDeal(pred, cards, 4))
    
    
    