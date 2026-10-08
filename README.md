# Introduction-To-Robotics

## IDE to be used for interacting with ESP32
Thonny is widely used IDE to interact with ESP32. You can download install Thonny browser from [here](https://thonny.org/)

## Flashing MicroPyhon onto your esp32

In orer to get started with programming esp32, the first thing you need to do is to update the firmware of the board. There are two ways you can do this. You may use epstool or you can install micropython using Thonny Browser.

### Using Thonny browser

For a very detailed instructions follow this [link](https://randomnerdtutorials.com/getting-started-thonny-micropython-python-ide-esp32-esp8266/) Look for section "Flashing MicroPython Firmware using Thonny IDE"

1) Connect your ESP32 or ESP8266 board to your computer.

2) Open Thonny IDE. Go to Tools > Options > Interpreter.

3) Install of update micropython.

### Using esptool

Firstlly install esptool.

If you are using Windows:

For Mac users:
* pip3 install esptool (or brew install esptool)

1) esptool erase flash
2) esptool -c esp32s3 write-flash 0 ESP32_GENERIC_S3-20260824-v1.29.0.bin

### Troubleshooting during MicroPython installation 

Follow one of the two procedures

1. Unplug the device
2. Press and hold the boot button
3. Plug the device in
4. After 2-3 seconds release the BOOT button.

Or

If the board isn’t responding to esptool at all, it may need to be manually reset into the bootloader download mode. Look for a button marked “BOOT” or “IO0” on your board and a second button marked “RESET” or “RST”. If you have both buttons, try these steps:
	1	Press “BOOT” (or “IO0”) and hold it down.
	2	Press “RESET” (or “RST”) and immediately release it.
	3	Release “BOOT” (or “IO0”).
	4	Re-run the flashing steps from the download page.


### ESP32 pin diagram

Refer to  [this](https://github.com/vcc-gnd/YD-ESP32-S3/blob/main/5-public-YD-ESP32-S3-Hardware%20info/ESP32-S3-0702%20(9).PNG)

Or [this](https://github.com/vcc-gnd/YD-ESP32-S3/blob/main/5-public-YD-ESP32-S3-Hardware%20info/YD-ESP32-S3.PNG)
