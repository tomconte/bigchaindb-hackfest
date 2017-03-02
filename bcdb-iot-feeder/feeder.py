#!/usr/bin/python3

# Read IoT events from the Event Hubs endpoint and send them to BigChainDB.

from async import *
from bcdbclient import BigChainDBClient

nb_partitions = 2

args = []
for i in range(0, nb_partitions):
    args.append('amqps://service:AwmJVqYgKM+w4+yapM6jnmMSLcYm+fUYImciAvkzXvo=@ihsuprodamres019dednamespace.servicebus.windows.net/iothub-ehub-bigchainha-121054-cf2d875cd6/ConsumerGroups/$Default/Partitions/' + str(i))

print(args)

class App(CallbackAdapter):

    def on_start(self):
        print("Started")
        self.client = BigChainDBClient('bcdbhack.westeurope.cloudapp.azure.com', 9984, 'F911cpKsZTP3Fxzx243mJqUh15CtGDTRuVBaw5xnvGXh', '6H6g4c6fwc5MCDMT4cmTgDDuij9Yhr6FXVJ7G2sMoztJ')
        for a in args:
            print("Subscribing to:", a)
            self.messenger.subscribe(a)
        self.messenger.recv()

    def on_recv(self, msg):
        print("Received:", msg)
        self.client.send_data_to_bdb(msg.body.decode('utf-8'), '9EBwea1UeivCVHQ4Wbm4jyFNN2FWMa97yQBhupwCrxnt')
        if msg.body == "die":
            self.stop()

    def on_stop(self):
        print("Stopped")

a = App(Messenger())
a.run()
