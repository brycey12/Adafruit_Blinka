# SPDX-FileCopyrightText: 2021 Melissa LeBlanc-Williams for Adafruit Industries
#
# SPDX-License-Identifier: MIT
"""Pin definitions for the Beagley-AI."""
from adafruit_blinka.microcontroller.am67x import pin

# Digital Pins
GPIO2 = pin.E11
GPIO3 = pin.B13
GPIO4 = pin.W26
GPIO5 = pin.B20
GPIO6 = pin.D20
GPIO7 = pin.B3
GPIO8 = pin.C12
GPIO9 = pin.C11
GPIO10 = pin.B12
GPIO11 = pin.A9
GPIO12 = pin.C20
GPIO13 = pin.E19
GPIO14 = pin.F24
GPIO15 = pin.C27
GPIO16 = pin.A25
GPIO17 = pin.A26
GPIO18 = pin.D25
GPIO19 = pin.C26
GPIO20 = pin.F23
GPIO21 = pin.B25
GPIO22 = pin.R27
GPIO23 = pin.B5
GPIO24 = pin.C8
GPIO25 = pin.P21
GPIO26 = pin.P26
GPIO27 = pin.N22

# I2C
SDA = GPIO2
SCL = GPIO3

# SPI
SPI_MISO = GPIO9
SPI_MOSI = GPIO10
SPI_SCLK = GPIO11
SPI_CS = GPIO8

# UART
UART_TX = GPIO14
UART_RX = GPIO15
