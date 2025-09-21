##################################################################################
# Copyright (c) 2025 Matthew Thomas Beck                                         #
#                                                                                #
# Licensed under the Creative Commons Attribution-NonCommercial 4.0              #
# International (CC BY-NC 4.0). Personal and educational use is permitted.       #
# Commercial use by companies or for-profit entities is prohibited.              #
##################################################################################





##########################################################
############### IMPORT/CREATE DEPENDENCIES ###############
##########################################################


########## IMPORT DEPENDENCIES ##########

##### import necessary libraries #####

import time # import time library for gait timing
import logging # import logging library for debugging





#####################################################
############### CREATE CONFIGURATIONS ###############
#####################################################


########## UTILITY CONFIGURATIONS ##########

##### set logging configuration #####

LOG_CONFIG = {
    'LOG_PATH': "/Robot_Dog/robot_dog.log", # TODO change me!
    'LOG_LEVEL': logging.INFO # set log level to logging.<DEBUG, INFO, WARNING, ERROR, or CRITICAL>
}

########## CAMERA CONFIGURATION ##########

##### set camera configuration #####

CAMERA_CONFIG = {
    'FOV': 75, # degrees
    'CAMERA_WIDTH': 4608,
    'CAMERA_HEIGHT': 2592,
    'FOV_HORIZONTAL': 66,  # degrees
    'FOV_VERTICAL': 41,  # degrees
    'PIXEL_SIZE_UM': 1.4,  # pixel size in micrometers
    'DEPTH_OF_FIELD': 0.1,  # depth of field distance in meters
    'APERTURE_RATIO': 1.8,
    'WIDTH': 640, # width of the camera image
    'HEIGHT': 480, # height of the camera image
    'FRAME_RATE': 30, # frame rate of the camera in frames per second
    'CROP_FRACTION': 0.5, # fraction of the image to crop from each side (0.0 to 1.0)
    'OUTPUT_WIDTH': 128, # width of the ML image
    'OUTPUT_HEIGHT': 48, # height of the image for ML inference
}


########## INFERENCE CONFIGURATIONS ##########

##### set ML configurations #####

INFERENCE_CONFIG = {
    'TPU_NAME': "MYRIAD",  # literal device name in code
    'MODEL_PATH': "/home/matthewthomasbeck/Projects/Robot_Dog/model/person-detection-0200.xml",  # TODO change me!
}


########## ROBOT CONTROL CONFIGURATIONS (internet and radio) ##########

##### declare movement channel GPIO pins #####

SIGNAL_TUNING_CONFIG = { # dictionary of signal tuning configuration for sensitivity
    'JOYSTICK_THRESHOLD': 40, # number of times condition must be met to trigger a request on a joystick channel
    'TOGGLE_THRESHOLD': 40, # number of times condition must be met to trigger a request on a button channel
    'TIME_FRAME': 0.10017, # time frame for condition to be met, default: 0.100158
    'DEADBAND_HIGH': 1600, # deadband high for PWM signal
    'DEADBAND_LOW': 1400 # deadband low for PWM signal
}

##### set receiver channels #####

RECEIVER_CHANNELS = { # dictionary of receiver channels' names, GPIO pins, and states
    'channel_0': {'name': 'tilt_up_down', 'gpio_pin': 17, 'counter': 0, 'timestamp': time.time()},
    'channel_1': {'name': 'trigger_shoot', 'gpio_pin': 27, 'counter': 0, 'timestamp': time.time()},
    'channel_2': {'name': 'squat_up_down', 'gpio_pin': 22, 'counter': 0, 'timestamp': time.time()},
    'channel_3': {'name': 'rotate_left_right', 'gpio_pin': 5, 'counter': 0, 'timestamp': time.time()},
    'channel_4': {'name': 'look_up_down', 'gpio_pin': 6, 'counter': 0, 'timestamp': time.time()},
    'channel_5': {'name': 'move_forward_backward', 'gpio_pin': 13, 'counter': 0, 'timestamp': time.time()},
    'channel_6': {'name': 'shift_left_right', 'gpio_pin': 19, 'counter': 0, 'timestamp': time.time()},
    'channel_7': {'name': 'extra_channel', 'gpio_pin': 26, 'counter': 0, 'timestamp': time.time()},
}

##### set receiver configuration #####

MAESTRO_CONFIG = {
    'SERIAL_PATH': "/dev/serial0", # set serial port name to first available
    'SERIAL_BAUD_RATE': 9600, # set baud rate for serial connection
    'SERIAL_TIMEOUT': 1 # set timeout for serial connection
}


########## PHYSICAL CONFIGURATION ##########

##### set accelerometer configuration #####

ACCELEROMETER_CONFIG = { # dictionary of accelerometer configuration

    'MPU_6050_ADDRESS': 0x68, # address of the accelerometer
    'PWR_MGMT_1': 0x6B, # power management register
    'SMPLRT_DIV': 0x19, # sample rate divider
    'CONFIG_REGISTER': 0x1A, # configuration register
    'GYRO_CONFIG': 0x1B, # gyro configuration register
    'INT_ENABLE': 0x38, # interrupt enable register
    'ACCEL_XOUT_H': 0x3B, # accelerometer x-axis output high register
    'ACCEL_YOUT_H': 0x3D, # accelerometer y-axis output high register
    'ACCEL_ZOUT_H': 0x3F, # accelerometer z-axis output high register
    'GYRO_XOUT_H': 0x43, # gyroscope x-axis output high register
    'GYRO_YOUT_H': 0x45, # gyroscope y-axis output high register
    'GYRO_ZOUT_H': 0x47 # gyroscope z-axis output high register
}