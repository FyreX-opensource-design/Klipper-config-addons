import os

#these two values should be set to your extruders rotation distance, they're needed for calculations later
extruder1_rot = 8
extruder2_rot = 8

if float(A) + float(B) > 1:
    os.system("echo M118 values are greater than 1")

if float(A) or float(B) == 1:
    os.system("echo SYNC_EXTRUDER_MOTION EXTRUDER=extruder MOTION_QUEUE= > tmp/printer")
    os.system("echo SYNC_EXTRUDER_MOTION EXTRUDER=extruder1 MOTION_QUEUE= > tmp/printer")
    if float(A) == 1:
        os.system("echo SET_EXTRUDER_ROTATION_DISTANCE EXTRUDER=extruder DISTANCE=" + extruder1_rot + " > tmp/printer")
        os.system("echo SET_EXTRUDER_ROTATION_DISTANCE EXTRUDER=extruder1 DISTANCE=0 > tmp/printer")
    elif float(B) == 1:
        os.system("echo SET_EXTRUDER_ROTATION_DISTANCE EXTRUDER=extruder1 DISTANCE=" + extruder2_rot + " > tmp/printer")
        os.system("echo SET_EXTRUDER_ROTATION_DISTANCE EXTRUDER=extruder DISTANCE=0 > tmp/printer")
else:
    os.system("echo SET_EXTRUDER_ROTATION_DISTANCE EXTRUDER=extruder DISTANCE=" + extruder1_rot / (float(A) * 10) + " > tmp/printer")
    os.system("echo SET_EXTRUDER_ROTATION_DISTANCE EXTRUDER=extruder1 DISTANCE=" + extruder2_rot / (float(B) * 10) + " > tmp/printer")
    os.system("echo SYNC_EXTRUDER_MOTION EXTRUDER=extruder MOTION_QUEUE=mixing > tmp/printer")
    os.system("echo SYNC_EXTRUDER_MOTION EXTRUDER=extruder1 MOTION_QUEUE=mixing > tmp/printer")
