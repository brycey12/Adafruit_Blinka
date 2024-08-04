# SPDX-FileCopyrightText: 2021 Melissa LeBlanc-Williams for Adafruit Industries
#
# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: 2022 Martin Schnur for Siemens AG
#
# SPDX-License-Identifier: MIT
"""TI AM67A pin names"""

import mraa

# pylint: disable=too-many-branches,too-many-statements
# pylint: disable=pointless-string-statement


# class Pin:
#     """Pins don't exist in CPython so...lets make our own!"""
#
#     # pin modes
#     IN = 0
#     OUT = 1
#     ADC = 2
#     DAC = 3
#     PWM = 4
#     # pin values
#     LOW = 0
#     HIGH = 1
#     # pin pulls
#     PULL_NONE = 0
#     PULL_UP = 1
#     PULL_DOWN = 2
#
#     id = None
#     _value = LOW
#     _mode = IN
#
#     def __init__(self, pin_id=None):
#         self.id = pin_id
#         self._mode = None
#         self._pull = None
#         self._pin = None
#
#     def __repr__(self):
#         return str(self.id)
#
#     def __eq__(self, other):
#         return self.id == other
#
#     def init(self, mode=IN, pull=None):
#         """Initialize the Pin"""
#         if self.id is None:
#             raise RuntimeError("Can not init a None type pin.")
#         if mode is not None:
#             if mode == self.IN:
#                 self._mode = self.IN
#                 mypin = mraa.Gpio(self.id)
#                 mypin.dir(mraa.DIR_IN)
#             elif mode == self.OUT:
#                 self._mode = self.OUT
#                 mypin = mraa.Gpio(self.id)
#                 mypin.dir(mraa.DIR_OUT)
#             elif mode in (self.ADC, self.DAC):
#                 # ADC (DAC not available) only available on Pin 0-5 (X12 Pin 1-6)
#                 if self.id not in (0, 1, 2, 3, 4, 5):
#                     raise ValueError("Pin does not have ADC capabilities")
#                 self._pin = mraa.Aio(self.id)
#             elif mode == self.PWM:
#                 # PWM only available on Pin 4-9 (X10 Pin 1-2, X11 Pin 5-8)
#                 if self.id not in (4, 5, 6, 7, 8, 9):
#                     raise ValueError("Pin does not have PWM capabilities")
#                 return
#             else:
#                 raise RuntimeError("Invalid mode for pin: %s" % self.id)
#             self._mode = mode
#         if pull is not None:
#             if self._mode != self.IN:
#                 raise RuntimeError("Cannot set pull resistor on output")
#             if pull == self.PULL_UP:
#                 mypin = mraa.Gpio(self.id)
#                 mypin.dir(mraa.DIR_IN)
#             elif pull == self.PULL_DOWN:
#                 mypin = mraa.Gpio(self.id)
#                 mypin.dir(mraa.DIR_IN)
#             else:
#                 raise RuntimeError("Invalid pull for pin: %s" % self.id)
#
#     def value(self, val=None):
#         """Set or return the Pin Value"""
#         # Digital In / Out
#         if self._mode in (Pin.IN, Pin.OUT):
#             if val is not None:
#                 if val == self.LOW:
#                     self._value = val
#                     mypin = mraa.Gpio(self.id)
#                     mypin.write(0)
#                 elif val == self.HIGH:
#                     self._value = val
#                     mypin = mraa.Gpio(self.id)
#                     mypin.write(1)
#                 else:
#                     raise RuntimeError("Invalid value for pin")
#                 return None
#             return mraa.Gpio.read(mraa.Gpio(self.id))
#         # Analog In
#         if self._mode == Pin.ADC:
#             if val is None:
#                 # Read ADC here
#                 mypin = mraa.Aio(self.id)
#                 mypin.read()
#                 return mypin.read()
#             # read only
#             raise AttributeError("'AnalogIn' object has no attribute 'value'")
#         # Analog Out
#         if self._mode == Pin.DAC:
#             """if val is None:
#                 # write only
#                 raise AttributeError("unreadable attribute")
#             # Set DAC here
#             mypin = mraa.Aio(self.id)
#             mypin.setBit(val)"""
#             raise AttributeError(
#                 "AM65xx doesn't have an DAC! No Analog Output possible!"
#             )
#         raise RuntimeError(
#             "No action for mode {} with value {}".format(self._mode, val)
#         )


# Digital Pins (GPIO 0-19)
E11 = Pin((0, 18))  # GPIO2
B13 = Pin((0, 17))  # GPIO3
W26 = Pin((1, 38))  # GPIO4
B20 = Pin((2, 15))  # GPIO5
D20 = Pin((2, 17))  # GPIO6
B3 = Pin((0, 9))  # GPIO7
C12 = Pin((0, 0))  # GPIO8
C11 = Pin((0, 4))  # GPIO9
B12 = Pin((0, 3))  # GPIO10
A9 = Pin((0, 2))  # GPIO11
C20 = Pin((2, 16))  # GPIO12
E19 = Pin((2, 18))  # GPIO13
F24 = Pin((2, 15))  # GPIO14
C27 = Pin((2, 13))  # GPIO15
A25 = Pin((2, 7))  # GPIO16
A26 = Pin((2, 8))  # GPIO17
D25 = Pin((2, 11))  # GPIO18
C26 = Pin((2, 12))  # GPIO19
F23 = Pin((2, 10))  # GPIO20
B25 = Pin((2, 9))  # GPIO21
R27 = Pin((1, 41))  # GPIO22
B5 = Pin((0, 7))  # GPIO23
C8 = Pin((0, 10))  # GPIO24
P21 = Pin((1, 42))  # GPIO25
P26 = Pin((1, 36))  # GPIO26
N22 = Pin((1, 33))  # GPIO27

# I2C allocation
I2C_SCL = B13
I2C_SDA = E11

# SPI allocation
SPIO_SCLK = A9
SPIO_MISO = C11
SPIO_MOSI = B12
SPIO_SS = C12

# UART allocation
UART_TX = F24
UART_RX = C27

# pwmOuts (GPIO 4-9)
PWM_0 = C20
PWM_1 = E19

# I2C
# ordered as sclID, sdaID
# i2c-4 (/dev/i2c-4) -> X10 Pin9, Pin10 (SDA, SCL)
i2cPorts = ((2, I2C_SCL, I2C_SDA),)

# SPI
# ordered as spiId, sckId, mosiID, misoID
spiPorts = ((0, SPIO_SCLK, SPIO_MOSI, SPIO_MISO),)

# UART
# use pySerial = dev/ttyS1
# ordered as uartID, txID, rxID
uartPorts = ((0, UART_TX, UART_RX),)

# PWM
# pwmOuts = (
#     ((0, 0), PWM_4),
#     ((0, 1), PWM_5),
#     ((2, 0), PWM_6),
#     ((2, 1), PWM_7),
#     ((4, 0), PWM_8),
#     ((4, 1), PWM_9),
# )
