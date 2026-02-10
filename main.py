import speech_recognition as sr
import webbrowser
import pyttsx3

recognizer=sr.Recognizer()
engine=pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(line):
    print(line)
    pass

if __name__=="__main__":

    speak("Initializing Jarvis .... ")
    while True:
        print("Listening...")
        r = sr.Recognizer()
              
        try:
            with sr.Microphone() as source:
                print("Listening ... ")
                audio = r.listen(source,timeout=2,phrase_time_limit=1)
            word=r.recognize_google(audio)
            # print(command)
            if(word.lower()=="hello"):
                speak("Yoo.. Bro.")

                with sr.Microphone() as source:
                    print("Jarvis Active ... ")
                    audio = r.listen(source,timeout=2,phrase_time_limit=1)
                    command=r.recognize_google(audio)

                    processCommand(command)

        except Exception as e:
            print("error;{0}".format(e))
