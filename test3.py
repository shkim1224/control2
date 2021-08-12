import pyfirmata


DELAY = 1

MIN = 5

MAX = 175

MID = 90


board = pyfirmata.Arduino('COM6')


servo = board.get_pin('d:11:s') #11번핀을 서보모터 신호선으로 설정

 

def move_servo(v):

    servo.write(v)

    board.pass_time(DELAY)


move_servo(MIN)

move_servo(MAX)

move_servo(MID)


board.exit()