import usb.core

import usb.util

import time

import sys

 

VENDOR_ID = 0x0c2e  # Replace with your scanner's vendor ID

PRODUCT_ID = 0x0b01  # Replace with your scanner's product ID


 

def read_scanner(dev):

    try:

        # Set the active configuration. With no arguments, the first

        # configuration will be the active one

        # dev.set_configuration()


 

        # Claim the interface

        usb.util.claim_interface(dev, 0)


 

        # Endpoint address and size depend on the specific scanner, you may need to adjust them

        endpoint = 0x87

        size = 0x08  # Adjust the size as needed


 

        while True:

            # Read data from the endpoint

            data = dev.read(endpoint, size, timeout=1000)


 

            # Process the scanned data (replace this with your desired processing logic)

            scanned_code = data.tobytes().decode('utf-8')

            print(f"Scanned code: {scanned_code}")
            print(data)


 

    except usb.core.USBError as e:

        if "Access denied" in str(e):

            print("Access denied. Make sure you have the necessary permissions.")

        else:

            print(f"USB error: {e}")


 

    except usb.core.USBTimeoutError as timeOutError:

        print("Scanner Read Time Out Occurred")


 

    except Exception as e:

        print(f"An exception occurred: {e}")


 

    finally:

        # Release the interface

        try:

            usb.util.release_interface(dev, 0)

        except usb.core.USBError as e:

            print(f"Error releasing interface: {e}")


 

        # Close the device object to release resources

        usb.util.dispose_resources(dev)


 

if __name__ == "__main__":

    while True:

        try:

            # find our device using vendor ID and Product ID

            dev = usb.core.find(idVendor=VENDOR_ID, idProduct=PRODUCT_ID)

            if dev.is_kernel_driver_active(0):
                try:
                    dev.detach_kernel_driver(0)
                except usb.core.USBError as e:
                    sys.exit("Could not detatch kernel driver from interface({0}): {1}".format(1, str(e)))



 

            if dev is not None:

                print("Device found:")

                # print(dev)

                read_scanner(dev)

            else:

                print("Device not found.")


 

        except Exception as e:

            print(f"An exception occurred: {e}")


 

        # Add a delay before the next iteration

        time.sleep(1)