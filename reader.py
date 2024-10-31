import usb.core

dev = usb.core.find(idVendor=0x0c2e, idProduct=0x0b01)
ep=dev[0].interfaces()[0].endpoints()[0]
i=dev[0].interfaces()[0].bInterfaceNumber
dev.reset()

if dev.is_kernel_driver_active(i):
    dev.detach_kernel_driver(i)

dev.set_configuration()

eaddr = ep.bEndpointAddress
r = dev.read(eaddr, 64)
print(r)
