import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary

from openai import OpenAI

recognizer=sr.Recognizer()

#pyttsx3.. it will convert text to speech
engine=pyttsx3.init()

# speak function declared
def speak(text):
    engine.say(text)
    engine.runAndWait()

# I used OpenROuter API key:--

def aiProcess(command):

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",

        # paste your own api key
        api_key="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"
    )

    completion = client.chat.completions.create(
        model="mistralai/mistral-7b-instruct",

        messages=[
            {
                "role": "system",
                "content": "You are a virtual assistant named Jarvis skilled in general tasks like Alexa, And give response in short."
            },
            {
                "role": "user",
                "content": command
            }
        ]
    )

    return completion.choices[0].message.content


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

    # integration of AI 

    else:
        output=aiProcess(c)
        speak(output)
        pass


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
                recognizer.adjust_for_ambient_noise(source,duration=1)
                audio = recognizer.listen(source, timeout=3, phrase_time_limit=5)

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
