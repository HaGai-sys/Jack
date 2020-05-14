import process
import pyttsx3


engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[0].id)

"""
this is the main jack app file, think of it as the executable
from the time he wakes up to the time he sleeps

"""



query = input("> ")
while query:
    if process.thought(query):
        engine.say(process.thought(query))
        engine.runAndWait()

    else:
        process.memory(query)


    query = input("> ")
