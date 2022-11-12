import time
import requests

botKey = '5481264314:AAF2jlw6rpAiLfnNSXnLy8Cm-cXAM1c6JN0'
chatId= '1601284205'
timeInterval=60

timeObject= (time.strftime("%H:%M"))

courant = '08:00'
sport= '09:00'
m11= '11:00'
LOL='12:00'
DzAndSite='14:00'
Eng = '15:00'
python='16:00'
M10='18:00'
eng='19:00'
revisionPourModule='20:00'
keyboard='12:00'

def emploitTime (timeObject,courant,sport,m11,LOL,DzAndSite,Eng,python,M10,eng,revisionPourModule,keyboard):
        timeObject =(time.strftime("%H:%M"))
        if courant == timeObject:
            return ("mat9olch liya f9ti l7amas dyalk hadi w9it l9or2an yak wanood 7fed chwita" )
        elif sport == (timeObject):
            return ("rah khasek dire sport bach ts7a7")
        elif m11 == (timeObject):
            return ("had modul dyal ndor khasek tfhmo 7sen mno M11")
        elif LOL == (timeObject):
            return ("wa 3yiti 9ser chwiya lol")
        elif DzAndSite == (timeObject):
            return ("dire site profetionnel ou tha fih rah tahoma mohim")
        elif Eng == (timeObject):
            return ("tferj fichi 7aja dyal eng ")
        elif python == (timeObject):
            return ("db wslna l a7san 7aja fnhar")
        elif M10 == (timeObject):
            return ("bensjay mskina darori tfhem 3la wditha had lmodul")
        elif eng == (timeObject):
            return ("wa khdem chi vedioyat eng ou 9ra m3a rask")
        elif revisionPourModule == (timeObject):
            return ("jbed traj3 rah regionnal 9reb")
        elif keyboard == (timeObject):
            return ("t3lem chwiya lclavier rah mohim bach trb7 lw9t")
        else :
            return("")        
def sendUpdate(chatId,msg):
    url = f"https://api.telegram.org/bot{botKey}/sendMessage?chat_id={chatId}&text={msg}"
    requests.get(url)
def main():
    sendUpdate(chatId,"salam")
    while True:
        
        sendUpdate(chatId,emploitTime(timeObject,courant,sport,m11,LOL,DzAndSite,Eng,python,M10,eng,revisionPourModule,keyboard))
        time.sleep(timeInterval)
main()