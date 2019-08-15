# '''
# Created on Jul 24, 2019
#      
# @author: daniel
# '''
# from kivy.app import App
# from kivy.uix.label import Label
# from kivy.uix.gridlayout import GridLayout
# from kivy.uix.button import Button
# from kivy.uix.dropdown import DropDown
#      
#      
# from Reader import Reader
# from math import ceil
#      
#      
# class GameScreen(GridLayout):
#     arr=[]
#     def __init__(self,players, **kwargs):
#         super(GameScreen, self).__init__(**kwargs)
#         self.cols=2
#         self.dropdown = DropDown()
#         self.dropdown.add_widget(Button(text='xd'))
#         self.add_widget(self.dropdown)
#         for p in range(players):
#             self.arr.append(Label(text="player "+str(p)))
#             self.add_widget(self.arr[p])
#             print('lol')
#          
#     def test(self,index):
#         self.arr[index].text='lol'
#         print('xdddddddd')
#      
#      
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
import tkinter





