import sys
import pyttsx3

def init_engine():
    engine = pyttsx3.init()
    ra = engine.getProperty('rate')
    engine.setProperty('rate','900')
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[7].id) # voice 7 acha  female ,10,32
    return engine

def say(s):
    engine.say(s)
    engine.runAndWait() #blocks

engine = init_engine()
say(str(sys.argv[1]))
sys.exit()