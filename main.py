import requests
import json

class ATSalarm:
    def __init__(self, alarmIP, alarmPort, alarmCode, alarmPin):
        #init variables
        self.alarmIP = alarmIP
        self.alarmPort = alarmPort
        self.alarmCode = alarmCode
        self.alarmPin = alarmPin
        self.server = 'https://security.syca.nl/'
        self.lastMessage = ''

        #making initial data dict
        self.data={'alarmIP':self.alarmIP,'alarmPort':self.alarmPort,'alarmCode':self.alarmCode,'alarmPin':self.alarmPin,'task':''}

        self.status()



    def startScan(self):
        task = 'servercheck'
        self.data['task'] = task

        #retrieve cookie and connect to server
        r = requests.post(self.server, data=self.data, verify=False)
        self.koekjes = r.cookies
        self.lastMessage = r.text
        print("status :")
        print(self.lastMessage)
        print("koekjessss:")
        print(self.koekjes)

    def status(self):
        # start connection
        self.startScan()

        # set task
        task = 'status'
        self.data['task'] = task

        # keep reconnecting till all data is retrieved
        while "\"reconnect\":true" in self.lastMessage:
            print(self.lastMessage[0])
            r = requests.post(self.server, data=self.data, verify=False, cookies=self.koekjes)
            print(r.text)
            self.lastMessage = r.text

            # Speeltuin om er een leesbare dict van te maken

    def arm(self):
        pass

    def disarm(self):
        pass


# TODO: test code thiss will become Homeassistants job later
alarm = ATSalarm(alarmIP='123.456.789.123', alarmPort='80', alarmCode='123456789012345678901234', alarmPin='0000')

