from robot import Robot
from question import get_last_item as get
import question
import pyttsx3


engine = pyttsx3.init()

"""
process.py is like the brain of the robot 
all queries are processed here and the required
output is returned
"""


def memory(query):
    with open("response.txt", "r") as file:
        for line in file:
            if line[:line.index(":")] == query:
                engine.say(line[line.index(":"):])
                engine.runAndWait()
            else:
                engine.say("I don't know. How do I respond to that?")
                engine.runAndWait()
                res = input("> ")
                if res:
                    file.write(f"\n{query + ':' + res}")
                    engine.say("Alright, " + res)
                    engine.runAndWait()

    # file = open("response.txt", "r")
    # for line in file:
    #     if line[:line.index(":")] == query:
    #         engine.say(line[line.index(":"):])
    #         engine.runAndWait()
            

    # else:
    #     file = open("response.txt", "a")
    #     engine.say("I don't know. How do I respond to that?")
    #     engine.runAndWait()
    #     res = input("> ")
    #     if res:
    #         file.write(f"\n{query + ':' + res}")
    #         engine.say("Alright, " + res)
    #         engine.runAndWait()
    #         file.close()


def thought(query):
    jack = Robot("Jack")
    """
    processes query and returns output
    :param query: 
    :return: 
    """
    if "hello" in query.lower():
        if get(query) not in question.allowed:
            return jack.say_name()
        elif get(query) in question.allowed:
            return "Hello Haggai"
        else:
            return jack.own_greeting()


    elif query.lower() in list(question.remarks.keys()):
        return question.remarks[query]

    elif query.lower() == jack.name.lower():
        return jack()

    elif query.lower() in question.daygreet:
        if query.lower() == jack.own_greeting().lower():
            return jack.own_greeting()
        else:
            return "actually it's " + jack.own_greeting().split()[-1]

    elif "not haggai" in query.lower():
        return "Oh, sorry. what is your name?"

    elif "my name is" in query.lower():
        return jack.greet(get(query))

    elif "how are you" in query.lower():
        return "Am fine, thanks...How are you?"

    elif "is the time" in query:
        return jack.tell_time()

    elif query.lower() == "goodbye":
        return "good bye, Haggai"

    else:
        return False

if __name__ == "__main__":
    memory("how do i open google")
