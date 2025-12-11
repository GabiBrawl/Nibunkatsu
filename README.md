# Nibunkatsu One ✦ にぶんかつ
### A Split Mechanical Keyboard Built with Hack Club Blueprint

![Nibunkatsu One](assets/hero2.png)
Nibunkatsu One is a compact, ergonomic split keyboard designed for everyday typing and programming. Built using the ESP32-S3 microcontroller with KMK firmware, featuring per-key RGB underglow, an OLED display, and a rotary encoder.

> にぶんかつ ✦ Nibunkatsu comes from the Japanese word for splitting in half.

This project was created as part of [Hack Club Blueprint](https://blueprint.hackclub.com), a program that empowers high school students to design, build, and ship real hardware products.

Estimation of time spent on this project: ~70 hours over 1 week of active work and learning.

## Features

- **Split Design**: 5x7 layout per half for comfortable typing
- **RGB**: 28 individually addressable LEDs per half under each key
- **OLED Display**: Shows layer status and keyboard info
- **Rotary Encoder**: Volume control
- **KMK Firmware**: Fully programmable with Python
- **3.5mm Audio Connection**: Split communication, with proper ESD protection.
- **Hotswap Sockets**: Easy switch replacement

## Keymap

The keyboard will use a 3-layer layout:

- **Layer 0 (Base)**: QWERTY layout with modifiers
- **Layer 1 (Numbers)**: Number row and symbols
- **Layer 2 (Navigation)**: Arrow keys and media controls

## Firmware

The firmware is written in Python using the KMK framework. It will support:

- Split communication via UART
- RGB lighting effects
- OLED display integration
- Rotary encoder support
- Multiple keymap layers

## Hardware

- **Microcontroller**: ESP32-S3 N8R4
- **Switches**: Cherry MX compatible hotswap sockets, personally I'll be using the Gateron Banana low profile switches!
- **Connection**: 3.5mm audio cable for split communication :P
- **Display**: 0.96" OLED screen
- **LEDs**: WS2812C-2020 RGB LEDs

## 3D Case Model
The case is designed using Shapr3D. The design files are included in the repository. Available in .3mf format.

There are 4 total models to be printed: Left case, Right case, Left plate and Right plate.

![Day 6 Image 2_1](assets/day6image2_1.png)

## Files

- `firmware/` - KMK firmware source code
- `PCB/` - EasyEDA PCB project files
- `CAD/` - 3D models for the keyboard case
- `assets/` - Most build photos and documentation

## Bill of Materials
The total projected cost for the build is approximately €175.30. Below is the breakdown of the major components used in this revision.

| Component | Part / Model | Qty | Notes |
| :--- | :--- | :--- | :--- |
| **Microcontroller** | ESP32-S3-WROOM-1-N4R2 | 3 | Dual-core MCU handling split logic |
| **Switches** | Gateron Low Profile (Banana) | 54 | Tactile, Hot-Swap compatible |
| **Keycaps** | Custom PBT Low Profile Set | 1 | Double-shot PBT, 144 keys |
| **PCB Fabrication** | Custom FR4 PCB (Left+Right) | 5 | Manufactured via JLCPCB |
| **Lighting** | WS2812C-2020 RGB LEDs | 55 | Per-key RGB Underglow |
| **Connectivity** | TRRS Cable (Coiled/Braided) | 1 | Premium interconnect cable for split comms |
| **Sockets** | Kailh Hot-Swap Sockets | 100 | Solder-free switch replacement |
| **Display** | OLED Display (0.91") | 1 | 128x32 pixel status indication |
| **Controls** | PEC11 Rotary Encoder | 1 | For volume/scroll control |
| **Misc Electronics** | Diodes, Caps, LDOs, Resistors | ~150 | Logic support, power regulation, ESD protection |

A complete CSV with links to specific suppliers can be found in bom.csv.

## License

This project is open-source and utilizes a three-part licensing model to ensure the appropriate protection for hardware, software, and documentation.

| Component | License | Description |
| :--- | :--- | :--- |
| **Hardware** | [CERN-OHL-W-2.0](LICENSE-hardware) | Covers the PCB designs, schematics, and mechanical CAD files. |
| **Firmware** | [MIT License](LICENSE-firmware) | Covers the Python/KMK firmware and source code. |
| **Documentation** | [CC BY-SA 4.0](LICENSE-assets) | Covers the assets, photos, diagrams, and written guides. |

### Why three licenses?
* **Hardware (CERN OHL):** Unlike software licenses, this explicitly covers physical manufacturing rights, ensuring that if someone builds or modifies this board, they must attribute the original design.
* **Firmware (MIT):** A standard permissive software license that allows the code to be easily reused or integrated into other projects.
* **Assets (CC BY-SA):** Ensures that the photos and diagrams are attributed if shared or used in other media.

**Note:** Third-party dependencies may have different licenses associated with them. Please refer to their respective repositories for license information.

## Acknowledgments

Designed with 💙 by 𝕲𝕭. Special thanks to the Hack Club community for support.
