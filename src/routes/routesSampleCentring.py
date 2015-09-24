from flask import session, redirect, url_for, render_template, request, Response
from .. import app as mxcube
import time, logging, collections


###----SSE SAMPLE VIDEO STREAMING----###
keep_streaming = True


def sse_pack(d):
    """Pack data in SSE format"""
    buffer = ''
    for k in ['retry', 'id', 'event', 'data']:
        if k in d.keys():
            buffer += '%s: %s\n' % (k, d[k])
    return buffer + '\n'
msg = {'retry': '1000'}
msg['event'] = 'message'


def stream_video():
    """it just send a message to the client so it knows that there is a new image. A HO is supplying that image"""
    event_id = 0
    logging.getLogger('HWR').info('[Stream] Camera video streaming started')
    while keep_streaming:
        mxcube.diffractometer.camera.new_frame.wait()
        im = mxcube.diffractometer.camera.new_frame.get()
        msg.update({
         'event': 'update',
         'data': im,
         'id': event_id
        })
        print "mezu bat", str(event_id), str(len(im))
        yield sse_pack(msg)
        event_id += 1
        #gevent.sleep(0.08)
        time.sleep(1)

@mxcube.route("/mxcube/api/v0.1/samplecentring/camera/subscribe", methods=['GET'])
def subscribeToCamera():
    """SampleCentring: subscribe to the streaming
    data = {generic_data} #or nothing?
    return_data={"url": url}
    """
    #data = dict(request.POST.items())
    logging.getLogger('HWR').info('[Stream] Camera video streaming going to start')
    return Response(stream_video(), mimetype="text/event-stream")

@mxcube.route("/mxcube/api/v0.1/samplecentring/camera/unsubscribe", methods=['GET'])
def unsubscribeToCamera():
    """SampleCentring: subscribe from the streaming
    data = {generic_data} #or nothing?
    return_data={"result": True/False}
    """
    keep_streaming = False
    return "True"

###----SAMPLE CENTRING----###
clicks = collections.deque(maxlen=3)
####
#To access parameters submitted in the URL (?key=value) you can use the args attribute:
#searchword = request.args.get('key', '')
@mxcube.route("/mxcube/api/v0.1/samplecentring/<id>/move", methods=['PUT'])
def moveSampleCentringMotor(id):
    """SampleCentring: move "id" moveable to the position specified in the data:position
    Moveable can be a motor (kappa, omega, phi), a ligth, light/zoom level.
    data = {generic_data, "moveable": id, "position": pos}
    return_data={"result": True/False}
    """
    new_pos = request.args.get('newpos','')
    motor_hwobj = mxcube.diffractometer.getObjectByRole(id.lower())
    logging.getLogger('HWR').info('[SampleCentring] Movement called for motor: "%s", new position: "%s"' %(motor, str(new_pos)))

    #the following if-s to solve inconsistent movement method
    try:
        if motor_hwobj.motor_name == 'Zoom':
            motor_hwobj.moveToPosition(new_pos)
        elif motor_hwobj.motor_name == 'Light':
            if new_pos: motor.wagoIn()
            else: motor.wagoOut()
        else: 
            motor_hwobj.move(new_pos)
    except Exception as ex:
        print ex.value
        return "False"
    logging.getLogger('HWR').info('[SampleCentring] Movement finished for motor: "%s", current position: "%s"' %(motor_hwobj.motor_name, str(motor_hwobj.getPosition()))) #zoom motor will fail in getPosition(), perhaps an alias there?
    return "True"

@mxcube.route("/mxcube/api/v0.1/samplecentring/status", methods=['GET'])
def get_status():
    """SampleCentring: get generic status, positions of moveables ...
    data = {generic_data}
    return_data = { generic_data, 
                  Moveable1:{'Status': status, 'position': position}, 
                  ...,  
                  MoveableN:{'Status': status, 'position': position} 
                  }
    """
    motors = ['Kappa', 'Omega', 'Phi', 'Zoom', 'Light'] #more are needed

    data = {}
    for mot in motors:
        motor_hwobj = mxcube.diffractometer.getObjectByRole(mot.lower())
        if mot == 'Zoom':
            pos = motor_hwobj.getCurrentPositionName()
            status = "unknown" 
        elif mot == 'Light':
            pos = motor_hwobj.getWagoState() # {0:"out", 1:"in", True:"in", False:"out"}
            status = motor_hwobj.getWagoState()
        else: 
            pos = motor_hwobj.get_position()
            status = motor_hwobj.get_state()

        data[mot] = {'Status': status, 'position': pos}    

    return data
    
@mxcube.route("/mxcube/api/v0.1/samplecentring/<id>/status", methods=['GET'])
def get_status_of_id(id):
    """SampleCentring: get status of element with id:"id"
    data = {generic_data, 'Moveable1', ..., MoveableN}
    return_data = {'Status': status, 'position': position}
    """
    data = {}
    motor = mxcube.diffractometer.getObjectByRole(id.lower())

    if motor.motor_name == 'Zoom':
        pos = motor.getCurrentPositionName()
        status = "unknown" 
    elif motor.motor_name == 'Light':
        pos = motor.getWagoState() # {0:"out", 1:"in", True:"in", False:"out"}
        status = motor.getWagoState()
    else: 
        pos = motor.get_position()
        status = motor.get_state()
    
    data[motor_name] = {'Status': status, 'position': pos}

    return data

@mxcube.route("/mxcube/api/v0.1/samplecentring/centring/<id>", methods=['GET'])
def get_centring_of_id(id):
    """SampleCentring: get centring point position of point with id:"id", id=1,2,3...
    data = {generic_data, "point": id}
    return_data = {"id": {x,y}}
    """
    return "True"

@mxcube.route("/mxcube/api/v0.1/samplecentring/centring/<id>", methods='POST')
def put_centring_with_id(id):
    """SampleCentring: set centring point position of point with id:"id", id=1,2,3...
    data = {generic_data, "point": id, "position": {x,y}}
    return_data={"result": True/False}
    """
    data = dict(request.POST.items())
    clicks.append([data['PosX'],data['PosY']])
    return "True"

@mxcube.route("/mxcube/api/v0.1/samplecentring/centre", methods=['PUT'])
def centre():
    """Start centring procedure
    data = {generic_data, "Mode": mode}
    return_data={"result": True/False}
    """
    return "True"

@mxcube.route("/mxcube/api/v0.1/samplecentring/snapshot", methods=['PUT'])
def snapshot():
    """Save snapshot of the sample view
    data = {generic_data, "Path": path} # not sure if path should be available, or directly use the user/proposal path
    return_data={"result": True/False}
    """
    return "True"
