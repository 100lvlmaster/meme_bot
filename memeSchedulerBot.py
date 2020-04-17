import os
import time,tweepy
import urllib.request
import subprocess

# Authenticate to Twitter
auth = tweepy.OAuthHandler("XXXXXXXXXXXXXX", "XXXXXXXXXXXXXXXXXXXX")
auth.set_access_token("XXXXXXXXXXXXXXXXXXXXXXX", "XXXXXXXXXXXXXXXXXXXXXXXXX")

# Create API object
api = tweepy.API(auth)

def getdatMemeBoi():
    y = 0
    x = 0
    memecounter=0
    already = []
    for i in range(0,28):
    	try:
    		batcmd = "curl -S --fail --silent --show-error https://meme-api.herokuapp.com/gimme"
    		result = subprocess.check_output(batcmd, shell=True)
    		result = str(result)
    		while "imgur" in result:
    			batcmd = "curl -S --fail --silent --show-error https://meme-api.herokuapp.com/gimme"
    			result = subprocess.check_output(batcmd, shell=True)
    			result = str(result)
    		sep = '"url":"'
    		result = result.rsplit(sep, 1)[1]
    		result = result.rsplit("\"", 1)[0]
    		name = result.replace("https://i.redd.it/",f"meme{x}")
    	except:
    		pass
    	try:
    		if name in already:
    			y = y + 1
    			pass
    		else:
    			try:
    				urllib.request.urlretrieve(result, name)
    				x = x + 1
    				already.append(name)
    				print("Got [" + str(x) + "] " + name + " Duplicates " + str(y))
    			except:
    				pass
    	except:
    		pass
    a=os.listdir()
    for name in a:
        endi=name[-3:]
        if endi=="jpg" or endi=="png":
            #api.update_with_media(name)
            memecounter=memecounter+1
            print(f"{name} uploaded")
            time.sleep(1)
        else:
            pass
    for name in a:
        if memecounter!=0:
            if name[-3:]=="jpg" or name[-3:]=="png":
                os.remove(name)
                memecounter=memecounter-1
                print(f"{name} removed")
            else:
                pass
        else:
            getdatMemeBoi()

while True:
    getdatMemeBoi()