# 🎙️ Jarvis Voice Assistant (Python)

A simple voice-controlled AI assistant built using Python.
It listens for the wake word **“Jarvis”** and performs basic predefined tasks like opening websites and playing songs from a custom music library.

---

## 🚀 Features

* Voice recognition using microphone
* Text-to-speech response
* Opens websites like Google, YouTube, and LeetCode
* Plays songs from a predefined music library
* Wake word activation (“Jarvis”)

---

## 🛠️ Requirements

Install the following Python libraries:

```bash
pip install SpeechRecognition
pip install pyttsx3
pip install pyaudio
```

⚠️ Note:
If `pyaudio` fails to install, try:

```bash
pip install pipwin
pipwin install pyaudio
```

---

## ▶️ How to Run

```bash
python main.py
```

Speak **“Jarvis”** followed by a command.

Example:

* "Jarvis open Google"
* "Jarvis play jharokhe"

---

## 📁 Project Structure

```
main.py          → Main voice assistant logic  
musicLibrary.py  → Stores song links  
```

---

## 🔮 Future Improvements

* Add more commands
* Add AI conversation support
* Integrate APIs for automation
* GUI interface

---

## 📌 Author

Aditya Sinha
