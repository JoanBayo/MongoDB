import ssl
import sys
import subprocess
from email import message
import time
import random

import paho.mqtt.client as mqtt

status = "OFF"
queueList = 0
queueInfinitTotal = 0
queueInfinit = 0
final = 0


def on_connect(client, userdata, flags, rc):
    print('connected (%s)' % client._client_id)
    client.subscribe(topic='Microdesys/f/m1command', qos=2)

    def on_message(client, userdata, message):
        global status, queueInfinitTotal,queueInfinit, queueList
        print(message.payload.decode().strip('{}'))

        # START
        if message.payload.decode().strip('{}') == 'm1start':
            if status == "OFF":
                client.publish("resposta/maquina", "STATUS SET ON")
                status = "ON"
                print(status)
            else:
                client.publish("resposta/maquina", "STATUS ALREADY ON")
                print(status)

            # STOP
            if message.payload.decode().strip('{}') == 'm1stop':
                if status == "ON":
                    client.publish("resposta/maquina", "STATUS SET OFF")
                    status = "OFF"
                print(status)
            else:
                client.publish("resposta/maquina", "STATUS ALREADY OFF")
                print(status)

        # RESET
        if message.payload.decode().strip('{}') == 'm1reset':
            client.publish("resposta/maquina", "A5")
            status = "OFF"
            print(status)
            time.sleep(10)
            client.publish("resposta/maquina", "STATUS RESET CORRECTLY")
            status = "ON"
            print(status)

        # EMERGENCIA
        if message.payload.decode().strip('{}') == 'm1emer':
            client.publish("resposta/maquina", "D1")

        # FER DOS PECES
        if message.payload.decode().strip('{}') == 'm1produce02':
            print(queueList)
            queueList = queueList + 2
            client.publish("resposta/maquina", "S'HAN AFEGIT DOS PECES")
            client.publish("resposta/maquina", "ARA HI HA " + queueList + " PECES A PRODUCCIO")
            print(status)

        # START PRODUCE INDIVIDUAL
        if message.payload.decode().strip('{}') == 'm1startproduce':
            if queueList > 0:
                client.publish("resposta/maquina", "PRODUINT " + queueList + " PECES")
                print(status)
                while queueList > 0:
                    time.sleep(5)
                    queueList = queueList - 1
                    if queueList == 1:
                        client.publish("resposta/maquina", "A2")
                    else:
                        client.publish("resposta/maquina", "QUEDEN " + queueList + "PER PRODUIR")

                time.sleep(5)
                client.publish("resposta/maquina", "A1")
            else:
                client.publish("resposta/maquina", "NO HI HA PECES PER A PRODUCCIO")

        # FER PECES INFINITES
        if message.payload.decode().strip('{}') == 'm1startproduceinfinit':
            while True:
                time.sleep(5)
                numero_aleatorio = random.randint(1, 20)
                if numero_aleatorio == 1:
                    queueInfinit = queueInfinit + 1
                    queueInfinitTotal = queueInfinitTotal + 1
                    client.publish("resposta/maquina", "m1goodpartleaving = 1")
                else:
                    client.publish("resposta/maquina", "m1partleaving = 0")
                    paraProduccioIninita(message)
                if final == 1:
                    client.publish("resposta/maquina", "m1picesproduced = " + queueInfinitTotal)
                    client.publish("resposta/maquina", "m1goodpicesproduced = " + queueInfinit)
                    break

    def paraProduccioIninita(message):
        global final
        print(message.payload.decode().strip('{}'))
        if message.payload.decode().strip('{}') == 'm1stopproduceinfinit':
            final = 1

    # print('------------------------------')
    # print('topic: %s' % message.topic)
    # print('payload: %s' % message.payload.decode())
    # print('qos: %d' % message.qos)


def main(on_message=None):
    client = mqtt.Client(client_id='Microdesys/f/m1command', clean_session=False)
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(host='127.0.0.1', port=1883)
    client.loop_forever()


if __name__ == '__main__':
    main()

sys.exit(0)


