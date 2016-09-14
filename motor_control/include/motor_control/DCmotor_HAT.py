#!/usr/bin/python

import pigpio
import time

class DCmotor_HAT:

          #BCM    pin
        in1 = 23      #16
        in2 = 24      #18
        in3 = 27      #13
        in4 = 22      #15

        FORWARD = 1
        BACKWARD = 2
        BRAKE = 3
        RELEASE = 4

        SINGLE = 1
        DOUBLE = 2
        INTERLEAVE = 3
        MICROSTEP = 4

        def __init__(self, addr = 0x60, freq = 1600):
                self.pi=pigpio.pi()
                self.motors = [ DCmotor(self, m) for m in range(2) ]
                
                #TODO
                #setfreq
                #self._pwm =  PWM(addr, debug=False)
                #self._pwm.setPWMFreq(self._frequency)

        def setPin(self, pin, value,duty=4096):
                
                if (value == 0):
                        self.pi.write(pin,0)
                        #self._pwm.setPWM(pin, 0, 4096)
                if (value == 1):
                        self.pi.set_PWM_dutycycle(pin,duty)
                        #self._pwm.setPWM(pin, 4096, 0)

        def getMotor(self, num):
                if (num < 1) or (num > 2):
                        raise NameError('MotorHAT Motor must be 1 or 2 ')
                return self.motors[num-1]



class DCmotor:
        def __init__(self, controller, num):
                self.MC = controller
                self.motornum = num
                pwm = in1 = in2 = 0
                #right motor
                if (num == 0):
                         pwm = 8
                         in2 = 22#24
                         in1 = 27#23
                #left motor
                elif (num == 1):
                         pwm = 13
                         in2 = 24#22
                         in1 = 23#27
                else:
                        raise NameError('MotorHAT Motor must be between 1 and 4 inclusive')
                self.PWMpin = pwm
                self.IN1pin = in1
                self.IN2pin = in2
                self.duty = 4096

                self.pi = pigpio.pi()
                self.pi.set_mode(in1, pigpio.OUTPUT)
                self.pi.set_mode(in2, pigpio.OUTPUT)
                self.pi.set_PWM_range(in1,4096)
                self.pi.set_PWM_range(in2,4096)

        def run(self, command):
                if not self.MC:
                        return
                if (command == DCmotor_HAT.FORWARD):
                        self.MC.setPin(self.IN2pin, 0,self.duty)
                        self.MC.setPin(self.IN1pin, 1,self.duty)
                if (command == DCmotor_HAT.BACKWARD):
                        self.MC.setPin(self.IN1pin, 0,self.duty)
                        self.MC.setPin(self.IN2pin, 1,self.duty)
                if (command == DCmotor_HAT.RELEASE):
                        self.MC.setPin(self.IN1pin, 0,self.duty)
                        self.MC.setPin(self.IN2pin, 0,self.duty)
        def setSpeed(self, speed):
                if (speed < 0):
                        speed = 0
                if (speed > 255):
                        speed = 255
                self.duty=speed*16



