#参照　：　https://github.com/NVIDIA/jetson-gpio
#Jetson.GPIOの公式リポジトリ
import Jetson.GPIO as GPIO
import time

#PWMピン番号を指定
output_pwm = 32

#DIOピン番号を指定
output_pin = 22

#デューティを指定
duty = 3 #デューティー比を%で指定

#PWM周波数を設定
freq = 50 #PWM周波数をHzで指定

#GPIOのpin指定方法を設定
GPIO.setmode(GPIO.BOARD)

#PWMピン設定
GPIO.setup(output_pwm, GPIO.OUT, initial=GPIO.HIGH)
pwm = GPIO.PWM(output_pwm, freq) #周波数を設定

#DIOピン設定
GPIO.setup(22, GPIO.OUT)


#左回転
def turn_left():
	GPIO.output(output_pin1, 1)
	GPIO.output(output_pin2, 0)
	GPIO.output(output_pin3, 0)
	GPIO.output(output_pin4, 1)

#右回転
def turn_right():
	GPIO.output(output_pin1, 0)
	GPIO.output(output_pin2, 1)
	GPIO.output(output_pin3, 1)
	GPIO.output(output_pin4, 0)

#前進
def forward():
	GPIO.output(output_pin1, 1)
	GPIO.output(output_pin2, 0)
	GPIO.output(output_pin3, 1)
	GPIO.output(output_pin4, 0)

#後退
def back():
	GPIO.output(output_pin1, 0)
	GPIO.output(output_pin2, 1)
	GPIO.output(output_pin3, 0)
	GPIO.output(output_pin4, 1)


def main():
	# GPIOでモータの回転方向を制御
	forward()

	#PWM出力
	pwm.start(duty) #Dutyを設定

	try:
		while True:
			pass
	finally:
		#CTRL+Cで停止
		#PWM停止
		pwm.stop()

		#GPIO初期化
		GPIO.cleanup()

if __name__ == '__main__':
    main()