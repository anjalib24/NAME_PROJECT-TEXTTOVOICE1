import tkinter as tk
from gtts import gTTS
import os

def convert_text_to_speech():
    text = text_entry.get()
    tts = gTTS(text)
    tts.save("output.mp3")
    os.system("start output.mp3")
root = tk.Tk()
root.title("Text-to-Speech Converter")


label = tk.Label(root, text="Enter text:")
label.pack()

text_entry = tk.Entry(root, width=50)
text_entry.pack()

# Create a button to trigger text-to-speech conversion
convert_button = tk.Button(root, text="Convert to Speech", command=convert_text_to_speech)
convert_button.pack()


root.mainloop()
