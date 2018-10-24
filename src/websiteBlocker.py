from stat import S_IREAD, S_IRGRP, S_IROTH, S_IWUSR
import os
import shutil
import time

class websiteBlock:

    home = "127.0.0.1"

    def __init__(self, minute, websites,sys,hosts=None):
        self.minute = minute
        self.websites = websites
        if sys=="w":
            self.hosts = r"C:\Windows\System32\Drivers\etc\hosts."
        else:
            self.hosts = "/etc/hosts"

    def backup(self, name):
        before = os.path.dirname(self.hosts)
        source = os.path.dirname(before)
        shutil.copy2(self.hosts, source)
        
        orgn = os.path.join(source, "hosts")
        new = os.path.join(source, name)
        os.rename(orgn, new)

    def start(self):
        before = os.path.dirname(self.hosts)
        source = os.path.dirname(before)
        mainS = source + "backupHosts"
        if os.path.isfile(mainS) == False:
            self.backup ("backupHosts")

        blockedList = self.websites.split(",")
        with open(self.hosts,'r+') as file:
            content=file.read()
            for website in blockedList:
                if website in content:
                    pass
                else:
                    file.write(self.home+" "+ website+"\n")
            os.chmod(self.hosts, S_IREAD|S_IRGRP|S_IROTH)
        time.sleep(self.minute*60)
        os.remove(source + "backupHosts")

    def revert(self):
        os.chmod(self.hosts, S_IWUSR|S_IREAD)
        clean = open(self.hosts, 'r+')
        clean.truncate(0)

        with open("./backupHosts",'r+') as file:
            content=file.readlines()
            with open(self.hosts,'r+') as file2:
                for line in content:
                    file2.write(line)

#MVX
