import requests
import json
import sys
import os
url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=YOUR_API_KEY'
headers = {'Content-Type': 'application/json'}
constraints  = "Act as a cli apllication named genie. genie can only answer questions about linux bash terminal only. Refuse any question politly if it is not related to the linux bash terminal definning that you are limited. so my question is : "
firstTime = True
choice = ""
# if len(sys.argv) > 1:

#    text = " ".join(sys.argv[1:])

os.system("clear")


while choice != 'exit' or choice != -1:
    if(firstTime ==1):
       print("hello from genie how can i help u in commands")
       firstTime = False
    print(">>> ", end = "")
    choice = input("")
    if choice == 'exit' or choice == -1:
        break
    print("\n")
    data = {
        'contents': [
        {
            'parts': [
                {
                    'text': constraints +  choice
               }
            ]
        }
        ]
    }
    os.system("clear")
    print("Q : ", choice)
    print("Loding .... ")

    response = requests.post(url, json=data, headers=headers)

    os.system("clear")                                                                                                                                                                                      
    print("Q : ", choice)                                                                                                                                                                                   
                                                                                                                                                                                                            
    print(response.json().get('candidates')[0].get('content').get('parts')[0].get('text'))
