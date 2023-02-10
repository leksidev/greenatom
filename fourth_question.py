''' Напиши функцию на Python, которая возвращает 
текущий публичный IP-адрес компьютера 
(например, с использованием сервиса ifconfig.me) '''

'''Я выбрала для написания функции библиотеку pystun3'''

'''pip install pystun3'''

from stun import get_ip_info

def getMyExternalIp():
 return get_ip_info()[1]

my_external_ip = getMyExternalIp()
print(f'Мой текущий публичный IP: {my_external_ip}')