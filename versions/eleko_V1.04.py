import speech_recognition as sr
import wikipedia as wiki
import pyttsx3
import requests
from pprint import pprint
import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import webbrowser
import cv2

r = sr.Recognizer()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')

def speak(text):
    print(text) 
    engine.say(text)
    engine.runAndWait()


def weather(city):
    def weather_data(query):
	    res=requests.get('http://api.openweathermap.org/data/2.5/weather?'+query+'&APPID=b35975e18dc93725acb092f7272cc6b8&units=metric')
	    return res.json()
    def print_weather(result,city):
        speak("{}'s temperature: {}°C ".format(city,result['main']['temp']))
        speak("Wind speed: {} m/s".format(result['wind']['speed']))
        speak("Description: {}".format(result['weather'][0]['description']))
        speak("Weather: {}".format(result['weather'][0]['main']))
    def main():
        try:
            query='q='+city
            w_data=weather_data(query)
            print_weather(w_data, city)
            print()
            
        except:
            print('City name not found...')
    if __name__=='__main__':
        main()


       

def eleko_wiki(text):
    for i in search:
	    if i in text:
		    k=text.split(i)
		    str1 = ""
		    for i in k:
			    str1+=i
    #print(wiki.summary(str1,sentences=3))
    return speak(wiki.summary(str1,sentences=3))

def eleko_greets(text):
    for i in greetings:
	    if i in text:
		    speak('Your Most Welcome!!')
def eleko_temp(text):    
    with sr.Microphone() as source:
        print("City Name: ")
        speak('say the city name')
        audio = r.listen(source)
        try: 
            city = r.recognize_google(audio)            
            print('you said {}'.format(city))
            weather(city)       
        except:
            speak('Speak Again')

def eleko_news():
    news_url = "https://news.google.com/news/rss"
    client = urlopen(news_url)
    xml_page = client.read()
    client.close()
    soup_page = soup(xml_page,"lxml")
    news_list = soup_page.findAll("item")
    t=0
    speak('here are top 5 news.')
    for news in news_list:
        t+=1
        speak(news.title.text)
        if t==5:
            speak('these are top 5 news for now... i will be back with breaking news after some time')
            break

def eleko_gmail():
    url = 'https://mail.google.com/mail/u/0/#inbox'
    webbrowser.open_new_tab(url)

def eleko_facebook():
    url = 'https://www.facebook.com/'
    webbrowser.open_new_tab(url)

def eleko_linkedin():
    url = 'https://www.linkedin.com/feed/'
    webbrowser.open_new_tab(url)

def eleko_cam():
    speak('you are looking good sir!!')
    cap = cv2.VideoCapture(0)
    while True:
        ret,frame = cap.read()
        cv2.imshow("eleko cam",frame)

        k = cv2.waitKey(100000)
        if k == 27:
            break
    cv2.destroyAllWindows()

def eleko_intro():
    speak('I am eleko, developed and created by Tanmoy Munshi. I am happy to help you.')

def test():
    print('yo')

speak('hiii, I am eleko. How may i help you')
t=1

while (t!=0):
    
    with sr.Microphone() as source:
        print("say anything")
        audio = r.listen(source)
        try: 
            text = r.recognize_google(audio)            
            print('you said {}'.format(text))

            search = ['search for','tell me','tell me about','define','meaning of','something about']
            greetings = ['thank you','thanks','bye']
            temp = ['temperature','weather','forecast']
            newss = ['news','latest news','breaking news','todays breaking news']
            intro = ['who made you','creators name','developers name']

            if any(x in text for x in search):
                eleko_wiki(str(text))

            elif any(x in text for x in greetings):
                eleko_greets(str(text))
                t=0
            elif any(x in text for x in temp):                
                eleko_temp(str(text))
            elif any(x in text for x in newss):
                eleko_news()
            elif 'gmail' in text:
                eleko_gmail()
            elif 'facebook' in text:
                eleko_facebook()
            elif 'LinkedIn' in text:
                eleko_linkedin()
            elif 'click a picture' in text:
                eleko_cam()
            elif any(x in text for x in intro):
                eleko_intro()

            else:
                speak('i dont understand')
            


        except:
            print('Try again!!')
            speak('I cant hear you')


'''a = str(input())
search = ['search for','tell me','define']
for p in search:
    k = a.split(p)
    str1 = ""
    for i in k:
        str1+=i

print(str1)'''

'''a = str(input())
search = ['search for','tell me','define']
for i in search:
    if i in a:
        k = a.split(i)
        str1 = ""
        for i in k:
            str1+=i

print(str1)'''


'''if search in a.split():
    print('1')
else:
    print('0')'''





