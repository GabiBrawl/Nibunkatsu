# Nibunkatsu One
## A Split Mechanical Keyboard Built with Hack Club Blueprint

![Nibunkatsu One](assets/hero2.png)

にぶんかつ ✦ Nibunkatsu One is a compact, ergonomic split keyboard designed for everyday typing and programming. Built using the ESP32-S3 microcontroller with KMK firmware, it features per-key RGB underglow, an OLED display, and a rotary encoder.

This project was created as part of [Hack Club Blueprint](https://blueprint.hackclub.com), a program that empowers high school students to design, build, and ship real hardware products.

## Features

- **Split Design**: Ergonomic 4x6 layout per half for comfortable typing
- **RGB Underglow**: 28 individually addressable LEDs with customizable animations
- **OLED Display**: Shows layer status and keyboard info
- **Rotary Encoder**: Volume control
- **KMK Firmware**: Fully programmable with Python
- **TRRS Connection**: Reliable split communication, with proper ESD protection.
- **Hotswap Sockets**: Easy switch replacement

## Build Process

### Day 1: Planning and Design
![Day 1 Image 1](assets/day1image1.png)
![Day 1 Image 2](assets/day1image2.png)

Started with initial keyboard layout design and component selection, alongside left-side schematics started and pcb design.

### Day 2: More planning and design
![Day 2 Image 1](assets/day2image1.png)
![Day 2 Image 2](assets/day2image2.png)
![Day 2 Image 3](assets/day2image3.png)
![Day 2 Image 4](assets/day2image4.png)

Kept iterating with the pcb design and schematic, still on the left side only.

### Day 3: Even more planning and design
![Day 3 Image 1](assets/day3image1.png)
![Day 3 Image 2](assets/day3image2.png)
![Day 3 Image 3](assets/day3image3.png)

Began working on the right side schematic and pcb design. Added custom artwork to the pcb.

### Day 4: Final design
![Day 4 Image 1](assets/day4image1.png)
![Day 4 Image 2](assets/day4image2.png)
![Day 4 Image 3](assets/day4image3.png)
![Day 4 Image 4](assets/day4image4.png)
![Day 4 Image 5](assets/day4image5.png)

Finalized both sides of the schematic and pcb design. Prepared files for manufacturing.
Only on PCB planning and design I easily spent around 30 hours, in those 4 days.

## Keymap

The keyboard uses a 3-layer layout:

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
- **Switches**: Cherry MX compatible hotswap sockets
- **Connection**: TRRS cable for split communication
- **Display**: 0.96" OLED screen
- **LEDs**: WS2812C-2020 RGB LEDs

## Files

- `firmware/` - KMK firmware source code
- `PCB/` - EasyEDA PCB design files
- `CAD/` - 3D models and CAD files (there's none yet, idk if there will be, this is not easy for me xD)
- `assets/` - Build photos and documentation (mostly screenshots. Actual renders and image exports available in ../PCB/)

## License

- **Hardware (PCB & CAD)**: CERN Open Hardware Licence v2.0
- **Firmware**: MIT License
- **Assets**: Creative Commons Attribution-ShareAlike 4.0 International

## Acknowledgments

Designed with 💙. Special thanks to the Hack Club community for support.
