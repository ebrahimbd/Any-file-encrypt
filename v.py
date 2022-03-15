#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 20:15:46 2022

@author: ebrahim
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 19:30:55 2022

@author: ebrahim
"""




from cryptography.fernet import Fernet
import os
from alive_progress import alive_bar
import time




def is_same(file):
    key = open("protect_file/encripted_text.key", "rb").read()
    data = open("protect_file/encripted_text.txt", "rb").read()
    decrypted_data = Fernet(key).decrypt(data)
    write_file = open("protect_file/temp", 'wb').write(decrypted_data)
    temp_file = open("protect_file/temp", "r+").read()
    if(file == temp_file):
        return True
    else:
        return False


def load_key():
    try:
        key = open("protect_file/encripted_text.key", "rb").read()
        data = open("protect_file/encripted_text.txt", "rb").read()
        f = Fernet(key)
        decrypted_encrypted = f.decrypt(data)
        open("protect_file/@#$.int", 'wb').write(decrypted_encrypted)
        print("Sucessfully decripred ebrahim")
    except:
        print("file name encripted_text.key and encripted_text.txtnot exists ")


def enc_or_dec():
    try:
        if os.path.exists('protect_file/@#$.int'):
            key = Fernet.generate_key()
            text = open("protect_file/@#$.int", "r").read()
            if is_same(text):
                os.remove("protect_file/temp")
                print("Your file is same as befor")
                os.remove("protect_file/@#$.int")
                print("we deleted main file")
            else:
                f = Fernet(key)
                encrypted = f.encrypt(text.encode())
                print(encrypted)
                open("protect_file/encripted_text.txt", "wb").write(encrypted)
                open("protect_file/encripted_text.key", "wb").write(key)
                print("your file is sucessfully edited")
                os.remove("protect_file/temp")
                os.remove("protect_file/@#$.int")
        else:
            load_key()
    except:
        print("file name protect_file not exists")



def ok(): 
    with alive_bar(100, bar='smooth', spinner='waves3') as bar:
        for i in range(100):
            time.sleep(.005)
            bar()
    
def delf():
    i=str(input("input file path name = "))
    os.rmdir(i)
    ok()
    
delf()




# with alive_bar(100, bar='smooth', spinner='waves3') as bar:
#     for i in range(100):
#         time.sleep(.005)
#         bar()
#     enc_or_dec()
