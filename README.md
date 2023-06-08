# LilyGO Higrow Soil Moisture Sensor - MicroPython

MicroPython code for using [LiLyGO Higrow soil moisture sensor](https://github.com/Xinyuan-LilyGO/LilyGo-HiGrow). The code reads various environmental parameters such as temperature, humidity, salinity, luminosity, and soil moisture. It utilizes the [Blynk platform](https://blynk.cloud) to send the collected sensor data for further analysis and monitoring.

**Higrow Sensor**
 ![Higrow](https://github.com/Xinyuan-LilyGO/LilyGo-HiGrow/blob/master/image/img1.jpg?raw=true)
 
**Blynk Platform**
 ![Blink](https://github.com/DanielBustillos/LilyGo-HiGrow-Micropython/blob/main/assets/blynk.png?raw=true)

## Introduction

The code provided here enables you to interface with the LilyGO Higrow sensor and retrieve important environmental data. By using MicroPython, the implementation offers a lightweight and efficient solution for reading sensor values and transmitting them to the Blynk platform for remote monitoring and analysis.

##  Implemented Sensors

The following sensors are implemented and their corresponding data is retrieved:

| Sensor             | Measurement        | Pin        |
| ------------------ | ------------------ | -----------|
| Temperature (DHT11)       | Read in Celsius    | 16        |
| Humidity (DHT11)           | Percentage         | 16        |
| Salinity           | Normalized Value   | 34        |
| Luminosity         | Lux                | SCL: 26, SDA:25        |
| Soil Moisture      | Normalized Value   | 32        |
| Battery      | Normalized Value   | 33        |

*Note:* BME280 sensor is not implemented yet.


## To run this code on your LilyGO Higrow sensor, follow these steps:

1. Install MicroPython on the LilyGO Higrow sensor board. I prefer using [Thonny IDE](https://randomnerdtutorials.com/getting-started-thonny-micropython-python-ide-esp32-esp8266/) by its simplicity. It can be done by using [esptool](https://docs.micropython.org/en/latest/esp32/tutorial/intro.html).
2. Copy the provided code and save it as a file on the LilyGO Higrow sensor board.
3. (Optional) Configure a Blynk device to send data ot it. You can follow this tutorial. The device Must have 6 virtual pins.
4. Update the configuration file **blynk_config** with the appropriate settings for your device. Make sure to replace the following elements with your own configuration:

- SSID: Your Wi-Fi network name.
- PASSWORD: Your Wi-Fi network password.
- blynk_token: Your Blynk authentication token.
- time_deepsleep_minutes: The time interval for deep sleep mode in minutes.

5. Run the code on the LilyGO Higrow sensor board using MicroPython. 
The code will read the sensor data from the implemented sensors, sende the collected data will be sent to the Blynk platform as an example and then deepsleep.

## Code explanation 
This board requires Pin(4) state to be set in High so other pins can be active and make measurements. I believe this for optimizing power consumption.

    p0 = Pin(4, Pin.OUT) 
    p0.value(1)  
    
   

## Contributing

Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request on the GitHub repository.

## License

This code is licensed under the MIT License.
