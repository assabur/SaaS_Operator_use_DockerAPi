#!/usr/bin/python3
from pip._vendor.distlib.compat import raw_input
import getpass
import sys
import docker
def log() :
    print("\tVeuillez renseigner les deux arguments de comme suit")
    print("\t format de la commande : depop [lien github] [tag]")

if len (sys.argv)==2 and sys.argv[1]!= "help" :
    log()
if len (sys.argv)==2 and sys.argv[1]== "help" or len (sys.argv)==1  :
    log()
if len (sys.argv) ==3 :
    mon_fichier = open("Dockerfile", "w")
    lien = sys.argv[1]
    mon_fichier.write(
                    "\nFROM ubuntu:latest"
                    "\nMAINTAINER abdalahmaiga <abdullahwin99@gmail.com>\n"
                    "\nENV TZ=Europe/Paris\n"
                    "\nRUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone\n"
                    "\nRUN apt-get update\n"
                    "\nRUN apt-get -y upgrade\n"
                    "\nRUN apt-get install -y git\n"
                    "\nRUN apt-get -y install apache2\n"
                    "\nRUN mkdir /var/www/html/medibed\n"                           
                    "\nRUN git clone "+lien +" /var/www/html/medibed\n"
                    "\nENV APACHE_RUN_USER www-data\n"
                    "\nENV APACHE_RUN_GROUP www-data\n"
                    "\nENV APACHE_LOG_DIR /var/log/apache2\n"
                    "\nENV APACHE_LOCK_DIR /var/lock/apache2\n"
                    "\nENV APACHE_PID_FILE /var/run/apache2.pid\n"
                    "\nEXPOSE 80\n"
                    "\nCMD /usr/sbin/apache2ctl -D FOREGROUND")
    mon_fichier.close()
    """user = sys.argv[2]
    passw = sys.argv[3]"""
    name = sys.argv[2]
    client = docker.from_env() #cree le client docker
    print("Start Building your docker image...")
    client.images.build(path = "./",tag = name)
    print("verification de la creation de "+name)
    #display all the create images
    """for x in range(len(client.images.list())):
        print (client.images.list()[x])"""
    print(client.images.get(name))
    print("deployment done !!!")
    val = raw_input("Voulez vous effectuer un PUSH sur Docker-HUB ? Y/N  ")
    if val =="y" or val =="Y":
        login = raw_input("Votre identifiant Docker Hub: ")
        mdp= getpass.getpass("votre mot de passe: ")
        #print(mdp)
        print("start pushing your docker image to docker hub")
        client.login(username= login, password= mdp)
        for line in client.images.push(name, stream=True, decode=True):
            print(line)
    else :
        print("Thanks bye")
else :
    if len(sys.argv) >3 :
        print (" Erreur faites depop help")

#https://github.com/assabur/PHP-MySQL-CRUD-Web-Application
