#keep
import requests
from bs4 import BeautifulSoup
import sys
import os
import colorama



download_direc = ""
letters_conf_yee = ["y", "Y"]
letters_conf_nay = ["n", "N"]



def confirm():

    conf = input(colorama.Fore.RED + f"Download? ({letters_conf_yee[0]}/{letters_conf_nay[0]}):\n===> " + colorama.Style.RESET_ALL)

    try: le_ah = conf[0]
    except: confirm()
    if le_ah in letters_conf_yee:
        print("Confirmed Install")
    elif le_ah in letters_conf_nay:
        print("Aborted Install.")
        exit()
    else:
        confirm()



try:
    arguments_website = ''.join(sys.argv[1])
except:
    print("No arguments applied\nuse -h for argument list")
    exit()


if arguments_website != '--mediafire' and arguments_website != "-h" and arguments_website != '--github':
    print('Invalid Service')
    exit()
elif arguments_website == "-h":
    print('''
    Arguments:
    -h          Help
    --mediafire Mediafire link downloader
    --github    Git clone but better
    ''')
    exit()
elif arguments_website == "--mediafire":
    try:
        arguments_link = ''.join(sys.argv[2])
    except:
        print("No mediafire link.")
        exit()


    def get_mediafire_download_link():
        global arguments_link
        try:
            response = requests.get(arguments_link)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            download_button = soup.find('a', class_='input popsok')
            
            if download_button:
                return download_button['href']
            else:
                return "Not a valid mediafire link."

        except Exception as e:
            print(e)
            exit()    
    def get_mediafire_packname():
        global arguments_link
        try:
            response = requests.get(arguments_link)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            paname = soup.find('div', class_='dl-btn-label')
            
            if paname:
                return paname.get('title')
            else:
                return "Not a valid mediafire link."

        except Exception as e:
            print(e)
            exit()

    package = get_mediafire_download_link()
    package_name = get_mediafire_packname()
    print(colorama.Style.RESET_ALL)
    print("Package: " + colorama.Fore.YELLOW)
    print(package_name)
    print(colorama.Style.RESET_ALL)
    print("Url: " + colorama.Fore.MAGENTA)
    print(package)
    print()
    confirm()
    print(colorama.Style.RESET_ALL)
    if package == "Not a valid mediafire link.":
        exit()
    os.system(f'cd {download_direc} ; wget ' + get_mediafire_download_link() + " > /dev/null 2>&1; echo Success")
elif arguments_website == '--github':
    try:
        arguments_link = ''.join(sys.argv[2])
    except:
        print("No github link.")
        exit()
    confirm()
    os.system(f"cd {download_direc} ; git clone " + arguments_link)