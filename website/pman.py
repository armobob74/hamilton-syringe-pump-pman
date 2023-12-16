
"""
Routes here are meant to be called by a PMAN runner
"""
import json
from flask import Blueprint, request,current_app
from serial import SerialException
from communicate import Communicator

pman = Blueprint('pman', __name__,url_prefix='/pman')

@pman.errorhandler(SerialException)
def handle_serial_exception(error):
    d = {'status':'Serial Error','message':"There has been a SerialException. Is device connected? Are permissions set?"}
    return d

@pman.route('/transfer', methods=['POST'])
def pmanTransfer():
    d = json.loads(request.data)
    args = d['args']
    from_port = int(args[0])
    to_port = int(args[1])
    vol = float(args[2])
    communicator = Communicator()
    transfer = communicator.transfer_command_string(from_port, to_port, vol)
    response_1 = communicator.send(str(transfer))
    return response_1

@pman.route('/listen', methods=['POST'])
def pmanListen():
    communicator = Communicator()
    response = communicator.readAnswer()
    return response
