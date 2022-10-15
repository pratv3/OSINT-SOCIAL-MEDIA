import requests as r
from colorama import Fore,Back,Style
print(f"{Fore.LIGHTCYAN_EX}   !!!!!!!       !!!!!!!!    !!!!!!!!!   !!!!!     !!!   !!!!!!!!!!")
print(f"{Fore.LIGHTCYAN_EX} !!        !!    !!              !!      !!! !!    !!!       !!")
print(f"{Fore.LIGHTCYAN_EX}!!          !!   !!!!!!!         !!      !!!  !!   !!!       !!")
print(f"{Fore.LIGHTCYAN_EX}!!          !!        !!         !!      !!!   !!  !!!       !!")
print(f"{Fore.LIGHTCYAN_EX} !!        !!         !!         !!      !!!    !! !!!       !!")
print(f"{Fore.LIGHTCYAN_EX}   !!!!!!!      !!!!!!!!     !!!!!!!!!   !!!     !!!!!       !!")
print(f"{Fore.CYAN}:-- Made by Pratv3 --:\n -----Time to Fetch socialmedia accounts----- ")
print(f"{Fore.YELLOW} Date of build:-15.10.2022")
print(f"{Fore.MAGENTA}:-- Support about 50 websites which are well reputated --:")
uname=str(input(f"{Fore.GREEN}[+] enter your username to fetch:-"))
tm=int(input(f"{Fore.GREEN}[+] enter your timeout:-"))
l1=["https://instagram.com/@",
    "https://m.facebook.com/",
    "https://github.com/",
    "https://snapchat.com/add/",
    "https://in.pinterest.com/",
    "https://in.linkedin.com/in/",
    "https://2Dimensions.com/a/",
    "https://devloper.apple.com/forums/profile/",
    "https://discusions.apple.com/profile/",
    "https://archiveofourown.org/users/",
    "https://archive.org/details/@",
    "https://create.arduino.cc/projecthub/",
    "https://community.cloudflare.com/u/",
    "https://codecademy.com/profiles/",
    "https://codechef.com/users/",
    "https://fiverr.com/",
    "https://hackerrank.com/",
    "https://play.google.com/store/apps/devloper?id=",
    "https://pypi.org/user/",
    "https://reddit.com/user/",
    "https://roblox.com/user.aspex?username=",
    "https://scratch.mit.edu/users/",
    "https://starva.com/atheletes/",
    "https://forum.sublimetext.com/u/",
    "https://t.me/",
    "https://tenor.com/users/",
    "https://tiktok.com/@",
    "https://tinder.com/@",
    "https://tryhackme.com/p/",
    "https://twitter.com/",
    "https://virustotal.com/ui/users/",
    "https://forums.whonix.org/u/",
    "https://en.wikipedia.org/wiki/",
    "https://xvideos.com/profiles/",
    "https://youporn.com/uservids/",
    "https://xhamster.com/users/",
    "https://forums.adobe.com.people/",
    "https://paypal.com/paypalme/",
    "https://forums.kali.org/member.php?username=",
    "https://youtube.com/",
    "https://quora.com/profile/",
    "https://open.spotify.com/user/",
    "https://steamcommunity.com/id/",
    "https://ebay.com/usr/",
    "https://g.dev/",
    "https://github.comunity/u/",
    "https://canva.com/",
    "https://khanacademy.org/profile/",
    "https://pixabay.com/en/users/",
    "https://codementor.io/@",
    "https://steam.me/",
    "https://user.teknik.io/",
]
g=0
f=open(f"{uname}.txt","a+")
f.write(f"-----------------DATA FOR ACTIVE SITES OF {uname} --------------\n")
for i in range(len(l1)):
    link=l1[i]+uname
    try :
        if r.get(link,timeout=tm):
            print(f"{Fore.YELLOW}{link}{Fore.BLUE}:-{Fore.GREEN}Found")
            f.write(link+"\n")
            g+=1 
    except :
        print(f"{Fore.YELLOW}{link}{Fore.BLUE}:-{Fore.RED}not found")
accu=(g/len(l1)*100)
print(f"{Fore.LIGHTRED_EX}[+] accuracy for the username is:-{Fore.GREEN}{accu}")
print(f"{Fore.LIGHTMAGENTA_EX} :-- The active website links for  {uname} are  saved at data.txt file --:")
f.write(f"\n-------------- ACCURACY FOR {uname} AT ALL DEFINED SITES IS :--({accu}) -------------")
f.close()
