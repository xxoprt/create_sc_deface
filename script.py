import os,sys,time
from time import sleep

#jalan
def jalan(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		sleep(0.5 / 100)


#banner
banner = ("""
author : ghannyxploit404
•=======================•
      [input menu]
1. create script
2. exit
•======================•
\n
""")

#main
os.system("touch index.html")
os.system("clear")
sleep(0.5)
jalan("Jangan lupa subscribe channel gua")
sleep(0.5)
os.system("xdg-open https://youtube.com/@termuxid404?si=r2IfZSsRBN-HxNlv")
os.system("clear")
sleep(1)
jalan(banner)
pilih = int(input("_> "))

if pilih ==1:
	os.system("clear")
	p1 = input("title   : ")
	p2 = input("heading : ")
	p3 = input("marquee : ")
	p4 = input("foto    : ")

	a_1 = "<DOCTYPE html>\n"
	a_2 = "<html>\n"
	a_3 = "  <head>\n"
	a_4 = "    <title>Hacked By {}</title>\n".format(p1)
	a_5 = "  </head>\n"
	a_6 = '  <body bgcolor="black">\n'
	a_7 = "    <center>\n"
	a_8 = '      <img src="{}" width="250px" height="250px"><br>\n'.format(p4)
	a_9 = '      <h3 style="color:white;font-style:Times New Roman,Times,serif">{}</h3>\n'.format(p2)
	a_10 = '      <font style="color:red;font-family:Lucida Console,Courier New,monospace;style:italic;font-weight:bold;">haiii guys, websait ini telah diretas oleh</font>\n'
	a_11 = '      <font style="color:white;font-family:Lucida Console,Courier New,monospace;style:italic;font-weight:bold;">ghannyxploit404. btw kalian mau ngapain disini</font><br><br>\n'
	a_12 = '      <br><br>\n'
	a_13 = '      <font style="color:white">-----------------------------------------------------------------------</font><marquee behavior="alternate" style="color:white;">{}/F</marquee>\n'.format(p3)
	a_14 = '      <font style="color:white">-----------------------------------------------------------------------</font>\n'
	a_15 = '    </center>\n'
	a_16 = '  </body>\n'
	a_17 = '</html>\n'

	fi = open("index.html", "w")

	fi.write(a_1)
	fi.write(a_2)
	fi.write(a_3)
	fi.write(a_4)
	fi.write(a_5)
	fi.write(a_6)
	fi.write(a_7)
	fi.write(a_8)
	fi.write(a_9)
	fi.write(a_10)
	fi.write(a_11)
	fi.write(a_12)
	fi.write(a_13)
	fi.write(a_14)
	fi.write(a_15)
	fi.write(a_16)
	fi.write(a_17)

	fi.close()
	print("selamat file deface anda telah jadi")
