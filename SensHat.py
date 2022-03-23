from sense_emu import SenseHat

def display_readings(hat):
    
    #data preparation needed
    hat.set_pixels([pixel for row in screen for pixel in row])

hat = SenseHat()

while True:
    display_readings(hat)
    sleep(0.1)