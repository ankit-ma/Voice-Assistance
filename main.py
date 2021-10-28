import datetime
from tkinter import *
import tkinter as tk
import speech_recognition as sr
import pyaudio
import wikipedia
import threading
from PIL import Image, ImageTk
from itertools import count, cycle
from threading import Thread
from subprocess import call

# root is tkinster window
root = tk.Tk()
root.geometry("640x360")
root.maxsize(640, 360)  # restricting size with maxsize and minsize
root.minsize(640, 360)
root.title("DEVAM")  # title of application


# gif animation class
class ImageLabel(tk.Label):

    def load(self, im):
        # opens image
        if isinstance(im, str):
            im = Image.open(im)
        frames = []

        try:
            for i in count(1):
                frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass
        self.frames = cycle(frames)

        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100

        if len(frames) == 1:
            self.config(image=next(self.frames))
        else:
            self.next_frame()

    def unload(self):
        self.config(image=None)
        self.frames = None

    def next_frame(self):
        if self.frames:
            self.config(image=next(self.frames))
            self.after(self.delay, self.next_frame)


# greeting
# def wishme():
# hour = int(datetime.datetime.now().hour)
# if hour >= 0 and hour < 12:
# call(["python3", "speak.py", "Good morning, mera naam DEVAM hai"])

# elif hour >= 12 and hour < 18:
# call(["python3", "speak.py", "Good Afternoon, mera naam DEVAM hai"])

# else:
# call(["python3", "speak.py", "Good evening, mera naam DEVAM hai"])

# listing function
def listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        call(["python3", "speak.py", "Listening"])
        r.pause_threshold = 0.5
        audio = r.listen(source)
        try:
            statement = r.recognize_google(audio, language='en-in')
            print(statement)
        except Exception as e:
            phr = "Pardon me sir say that again"
            call(["python3", "speak.py", phr])
            print("in exception")
            return "None"
        return statement


def initialise():
    assitName = ["who are you", "who created you", "what is your name", "your name", "for whom you work",
                 "who make you", "Aapka naam", "naam", "Aap kaun hai","tumko kisne banaya","tum kaun ho"]
    greeting =["kya hal hai","kaise ho"]
    jokequestion = ["tell me a joke", "crack a joke", "can you say a joke", "joke"]
    jokeanswer = ["what we call a sleeping bull?............... bulldoger..... he he he he he he he he he he he"]
    weather = ["mausam ka haal", "mausam", "kaisa hai mausam"]

    call(["python3", "speak.py", "Namaskar, mera naam DEVAM hai"])

    while True:
        qu = listen().lower()
        if qu == 0:
            continue
        if "good bye" in qu or "bye" in qu or "stop" in qu:
            para = "Good bye agli baar milte hai"
            call(["python3", "speak.py", para])
            root.destroy()
            break
        if "wikipedia" in qu:
            try:
                call(["python3", "speak.py", "Searching wikipedia....."])
                qu = qu.replace("wikipedia", "")
                qu = qu.replace("search", "")
                results = wikipedia.summary(qu, sentences=2)
                call(["python3", "speak.py", "According to wikipedia" + results])
                print(results)
            except Exception as e:
                call(["python3", "speak.py", "Sorry koi result nhi mila"])
        if qu in assitName:
            call(["python3", "speak.py", "Mera naam DEVAM hai mujhe Ankit kumar ne banaaya haii "])

        elif qu in jokequestion:
            call(["python3", "speak.py", jokeanswer[0]])

        elif "laugh" in qu or "smile" in qu:
            sp = 'he he he he he he he he he he he he he i am laughing he he he he he he he he he he he he he '
            call(["python3", "speak.py", sp])
        elif qu in greeting:
            spm = 'ekdam mast mazze me'
            call(["python3","speak.py",spm])


# made this as daemon thread which will kill after main program ends
threading.Thread(target=initialise, daemon=True).start()
lbl = ImageLabel(root)
lbl.pack()
lbl.load('vertical.gif')

# btn = Button(root, width=300, height=300, image=img).pack()
root.mainloop()
