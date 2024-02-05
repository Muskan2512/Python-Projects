import os
import win32com.client as wincom

speak = wincom.Dispatch("SAPI.SpVoice")

while(True):
  text=input("Enter the text:")
  # text = "Python text-to-speech test. using win32com.client"
  if(text=="over"):
    break
  speak.Speak(text)
