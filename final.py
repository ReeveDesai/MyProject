import math
import sys
import time
from grove.adc import ADC

class GroveGSRSensor:

    def __init__(self, channel):
        self.channel = channel
        self.adc = ADC()

    @property
    def GSR(self):
        value = self.adc.read(self.channel)
        return value

def write_to_file(sensor, file):
    gsr_value = sensor.GSR
    file.write(str(gsr_value)+'\n')

def main():
    if len(sys.argv) < 2:
        print('Usage: {} adc_channel'.format(sys.argv[0]))
        sys.exit(1)

    sensor = GroveGSRSensor(int(sys.argv[1]))

    print('Detecting...')
    gsr_values = []
    print('Taking readings...')
    for i in range(30):
        gsr_value = sensor.GSR
        gsr_values.append(gsr_value)
        time.sleep(1)

    average = sum(gsr_values) / len(gsr_values)
    hydration_threshold = 300
    dehydration_threshold = 500
    if(average <= hydration_threshold):
        print("Hydrated")
    elif(average <= dehydration_threshold):
        print("Dehydrated")
    else:
        print("Normal")

if __name__ == '__main__':
    main()
