#!/bin/env python3

"""

you can re run setup.py 
if you have added some wrong value

"""
import sys
import os
re = "\033[1;31m"
gr = "\033[1;32m"
cy = "\033[1;36m"


def banner():
    os.system('clear')
    print(f"""
	{re}╔═╗{cy}┌─┐┌┬┐┬ ┬┌─┐
	{re}╚═╗{cy}├┤  │ │ │├─┘
	{re}╚═╝{cy}└─┘ ┴ └─┘┴
	""")


def requirements():
    def csv_lib():
        banner()
        print(gr+'['+cy+'+'+gr+']'+cy+' this may take some time ...')
        os.system("""
			pip3 install cython numpy pandas
			python3 -m pip install cython numpy pandas
			""")
    banner()
    print(gr+'['+cy+'+'+gr+']'+cy +
          ' it will take up to 10 min to install csv merge.')
    input_csv = input(gr+'['+cy+'+'+gr+']'+cy +
                      ' do you want to enable csv merge (y/n): ').lower()
    if input_csv == "y":
        csv_lib()
    else:
        pass
    print(gr+"[+] Installing requirements ...")
    os.system("""
		pip3 install telethon requests configparser
		python3 -m pip install telethon requests configparser
		touch config.data
		""")
    banner()
    print(gr+"[+] requirements Installed.\n")


def config_setup():
    import configparser
    banner()
    cpass = configparser.RawConfigParser()
    cpass.add_section('cred')
    xid = input(gr+"[+] enter api ID : "+re)
    cpass.set('cred', 'id', xid)
    xhash = input(gr+"[+] enter hash ID : "+re)
    cpass.set('cred', 'hash', xhash)
    xphone = input(gr+"[+] enter phone number : "+re)
    cpass.set('cred', 'phone', xphone)
    setup = open('config.data', 'w')
    cpass.write(setup)
    setup.close()
    print(gr+"[+] setup complete !")


def merge_csv():
    import pandas as pd
    import sys
    banner()
    file1 = pd.read_csv(sys.argv[2])
    file2 = pd.read_csv(sys.argv[3])
    print(gr+'['+cy+'+'+gr+']'+cy+' merging ' +
          sys.argv[2]+' & '+sys.argv[3]+' ...')
    print(gr+'['+cy+'+'+gr+']'+cy+' big files can take some time ... ')
    merge = file1.merge(file2, on='username')
    merge.to_csv("output.csv", index=False)
    print(gr+'['+cy+'+'+gr+']'+cy+' saved file as "output.csv"\n')


try:
    if any([sys.argv[1] == '--config', sys.argv[1] == '-c']):
        print(gr+'['+cy+'+'+gr+']'+cy+' selected module : '+re+sys.argv[1])
        config_setup()
    elif any([sys.argv[1] == '--merge', sys.argv[1] == '-m']):
        print(gr+'['+cy+'+'+gr+']'+cy+' selected module : '+re+sys.argv[1])
        merge_csv()
    elif any([sys.argv[1] == '--install', sys.argv[1] == '-i']):
        requirements()
    elif any([sys.argv[1] == '--help', sys.argv[1] == '-h']):
        banner()
        print("""
	( --config  / -c ) setup api configration
	( --merge   / -m ) merge 2 .csv files in one 
	$ python3 setup.py -m file1.csv file2.csv
	( --install / -i ) install requirements
	( --help    / -h ) show this msg 
			""")
    else:
        print('\n'+gr+'['+re+'!'+gr+']'+cy +
              ' unknown argument : ' + sys.argv[1])
        print(gr+'['+re+'!'+gr+']'+cy+' for help use : ')
        print(gr+'$ python3 setup.py -h'+'\n')
except IndexError:
    print('\n'+gr+'['+re+'!'+gr+']'+cy+' no argument given : ' + sys.argv[1])
    print(gr+'['+re+'!'+gr+']'+cy+' for help use : ')
    print(gr+'['+re+'!'+gr+']'+cy +
          ' https://github.com/heosua91/telegram-scraper#-how-to-install-and-use')
    print(gr+'$ python3 setup.py -h'+'\n')
