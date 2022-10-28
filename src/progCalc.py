from mechafiles import mecha as mecha
from mechafiles.Handlers import Tester,UIElements as UI
import json

from src.mechafiles.Views import EditBoxSource


def sum(x:int, y:int):
    return x + y

def sub(x, y):
    return x - y

def init():

    lib = mecha.mechanism()
    layout = lib.Layout(UI.Layouts.linearLayout, id="linearLayout", orientation="Vertical", title="Calculator")
    inputx = lib.EditBox("inputX",'wp',"mp",hint="Value of X")
    inputy = lib.EditBox("inputY",'wp',"mp",hint="Value of Y")
    btnAdd = lib.Button("btnAdd",'wp','mp','Add')
    btnAdd.onClick(funcName=sum, inputSources=[inputx.getId(), inputy.getId()])

    print(btnAdd.getMap())
    layout.appendChild(inputx.getMap())
    layout.appendChild(inputy.getMap())
    layout.appendChild(btnAdd.getMap())
    Tester.testJson(json.dumps(layout.layoutMap, indent=4))
    #Pretty.pretty(layout.layoutMap)


init()

