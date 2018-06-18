Door Status Display
======

Here is the display manual:
[https://www.crystalfontz.com/products/document/3285/CFA632_Family_Data_Sheet_Release_Date_2014-02-25.pdf](https://www.crystalfontz.com/products/document/3285/CFA632_Family_Data_Sheet_Release_Date_2014-02-25.pdf)

I bought this to mount to the outside-facing side of my door. I mounted the RF Engine (and a 3.3V power
converter) behind the display. I ran a 5V power connection over the door. There is an AC outlet near the
door for the wall-wart power supply.

I can change status messages from my web page.

![](https://github.com/topherCantrell/OfficeDoorLCD/blob/master/art/Display.jpg)

I used a balsa frame to hold everything. The RF Engine is mounted on a break-out board that has a built-on
3.3V power regulator. You can see the black power-jack on the right side of the frame and the blue push-button
on the left side.

![](https://github.com/topherCantrell/OfficeDoorLCD/blob/master/art/display5.jpg)

Here is the wiring chart:

| Wire     | Display                         | RFEngine                 |
|----------|---------------------------------|--------------------------|
| Red      | J2-2 (5V LCD) and J2-3 (5V LED) | Power Regulator to VCC   |
| Black    | J2-1 (GROUND) and Button        | Ground                   |
| Green    | J2-4 (DATA_IN)                  | GPIO12 (SPI MOSI)        |
| Purple   | J2-5 (SPI_CS)                   | GPIO15                   |
| Blue     | J2-6 (SPI_CLK)                  | GPIO13 (SPI CLK)         |
| Gray     | J2-7 (SPI_BUSY)                 | GPIO16                   |
| White    | Button                          | GPIO17                   |

Here is a close-up of the final assembly. You can see the "F" antenna on the RFEngine sticking out the left
side (the bottom of the display).

![](https://github.com/topherCantrell/OfficeDoorLCD/blob/master/art/display4.jpg)

Here is the display mounted to my door:

![](https://github.com/topherCantrell/OfficeDoorLCD/blob/master/art/display3.jpg)

![](https://github.com/topherCantrell/OfficeDoorLCD/blob/master/art/display2.jpg)
