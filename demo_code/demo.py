# -*_ coding: utf-8 -*-
import serial
import time

main_pump_address = '1'
waste_pump_address = '2'
p_speed = str(10)
p_step = str(100)  # arbitrary

# b metering
b_speed = str(100)
b_step = str(250)  # arbitrary

# Concatenate strings
p_cmd = '/' + main_pump_address + 'V' + p_speed + 'P' + p_step + 'R\r\n'
b_cmd = '/' + main_pump_address + 'V' + b_speed + 'P' + b_step + 'R\r\n'

# set a different value for responseBit

responseBit = 'A'

#update the COM ports to your own setup

with serial.Serial('COM3', 9600, timeout=5) as main_pump, \
        serial.Serial('COM6', 9600, timeout=5) as waste_pump:
    print(main_pump.name)
    print(waste_pump.name)

 # Pump Step 1
    main_pump.write(bytes(p_cmd, 'utf-8'))
    print(p_cmd)

# Pump step 2
    main_pump.write(bytes(b_cmd, 'utf-8'))
    print(b_cmd)
