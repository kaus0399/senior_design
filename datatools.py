# import gpiozero

class Microphone(object):
    def __init__(self, time: int, lc: int, hc: int, pin: int, status = False):
        self.time = time
        self.pin = pin
        self.status = status

    def record(self):
        # print(self.pin)
        # print(self.status)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.IN)
        
        while True:
            if GPIO.input(10):
                print('Noisy')
            else:
                print('Quiet')
            time.sleep(0.1)


    # def print_time(self):
    #     print(self.time)
    #     print(self.status)


# class Button(object):
#     def __init__(self, status):
#         self.time = time
#         self.status = False



# #Object : Microphone
# Time 
# Frequency (lc,hc)
# Measurement 
# Processsing
# Status: False
# if TImer == 0 .. set True


# #Button Object 
# Boolean (Button) True or False
# Track status of boolean


# While at least one microphone False:
#     Keep going 

# If all microphones True:
#     terminate 





