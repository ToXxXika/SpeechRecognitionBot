import speech_recognition as sr
import pyttsx3
import wikipedia
import pywhatkit
listener = sr.Recognizer()
##Initialize the python text to speech Library
player = pyttsx3.init()


def speak(text):
    ##player.say("You said" + text)
    player.runAndWait()


def listen():
    with sr.Microphone() as Mic:
        print("Microphone Enabled , please Speak ")
        voiceContent = listener.listen(Mic)
        text = listener.recognize_google(voiceContent)
        print(text)
        return text


def runBot():
    ResultText = listen()
    if "what is" in ResultText:
        ResultText = ResultText.replace("what is", "")
        info = wikipedia.summary(ResultText, 5)
        speak(info)
    if "play my shit" in ResultText:
        ResultText= ResultText.replace("play my shit","")
        pywhatkit.playonyt("https://www.youtube.com/watch?v=qKnyHXm53is&t=40s")
    if "play" or "Play"  in ResultText:
        ResultText=ResultText.replace("play","")
        pywhatkit.playonyt(ResultText)
runBot()