# LilyGO Higrow Sensor - Soil Moisture Sensor MicroPython Implementation

This MicroPython code provides an implementation for using the soil moisture sensor of the [LilyGO Higrow sensor](https://github.com/Xinyuan-LilyGO/LilyGo-HiGrow). The code reads various environmental parameters such as temperature, humidity, salinity, fertility, luminosity, and soil moisture. It utilizes the [Blynk platform](https://blynk.cloud) to send the collected sensor data for further analysis and monitoring.

Higrow Sensor
 ![Higrow](https://github.com/Xinyuan-LilyGO/LilyGo-HiGrow/blob/master/image/img1.jpg?raw=true)
 
 Blynk Platform
 ![Blink]([https://github.com/Xinyuan-LilyGO/LilyGo-HiGrow/blob/master/image/img1.jpg?raw=true](https://github.com/DanielBustillos/LilyGo-HiGrow-Micropython/blob/main/assets/blynk.png?raw=true))
 
**Table of Contents**

1. Implemented Sensors
2. Installation
3. Usage
4. Contributing
5. License

## Introduction

The code provided here enables you to interface with the LilyGO Higrow sensor and retrieve important environmental data. By using MicroPython, the implementation offers a lightweight and efficient solution for reading sensor values and transmitting them to the Blynk platform for remote monitoring and analysis.

##  Implemented Sensors

The following sensors are implemented and their corresponding data is retrieved:

| Sensor             | Measurement        |
| ------------------ | ------------------ |
| Temperature        | Read in Celsius    |
| Humidity           | Percentage         |
| Salinity           | Normalized Value   |
| Fertility          | Normalized Value   |
| Luminosity         | Lux                |
| Soil Moisture      | Normalized Value   |


## To run this code on your LilyGO Higrow sensor, follow these steps:

1. Install MicroPython on the LilyGO Higrow sensor board. Refer to the official MicroPython documentation for detailed instructions.
2. Copy the provided code and save it as a file on the LilyGO Higrow sensor board.
3. Update the configuration file **blynk_config** with the appropriate settings for your device. These files contain information such as pin assignments, Blynk token, and other device-specific configurations. This step can be ommited.
4. Run the code on the LilyGO Higrow sensor board using MicroPython. 
The code will read the sensor data from the implemented sensors, including temperature, humidity, salinity, fertility, luminosity, and soil moisture.
The collected data will be sent to the Blynk platform as an example.

## Contributing

Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request on the GitHub repository.

## License

This code is licensed under the MIT License.
