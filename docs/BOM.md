# Working bill of materials

This list is derived from the FluidNC configuration, wiring diagram, CAD filenames, and build photos. Product URLs are intentionally not guessed; verify each exact listing against the AliExpress order history before purchasing replacements.

| Subsystem | Part | Qty. | Design evidence |
| --- | --- | ---: | --- |
| Controller | Wemos D1 R32 | 1 | FluidNC configuration and circuit diagram |
| Motion control | CNC Shield V3 | 1 | FluidNC configuration and circuit diagram |
| Motion control | DRV8825 stepper driver | 2 | One driver for each X/Y stage |
| Motion | NEMA 11 linear stage / actuator | 2 | X/Y CAD and configuration |
| Laser | LaserTree LT-40W-A 5 W optical module | 1 | Configuration and build photos |
| Laser | P-DA-01 driver adapter | 1 | CAD assembly and circuit diagram |
| Power | Mean Well LRS-150-12, 12 V / 150 W supply | 1 | CAD model and electronics-box photo |
| Power entry | IEC320-C14 inlet / switch assembly | 1 | CAD model and build photo |
| Cooling | 12 V DC fan | 1 | CAD model and build photo |
| Structure | Custom cage, slider, and electronics-box parts | 1 set | SOLIDWORKS assemblies and STL exports |

## Configuration references

- X/Y travel: 100 mm
- X/Y steps per millimetre: 3,200
- X/Y maximum rate: 600 mm/min
- Laser PWM: 5 kHz on GPIO19
- Full wiring reference: [`media/diagrams/circuit-diagram.png`](../media/diagrams/circuit-diagram.png)

