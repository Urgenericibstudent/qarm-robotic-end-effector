# !/usr/bin/env python3
# coding: utf-8
# --------------------------------------------------------------------------------

import sys

sys.path.append("../")

from time import sleep
from Common.qarm_interface_wrapper import *

GRIPPER_IMPLEMENTATION = 1
arm = QArmInterface(GRIPPER_IMPLEMENTATION)
scan_barcode = BarcodeScanner.scan_barcode

# --------------------------------------------------------------------------------
# STUDENT CODE BEGINS
# ---------------------------------------------------------------------------------
arm.home()

"""
def pack_products(product_list):
    for i in range(0,len(product_list),1):
        if product_list[i]=="Sponge":
            arm.home()
            arm.rotate_base(20)
            arm.rotate_shoulder(10)
            arm.rotate_gripper(20)
        if product_list[i]=="Bottle":
            arm.home()
            arm.rotate_base(20)
            arm.rotate_shoulder(10)
            arm.rotate_gripper(20)
        if product_list[i]=="Rook"
            arm.home()
            arm.rotate_base(20)
            arm.rotate_shoulder(10)
            arm.rotate_gripper(20)
        if product_list[i] == "D12":
            arm.home()
            arm.rotate_base(20)
            arm.rotate_shoulder(10)
            arm.rotate_gripper(20)
        if product_list[i]=="WitchHat":
            arm.home()
            arm.rotate_base(20)
            arm.rotate_shoulder(10)
            arm.rotate_gripper(20)
        if product_list[i]=="Bowl":
            arm.home()
            arm.rotate_base(20)
            arm.rotate_shoulder(10)
            arm.rotate_gripper(20)
        if product_list[i]=="Labubu":
"""

while True:
    #
    items=scan_barcode()
    item_list=items.split(" ")
    for i in range(0,len(item_list),1):

        if item_list[i]=="Sponge":
            arm.home()
            arm.rotate_base(20)
            arm.rotate_elbow(-12)
            arm.rotate_shoulder(45)
            arm.home()
            arm.rotate_base(-55)
            arm.rotate_elbow(20)

        if item_list[i]=="Bottle":
            arm.home()
            arm.rotate_base(14)
            arm.rotate_elbow(-12)
            arm.rotate_shoulder(45)
            arm.home()
            arm.rotate_base(-55)
            arm.rotate_elbow(20)

        if item_list[i]=="Rook":
            arm.home()
            arm.rotate_elbow(-12)
            arm.rotate_base(7)
            arm.rotate_shoulder(50)
            sleep(5)
            arm.home()
            arm.rotate_base(-55)
            arm.rotate_elbow(20)

        if item_list[i]=="D12":
            arm.home()
            arm.rotate_elbow(-12)
            arm.rotate_base(-5)
            arm.rotate_shoulder(50)
            sleep(5)
            arm.home()
            arm.rotate_base(-55)
            arm.rotate_elbow(20)

        if item_list[i]=="WitchHat":
            arm.home()
            arm.rotate_elbow(-12)
            arm.rotate_base(-9)
            arm.rotate_shoulder(50)
            sleep(5)
            arm.home()
            arm.rotate_base(-55)
            arm.rotate_elbow(20)

        if item_list[i]=="Bowl":
            arm.home()
            arm.rotate_elbow(-15)
            arm.rotate_base(-16)
            arm.rotate_shoulder(51)
            sleep(5)
            arm.home()
            arm.rotate_base(-55)
            arm.rotate_elbow(20)


#pack_products()













# ---------------------------------------------------------------------------------
# STUDENT CODE ENDS
# ---------------------------------------------------------------------------------

arm.end_arm_connection()
