import json
from src.mechafiles.Handlers import UIElements as Elements
from src.mechafiles.Layouts import LinearLayoutSource
from src.mechafiles.Views import ButtonSource,EditBoxSource
class mechanism:

    def __init__(self):
        self.json = {}

    def Layout(self,layoutType,id,orientation, title):
        if layoutType == Elements.Layouts.linearLayout:
            return LinearLayoutSource.LinearLayout(id,orientation=orientation, title = title, height="mp", width= "mp")

    def Button(self,id,height,width,btnText):
        return ButtonSource.Button(id,height,width,btnText)

    def EditBox(self,id,height,width,hint):
        return EditBoxSource.EditBox(id,height,width,hint)





















