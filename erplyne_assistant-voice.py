from pyttsx3 import init
from speech_recognition import Recognizer, Microphone
from datetime import datetime
import webbrowser as wb
from random import choice 
engine = init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.say("ciao utente come posso aiutarti")
engine.runAndWait()
r = Recognizer()
with Microphone() as source:
	print("sono pronto ad udirti....")
	audio = r.listen(source)
	testo = r.recognize_google(audio, language="it-IT").lower()
	errore = "esprimiti meglio"
	print(testo)
	if "come posso progammare" in testo:
               with open("impariamo_progammare.txt","w") as f:
                f.write("ecco un mini tutorial per,te")
                risposta = "ho creato per te, un testo con una gudia per imparare progammare"
if "spia" in testo:
	wb.open("https://www.amazon.it/YYANG-Microcamera-Videocamera-Sorveglianza-Rilevamento/dp/B0BQ31NJSN/ref=sr_1_7?__mk_it_IT=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2GLGVPR4IKMX0&keywords=spia&qid=1673788912&sprefix=spia%2Caps%2C795&sr=8-7")
    
if "saga" in testo:
    risposta ="nfire è un youtuber da 100.000.00 iscritti e un ingegnere informatico che porta video predefiniti sulla virus saga"
engine.say(risposta)
engine.runAndWait()
if "versione" in testo:
	elseif = "versione attuale 2023.3.3"
	engine.say(elseif)
	engine.runAndWait()
def lingua_sbagliata(audio):
	voices = engine.getProperty("voices")
	engine.setProperty("voice", voices[0].id)
