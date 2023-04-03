import RPi.GPIO as GPIO
import time

servo_pin = 18  # Le numéro de la broche GPIO que vous avez connecté au fil de signal du servo

GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)

pwm = GPIO.PWM(servo_pin, 50)  # Configurez la broche pour une fréquence de 50 Hz
pwm.start(0)  # Démarrez la modulation de largeur d'impulsion avec un rapport cyclique de 0

def set_angle(angle):
    duty = angle / 18 + 2
    GPIO.output(servo_pin, True)
    pwm.ChangeDutyCycle(duty)
    time.sleep(1)
    GPIO.output(servo_pin, False)
    pwm.ChangeDutyCycle(0)

try:
    while True:
        angle = float(input("Entrez l'angle (0 à 180 degrés) : "))
        set_angle(angle)
except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()
