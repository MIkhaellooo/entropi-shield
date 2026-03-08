# EntropyShield v1.0
**Hardware-Driven Entropy Generator for ThinkPad T480 Systems**

## Overview
**EntropyShield** is a Python-based key generator application that exploits the physical "noise" of the Lenovo ThinkPad T480 hardware. It captures real-time CPU temperature data and combines it with nanosecond-level timing precision to create a *High-Entropy Seed*.

The final output is processed using the **SHA-256** algorithm to generate a unique cryptographic token.

## Key Features
* **Real-time Hardware Entropy**: Pulls temperature data from all CPU cores using `psutil`.
* **Nanosecond Jitter**: Uses the nanosecond-level *System Clock* as the primary randomizer.
* **Glassmorphism UI**: Modern NiceGUI-based dashboard with Tailwind CSS styling.
* **JavaScript Clipboard Bridge**: One-click feature to copy tokens directly to the clipboard.

## Tech Stack
* **Language**: Python 3.12+
* **System Monitoring**: `psutil`
* **Cryptography**: `hashlib`
* **Frontend/UI**: [NiceGUI](https://nicegui.io/)
* **CSS Engine**: Tailwind CSS
* **Environment**: Ubuntu 24.04 (Optimized for ThinkPad T480)
