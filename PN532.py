import NFC_PN532 as nfc
from machine import Pin, SPI

# SPI
spi_dev = SPI(2, baudrate=1000000, sck=Pin(25), mosi=Pin(26), miso=Pin(33))
cs = Pin(14, Pin.OUT)
cs.on()


# SENSOR INIT
pn532 = nfc.PN532(spi_dev,cs)
def init():
#     # SPI
#     spi_dev = SPI(2, baudrate=1000000, sck=Pin(25), mosi=Pin(26), miso=Pin(27))
#     cs = Pin(14, Pin.OUT)
#     cs.on()
#     
# 
#     # SENSOR INIT
#     pn532 = nfc.PN532(spi_dev,cs)
    ic, ver, rev, support = pn532.get_firmware_version()
    print('Found PN532 with firmware version: {0}.{1}'.format(ver, rev))

    # Configure PN532 to communicate with MiFare cards
    pn532.SAM_configuration()


def access():
    last_uid = None
    while True:
        # Check if a card is available to read
        uid = pn532.read_passive_target()
        # Try again if no card is available
        if uid is None:
            last_uid = None
            continue
        if last_uid == uid:
            pass
        else:
            print("Found card with UID:", [hex(i) for i in uid])
            # Format short string showing UID
            suid = ""
            for i in uid:
                if len(suid) > 0:
                    suid += ":"
                s = hex(i)[2:4]
                suid += s
            # Display result 
        print('UID Found')
        print(suid)
        return str(suid)
