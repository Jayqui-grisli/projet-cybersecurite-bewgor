import helper as h
import os
import json


conf_file=open("config.json","r")

configs=json.load(conf_file)

func=configs["functions"]
print(func["initiale"])



mot="test"

mot_up=h.toUpper(mot)

print(mot_up)

