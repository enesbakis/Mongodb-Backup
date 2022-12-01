import subprocess as sp
import datetime 
import shutil as su
import os 
import json

scriptPath = os.path.dirname(os.path.realpath(__file__))

exeCurrentPath =r"/home/enes/Desktop/Backup/mongodump"
tmp = scriptPath+"/tmp"

with open('info.json') as json_file:
    data = json.load(json_file)

for item in data:
    now = datetime.datetime.now()

    os.mkdir(tmp)

    sp.run([f'{exeCurrentPath}','--host='+item['host'],'--port='+item['port'], '--username='+item['username'], '--password='+item['password'], '--out='+tmp])


    su.make_archive(
        os.path.join(
            scriptPath,
            item['name']+" - Backup - "+now.strftime("%d.%m.%Y_%H-%M-%S")
                    ),
        'zip',
        tmp
        
                    )

    su.rmtree(tmp)

