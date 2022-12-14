from src.mechafiles.Handlers import UIElements


class EditBox:

    def __init__(self, id, height, width, hint):
        self.id = id
        self.EditBoxMap = {id: {
            'class': 'view',
            'type': UIElements.Views.editBox,
            'specs': {
                'hint': hint,
                'height': height,
                'width': width
            }
        }}

    def getMap(self):
        return self.EditBoxMap

    def getId(self):
        return self.id
#
# def test():
#     editbox = EditBox('inputX','mp','mp','Value of x')
#     #print(editbox.getMap())
#     print(editbox.getMap().keys())
#
# test()
