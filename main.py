import sys
from neuralintents import GenericAssistant
import speech_recognition
import pyttsx3 as tts 
import nltk
import os
import datetime
import wikipedia
import webbrowser
import wikipedia

nltk.download('omw-1.4')

recognizer = speech_recognition.Recognizer()
speaker = tts.init()

"""voices = speaker.getProperty('voices')
speaker.setProperty('voices', voices[0].id)
"""
speaker.setProperty('rate', 150)


MASTER = 'Deepak'
chromePath = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"
todo_list = []


def wishMe():
	hour = int(datetime.datetime.now().hour)
	if hour >=0 and hour < 12:
		speaker.say('Good morning' + MASTER)

	elif hour >= 12 and hour < 18:
		speaker.say('Good afternoon' + MASTER)

	else:
		speaker.say('Good evening' + MASTER)
wishMe()

def chrome():
	try:
		os.startfile(chromePath)
	except Exception as e:
		speaker.say("Sorry, something is wrong")
		speaker.runAndWait()

def opencmd():
	try:
		os.startfile("C:/Windows/System32/cmd.exe")
		speaker.runAndWait()
	except Exception as e:
		speaker.say("Sorry, something is wrong")
		speaker.runAndWait()

def editor():
	try:
		os.startfile("C:/Program Files/Sublime Text/sublime_text.exe")
		speaker.runAndWait()
	except Exception as e:
		speaker.say("Sorry, something is wrong")
		speaker.runAndWait()

def create_note():
	global recognizer
	speaker.say("what do you want to write in your note?")
	speaker.runAndWait()

	done = False

	while not done:
		try:
			with speech_recognition.Microphone() as mic:
				recognizer.adjust_for_ambient_noise(mic, duration=0.2)
				audio = recognizer.listen(mic)

				note = recognizer.recognize_google(audio)
				note = note.lower()

				speaker.say('Choose a file name')
				speaker.runAndWait()

				recognizer.adjust_for_ambient_noise(mic, duration=0.2)
				audio = recognizer.listen(mic)

				filename = recognizer.recognize_google(audio)
				filename = filename.lower()

			with open(filename, 'w') as f:
				f.write(note)
				done = True
				speaker.say(f'Note created')
				speaker.runAndWait()
		except speech_recognition.UnknownValueError:
			recognizer = speech_recognition.Recognizer()
			speaker.say('Sorry i did not understand please try again')
			speaker.runAndWait()

def add_todo():
	global recognizer

	speaker.say("Whats to do you want to add?")
	speaker.runAndWait()
	done = False

	while not done:
		try:
			with speech_recognition.Microphone() as mic:
				recognizer.adjust_for_ambient_noise(mic, duration=0.2)
				audio = recognizer.listen(mic)

				item = recognizer.recognize_google(audio)
				item = item.lower()

				todo_list.append(item)
				done = True
				speaker.say(f"I added {item} to the list")
				speaker.runAndWait()

		except speech_recognition.UnknownValueError:
			recognizer = speech_recognition.Recognizer()
			speaker.say('Sorry i did not understand please try again')
			speaker.runAndWait()

def show_todo():

	if not todo_list:
		speaker.say('Your to do list is empty')
		speaker.runAndWait()
	else:
		speaker.say('Items in your do to list are following')
		for item in todo_list:
			speaker.say(item)

		speaker.runAndWait()

def wikiPedia():
	global recognizer

	speaker.say("What do you want to search in wikipedia")
	speaker.runAndWait()
	done = False

	while not done:
		try:
			with speech_recognition.Microphone() as mic:
				recognizer.adjust_for_ambient_noise(mic, duration=0.2)
				audio = recognizer.listen(mic)

				query = recognizer.recognize_google(audio)
				query = query.lower()

				result = wikipedia.summary(query, sentences=4)
				
				done = True
				speaker.say("According to wikipedia")
				speaker.say(result)
				speaker.runAndWait()

		except speech_recognition.UnknownValueError:
			recognizer = speech_recognition.Recognizer()
			speaker.say('Sorry i did not understand please try again')
			speaker.runAndWait()

def youTube():
	url = "youtube.com"
	webbrowser.open(url)
	speaker.runAndWait()
	

def vbm():
	url = 'birlavidyamandir.com'
	webbrowser.open(url)
	speaker.runAndWait()

def news():
	url = 'indianexpress.com/section/india'
	webbrowser.open(url)
	speaker.runAndWait()

def twitter():
	url = 'twitter.com'
	webbrowser.open(url)
	speaker.runAndWait()

def facebook():
	url = 'facebook.com'
	webbrowser.open(url)
	speaker.runAndWait()

def time():
	tm = datetime.datetime.now().strftime("%H:%M:%S")
	speaker.say(tm)

def thanks():
	speaker.say('My plasere' + MASTER)
	speaker.runAndWait()		

def hello():
	speaker.say('Hello, What can i do for you?')
	speaker.runAndWait()

def about():
	speaker.say('I am Jarvis, a virtual assistant')
	speaker.say('I am here to help you')
	speaker.runAndWait()

def made():
	speaker.say('I am made by BVM Computer students using AI')
	speaker.runAndWait()


def quit():
	speaker.say("Hope you liked my performance, good bye")
	speaker.runAndWait()
	sys.exit(0)




mapping = {
	"greeting":hello,
	"exit":quit,
	"about":about,
	"built":made,
	"opencmd":opencmd,
	"thanks":thanks,
	"chrome":chrome,
	"create_note":create_note,
	"add_todo":add_todo,
	"show_todo": show_todo,
	"youtube":youTube,
	"vbm":vbm,
	"news":news,
	"twitter":twitter,
	"facebook":facebook,
	"editor":editor,
	"wikipedia":wikiPedia
}

assistant = GenericAssistant('intents.json', intent_methods=mapping)
assistant.train_model()


while True:
	try:
		with speech_recognition.Microphone() as mic:

			recognizer.adjust_for_ambient_noise(mic, duration=0.2)
			audio = recognizer.listen(mic)

			message = recognizer.recognize_google(audio)
			message = message.lower()

		assistant.request(message)

	except speech_recognition.UnknownValueError:
		recognizer = speech_recognition.Recognizer()