# import os
# import say

# if __name__ == '__main__':
#     # os.system()
#     print("Swagat h aapka TomSpeaker 1.0. m (Harsh dwara banaya gya)")
#     while True:
#         x= input("Aap kya khna chahte h likhiye: ")
#         if x=="q":
#             break
#         command =f"say {x}"
#         os.system(command)

#         # Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('Namste');   



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