import speech_recognition as sr
import webbrowser
import pyttsx3

print(" WELCOME SIR, I'M REJOICE")
pyttsx3.speak("welcome sir i am rejoice")
r=sr.Recognizer()
while (ch!='stop'):
    with sr.Microphone() as source :
         print('Tell me something to do')
         pyttsx3.speak("Tell me something to do")
         audio=r.listen(source)
         print("listening")
    ch=r.recognize_google(audio)
    if ("hello" in ch) and ("jarvis" in ch):
        pyttsx3.speak("hello sir")
    elif  ("date" in ch) and ("run" in ch):
        print('okay sir')
        pyttsx3.speak('okay sir')
        webbrowser.open("http://192.168.43.122/cgi-bin/my.py?x=date")
    elif ("cal" in ch) and ("run" in ch):
        print('okay sir')
        pyttsx3.speak("okay sir")
        webbrowser.open("http://192.168.43.122/cgi-bin/my.py?x=cal")
    elif ("ip" in ch) and ("show" in ch):
        print('okay sir')
        pyttsx3.speak("okay sir")
        webbrowser.open("http://192.168.43.122/cgi-bin/my.py?x=ifconfig")
    elif ("hadoop" in ch) and ("run" in ch):
        print('okay sir')
        pyttsx3.speak("okay sir")
        webbrowser.open("http://192.168.43.122/cgi-bin/my.py?x=systemctl status hadoop")
    elif ("list" in ch) and ("show" in ch):
        print('okay sir')
        pyttsx3.speak('okay sir')
        webbrowser.open("http://192.168.43.122/cgi-bin/my.py?x=ls")
    elif ("ping" in ch) and ("google" in ch):
        print('okay sir')
        pyttsx3.speak('okay sir')
        webbrowser.open("http://192.168.43.122/cgi-bin/my.py?x=ping google.com")
    elif ("exit" in ch) or ("stop" in ch):
        break
    else:
        print("not recpgniosed command sir")
        pyttsx3.speak('sorry sir i can not do that')
