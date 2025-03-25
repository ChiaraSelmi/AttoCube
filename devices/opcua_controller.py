'''
Authors
  - C. Selmi:  written in March 2025
'''

import numpy as np
from opcua import Client

server = "opc.tcp://192.168.11.151:4840"
time_node = "ns=4;s=MAIN.sTel.Epoch"
attocube_node = "ns=4;s=MAIN.sTel.Attocube_SI"

class OpcUaController():
  """
  Function exporting variable via OpcUa from TwinCAT solution

  HOW TO USE IT::

    from AttoCube.devices.opcua_controller import OpcUaController
    plc = OpcUaController()
    plc.get_blabla()
    plc.disconnect()
  """

  def __init__(self):
    """The constructor """
    self._client = Client(url=server)
    self._client.connect()

  def get_absolute_time(self):
    """ Absolute time, according to the PLC clock"""
    node = self._client.get_node(time_node)
    absolute_time = node.get_value()
    return absolute_time

  def get_all_attocube_measurements_in_SI(self):
    """ Get the SI value (pm) for all the attocubes"""
    node = self._client.get_node(attocube_node)
    attocube_positions = node.get_value()
    return np.array(attocube_positions)
  
  def get_attocube_meas_in_SI(self, attocube_number, axis_number):
    all_meas = self.get_all_attocube_measurements_in_SI()
    if attocube_number == 1:
      if axis_number == 1:
        my_meas = all_meas[0]
      elif axis_number == 2:
        my_meas = all_meas[1]
      elif axis_number == 3:
        my_meas = all_meas[2]
      else:
        raise Exception("Axis_number selected does not exist")
    elif attocube_number == 2:
      if axis_number == 1:
        my_meas = all_meas[3]
      elif axis_number == 2:
        my_meas = all_meas[4]
      elif axis_number == 3:
        my_meas = all_meas[5]
      else:
        raise Exception("Axis_number selected does not exist")
    elif attocube_number == 3:
      if axis_number == 1:
        my_meas = all_meas[6]
      elif axis_number == 2:
        my_meas = all_meas[7]
      elif axis_number == 3:
        my_meas = all_meas[8]
      else:
        raise Exception("Axis_number selected does not exist")
    elif attocube_number == 4:
      if axis_number == 1:
        my_meas = all_meas[9]
      elif axis_number == 2:
        my_meas = all_meas[10]
      elif axis_number == 3:
        my_meas = all_meas[11]
      else:
        raise Exception("Axis_number selected does not exist")
    else:
      raise Exception("Attocube_number selected does not exist")
    return my_meas
  
  def disconnect(self):
    self._client.disconnect()
    return  

