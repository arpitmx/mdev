class LinearLayout:
    def __init__(self, id, orientation, title, height, width):
        self.id = id
        self.layoutMap = {

            id: {
                'class': 'layout',
                'type': 'LinearLayout',
                'specs': {
                    'orientation': orientation,
                    'title': title,
                    'height': height,
                    'width': width
                },
                'children':{}
            }
        }

    def getMap(self):
        return self.layoutMap

    def appendChild(self, viewMap):
        id = list(viewMap.keys())[0]
        self.layoutMap[self.id]['children'][id] = viewMap
