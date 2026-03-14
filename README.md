# capstone-SIC-project
Smart hostel automation and power monitoring using IoT – Samsung Innovation Campus project.


## Abstract

The **Smart Hostel Room Automation and Power Monitoring System** is an IoT-based solution that allows students to remotely control appliances such as lights and fans while monitoring power consumption to improve energy efficiency in hostels.

Data from **ESP32 devices** is processed by a **Raspberry Pi** and stored on cloud platforms such as **Google Sheets** for tracking and analysis of power usage.

---

## Problem Statement

In many hostels, electrical appliances like lights and fans are often left running even when rooms are unoccupied, leading to **energy wastage and higher electricity costs**. Additionally, there is limited visibility into **individual room power usage**.

A smart system is required to **monitor energy consumption and allow remote control of devices** for efficient power management.

---

## Objectives

* Develop an **IoT-based smart system** for controlling hostel room appliances remotely.
* Monitor **electricity usage in real time**.
* Store power consumption data for **analysis and tracking**.
* Reduce **unnecessary electricity consumption** in hostel rooms.
* Create a **scalable system** that can be implemented across multiple hostel rooms.

---

## System Architecture

Mobile App
↓
MQTT Broker
↓
Raspberry Pi (Edge Processor)
↓
ESP32 Microcontroller
↓
Relay Module → Lights / Fans
↓
Power Controller → Data Monitoring
↓
Cloud Storage (Google Sheets)

---

## Technologies Used

### Hardware

* ESP32 Microcontroller
* Raspberry Pi
* Relay Module
* Breadboard and Jumper Wires

### Software

* Python
* MQTT Protocol
* Mosquitto MQTT Broker
* Google Sheets API
* WiFi Communication

### Platforms

* Raspberry Pi OS
* GitHub (Version Control)

---

## Implementation

The implementation of the project is managed using **Git for version control**.
All source code including **ESP32 scripts, Raspberry Pi Python scripts, and documentation** are maintained in a Git repository for collaboration and version tracking.

---

## Challenges Faced

* Establishing stable communication between **ESP32 and Raspberry Pi**
* Handling **MQTT message reliability and connectivity issues**
* Integrating cloud services such as **Google Sheets API**
* Managing **real-time data processing and filtering** at the edge device
* Hardware wiring and **power supply management during testing**

---

## Future Improvements

* Integration of a **mobile application** for user-friendly control
* Addition of **AI-based energy consumption analysis**
* Integration of **smart sensors** such as smoke detectors and motion sensors
* Development of a **dashboard for real-time visualization** of power data
* Scaling the system to support **multiple hostel rooms and buildings**
