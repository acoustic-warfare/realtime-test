import ctypes
#Do not edit this config file! Add constants and expressions in config.json and build with make. 

#General constants for both c and python.
N_MICROPHONES = 192
N_SAMPLES = 128
UDP_PORT = 21844
UDP_IP = "10.0.0.1"
BUFFER_LENGTH = N_SAMPLES * N_MICROPHONES

#Python specific constants
azimuth = 0.0
elevation = 0.0
columns = 8
rows = 8
distance = 0.02
fs = 48828
propagation_speed = 340.0
TIMEOUT = 30
DTYPE = ctypes.c_int32
