import requests
from bs4 import BeautifulSoup

import os
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

def speak(string):
    tts = gTTS(string, lang='tr')
    rand = (9000)
    file = 'audio-' + str(rand) + '.mp3'
    tts.save(file)
    playsound(file)
    os.remove(file)

speak("hangi yemeği öğrenmek istiyorsunuz")

def Komutal():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Dinliyorum")
        speak("Dinliyorum")
        audio = r.listen(source)

        try:
            durum = r.recognize_google(audio, language='tr-tr')
            print(f"user said:{durum}\n")

        except Exception as e:
            speak("Rica etsem tekrar söyler misiniz?")
            return "None"
        return durum

Tr2Eng = str.maketrans("çğıöşü ", "cgiosu-")
yemek = Komutal()
yemek2 = yemek.translate(Tr2Eng)



yemekurl = "https://www.nefisyemektarifleri.com/"+yemek2+"/"

r = requests.get(yemekurl)

fark = BeautifulSoup(r.content,"html.parser")

malzemeler = fark.find_all("ul",{"class":"recipe-materials"})
tarif = fark.find_all("article",{"class":"recipe-preparation content-articles"})

for yemek3 in malzemeler:
    malzemeler2 = yemek3.find_all("li",{"itemprop":"ingredients"})
    gereklilikler3 = str(malzemeler2)
    gereklilikler4 = gereklilikler3.replace('<li itemprop="ingredients">',"")
    gereklilikler5 = gereklilikler4.replace('</li>'," ")
    print(gereklilikler5)
    speak(yemek + " için malzemeler"+ gereklilikler5)
    devam = input("Devam etmek için entera basınız")
    if devam == "":
        speak("tarife geçiyorum")
        continue


for yemek4 in tarif:
    tarif = yemek4.find_all("ol",{"class":"recipe-instructions"})
    tarif2 = str(tarif)
    tarif3 = tarif2.replace('[<ol class="recipe-instructions" itemprop="recipeInstructions">', "")
    tarif4 = tarif3.replace('<li>', " ")
    tarif5 = tarif4.replace("</li>","")
    tarif6 = tarif5 .replace("</ol>]","")
    tarif7 = yemek4.find_all("p",{})
    tarif8= str(tarif7)
    tarif9 = tarif8.replace("3 milyon","")
    tarif10 = tarif9.replace("kişinin takip ettiği <a href=","")
    tarif11= tarif10.replace(" title=","")
    tarif12 = tarif11.replace("</p>, <p><strong></strong>","")
    tarif13= tarif12.replace(">Youtube kanalımızda</a> videolu tariflerimizi bulabilirsiniz.</p>, <p>4 milyondan fazla kişinin indirdiği Nefis Yemek Tarifleri uygulaması ile <strong>700.000'den fazla</strong> denenmiş tarif her zaman yanınızda. <a href=","")
    tarif14= tarif13.replace(">Hemen siz de indirin.</a></p>, <p><strong>","")
    tarif15 = tarif14.replace("Nefis Yemek Tarifleri Android ve iOS uygulaması indir","")
    tarif16 = tarif15.replace("youtube nefis yemek tarifleri","")
    tarif17= tarif16.replace("https://link.nefisyemektarifleri.com/youtube","")
    tarif18=tarif17.replace("https://link.nefisyemektarifleri.com/app","")
    tarif19 = tarif18.replace("<p>","")
    tarif20 = tarif19.replace("<br/>","")
    tarif21 = tarif20.replace("[<strong></strong> ","")
    print(tarif6)
    print(tarif21)
    speak(tarif6)
    speak(tarif21)















