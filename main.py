import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary

# recognizer=sr.Recognizer()

#pyttsx3.. it will convert text to speech
engine=pyttsx3.init()

# speak function declared
def speak(text):
    engine.say(text)
    engine.runAndWait()

#here we are defining basic pre defined task
def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")

    elif "open youtube" in c.lower() or "open yt" in c.lower():
        webbrowser.open("https://youtube.com")

    elif "open leetcode" in c.lower():
        webbrowser.open("https://leetcode.com/")

    elif c.lower().startswith("play"):

        song= c.lower().split(" ")[1]
        link=musicLibrary.music[song]
        webbrowser.open(link)



if __name__=="__main__":
#initialised our AI chatbot

    speak("Initializing Jarvis .... ")

# an infinite loop is created to always listen our words

    while True:
        print("Listening...")        
        r = sr.Recognizer()

        try:
            # program is hearing our voice 
            with sr.Microphone() as source:
                print("Recognizing ... ")
                recognizer.adjust_for_ambient_noise(source,duration=0.5)
                # audio = r.listen(source,timeout=2,phrase_time_limit=1)
                audio=r.listen(source)
            word=r.recognize_google(audio)
            print(word)
            
            if(word.lower()=="jarvis" or word.lower()=="hello"):
                speak("Yes..")

                # now the step 2 will begin
                #it will work as per pre defined commands

                with sr.Microphone() as source:
                    print("Jarvis Active ... ")
                    audio = r.listen(source,timeout=2,phrase_time_limit=1)
                    command=r.recognize_google(audio)

                #refer the given command to out process command function
                    processCommand(command)

# to deal with any unusual type of error
        except Exception as e:
            print("error;{0}".format(e))
