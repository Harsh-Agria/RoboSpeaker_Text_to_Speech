# FOR WINDOWS->
import os
import win32com.client as wincom

if __name__ =='__main__':
    s=wincom.Dispatch("SAPI.SpVoice")
    print("Welcome to the RoboSpeaker: ")
    s.Speak("Welcome to the RoboSpeaker: ")
    s.Speak("Enter what do you want me to speak: ")
    while True:
        print("Enter what do you want me to speak: ")
        x=input()
        if x=="q" :
            print("Thanks for using RoboSpeaker....")
            s.Speak("Thanks for using RoboSpeaker....")
            break
        s.Speak(x)
