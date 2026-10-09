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

## Runtime Calibration

Home offsets, probe offsets, and extruder E-steps are adjustable without recompiling:

```gcode
M206 X0 Y0 Z0        ; Set XYZ home offsets
M851 X9 Y-29 Z-2.3   ; Example probe offsets; calibrate for your mounting
M92 E932            ; BIQU H2 V2S default E-steps (steps/mm)
M500                ; Save all settings to EEPROM
M503                ; Report current settings
```

M851 accepts X and Y offsets from -50 to +50 mm and Z offsets from -5 to +3 mm.
Z-safe homing places the probe at the 165×165 mm bed center (82.5, 82.5 mm).
After homing, use the LCD Z Probe Offset control for 0.01 mm babystepping
while preparing or printing the first layer. Run M500 after adjustments to
save the updated probe offset across power cycles.

Previously saved EEPROM values can override new firmware defaults. If needed,
run `M92 E932` followed by `M500` to apply the new extruder default without
resetting other calibration. `M501` reloads saved settings; `M502` resets all
settings to firmware defaults (save with `M500` only if that reset is intended).
