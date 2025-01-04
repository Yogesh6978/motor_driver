from machine import Pin,PWM,I2C
import ssd1306
from time import sleep

P1 = Pin(12,Pin.OUT)
P2 = Pin(13,Pin.OUT)
motor = PWM(33,100)
i2c = I2C(0,scl = Pin(22),sda = Pin(21))
oled = ssd1306.SSD1306_I2C(128,64,i2c)

def refresh_oled(txt1,wid1,ht1,txt2,wid2,ht2):
    oled.fill(0)
    oled.text(txt1,wid1,ht1)
    oled.text(txt2,wid2,ht2)
    oled.show()
    
while True:
    
    refresh_oled("Motor driver",10,20,"Initialising",10,40)
    sleep(5)

    P1.on()
    P2.off()
    motor.duty(1023)
    refresh_oled("Forward rotation",0,20,"Motor speed:100%",0,40)
    sleep (5)
    
    P1.off()
    P2.off()
    refresh_oled("No rotation",15,20,"Motor speed:0%",0,40)
    sleep(3)
    
    P1.off()
    P2.on()
    refresh_oled("Reverse rotation",0,20,"Motor speed:100%",0,40)
    sleep(5)
    
    P1.off()
    P2.off()
    refresh_oled("No rotation",15,20,"Motor speed:0%",0,40)
    sleep(3)
    
    
    P1.on()
    P2.off()
    motor.duty(512)
    refresh_oled("Forward rotation",0,20,"Motor speed:50%",0,40)
    sleep (5)
    
    P1.off()
    P2.off()
    refresh_oled("No rotation",15,20,"Motor speed:0%",0,40)
    sleep(3)
    
    P1.off()
    P2.on()
    refresh_oled("Reverse rotation",0,20,"Motor speed:50%",0,40)
    sleep(5)
    
    P1.off()
    P2.off()
    refresh_oled("No rotation",15,20,"Motor speed:0%",0,40)
    sleep(3)
    
    P1.on()
    P2.off()
    motor.duty(256)
    refresh_oled("Forward rotation",0,20,"Motor speed:25%",0,40)
    sleep (5)
    
    P1.off()
    P2.off()
    refresh_oled("No rotation",15,20,"Motor speed:0%",0,40)
    sleep(3)
    
    P1.off()
    P2.on()
    refresh_oled("Reverse rotation",0,20,"Motor speed:25%",0,40)
    sleep(5)
    
    P1.off()
    P2.off()
    refresh_oled("No rotation",15,20,"Motor speed:0%",0,40)
    sleep(3)
    
