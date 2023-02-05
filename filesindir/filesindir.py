#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 19:22:52 2017

@author: arne

filesindir.py
    Aufgabe: Auf Basis einer Datei mit den Informationen zu Verzeichnis und 
    Anzahl Dateien wird diese analysiert. Ziel ist es sinnvolle Volumes 
    abzuleiten, damit die maximale Anzahl von Dateien je Volume nicht über-
    schritten wird. 
    
    1. Erstelle einen Report, je Verzeichnis wird die Anzahl der Dateien aggregiert, 
    d.h. zu jedem Oberverzeichnis werden die Anzahl der Dateien in den 
    Unterverzeichnissen addiert. 
    2. Erstellung eines Reports mit sortierterter aggregierter Dateianzahl. 
    3. Optimierung? 


"""
import re                          # regular expression
import os                          # os (für logging)
import json                        # json Struktur (für logging)
import logging.config              # Logging
from operator import itemgetter    # für Aufgabe 2

l_files=[]                # Liste der Verzeichnisse und deren Anzahl Files
dirname=[]                # Liste der Verzeichnisse und der aggregierten Anzahl Files
count=0                   # Zähler für das aggregieren

# Anzahl maximaler Files in einem Volume. Bei MapR werden Dateien < 64 KB
# im Namecontainer gespeichert. Ab 25 Mio. Einträgen gibt es eine Warnung, 
# prinzipiell kann diese beliebig wachsen abhängig von der Größe der Disk. 
# Da eine Verschiebung dann nicht mehr möglich ist, kann man Out of Space laufen. 
# Daher Annahme: Erstelle Volumes mit max. 5 Mio Einträgen, d.h. im Extremfall 
# 5 Mio x 64 Kb ~ 320GB für den Namecontainer je Volume. Das sollte "klein" 
# genug sein, um diesen Container zu verschieben. 
max_count = 5000000                                 

max_dir_level = 1         # Maximale Tiefe der Directory-Struktur


#s_filename = input("Filename: ")
s_filename = "lfdbmprod.txt"                       # Filename

# Logger Setup
def setup_logging(
    default_path='logging.json',
    default_level=logging.INFO,
    env_key='LOG_CFG'
):
    """Setup logging configuration

    """
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = json.load(f)
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)

setup_logging()
log = logging.getLogger(__name__)

# Implementierung von Aufgabe 1. Erstelle einen Report 
# File lesen und aufspalten in Verzeichnisname und Anzahl Dateien
s_filehandle = open(s_filename)
for s_line in s_filehandle:
    s_filename, i_count = s_line.split(':')
    i_count=int(i_count)
    l_files.append((s_filename,i_count))
    if (s_filename.count('/') > max_dir_level):
        max_dir_level = s_filename.count('/')
s_filehandle.close

l_files.sort(reverse=True)

# Logging
for key,value in l_files:
    log.info("KEY={}  - VALUE={}".format(key,value))

print ("Report über die gruppierte Anzahl von Dateien")
print ("Max Directory Level: {}".format(max_dir_level))
print ("="*150)

# Hier sehr imperformant - gehe über l_files x l_files
for key,value in l_files:
    count=0
    reg = re.compile("^"+key)
    for tkey,tvalue in l_files:
         if (reg.match(tkey)):
             log.debug("tkey ist wie folgt definiert:")
             log.debug(tkey)
             count += tvalue
    dirname.append((key,count))
    log.debug("Speichere Key {} mit Count {}".format(key,count))

# ********************************************************************
# * 1. Ausgabe eines Reports. Aggregierte Anzahl Dateien je Verzeichnisebene
# ********************************************************************
for k in range(1,max_dir_level):
    print ("EBENE: {}".format(k))
    for key, value in dirname:
        if (key.count('/') == k):
            print ("{0:>130s}: {1:12d}".format(key, value))
    print ("-"*150)


# ********************************************************************
# * 2. Sortiere nach der aggregierten Anzahl an Dateien und gebe diese 
# *    sortiert aus. Füge eine Zeile "-" ein, wenn Anzahl Dateien größer
# *    der max_count Variabel. Dies sind Kandidaten für eigene Volumes
# ********************************************************************
dirname = sorted(dirname, key=itemgetter(1), reverse=True)
print ("*"*150)
print ("Sortierte Liste der gruppierten Anzahl von Dateien")
for key,value in dirname:
    print ("{0:>130s}: {1:12d}".format(key, value))
    log.info("KEY={}  - VALUE={}".format(key,value))
    # Immer wenn mehr Dateien als in max_count definiert ist, dann eine 
    # Zeile mit "-" Zeichen ausgeben
    if (value >= max_count):
        print("-"*150)

    
             
