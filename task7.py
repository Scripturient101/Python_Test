import pyttsx3

file1 = open("song.txt","r")
l= file1.read()
print(l)
file1.close()


engine = pyttsx3.init()
engine.say(l)
#engine.say(l2)
engine.runAndWait()