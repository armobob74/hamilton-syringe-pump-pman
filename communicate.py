import serial

syringe_size = 50 # mL
resolution = 3000 # standard config
syringe_usability = 0.9 # can use 90% of syringe before facing issues
max_draw_volume = syringe_usability * syringe_size
max_height = int(syringe_usability * resolution)
#serial_port = '/dev/ttyUSB0'
serial_port = '/dev/pts/7'
baud_rate = 9600
address = '0' # set on machine physically

class Communicator:
    def transfer_command_string(self, from_port, to_port, volume):
        """
        Prepare the <Data> to be sent to the pump
        inputs:
            from_port -- the input port
                range: 1 to 8
            to_port -- the output port
                range: 1 to 8
            volume -- volume to transfer
                units: mL
        """
        full_transfers = ''
        if volume > max_draw_volume:
            loops = int(volume // max_draw_volume)
            full_transfers = f'gI{from_port}A{max_height}O{to_port}A0G{loops}'
    
        remainder = volume % max_draw_volume
        partial_transfer_steps = int((remainder / syringe_size) * resolution)
        if remainder == 0:
            partial_transfers = ''
        else:
            partial_transfers = f"I{from_port}A{partial_transfer_steps}O{to_port}A0"
        return partial_transfers + full_transfers
    
    def terminal_protocal_command(self, data, address=address):
        """
        given a <Data> string, prepare a command following the terminal protocol in section 4.2 of the manual:
        /<addr><Data><CR>
        """
        return f"/{address}{data}\r"

    def parse_return_string(self, return_string):
        """
        Parse the return string in the format "/0<Status Byte><Data><ETX><CR><LF>".

        Args:
        return_string (str): The return string from the machine.

        Returns:
        dict: A dictionary containing the status byte and data.
        """
        ETX = '\x03' # end of text character

        if return_string.startswith("/0") and return_string.endswith("\r\n"):
            # Extract content between /0 and <CR><LF>
            content = return_string[2:-2]
            etx_position = content.find(ETX)
            return {"status_byte": content[:etx_position], "data": content[etx_position + 1:]}

        raise ValueError("Invalid return string format")

    def send(self,data):
        """
        Turn the 'data' string into a command and send it
        First response acknowledges that the command was recieved
        """
        command_string = self.terminal_protocal_command(data, address=address)
        with serial.Serial(serial_port, baud_rate, timeout=5) as pump:
            pump.write(command_string.encode())
            first_response = pump.read_until(b'\r\n')
        return first_response.decode()

    def readAnswer(self):
        """
        read the answer from the pump
        """
        with serial.Serial(serial_port, baud_rate, timeout=5) as pump:
            response = pump.read_until(b'\r\n')
        return response

    def queryStatus(self):
        data = 'Q'
        response = self.send(data)
        print('response:',response)

if __name__ == "__main__":
    com = Communicator()
    com.queryStatus()
