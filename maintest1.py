import instaloader
from datetime import datetime
from itertools import dropwhile, takewhile
import array

strUName="petfinderrs"
strPWD="@P3tF1nd3r@"

ig=instaloader.Instaloader()
ig.login(strUName, strPWD)
profilelist = ["meubichotasalvocanoas"]
#profilelist.append("acheseupetrs")
#profilelist.append("caesresgatadoscanoas")
#profilelist.append("onlycats.canoas")
#profilelist.append("animaisresgatadosmathias")
#profilelist.append("petsperdidoscanoas")
#profilelist.append("petresgatado_canoas")
#profilelist.append("acheseudogulbra")
profilelist.append("tosalvopetpoa")
               
for profilename in profilelist:
    #usrname=input("Enter Username: ")
    usrname=profilename
    #profile=instaloader.Profile.from_username(ig.context, usrname)
    posts=instaloader.Profile.from_username(ig.context, usrname).get_posts() 
    #print("Username: ", profile.username)
    #print("Number of Posts Uploads: ", profile.mediacount)
    #print(profile.username+" is having " +  str(profile.followers)+' followers.')
    #print(profile.username+" is following " + str(profile.followees)+' people')
    #print("Bio: ", profile.biography)
    SINCE = datetime(2024, 5, 10)
    UNTIL = datetime(2024, 5, 11)
    k = 0  # initiate k
    #k_list = []  # uncomment this to tune k
    for post in posts:
        postdate = post.date
        if postdate > UNTIL:
            continue
        elif postdate <= SINCE:
            k += 1
            if k == 50:
                break
            else:
                continue
        else:
            ig.download_post(post,usrname)
            # if you want to tune k, uncomment below to get your k max
            #k_list.append(k)
            k = 0  # set k to 0
    #instaloader.Instaloader().download_profile(usrname,profile_pic_only=True)