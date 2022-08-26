import RPi.GPIO as GPIO
#import random
#import time

pins = [{'pin_num': 17, 'canal': 1},
        {'pin_num': 18, 'canal': 2},
        {'pin_num': 22, 'canal': 3},
        {'pin_num': 23, 'canal': 4}]

GPIO.setmode(GPIO.BCM)  # use GPIO numbering, not generic
#GPIO.setwarnings(False)

# setup all pins based on above configuration
for pin in pins:
    GPIO.setup(pin['pin_num'], GPIO.OUT, initial=GPIO.LOW)


def toggle_canal(canal: int, state: str):
    for pin in pins:
        if pin['canal'] == canal:
            if state == 'on':
                GPIO.output(pin['pin_num'], GPIO.HIGH)
            elif state == 'off':
                GPIO.output(pin['pin_num'], GPIO.LOW)


def canal_on(canal: int:
    toggle_canal(canal, 'on')


def canal_off(canal: int):
    toggle_canal(canal, 'off')


def all_on():
    for pin in pins:
        GPIO.output(pin['pin_num'], GPIO.HIGH)


def all_off():
    for pin in pins:
        GPIO.output(pin['pin_num'], GPIO.LOW)


def pin_on(pin_num: int):
    GPIO.output(pin_num, GPIO.HIGH)


def pin_off(pin_num: int):
    GPIO.output(pin_num, GPIO.LOW)
