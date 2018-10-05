#!/usr/bin/python

from bs4 import BeautifulSoup
from urllib.request import urlopen
import time
import smtplib
from twilio.rest import Client

mainWebSite = 'https://www.am.com.mx'
secondsToWait = 300
page = urlopen(mainWebSite)
noteTitle=""
currentNote="-1"
#Twilio config
account_sid = "KEY"
auth_token  = "KEY"
client = Client(account_sid, auth_token)

soup = BeautifulSoup(page, 'html.parser')


def sendsms(msg):
	message = client.messages.create(
    to="PHONE", 
    from_="PHONE",
    body=msg)


while True:
	print("Searching ...")
	mydivs = soup.find("div", {"data-tb-region": "home_notaPrincipal"})
	noteTitle = mydivs.find("p").text
	articleURL = mydivs.find("a")['href']
	if((noteTitle!=currentNote)):
		currentNote = noteTitle
		print(" -> Main Article: %s%s/%s\n" % (noteTitle,mainWebSite,articleURL))
		print(" -> Send SMS 477 <-\n" )
		sendsms(noteTitle + "\n" + mainWebSite + "/" + articleURL)
		time.sleep(secondsToWait)
		continue
	else:
		print(" -> Main article has not updated, wait a few minutes . . .\n")
		time.sleep(secondsToWait)
		continue

