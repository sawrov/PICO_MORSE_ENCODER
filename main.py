from machine import Pin
import utime

led = Pin(25,Pin.OUT)
unit_time=0.075
def dot(led):
    led.value(1)
    utime.sleep(unit_time)
    led.value(0)
    utime.sleep(unit_time)


def dash(led):
    led.value(1)
    utime.sleep(unit_time*3)
    led.value(0)
    utime.sleep(unit_time)


def element_spacing(led):
    utime.sleep(unit_time*2)

def word_spacing(led):
    utime.sleep(unit_time*4)
    

morse_dict = { 'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 'H':'....', 
                'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.',
                'Q':'--.-','R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 
                'X':'-..-', 'Y':'-.--', 'Z':'--..', '1':'.----', '2':'..---', '3':'...--', 
                '4':'....-', '5':'.....', '6':'-....','7':'--...', '8':'---..', '9':'----.',
                '0':'-----', ', ':'--..--', '.':'.-.-.-', '?':'..--..', '/':'-..-.', '-':'-....-', 
                '(':'-.--.', ')':'-.--.-'}
led.value(0)
plain_text=input("Enter string to Encode!\n").upper()
for element in plain_text:
    try:
        for char in (morse_dict[element]):
            if (char == "."):
                dot(led)
            elif (char == "-"):
                dash(led)
            element_spacing(led)
    except KeyError:
        if (element==" "):
            word_spacing(led)
        else:
            print ("Cannot Encode the character:"+ element)
    
        

