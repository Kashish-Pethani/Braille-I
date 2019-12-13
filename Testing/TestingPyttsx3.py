import time
import pyttsx3

engine = pyttsx3.init()

def speak_en(text):
    """
    This function is used to talk out a string entered in the arguement using the pyttsx3 module
    """
    engine.say(text)
    engine.runAndWait()
    time.sleep(1)

def retrive_text(filepath):
    """
    Enter the filepath of the the file to be read using r to indicate a raw string
    """
    file = open(filepath, "r")
    text = file.read()
    return text

text=retrive_text(r"C:\Users\aniru\OneDrive\Desktop\Blah.txt")  # Enter the 
                                                                # textfile's loaction
speak_en(text)          
