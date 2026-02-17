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
        return output


# Function that listens to microphone
def listen(output_text, status_label):

    try:
        with sr.Microphone() as source:
            status_label.config(text="Listening...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)

        text = recognizer.recognize_google(audio)

        output_text.after(0, lambda: output_text.insert(tk.END, "You: " + text + "\n"))
        status_label.after(0, lambda: status_label.config(text="Recognized"))

        response = processCommand(text)

        if response:
            output_text.after(0, lambda: output_text.insert(tk.END, "Jarvis: " + response + "\n"))

    except sr.WaitTimeoutError:
        status_label.after(0, lambda: status_label.config(text="Listening Timeout"))

    except sr.UnknownValueError:
        output_text.after(0, lambda: output_text.insert(tk.END, "Could not understand\n"))
        status_label.after(0, lambda: status_label.config(text="Error"))

    except Exception:
        status_label.after(0, lambda: status_label.config(text="Network Error"))


# Function to start thread
def start_listening(output_text, status_label):

    thread = threading.Thread(
        target=listen,
        args=(output_text, status_label)
    )
    thread.daemon = True
    thread.start()


if __name__=="__main__":
#initialised our AI chatbot

    speak("Initializing Jarvis .... ")

# Tkinter GUI starts here

    root = tk.Tk()
    root.title("Jarvis Assistant")
    root.geometry("450x450")

    output_text = tk.Text(root, height=18, width=55)
    output_text.pack(pady=10)

    status_label = tk.Label(root, text="Idle", fg="blue")
    status_label.pack(pady=5)

    mic_button = tk.Button(
        root,
        text="🎤",
        font=("Arial", 20),
        command=lambda: start_listening(output_text, status_label)
    )
    mic_button.pack(pady=10)

    root.mainloop()
