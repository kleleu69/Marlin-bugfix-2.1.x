# Marlin Firmware - Ender 2 Pro BIQU Configuration

**Configured for Ender 2 Pro 3D Printer with BIQU Components**

## Hardware Setup
- **Printer**: Creality Ender 2 Pro
- **Extruder**: BIQU V2H2S (Direct Drive)
- **Bed Leveling Probe**: BIQU MicroProbe V2 (Auto Bed Leveling)
- **Filament Sensor**: BIQU Filament Runout Sensor
- **Motherboard**: BIGTREETECH SKR Mini E3 V3.0 (STM32G0B1)

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
Use PlatformIO with the board environment selected in `platformio.ini`.

### PlatformIO
```bash
platformio run -e STM32G0B1RE_btt
```

### Dependency-Only Environment Setup

The `.github/workflows/copilot-setup-steps.yml` workflow installs PlatformIO
and downloads the board's pinned platform, toolchain, framework, and libraries.
It does **not** compile firmware or replace configuration files. Merge this
workflow into the default branch to prepare each new Copilot session automatically.
It can also be run manually from the Actions tab to check dependency installation.

The setup retains the package versions specified by this firmware instead of
upgrading the STM32 framework or compiler independently. Keep the Copilot firewall
enabled and allow `platformio.org` for registry/download access.

## Upstream Configuration References

Primary reference: [MarlinFirmware/Configurations, bugfix-2.1.x](https://github.com/MarlinFirmware/Configurations/tree/2c8f5fc370eeeae4d242e6d0d69f0958e7a8b207).
The reviewed examples use configuration version `02010300`, matching this firmware:

- [Ender-2 Pro / CrealityV423](https://github.com/MarlinFirmware/Configurations/tree/2c8f5fc370eeeae4d242e6d0d69f0958e7a8b207/config/examples/Creality/Ender-2%20Pro/CrealityV423) for printer reference.
- [Ender-3 / SKR Mini E3 V3.0](https://github.com/MarlinFirmware/Configurations/tree/2c8f5fc370eeeae4d242e6d0d69f0958e7a8b207/config/examples/Creality/Ender-3/BigTreeTech%20SKR%20Mini%20E3%203.0) for board, serial ports, and TMC2209 drivers.

Secondary references: BIGTREETECH's [SKR Mini E3 documentation](https://github.com/bigtreetech/docs/blob/master/docs/SKR%20MINI%20E3.md)
and [MicroProbe documentation and manuals](https://github.com/bigtreetech/MicroProbe).

Neither Marlin example represents this complete modified printer. Do not copy
either configuration wholesale: preserve the 165 mm bed, calibrated travel limits,
932 E-steps, probe offsets, linear leveling, and center parking. Controller fan
wiring remains FAN1 (PC7); the hotend automatic fan remains FAN2 (PB15).
Native MicroProbe V2 support uses the board's PA1 enable output and PC14 probe input
with a LOW trigger state and an explicit 30 ms wake-up delay. Verify that the
physical wiring matches before flashing.

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

## Nozzle Parking

The configured parking point is X82.5, Y82.5, Z180 mm. Normal parking
(`G27 P0`, including pause/filament-change parking) raises Z before moving
to the bed center. It never lowers Z if the nozzle is already above 180 mm,
and retains Marlin's minimum clearance and existing travel limits.

SD-print completion runs `G27 P0` followed by `M84XYE`, keeping Z enabled
immediately after parking. The normal stepper inactivity timeout still applies.
In your slicer's end G-code, put `G27 P0` before any stepper-disable command
and use `M84XYE` instead of `M84` if Z must remain enabled. This is also
needed for host/USB printing, which does not use the SD-completion hook.
Parking requires homed axes; if the slicer disables motors first, the
firmware safely refuses to park. Do not home over a finished print.

Avoid `G27 P1` after printing: it forces Z180 even if this would lower the
nozzle into a taller object. Ensure the print is below the parking height
with enough clearance for the move to the center.
