
"""
Routes here are meant to be called by a PMAN runner
"""
import json
from flask import Blueprint, request,current_app
from serial import SerialException

pman = Blueprint('pman', __name__,url_prefix='/pman')

@pman.errorhandler(SerialException)
def handle_serial_exception(error):
    d = {'status':'Serial Error','message':"There has been a SerialException. Is device connected? Are permissions set?"}
    return d

@pman.route('/transfer', methods=['POST'])
def pmanTransfer():
    port = current_app.config['HOST_PORT']
    activeConfig = ActiveConfig.query.filter_by(port=port).first()
    config = Config.query.filter_by(name=activeConfig.name).first()

    syringe_size = config.syringe_volume_ml
    N = int(config.microstep_resolution)

    d = json.loads(request.data)
    args = d['args']

    from_port = int(args[0])
    to_port = int(args[1])
    vol = float(args[2])
    transfer = Sequence.Transfer(from_port,to_port,vol,syringe_size,N)
    communicator = Communicator(config.com_port, config.addr,timeout=1000)
    current_app.config['hardstop'] = communicator.hardstop # enable hardstop to access com port and end the blocking listen
    response_1 = communicator.send(str(transfer)+'R') # tells you that process has started
    response_2  = communicator.readAnswer() # tells you that process has ended
    current_app.config['hardstop'] = None # clear this object so that hardstop does not try to close a listen that does not exist
    return response_2

@pman.route('/hardstop', methods=['GET', 'POST'])
def cancelRead():
    if current_app.config['hardstop']:
        response = current_app.config['hardstop']()
        current_app.config['hardstop'] = None
    else:
        port = current_app.config['HOST_PORT']
        activeConfig = ActiveConfig.query.filter_by(port=port).first()
        config = Config.query.filter_by(name=activeConfig.name).first()
        communicator = Communicator(config.com_port, config.addr,timeout=1000)
        response = communicator.send('T')
    return response
