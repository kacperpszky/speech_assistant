import os
import time
import playsound
import speech_recognition as sr
import random
import urllib
from urllib.request import urlopen
import re
import pywhatkit
import webbrowser
import keyboard

PROCESS = True
NASLUCHIWANIE = False
WIN_USER = 'kacper'
# OPERA = webbrowser.get('opera')

def speak(text):
	r1 = random.randint(1,10000000)
	r2 = random.randint(1,10000000)
	tts = gTTS(text = text, lang ='pl')
	filename =  str(r2)+"randomtext"+str(r1) +".mp3"
	tts.save(filename)
	#print("Mówię...")
	playsound.playsound(filename)
	os.remove(filename)

def listen():
	if NASLUCHIWANIE == False:
		result = input("Podaj komende >>> ")
	else:
		print("Nasłuchuję...")
		r = sr.Recognizer()
		with sr.Microphone() as source:
			r.adjust_for_ambient_noise(source) 
			audio = r.listen(source)
			result = ""
			try:
				result = r.recognize_google(audio, language = 'pl-PL')
				print("Twoja komenda >>> " + str(result))
			except Exception as e:
				return 'None'

	return str(result)

def getParams(audio, int1):
	words = audio.split()
	command = words[1]
	parameters = words[int(int1):]
	full_param = ""
	for param in parameters:
		full_param += str(param + " ")
	#print(str(full_param))

	return str(full_param)


# def otworzStrone():
# 	speak("OK, jaką stronę chcesz zobaczyć?")
# 	name = str(listen())
# 	global OPERA
# 	if name in "Netflix":
# 		OPERA.open_new('https://www.netflix.com/browse')

# 	elif name in "Twitch":
# 		OPERA.open_new('https://www.twitch.tv')

# 	elif name in "YouTube":
# 		OPERA.open_new('https://www.youtube.com')

# 	speak("Gotowe!")


def wlaczApp():
	speak("OK, jaką aplikacje chcesz włączyć?")
	name = str(listen())

	if name in 'Discord':
		os.startfile("C:\\Users\\" + str(WIN_USER) + "\\AppData\\Local\\Discord\\app-1.0.9005\\Discord.exe")

	elif name in 'Steam':
		os.startfile("C:\\Users\\" + str(WIN_USER) + "\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Steam.exe")

	speak("Zrobione!")

def zamknijApp():
	speak("OK, jaką aplikacje chcesz wyłączyć?")
	name = str(listen())

	if name in 'Discord':
		os.system("TASKKILL /F /im Discord.exe")

	if name in 'Steam':
		os.system("TASKKILL /F /im Steam.exe")

	speak("Zrobione!")

def wlaczMuzyke():
	speak('OK podaj tylko tytuł utworu')
	keyword = str(listen()) 
	keyword1 = keyword.replace(" ","+")
	html = urllib.request.urlopen("https://www.youtube.com/results?search_query="+keyword1)
	video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
	video_id = "https://www.youtube.com/watch?v="+video_ids[0]
	pywhatkit.playonyt(str(video_id))

	speak("Miłego Słuchania!")

def MuzykaDostep():
	speak("Co robimy?")
	name = str(listen())

	if ('zastopuj' or 'Zastopuj' in name):
		time.sleep(1)
		keyboard.press('space bar')

	elif ('od nowa' or 'Od nowa' in name):
		time.sleep(1)
		keyboard.press('0')

	elif ('wycisz' or 'Wycisz' in name):
		time.sleep(1)
		keyboard.press('m')

	elif ('Następne' or 'Następne' in name):
		time.sleep(1)
		keyboard.press('l')

	speak("Gotowe!")

while PROCESS:
	command = str(listen())
	if 'Fabian' in command:
		speak("W gotowości!")
		while True:
			command = str(listen())
			if ('Witaj' in command):
				speak("Witaj, jestem FABIAN, czyli twój personalny asystent. Potrzebujesz pomocy?")
				continue
			
			elif ('Jak się czujesz' in command):
				speak('Dzis jest w sumie dobrze! Mam nadzieje że też sie dobrze trzymasz...')
				continue
		
			elif ('Włącz muzykę' in command):
				wlaczMuzyke()
				continue
		
			elif ('Włącz aplikację' in command):
				wlaczApp()
				continue
		
			elif ('Wyłącz aplikację' in command):
				zamknijApp()
				continue
		
			elif ('YouTube' in command):
				MuzykaDostep()
				continue

			elif ('Włącz stronę' in command):
				otworzStrone()
				continue

			elif ('Koniec' or 'koniec' in command):
				speak('Dobrzę, widzimy się następnym razem!')
				exit()

	

	

	


