# Marlin Firmware - Ender 2 Pro BIQU Configuration

**Configured for Ender 2 Pro 3D Printer with BIQU Components**

## Hardware Setup
- **Printer**: Creality Ender 2 Pro
- **Extruder**: BIQU V2H2S (Direct Drive)
- **Bed Leveling Probe**: BIQU Level Probe (Auto Bed Leveling)
- **Filament Sensor**: BIQU Filament Runout Sensor
- **Motherboard**: Creality V4 (4.2.7)

## Features Enabled
- ✅ Auto Bed Leveling (ABL) with BIQU probe
- ✅ Direct Drive Extruder Configuration
- ✅ Filament Runout Detection & M600 Support
- ✅ Babystepping for Fine Z-Offset Adjustment
- ✅ Thermal Runaway Protection
- ✅ Linear Advance for Print Quality

## Configuration Files
- `Marlin/Configuration.h` - Main printer configuration
- `Marlin/Configuration_adv.h` - Advanced features and settings

## Building the Firmware
This firmware is configured for PlatformIO or Arduino IDE.

### PlatformIO
```bash
platformio run -e creality_v4
```

### Arduino IDE
1. Install Marlin board definitions
2. Select: Tools → Board → Creality V4 (CR-10S/Ender-X)
3. Compile and upload

## Notes
- E-steps calibrated for BIQU V2H2S extruder
- Probe offsets and bed size configured for Ender 2 Pro (165x165mm bed)
- Based on Marlin bugfix-2.1.x branch
- GPL-3.0 License
