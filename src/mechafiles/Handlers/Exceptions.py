

noneId = "ID can't be null, pass ID"
class Exceptions:

    def isNoneID(self,id):
        if (id == ''):
            print("Class : ",Exception.__qualname__," \nError : ",noneId)
            quit()


