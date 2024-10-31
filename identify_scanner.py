import usb.core     # main module

import usb.util     # contains utility functions

import string

 

 

VENDOR_ID = 0x0c2e  # Vendor ID for the device

PRODUCT_ID = 0x0b01  # Product ID for the device

 

while True:

    try:

        # find our device using vendor ID and Product ID

        dev = usb.core.find(idVendor=VENDOR_ID, idProduct=PRODUCT_ID)

        print(dev)

    except usb.core.USBTimeoutError as timeOutError:

        print("Scanner Read Time Out Occurred \n")

        print("Closing device Object and")

       

 

    except Exception as e:

        print(f"The following exception has occurred {e} \n . Retrying.........")

        