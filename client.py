
class Client:
    def __init__(self, name):
        self.__name = name

# get
    @property
    def name(self):
        print("calling @property name()")
        return self.__name.title()

# set
    @name.setter
    def name(self, new_name):
        print("calling setter name()")
        self.__name = new_name
