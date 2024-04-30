wordinbox=input("vad för ord vill du ha i mitten? ")

lenght=len(wordinbox)

space=int(input("hur stor mellanrum ska vara i lådan? "))

tb=space+space+lenght+2
ib=space+space+lenght

box=""
box += "#" * tb + "\n" 
box += "#" + ib + "#" + "\n"
box += "#" + space + wordinbox + space "#" + "\n"
box += "#" + ib + "#" + "\n"
box += "#" * tb + "\n" 



print(box)
