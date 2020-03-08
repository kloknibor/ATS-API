import requests
import json
import base64

class ATSalarm:
    def __init__(self, alarmIP, alarmPort, alarmCode, alarmPin):
        #init variables
        self.alarmIP = alarmIP
        self.alarmPort = alarmPort
        self.alarmCode = alarmCode
        self.alarmPin = alarmPin
        self.server = 'https://security.syca.nl/'
        self.lastMessage = {}

        #making initial data dict
        self.data={'alarmIP':self.alarmIP,'alarmPort':self.alarmPort,'alarmCode':self.alarmCode,'alarmPin':self.alarmPin,'task':''}

        self.status()


    def startScan(self):
        task = 'servercheck'
        self.data['task'] = task

        #retrieve cookie and connect to server
        r = requests.post(self.server, data=self.data, verify=False)
        self.koekjes = r.cookies
        self.lastMessage = json.loads(r.text)
        print (self.lastMessage)


    def status(self):
        # start connection
        self.startScan()

        # set task
        task = 'status'
        self.data['task'] = task

        # keep reconnecting till all data is retrieved
        #print(self.lastMessage)
        while "reconnect" in self.lastMessage:
            if self.lastMessage["reconnect"]:
                r = requests.post(self.server, data=self.data, verify=False, cookies=self.koekjes)
                self.lastMessage = json.loads(r.text)
                #print(self.lastMessage)

                if "messages" in self.lastMessage:
                    for message in self.lastMessage["messages"]:
                        if message["type"] == "data":
                            if message["status"] == "areaButtons":
                                print(message["code"])
                                print(base64.standard_b64decode(message["code"]))
            else:
                break

    def arm(self):
        pass

    def disarm(self):
        pass


# TODO: test code thiss will become Homeassistants job later
alarm = ATSalarm(alarmIP='123.456.789.123', alarmPort='80', alarmCode='123456789012345678901234', alarmPin='0000')

