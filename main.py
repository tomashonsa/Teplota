import dht
import machine
from time import sleep
sensor = dht.DHT11(machine.Pin(4))

led1 = machine.Pin(0, machine.Pin.OUT)
led2 = machine.Pin(1, machine.Pin.OUT)
led3 = machine.Pin(2, machine.Pin.OUT)
led4 = machine.Pin(3, machine.Pin.OUT)


while True:
  sensor.measure()
  temp = sensor.temperature()
  hum = sensor.humidity()
  print('teplota: %3.1f' %temp)
  print('vlhkost: %3.1f %%' %hum)
  teplota=('%3.1f'%temp)
  vlhkost=('%3.1f %%' %hum)
  print(teplota)
  if teplota=="22.0":
    led1.value(1)
    sleep(2)
    led1.value(0)
  elif teplota=="23.0":
    led1.value(1)
    led2.value(1)
    sleep(2)
    led1.value(0)
    led2.value(0)
  elif teplota=="24.0":
    led1.value(1)
    led2.value(1)
    led3.value(1)
    sleep(2)
    led1.value(0)
    led2.value(0)
    led3.value(0)
  else:
    print("nic")
