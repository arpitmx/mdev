from typing import List

from src.mechafiles.Handlers import UIElements
import inspect
class Button:

    def __init__(self, id, height, width, btnText):

        self.id = id
        self.ButtonMap = {id: {
            'class': 'view',
            'type': UIElements.Views.button,
            'specs': {
                'text': btnText,
                'height': height,
                'width': width,
            }
        }}

    def onClick(self, funcName):

        params = inspect.signature(funcName)
        print(params)

        onClickMap = {
            'func': funcName
            #'params': params
        }
        self.ButtonMap[self.id]['specs']['onClick'] = onClickMap


    def getMap(self):
        return self.ButtonMap

def sum(x:int, y:int):
    return x + y

def ins(funcName):
   params = list([inspect.signature(funcName)][0].parameters.values())
   dict = {}







ins(sum)


