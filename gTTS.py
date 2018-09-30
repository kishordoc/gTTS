from gtts import gTTS
import speech_recognition as sr
import os

language='en'

harvard = sr.AudioFile('sample.wav') #select local audio file
r=sr.Recognizer()

with harvard as source:
	print("Say Anything")
	#print('Before')
	audio = r.record(source) 
	#print('After')
	try:
		mytext=r.recognize_google(audio)
		print('you said : {}'.format(mytext))
	except:
		mytext="try again"
		print("Failed")
		
myobj = gTTS(text=mytext, lang=language, slow=False) 
myobj.save("welcome.mp3") 
os.system("welcome.mp3") 
#os.remove("welcome.mp3")

