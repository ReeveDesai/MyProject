# H2O Sense
***
This repository contains the code and instructions to build a hydration detection system using a Raspberry Pi 4, Grove Base Hat and a galvanic skin response sensor.

# Introduction
***
Dehydration can lead to serious health problems, and it is important to monitor our hydration levels, especially during physical activity or hot weather. Galvanic skin response (GSR) sensors can detect changes in the conductivity of the skin, which are correlated with changes in hydration levels.

This project aims to build a hydration detection system using a Raspberry Pi 4, Grove Base Hat and a GSR sensor. The Raspberry Pi 4 is a powerful and versatile single-board computer that can be used for a wide range of projects. The GSR sensor is a low-cost and easy-to-use device that can provide reliable hydration measurements.

# Requirements
***
To build this project, you will need:

* Raspberry Pi 4 (2GB or more)
* MicroSD card (16GB or more)
* Galvanic Skin Response Sensor
* Grove Base Hat
* USB cable (Type-C to Type-A)
* HDMI cable
* Monitor with HDMI input
* USB Keyboard and Mouse
* Internet Connection	

# Installation
***
1) Install Raspbian on the Raspberry Pi 4.

2) Connect the Grove Base Hat to the Raspberry Pi 4.

3) Connect the GSR sensor to the Raspberry Pi 4 using grove base hat. Connect the senosr to A0 pin (Analog Pin) to the grove base hat.

4) Clone this repository to your Raspberry Pi 4 using the following command:

      git clone https://github.com/Seeed-Studio/grove.py
      
5) Run the main script using the following command:

      python final.py
      
6) If you want to analyze and chane the thresold value the run the main script using following command:

      python grove_gsr_sensor.py 0
      
7) Follow the on-screen instructions to calibrate the sensor and start the hydration detection.

# Usage
***
The hydration detection system will display real-time hydration measurements on the screen. You can adjust the sensitivity of the sensor by changing the threshold value in the script. You can also customize the script to send hydration data to a server or to trigger an alert when the hydration level falls below a certain threshold.

# Contributing
***
Contributions are welcome! If you find a bug or want to add a new feature, please submit a pull request.
