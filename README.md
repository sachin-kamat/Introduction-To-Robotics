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

1) esptool erase flash
2) esptool -c esp32s3 write-flash 0 ESP32_GENERIC_S3-20260824-v1.29.0.bin
