import pyfirmata as pf

import time


ard = pf.Arduino('COM6')

ard.get_pin('d:13:o') #디지털핀 13번을 출력으로 설정

while True:

    ard.digital[13].write(1)

    time.sleep(0.5)

    ard.digital[13].write(0)

    time.sleep(0.5)

