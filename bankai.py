import pyttsx3
import speech_recognition as sr

s=["bankai"]
f=pyttsx3.init()

print("//start//...")
rec=sr.Recognizer()
with sr.Microphone() as source:
          text=rec.listen(source)
          text_1=rec.recognize_google(text)
          print(text_1)
if text_1 in s:
          print("1")
          f.setProperty("rate",150)
          f.setProperty("pitch",70)
          f.say("senbonzakura")
          f.say("kageyoshi")
else:
          print("2")
          f.say("spiritual pressure is not enough")
f.runAndWait()

