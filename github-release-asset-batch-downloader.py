import os
import subprocess


release_details = os.popen("gh release view APKs").read().split('\n')
for i in release_details:
    if "asset" in i:
        print("Downloading: "+i[7:])
        subprocess.call("wget https://github.com/stotlefake/stotlefake.github.io/releases/download/APKs/"+i[7:]+" -p releases", shell=True)


            
