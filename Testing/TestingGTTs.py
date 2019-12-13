import playsound
from gtts import gTTS

def speak_en(text):
    """
    This function takes a string and converts into a mp3 file using gTTS
    and later to  plays the mp3 file using the playsound module
    """
    tts = gTTS(text=text, lang="en",slow=False )  # Set the value of slow to
                                                    #  true for the language to
                                                    #  be spoken much much
                                                    #  slower than usual 
    filename = "Spoken_text.mp3"
    tts.save(filename)
    playsound.playsound(filename)

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
