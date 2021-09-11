
class Radio:
    Color = "Brown"
    Brand = "Philips"
    ACpower = False
    headphone = False
   
    def __init__(self):
        self.power_led = "ON"
        self.mode_led = None
        self.frequency = 0.0
        self.volume = 0

    def power_switch (self,power):
        self.power_led = power
        print("Your radio is turned " + str(self.power_led))
    def mode_switch (self,mode):
        self.mode_led = mode
        print("Your radio mode is set to " + str(self.mode_led))
    def Band_tuner (self,frequency_value):
        self.frequency = frequency_value
        print("Your radio frequency is set to " + str(self.frequency))
    def Volume_tuner (self,volume_value):
        self.volume = volume_value
        print("Your radio volume is set to " + str(self.volume))
my_radio = Radio()
print("Your Radio is ready to use..")
print("colour of Radio is " + str(Radio.Color))
print("brand of Radio is " + str(Radio.Brand))
my_radio.power_switch("ON")
my_radio.mode_switch("FM")
my_radio.Band_tuner(102.2)
my_radio.Volume_tuner(8)
my_radio.power_switch("OFF")
my_radio = None