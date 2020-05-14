import question
from time import localtime
import random


class Robot:
    # stupid python only has one constructor
    def __init__(self, name):
        self.__model_number = 1000
        self.name = name

    def say_name(self):
        return "my name is " + self.name

    def greet(self, person):
        return "How are you " + person

    def own_greeting(self):
        lacal = localtime()
        if lacal[3] > 12 and lacal[3] <16:
            return question.daygreet[1]
        elif lacal[3] > 15 and lacal[3] < 24:
            return question.daygreet[2]
        else:
            return question.daygreet[0]

    def tell_time(self):
        return "the time is " + str(localtime()[3]) + ":" + str(localtime()[4])

    def __repr__(self):
        return """this is a Robot that can do automated 
        things for you like copy files, lookup something 
        and store it  in it's database for future reference"""



    def __call__(self):
        """
        when the call is invoked it prints out all it's capabilities
        :return:
        """
        return f"{random.choice(question.conversion)}"

if __name__ == "__main__":
    jack = Robot("jack")
