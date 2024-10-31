import sys
import usb.core
import usb.util

VENDOR_ID = 0x0c2e  # Vendor ID for the device

PRODUCT_ID = 0x0b01  # Product ID for the device

dev = usb.core.find(idVendor=VENDOR_ID, idProduct=PRODUCT_ID)

if dev.is_kernel_driver_active(0):
    try:
        dev.detach_kernel_driver(0)
    except usb.core.USBError as e:
        sys.exit("Could not detach kernel driver: %s" % str(e))