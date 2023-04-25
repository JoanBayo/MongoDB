import ssl
import sys
import subprocess

import paho.mqtt.client as mqtt

status = "OFF"
queue2 = 0

def on_connect(client, userdata, flags, rc):
	print('connected (%s)' % client._client_id)
	client.subscribe(topic='Microdesys/f/m1command', qos=2)

def on_message(client, userdata, message):
	global status
	global queue2
	print(message.payload.decode().strip('{}'))

# START
	if message.payload.decode().strip('{}') == 'm1start':
		if status == "OFF":
			client.publish("resposta/maquina","STATUS SET ON")
			status = "ON"
			print(status)
		else:
			client.publish("resposta/maquina","STATUS ALREADY ON")
			print(status)

		if queue2 > 0:
			client.publish("resposta/maquina","PRODUINT " + queue2 + "PECES")
			queue2 = 0
			print(status)

# STOP
	if message.payload.decode().strip('{}') == 'm1stop':
		if status == "ON":
			client.publish("resposta/maquina","STATUS SET OFF")
			status = "OFF"
			print(status)
		else:
			client.publish("resposta/maquina","STATUS ALREADY OFF")
			print(status)

# RESET

# EMERGENCIA

# FER DOS PECES
	if message.payload.decode().strip('{}') == 'm1produce02':
		print(queue2)
		if queue2 == 0:
			client.publish("resposta/maquina","S'HAN AFEGIT DOS PECES")
			queue2 = 2
			print(status)
		else:
			queue2 = queue2 + 2
			client.publish("resposta/maquina","S'HAN AFEGIT DOS PECES")
			client.publish("resposta/maquina","HI HA " + queue2 + "PECES A PRODUCCIO")
			print(status)

# START PRODUCING
	if message.payload.decode().strip('{}') == 'm1startproduce':
		if queue2 > 0:
			client.publish("resposta/maquina","PRODUINT " + queue2 + "PECES")
			queue2 = 0
			print(status)
		else:
			client.publish("resposta/maquina","PRODUINT " + queue2 + "NO HI HA PECES A PRODUCCIO")



# print('------------------------------')
# print('topic: %s' % message.topic)
# print('payload: %s' % message.payload.decode())
# print('qos: %d' % message.qos)

def main():
	client = mqtt.Client(client_id='Microdesys/f/m1command', clean_session=False)
	client.on_connect = on_connect
	client.on_message = on_message
	client.connect(host='127.0.0.1', port=1883)
	client.loop_forever()

if __name__ == '__main__':
	main()


	sys.exit(0)
