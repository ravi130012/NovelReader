
import requests
from bs4 import BeautifulSoup
import pyttsx3
import colorama
from colorama import Fore
import os
import random
from inputimeout import inputimeout
# from time import sleep
def savetexttospeech(text,filename,voice = 2,voicerate=145):
    
    # Initialize the Pyttsx3 engine
    engine = pyttsx3.init()

    #setting up voice
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[voice].id)
    newVoiceRate = voicerate
    engine.setProperty('rate',newVoiceRate)


    # We can use file extension as mp3 and wav, both will work
    engine.save_to_file(text, filename)

    # Wait until above command is not finished.
    engine.runAndWait()


def speak(text,voice=2):
    #intitializing rax
        rax = pyttsx3.init('sapi5')
        rax_voice = rax.getProperty('voices')
        # print(rax_voice)
        rax.setProperty('voice', rax_voice[voice].id)
        newVoiceRate = 170
        rax.setProperty('rate',newVoiceRate)

        #say rex
        try:
            rax.say(text)
            rax.runAndWait()
        except KeyboardInterrupt:
            speak("Thanks for listening to the beginning after the end novel!")
            exit()

def getanime(url,ch_num=1,line_num=0,issave = True,filenametosave = "beginning_after_the_end"):
    all_data = []
    req_data = []
    r = requests.get(url)
    with open("beginning.html","w",encoding='utf-8') as w:
        w.write(r.text)

    with open("beginning.html","r",encoding='utf-8') as data:
        data = data.read()

    soup = BeautifulSoup(data,'html.parser')
    datas = soup.find("div",{"class":"entry-content"}).find_all("p")
    for data in datas:
        data = data.text.replace("<p>","").replace("</p>","")
        # print(data)
        all_data.append(data)

    # print(all_data)

    for sentences in all_data:
        if all_data.index(sentences) >= line_num:
            if sentences == f"Tags: The Beginning After the End Light Novel Chapter {ch_num}, The Beginning After the End Light Novel Chapter {ch_num} raw,The Beginning After the End Light Novel Chapter {ch_num}, New The Beginning After the End Manga Online, The Beginning After the End Light Novel Chapter {ch_num} English, read The Beginning After the End Light Novel Chapter {ch_num}, The Beginning After the End Light Novel Chapter {ch_num} raw manga, The Beginning After the End Light Novel Chapter {ch_num} manga online, New The Beginning After the End Light Novel Chapter {ch_num}, The Beginning After the End Light Novel Chapter {ch_num} English Scans":
                continue
            req_data.append(sentences)

    if issave:
        with open(f"{filenametosave}.txt","w",encoding='utf-8') as wx:
            for data in req_data:
                wx.write(f"{data}\n")




    return req_data

def read_details():
    try:
        with open("lines.txt",'r') as r:
            getdata = r.readlines()
        if getdata != []:
            ch_number = int(getdata[0].split('=')[1].replace('\n','').replace(' ',''))
            line_number = int(getdata[1].split('=')[1].replace('\n','').replace(' ',''))
        # print(getdata)
        else:
            ch_number = int(input(Fore.RED+"Enter the chapter number of the beginning after the end novel: "+Fore.GREEN))
            line_number = 0
    except FileNotFoundError:
        ch_number = int(input(Fore.RED+"Enter the chapter number of the beginning after the end novel: "+Fore.GREEN))
        line_number = 0
        pass

    return ch_number,line_number


def readfile(filename):
    with open(filename,"r",encoding='utf-8') as r:
        datas = r.readlines()
        for data in datas:
            data = data.replace('\n','').replace('â€™',"'").replace("_")
            print(data)
            speak(data)
    
    print(datas)
    
    return data

def write_details(ch_number=1,line_number=0):
    with open("lines.txt","w") as ax:
        ax.write(f"ch_number = {ch_number}\n")
        ax.write(f"line_number = {line_number}\n")

    return None

def read_Tbate():
    auto_start = True
    colorama.init(autoreset=True) 

    if os.path.isfile('lines.txt') != True:
        write_details()

    ch_number = read_details()[0]
    line_number = read_details()[1]

    if ch_number != 1:
        speak(f"you are already on chapter {ch_number}, line number {line_number}. would you like to continue?")
        continues = input(Fore.GREEN+f"you are already on chapter {ch_number}. would you like to continue?(default = yes): "+Fore.RED)

        if continues != "":
            speak("please Enter your desired chapter number.")
            while True:
                try:
                    ch_number = int(input(Fore.GREEN+"Enter your desired chapter number: "+Fore.RED))
                    line_number = 0
                    break
                except ValueError:
                    speak("Invalid chapter number, please try again!")
                    print(Fore.RED+"[-]Invalid chapter number, please try again!")
                    continue

    while True:
        getanime(f"https://beginningafterend.com/novel/the-beginning-after-the-end-3-chapter-light-novel-chapter-{ch_number}/",ch_number,line_number)
        speak(f"Reading chapter {ch_number} of the beginning after the end")
        Color = [Fore.GREEN,Fore.RED,Fore.CYAN,Fore.MAGENTA,Fore.YELLOW,Fore.LIGHTBLUE_EX]
        with open("beginning_after_the_end.txt","r",encoding='utf-8') as rbx:
            datas = rbx.readlines()
            for data in datas:
                ran_color = random.choice(Color)
                data = data.replace('\n','').replace('â€™',"'")
                write_details(ch_number,line_number)
                print(ran_color+data)
                speak(data,voice=2)
                line_number = line_number+1
                # with open("beginning_after_the_end.txt","r",encoding='utf-8') as rbx: 
        ch_number = ch_number+1
        line_number = 0
        speak("Would you like to move on to the next chapter?")
        try:
            ask = inputimeout(Fore.GREEN+"Would you like to move on to the next chapter?(default : yes): "+Fore.RED,timeout=10) 
        except Exception:
            ask = None

        if ask == "" or ask == "yes" or ask == "y" or ask == None:
            continue
        else:
            speak("Thank you for reading the novel the beginning after the end!")
            print(Fore.RED+"Thank you for reading the novel the beginning after the end!")
            break




if __name__ == "__main__":
    read_Tbate()





    


    

    