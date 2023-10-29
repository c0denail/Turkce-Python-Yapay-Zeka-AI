from playsound import playsound
from gtts import gTTS
import speech_recognition as sr
import os
import time
from datetime import datetime
import random
from random import choice
import webbrowser

r = sr.Recognizer()

def record(ask = False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        voice = ""
        try:
            voice = r.recognize_google(audio, language="tr-TR")
        except sr.UnknownValueError:
            print("Cindia : Anlayamadım")
        except sr.RequestError:
            print("Cindia: Sistem Çalışmıyor")
        return voice
    
def response(voice):
    if "merhaba" in voice:
        selection = ["Merhaba", "Seni gördüğüme sevindim!"]
        selection = random.choice(selection)
        speak(selection)
    if "nasılsın" in voice:
        selection = ["İyiyim sen nasılsın?", "Kendimi iyi hissetmiyorum, sen nasılsın", "Çok iyiyim, sen nasılsın?"]
        selection = random.choice(selection)
        speak(selection)
    if "ben de iyiyim" in voice:
        speak("seni dinliyorum Emirhan")

    if "kötüyüm" in voice:
        selection = ["Bunu duyduğuma üzüldüm, senin için ne yapabilirim?", "Seni neşelendirecek bir fıkra anlatmamı ister misin?"]
        selection = random.choice(selection)
        speak(selection)
        if "anlat" in voice or "evet" in voice or "isterim" in voice:
            speak("Temel'e rüyasında Allah yürü ya kulum demiş. Temel'de arabasını satmış.")


    if "selam" in voice:
        speak("Selam Emirhan, sana nasıl yardımcı olabilirim?")
    if "teşekkür ederim" in voice or "teşekkürler" in voice:
        speak("Rica ederim!")
    if "görüşürüz" in voice or "görüşmek üzere" in voice or "baybay" in voice:
        selection = ["Görüşürüz", "Kendine iyi bak"]
        selection = random.choice(selection)
        speak(selection)
        exit()
    if "senden bir şey yapmanı istiyorum" in voice:
        speak("Tabi seni dinliyorum Emirhan")
    if "hangi gündeyiz" in voice or "bugün günlerden ne" in voice or "bugün hangi gün" in voice:
        today = time.strftime("%A")
        today.capitalize()
        if today == "Monday":
            today = "Pazartesi"
        
        elif today == "Tuesday":
            today = "Salı"
        
        elif today == "Wednesday":
            today = "Çarşamba"
        
        elif today == "Thursday":
            today = "Perşembe"
        
        elif today == "Friday":
            today = "Cuma"
        
        elif today == "Saturday":
            today = "Cumartesi"
        
        elif today == "Sunday":
            today = "Pazar"
        speak(today)
    
    if "saat kaç" in voice:
        selection = ["Saat şu an:", "Hemen Bakıyorum:"]
        clock = datetime.now().strftime("%H:%M")
        selection = random.choice(selection)
        speak(selection + clock)

    if "google'da ara" in voice or "arama yap" in voice or "internette arama yap" in voice:
        speak("Ne aramamı istersin?")
        search = record()
        url = "https://www.google.com/search?q={}".format(search)
        webbrowser.get().open(url)
        speak("{} için Google'da bulabildiklerimi listeliyorum.".format(search))

    if "youtube'da ara" in voice:
        speak("Ne aramamı istersin?")
        search = record()
        url = "https://www.youtube.com/results?search_query={}".format(search)
        webbrowser.get().open(url)
        speak("{} için Youtube'da bulabildiklerimi listeliyorum.".format(search))
    
    if "uygulama aç" in voice:
        speak("Hangi uygulamayı açmamı istersin?")
        runApp = record()
        runApp = runApp.lower()
        if "valorant" in runApp:
            os.startfile("C:\Riot Games\Riot Client\RiotClientServices.exe")
            speak("İstediğin uygulamayı çalıştırıyorum.")
        if "spotify" in runApp:
            os.startfile("C:\Program Files\WindowsApps\SpotifyAB.SpotifyMusic_1.222.982.0_x64__zpdnekdrzrea0")
            speak("İstediğin uygulamayı çalıştırıyorum.")
        else:
            speak("İstediğin uygulama program listemde mevcut değil.")
    
    if "not al" in voice:
        speak("Dosya ismini nasıl adlandırmak istersin?")
        txtFile = record() + ".txt"
        speak("Ne kaydetmek istersin?")
        theText = record()
        f = open(txtFile, "w", encoding="utf-8")
        f.writelines(theText)
        f.close()



def speak(string):
    tts = gTTS(text=string, lang="tr",)
    file = "answer.mp3"
    tts.save(file)
    playsound(file)
    os.remove(file)
  

speak("Merhaba Emirhan")
while True:
    voice = record()
    if voice != '':
        voice = voice.lower()
        print(voice.capitalize())
        response(voice)