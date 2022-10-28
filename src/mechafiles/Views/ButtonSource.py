from typing import List

from src.mechafiles.Handlers import UIElements
import inspect

from src.mechafiles.Views import EditBoxSource


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

    def onClick(self, funcName, inputSources: list[str]):
        func = funcName.__qualname__
        params = self.getParams(funcName, inputSources)
        onClickMap = {
            'func': func,
            'params': params
        }
        self.ButtonMap[self.id]['specs']['onClick'] = onClickMap

    def getMap(self):
        return self.ButtonMap

    def getParams(self, funcName, paramValues) -> dict:
        params = list([inspect.signature(funcName)][0].parameters.values())
        #print('Params : ', params)
        funcDict = {}
        for i in range(0, len(params)):
            prm = params[i]
            funcDict[prm.name] = {
                'dataType': self.formatParam(str(prm.annotation).split(" ")[1]),
                'dataSourceID': paramValues[i]
            }

        return funcDict

    def formatParam(self, text):
        dic = {"'": "", ">": ""}
        for i, j in dic.items():
            text = text.replace(i, j)
        return text


def sum(x: int, y: int):
    return x + y

