import random
from numpy import true_divide
from vosk import Model, KaldiRecognizer
import pyaudio
import pyttsx3
import datetime
import os 
import time




engine = pyttsx3.init()
engine.say("LOADING")  ## On start up it says Loading
engine.runAndWait()

model = Model (" PATH HERE   ") # The path to the model of voice
recognizer = KaldiRecognizer(model, 16000)


cap = pyaudio.PyAudio()
stream = cap.open(format=pyaudio.paInt16, channels=1,
rate=16000,input=True,
frames_per_buffer=8192)
stream.start_stream()


print(datetime.datetime.now().strftime("%H  %M %S"))    # Prints the time when its done loading
engine.say("Done loading")  ## Says done loading 
engine.runAndWait()


while True:
    data = stream.read(22050)
    if len(data) == 0:
        break
    if recognizer.AcceptWaveform(data):

        ###bellow goes the code when the voice has been accepted
       things_said = recognizer.Result() #### things_said valuable 
       print(things_said)  ### Prints the things someone said
     
       if  ("the time" in things_said) or ("okay what is the time" in things_said):   ### if  word inside  " " is in  things_said then it will carry on with the script
        print ("I found the word ")        
        time = (datetime.datetime.now().strftime("%H Hours  " +  " %M Minutes " + " " +" " " %S  Seconds"  +  "  " + "%p"))
        print (time) 
        engine.say (time)
        engine.runAndWait()
        




       elif "tell me the date"  in things_said:
        print ("Word stuff im lazy to name this")
        date = (datetime.datetime.now().strftime(" Day: %A       ..                    Day:  %d         ..      Month: %m       ..     Year: %G"))
        print (date)
        engine.say (date)
        engine.runAndWait()
        



       elif "Never gonna"  in things_said:
        print ("You know the Rules ...      So do i ....      Say Goodbye")
        engine.say ("You know the Rules ...      So do i ....      Say Goodbye")
        engine.runAndWait()

        
       elif "random number" in things_said:       ## Gives you a random number from 1 to 10
        randomnumber = random.randrange(1,10)
        engine.say(randomnumber)
        engine.runAndWait()
        print(randomnumber)

       elif "what is your name" in things_said:
        print ("My name is bob")
        engine.say("My name is bob")


       elif "bob" in things_said:
        print ("Yes Im here")
        engine.say("Yes.. im.         here..")
        engine.runAndWait()

       elif "credits" in things_said:
        print ("Credits goes to  ")

        print ("Vosk (Voice to text)                      https://github.com/alphacep/vosk-api")
        print ("Dnigamer (Helper)                         https://github.com/dnigamer")
        print ("FujiTheFox (Owner of the python Script)   https://github.com/FujiTheFox")
        engine.say("Here are the Credits ")
        engine.runAndWait()


       elif "lights on" in things_said:
        print ("Lights On")
        engine.say("Turning the lights on")
        engine.runAndWait()
        os.system(" ") # Executes an command (This can be any command for example cmd command or SSH)
       

       elif "lights off" in things_said:
        print ("Lights off")
        engine.say("Turning the lights on")
        engine.runAndWait()
        os.system(" ") # Executes an command (This can be any command for example cmd command or SSH)
   
       elif "tell me a joke" in things_said:
        print ("Telling a joke")
        engine.say("What does a lemon say when it answers the phone?    .  Yellow!")
        engine.runAndWait()
    

               
    
                  
    




