import pyfirmata
board = pyfirmata.Arduino('com3')
iterator = pyfirmata.util.Iterator('board')
iterator.start()
led1 = board.get_pin('d:3:o')
led2 = board.get_pin('d:7:o')
buz = board.get_pin('d:11:o')
a = 1
def led(x):
    if x == 1:
        led1.write(0)
        led2.write(1)
        buz.write(1)

    else:
        led1.write(1)
        led2.write(0)
        buz.write(0)


    
  
