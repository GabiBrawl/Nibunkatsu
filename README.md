# Nibunkatsu One ✦ にぶんかつ
### A Split Mechanical Keyboard Built with Hack Club Blueprint

![Nibunkatsu One](assets/hero2.png)

> にぶんかつ ✦ Nibunkatsu comes from the Japanese word for splitting in half.

Nibunkatsu is a compact split keyboard for typing and programming. I'll be using the ESP32-S3 microcontroller with KMK firmware, featuring RGB under the keys, an OLED display on the left half, and a rotary encoder in the right half!!

This project was created as part of the [Hack Club Blueprint](https://blueprint.hackclub.com) program that empowers high school students to design and build real hardware projects.

**Project Stats:** ~70 hours over the course of 1 week of active work and learning!

---

## Features

- **Split Design** — 5x7 layout per half, including a number row
- **RGB Underglow** — 28 individually addressable WS2812C LEDs per half
- **OLED Display** — 0.91" display for layer status and other keyboard info
- **Rotary Encoder** — PEC11 encoder for volume control and maybe more?
- **Hotswap Sockets** — Simple switch replacement without constant soldering
- **KMK Firmware** — Programmable using Python
- **TRRS Connection** — A 3.5mm audio cable for split communication between both halves. Also with ESD protection, protecting the MCU's TX/RX pins.

## Repository Structure

```
├── firmware/     - KMK firmware code and configuration
├── PCB/          - EasyEDA PCB project files and schematics
├── CAD/          - 3D models for the keyboard case and plates (.3mf and .step)
└── assets/       - Work screenshots and photos 
├── bom.csv       - Bill of Materials with supplier links, prices and quantities
```

---

## Hardware Specifications

### Core Components
- **Microcontroller:** ESP32-S3-WROOM-1-N4R2
- **Switches:** Cherry MX compatible hotswap sockets (I'll be personally using Gateron Banana low profile switches)
- **RGB LEDs:** WS2812C-2020
- **Display:** 0.91" OLED (128×32 pixels)
- **Encoder:** PEC11 rotary encoder with 24 steps and push button
- **Connection:** TRRS cable for communication between halves

### Case & Mounting
The case was designed in Shapr3D with 4 printable models:
- Left case + Left plate
- Right case + Right plate

Bo th available in `.3mf` and `.step` formats positioned in the [`CAD/`](CAD/) directory!

![3D Case Model](assets/day6image2_1.png)

---

## Keymap

3-layer configuration:

- **Layer 0 (Base):** QWERTY layout with a number row
- **Layer 1 (Shortcuts):** Some operating system shortcuts maybe
- **Layer 2 (Navigation):** Arrow keys and media controls

## Firmware

Written in Python using the [KMK firmware framework](https://github.com/KMKfw/kmk_firmware).

The firmware source code is available in [`firmware/`](firmware/).

---

## Bill of Materials

**Total cost:** €153.11

| Component Type | Part Name | Qty | Other Notes |
| :--- | :--- | :--- | :--- |
| **Microcontroller** | ESP32-S3-WROOM-1-N4R2 | 3 | MCU |
| **Switches** | Gateron Low Profile (Banana) | 54 | Tactile yet silent |
| **Keycaps** | PBT Low Profile | 1 | Double-shot PBT, getting shine-through letters |
| **PCB Fabrication** | Custom PCB | 5 | via JLCPCB |
| **RGB LEDs** | WS2812C-2020 | 55 | Per-key RGB underglow |
| **Connectivity** | TRRS Cable | 1 | Interconnect cable |
| **Sockets** | Kailh Hot-Swap Sockets | 100 | Solder-free switch replacement |
| **Display** | 0.91" OLED | 1 | 128×32 pixel status display |
| **Controls** | PEC11 Rotary Encoder | 1 | Volume control |
| **Misc Electronics** | Diodes, Capacitors, LDOs, Resistors | ~150 | Logic, power regulation, ESD protection |

The complete CSV with supplier links is available here: [`bom.csv`](bom.csv)

---

## License

This project uses a three-part licensing model to appropriately protect hardware, software, and documentation.

| Component | License | Covers |
| :--- | :--- | :--- |
| **Hardware** | [CERN-OHL-W-2.0](LICENSE-hardware) | PCB designs, schematics, mechanical CAD files |
| **Firmware** | [MIT License](LICENSE-firmware) | Python/KMK firmware and source code |
| **Documentation** | [CC BY-SA 4.0](LICENSE-assets) | Assets, photos, diagrams, written guides |

### Why Three Licenses?

- **Hardware (CERN OHL):** Covers physical manufacturing rights and ensures attribution for derivative designs
- **Firmware (MIT):** Permissive software license allowing easy reuse and integration
- **Assets (CC BY-SA):** Ensures proper attribution for media assets and documentation

> **Note:** Third-party project dependencies may have different licenses. Please refer to their respective repositories for licensing information.

---

## Acknowledgments

Designed with 💙 by 𝕲𝕭

Special thanks to the Hack Club community for their support!
