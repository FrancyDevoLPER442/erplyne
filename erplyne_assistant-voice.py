from pyttsx3 import init
from speech_recognition import Recognizer, Microphone
from datetime import datetime
import webbrowser as wb
from random import choice 
import tkinter 
engine = init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[-0].id) 
engine.say("ciao utente come posso aiutarti")
engine.runAndWait()
r = Recognizer()
errore = "bho"
risposta = ""
with Microphone() as source:
	print("sono pronto ad udirti....")
	audio = r.listen(source)
	testo = r.recognize_google(audio, language="it-IT").lower()
	print(testo)
	if "come posso progammare" in testo:
               with open("impariamo_progammare.txt","w") as f:
                f.write("ecco un mini tutorial per,te")
                risposta = "ho creato per te, un testo con una gudia per imparare progammare"
                engine.say(risposta)
                engine.runAndWait()
if "spia" in testo:
	wb.open("https://www.amazon.it/YYANG-Microcamera-Videocamera-Sorveglianza-Rilevamento/dp/B0BQ31NJSN/ref=sr_1_7?__mk_it_IT=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2GLGVPR4IKMX0&keywords=spia&qid=1673788912&sprefix=spia%2Caps%2C795&sr=8-7")
	engine.say(risposta)
	engine.runAndWait()
    
if "saga" in testo:
    risposta ="nfire è un youtuber da 100.000.00 iscritti e un ingegnere informatico che porta video predefiniti sulla virus saga"
engine.say(risposta)
engine.runAndWait()
if "versione" in testo:
	risposta = "versione attuale 2023.3.3"
	engine.say(risposta)
	engine.runAndWait()

if "pc portatile" in testo:
	wb.open("https://www.lenovo.com/it/it/laptops/ideapad/300-series/IdeaPad-3i-15-inch-Intel/p/81WB01ELIX?clickid=3YD06JRVkxyNWT9W9ywHf2h8UkAwJH0dgVbyy40&Program=3832&pid=1398965&cid=it%3Aaffiliate%3Acopxyq")

if "chi è aranzulla" in testo:
	risposta = "progammatore creato un sito web 13 anni  fa divento famoso che oltre ogni cosa che si scrive sulla informatica esce il suo sito web"
	engine.say(risposta)
	engine.runAndWait()

	if "spegni pc" in testo:
		risposta = "non posso spegnere il pc pero se vuoi prova dire parti pcoff.bat"
		engine.say(risposta)
		engine.runAndWait()

		if "pcoff.bat" in testo:
			risposta = "ok apro il pcoff.bat"
			engine.say(risposta)
			engine.runAndWait()
def lingua_sbagliata(audio):
	voices = engine.getProperty("voices")
	engine.setProperty("voice", voices[-1].id)
	risposta = "eprimiti meglio, cavolo"

class altre:
	if "gioco in python" in testo:
		risposta = "pygame SDL nato nel 2000 come libreria di python per fare giochi semplici poi nei anni divento famoso per fare giochi solo con il linguagio python versione 2 3"
		engine.say(risposta)
		engine.runAndWait()
        
   
if "come posso lanciare" in testo:
    	risposta = "ho trovato per te un tutorial per lanciare"
    	wb.open("https://www.google.com/search?q=come+lanciare&ei=mIHEY4q6HoXxkwW28Y7wDQ&ved=0ahUKEwiK5uST08r8AhWF-KQKHba4A94Q4dUDCA8&uact=5&oq=come+lanciare&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6CggAEEcQ1gQQsAM6BwgAELADEEM6DQgAEOQCENYEELADGAE6DAguEMgDELADEEMYAjoMCC4Q6gIQtAIQQxgDOg8ILhDUAhDqAhC0AhBDGAM6CQgAEEMQRhD_AToHCC4Q1AIQQzoECAAQQzoLCAAQgAQQsQMQgwE6BAguEEM6CgguEMcBENEDEEM6BwgAELEDEEM6BAgAEAM6CAgAEIAEELEDOgsILhCABBCxAxCDAToICAAQsQMQgwE6DgguEIAEELEDEMcBENEDOgUILhCxAzoLCC4QgAQQxwEQrwE6BQguEIAEOggILhCxAxCABDoICC4QgAQQsQM6CAguEIAEENQCSgQIQRgASgQIRhgBUIsaWIZdYMRfaANwAXgAgAHEBYgB0RiSAQswLjguMy41LTEuMZgBAKABAbABCsgBEMABAdoBBggBEAEYCdoBBggCEAEYCNoBBAgDGAc&sclient=gws-wiz-serp")
    	engine.say(risposta)
    	engine.runAndWait()
if "massimiliano" in testo:
	wb.open("https://www.google.com/search?q=massimiliano+fiori&ei=jIfEY6j9LOCKi-gPz72UyAo&ved=0ahUKEwio88zq2Mr8AhVgxQIHHc8eBakQ4dUDCA8&uact=5&oq=massimiliano+fiori&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyCwguEIAEEMcBEK8BOgoIABBHENYEELADOhYIABDqAhC0AhCKAxC3AxDUAxDlAhgBOgsIABCABBCxAxCDAToICAAQgAQQsQM6BQguEIAEOgsILhCABBCxAxCDAToECAAQAzoLCC4QgwEQsQMQgAQ6CAgAELEDEIMBOhEILhCABBCxAxCDARDHARDRAzoICC4QgAQQsQM6CwguELEDEIMBENQCOg4ILhCxAxCDARDHARCvAToECAAQQzoICC4QgAQQ1AJKBAhBGABKBAhGGABQgAdY0y1gjDtoAnABeACAAYEHiAHXMpIBDTAuNC4wLjMuNS4yLjKYAQCgAQGwAQrIAQjAAQHaAQQIARgH&sclient=gws-wiz-serp")
	risposta = "risulatoto per, massimiliano-fiori. su facebook questo il risultato .che volevi trovare?"
	engine.say(risposta)
	engine.runAndWait()
if "scopa forte" in testo:
	wb.open("https://it.pornhub.com/view_video.php?viewkey=ph5d6ce762b1afd")
	risposta = "risultato per scopare forte su internet"
	engine.say(risposta)
	engine.runAndWait()

if "come iniziare a fare il nautico" in testo:
	wb.open("https://www.guidaconsumatore.com/professioni/come-diventare-comandante-listituto-nautico.html")
	risposta = "risultato per come iniziarea fare il nautico"
	engine.say(risposta)
	engine.runAndWait()
if "come iniziarea a progammare videogiochi" in testo:
    wb.open("https://www.aranzulla.it/come-programmare-un-gioco-25840.html")
    risposta = "risultato per te, per progammare videogiochi senza conoscenze del c++ c#"
    engine.say(risposta)
    engine.runAndWait()

if "come progammare in unity" in testo:
	wb.open("https://www.google.com/search?q=come+imparare+ad+usare+unity3d&oq=come+imparare+ad+usare+unity3d&aqs=chrome..69i57.14442j1j4&sourceid=chrome&ie=UTF-8")
	risposta = "risposta per come imparare a progammare su unity"
	engine.say(risposta)
	engine.runAndWai()

class pc:
    if "come fare un virus innocuo amici" in testo:
    	wb.open("https://www.aranzulla.it/come-creare-un-virus-che-spegne-il-pc-14879.html#:~:text=Per%20creare%20un%20virus%20capace,personalizzato%20in%20stile%20virus%2C%20appunto.")
    	risposta = "risultato per fare un virus innocuo amici"
    	engine.say(risposta)
    	engine.runAndWait()
if "le cause della batteria si scarica velocemente" in testo:
   risposta = "le cause della batteria che si scarica velocemente puo trattarsi del celle di batteria oppure batteria dannegiata"
   engine.say(risposta)
   engine.runAndWait()

if "come nasce html" in testo:
     wb.open("https://www.google.com/search?q=come+nasce+html&oq=come+nasce+ht&aqs=chrome.1.69i57j33i160l3.7546j0j9&sourceid=chrome&ie=UTF-8")
     risposta = "Storia. L'HTML è stato sviluppato nei primissimi anni novanta del XX Tim Berners-Lee al CERN di Ginevra Svizzera"
     engine.say(risposta)
     engine.runAndWait()