import os
import sys
import string


banner = """ ___ ___ ___ ___ ___ ___ 
|  _| .'| -_|_ -| .'|  _|
|___|__,|___|___|__,|_|  
\tmade by @jhosua
"""

shift = 3
plaintext = ""
chipertext = ""
alfabet = string.ascii_lowercase


def caesarchiper(text, mode):
     r = ""
     for i in text:
          try:
               if i == " ":
                    r += " "
                    continue
               else:
                    if mode == "dec":
                         next = (alfabet.index(i.lower()) - shift) % 26
                    if mode == "enc":
                         next = (alfabet.index(i.lower()) + shift) % 26
                    r += alfabet[next]
          except ValueError:
               print("(skip) " + i + " non alfabet")
               continue
               
     return r.upper()


while True:
     os.system("clear")
     print(banner)
     select = input("1. encryption\n2. decryption\n0. exit\n\n>> ")
     
     # mode
     mode = "enc" if select == "1" else "dec" if select == "2" else sys.exit()
     text = input("\nplaintext  : ") if mode == "enc" else input("\nchipertext : ") 
     res = caesarchiper(text, mode)
     
     # show result
     print("chipertext : " + res if mode == "enc" else "plaintext  : " + res)

     input("\n\npress enter to continue... ")
