import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import datetime
import threading
import tkinter as tk
from openai import OpenAI

recognizer=sr.Recognizer()

#pyttsx3.. it will convert text to speech
engine=pyttsx3.init()


# Function that listens to microphone
def listen(output_text, status_label):
    try:
        with sr.Microphone() as source:
            status_label.config(text="Listening...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)

        text = recognizer.recognize_google(audio)

        # Update GUI safely using after()
        output_text.after(0, lambda: output_text.insert(tk.END, "You: " + text + "\n"))
        status_label.after(0, lambda: status_label.config(text="Recognized"))

    except sr.WaitTimeoutError:
        status_label.after(0, lambda: status_label.config(text="Listening Timeout"))

    except sr.UnknownValueError:
        output_text.after(0, lambda: output_text.insert(tk.END, "Could not understand\n"))
        status_label.after(0, lambda: status_label.config(text="Error"))

    except Exception:
        status_label.after(0, lambda: status_label.config(text="Network Error"))

# speak function declared
def speak(text):
    engine.say(text)
    engine.runAndWait()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="your_key"
)

conversation = [
    {
        "role": "system",
        "content": "You are Jarvis assistant"
    }
]

# it will store the conversation for further talks

def logConversation(user, assistant):

    with open("logs.txt", "a") as file:
        file.write(f"{datetime.datetime.now()}\n")
        file.write(f"User: {user}\n")
        file.write(f"Assistant: {assistant}\n\n")


# I used OpenROuter API key:--

def aiProcess(command):

    try:
        conversation.append({
            "role": "user",
            "content": command
        })

        completion = client.chat.completions.create(
            model="mistralai/mistral-7b-instruct",
            messages=conversation
        )

        reply = completion.choices[0].message.content

        conversation.append({
            "role": "assistant",
            "content": reply
        })

        # storing chats for further assistance
        logConversation(command, reply)

        return reply

    except Exception:
        return "Network issue occurred"


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
            
            #giving only one  wake up word 
            if(word.lower()=="jarvis"):
                speak("Yes..")

#some minimal changes are done

                # now the step 2 will begin
                #it will work as per pre defined commands

                with sr.Microphone() as source:
                    print("Jarvis Active ... ")
                    #phrase time limit increased from 1 to 5.
                    audio = r.listen(source,timeout=2,phrase_time_limit=5)
                    command=r.recognize_google(audio)

                #refer the given command to out process command function
                    processCommand(command)

# to deal with any unusual type of error
        except Exception as e:
            print("error;{0}".format(e))
