# Nibunkatsu One ✦ にぶんかつ
### A Split Mechanical Keyboard Built with Hack Club Blueprint

![Nibunkatsu One](assets/hero2.png)

> にぶんかつ ✦ Nibunkatsu comes from the Japanese word for splitting in half.

Nibunkatsu One is a compact, ergonomic split keyboard designed for everyday typing and programming. Built using the ESP32-S3 microcontroller with KMK firmware, featuring per-key RGB underglow, an OLED display, and a rotary encoder.

This project was created as part of [Hack Club Blueprint](https://blueprint.hackclub.com), a program that empowers high school students to design, build, and ship real hardware products.

**Project Stats:** ~70 hours over 1 week of active work and learning.

---

## Features

- **Split Design** — 5x7 layout per half for comfortable typing
- **RGB Underglow** — 28 individually addressable WS2812C LEDs per half
- **OLED Display** — 0.91" screen showing layer status and keyboard info
- **Rotary Encoder** — PEC11 encoder for volume/scroll control
- **Hotswap Sockets** — Easy switch replacement without soldering
- **KMK Firmware** — Fully programmable with Python
- **TRRS Connection** — 3.5mm audio cable for split communication with ESD protection

## Repository Structure

```
├── firmware/     - KMK firmware source code (Python)
├── PCB/          - EasyEDA PCB project files and schematics
├── CAD/          - 3D models for keyboard case (.3mf format)
└── assets/       - Build photos and documentation
```

---

## Hardware Specifications

### Core Components
- **Microcontroller:** ESP32-S3-WROOM-1-N4R2 (dual-core)
- **Switches:** Cherry MX compatible hotswap sockets (Gateron Banana low profile)
- **Keycaps:** Custom PBT low profile set
- **RGB LEDs:** WS2812C-2020 (55 total)
- **Display:** 0.91" OLED (128×32 pixels)
- **Encoder:** PEC11 rotary encoder
- **Connection:** TRRS cable for split communication

### Case & Mounting
The case is designed in Shapr3D with 4 printable models:
- Left case + Left plate
- Right case + Right plate

Available in `.3mf` format in the `CAD/` directory.

![3D Case Model](assets/day6image2_1.png)

---

## Keymap

3-layer layout configuration:

- **Layer 0 (Base):** QWERTY layout with modifiers
- **Layer 1 (Numbers):** Number row and symbols
- **Layer 2 (Navigation):** Arrow keys and media controls

## Firmware

Written in Python using the [KMK firmware framework](https://github.com/KMKfw/kmk_firmware):

- Split communication via UART
- RGB lighting effects and animations
- OLED display integration
- Rotary encoder support
- Multiple customizable keymap layers

Firmware source code is located in `firmware/`.

---

## Bill of Materials

**Total estimated cost:** €153.11

| Component | Part / Model | Qty | Notes |
| :--- | :--- | :--- | :--- |
| **Microcontroller** | ESP32-S3-WROOM-1-N4R2 | 3 | Dual-core MCU handling split logic |
| **Switches** | Gateron Low Profile (Banana) | 54 | Tactile, hot-swap compatible |
| **Keycaps** | Custom PBT Low Profile Set | 1 | Double-shot PBT, 144 keys |
| **PCB Fabrication** | Custom FR4 PCB (Left+Right) | 5 | Manufactured via JLCPCB |
| **Lighting** | WS2812C-2020 RGB LEDs | 55 | Per-key RGB underglow |
| **Connectivity** | TRRS Cable (Coiled/Braided) | 1 | Premium interconnect cable |
| **Sockets** | Kailh Hot-Swap Sockets | 100 | Solder-free switch replacement |
| **Display** | OLED Display (0.91") | 1 | 128×32 pixel status display |
| **Controls** | PEC11 Rotary Encoder | 1 | Volume/scroll control |
| **Misc Electronics** | Diodes, Caps, LDOs, Resistors | ~150 | Logic, power regulation, ESD protection |

Complete CSV with supplier links: [`bom.csv`](bom.csv)

---

## License

This project uses a three-part licensing model to appropriately protect hardware, software, and documentation.

| Component | License | Covers |
| :--- | :--- | :--- |
| **Hardware** | [CERN-OHL-W-2.0](LICENSE-hardware) | PCB designs, schematics, mechanical CAD files |
| **Firmware** | [MIT License](LICENSE-firmware) | Python/KMK firmware and source code |
| **Documentation** | [CC BY-SA 4.0](LICENSE-assets) | Assets, photos, diagrams, written guides |

### Why Three Licenses?

- **Hardware (CERN OHL):** Explicitly covers physical manufacturing rights and ensures attribution for derivative designs
- **Firmware (MIT):** Permissive software license allowing easy reuse and integration
- **Assets (CC BY-SA):** Ensures proper attribution for media and documentation

> **Note:** Third-party dependencies may have different licenses. Please refer to their respective repositories for license information.

---

## Acknowledgments

Designed with 💙 by 𝕲𝕭

Special thanks to the Hack Club community for their support!
