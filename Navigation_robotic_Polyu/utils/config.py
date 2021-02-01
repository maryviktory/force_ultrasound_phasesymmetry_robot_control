from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
# import yaml

import numpy as np
from easydict import EasyDict as edict


config = edict()
config.Mode_Develop = False #Allows to launch code without robot
config.IP_ADRESS = "158.132.172.194"
config.FOV = 0.045 #Field of view of the robot
config.alpha = 0.5

config.w = 400
config.hg = 360
config.Trajectory_n = '3probe'

config.FORCE = edict()

config.FORCE.Fref_first_move = 4 #Force [N]
config.FORCE.Fref = 6 #Force [N]
config.FORCE.Fmax = 20 #Force [N]
config.FORCE.Fcrit = 30 #Force [N]
config.FORCE.K_delta = 0.0005
config.FORCE.Kf = 0.002
config.FORCE.Kz = 0.6
config.FORCE.v = 0.007 #move first point
config.FORCE.a = 0.01 #move first point
config.FORCE.thr = 0.004
