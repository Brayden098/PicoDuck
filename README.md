
---

# 🦆 PicoDuck

**PicoDuck** is a powerful, multi-payload deployment tool designed for the Raspberry Pi Pico, offering an easy way to install custom scripts for automation, security testing, and entertainment. From reverse shells to Rickrolls, PicoDuck makes setting up and running payloads quick and simple.

---

## 🚀 Features
- **Versatile Payloads**: Quickly deploy Reverse Shells, WiFi Extractors, Hacked Messages, and classic Rickrolls.
- **Easy Installation**: Automated setup process for your Raspberry Pi Pico.
- **Simple Interface**: Select and deploy scripts with just a few clicks.

---

## ⚙️ Requirements
- **Python 3.x** installed on your system
- A **Raspberry Pi Pico** with CircuitPython support
- **USB cable** for connecting the Pico to your computer

---

## 📥 Installation

1. Clone the PicoDuck repository:
   ```bash
   git clone https://github.com/ShadowByte098/PicoDuck.git
   cd PicoDuck
   ```

---

## 🖥️ Usage (Windows)
1. **Connect the Raspberry Pi Pico**: 
   - Hold down the **BOOTSEL** button on your Pico.
   - While holding it, connect the Pico to your computer via USB.
   - Release the button once connected. The Pico should appear as a USB drive named `RPI-RP2`.

2. **Run PicoDuck**:
   - In your terminal or command prompt, navigate to the project folder and run:
     ```bash
     python PicoDuck_Windows.py
     ```

3. **Choose a Payload**: 
   - Follow the on-screen instructions to select a payload:
     - **1** - Reverse Shell
     - **2** - Disable Antivirus
     - **3** - WiFi Extractor
     - **4** - Rickroll (by *The Ugly Gamer*)
     - **5** - Hacked Message
     - **6** - Custom Script

4. **Deploy the Payload**:
   - After selecting a payload, follow the prompts to complete the deployment. PicoDuck will handle formatting, flashing, and copying files for you.

---

## 💡 How It Works

PicoDuck leverages the Raspberry Pi Pico as a USB Rubber Ducky, allowing it to deploy various scripts automatically when plugged into a target system. The payloads are customizable, so you can tailor each script to your specific needs.

---

## ⚠️ Disclaimer
PicoDuck is intended for **ethical use only**. Always have permission before deploying any payloads on devices that aren't yours. Use responsibly!

---

## 📜 License
This project is open-source and available under the MIT License. See the [LICENSE](LICENSE) file for more details.

--- 
