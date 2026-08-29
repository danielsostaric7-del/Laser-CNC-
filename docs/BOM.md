# Working bill of materials

This list is derived from the FluidNC configuration, wiring diagram, CAD filenames, and build photos. The exact AliExpress product-page URLs supplied for this build are listed below; verify the selected variant before purchasing replacements.

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
| Structure | Custom cage, slider, and electronics-box parts | 1 set | SOLIDWORKS assemblies and parts |

## Purchased AliExpress listings

These are the seven product-page URLs supplied for this build, kept in the order provided. Listings without a confirmed component mapping are intentionally left unassigned rather than guessed.

| Order | Product page | Build mapping |
| ---: | --- | --- |
| 1 | [AliExpress item 32910354223](https://www.aliexpress.com/item/32910354223.html) | Purchased listing — component mapping to verify |
| 2 | [AliExpress item 1005007144892529](https://www.aliexpress.com/item/1005007144892529.html) | Purchased listing — component mapping to verify |
| 3 | [AliExpress item 1005006478108991](https://www.aliexpress.com/item/1005006478108991.html) | CNC Shield V3 / DRV8825 listing — variant to verify |
| 4 | [AliExpress item 1005006031010342](https://www.aliexpress.com/item/1005006031010342.html) | LaserTree laser-module listing — power variant to verify |
| 5 | [AliExpress item 1005003012523694](https://www.aliexpress.com/item/1005003012523694.html) | Purchased listing — component mapping to verify |
| 6 | [AliExpress item 1005008513205849](https://www.aliexpress.com/item/1005008513205849.html) | Purchased listing — component mapping to verify |
| 7 | [AliExpress item 1005008638665400](https://www.aliexpress.com/item/1005008638665400.html) | Purchased listing — component mapping to verify |

## Configuration references

- X/Y travel: 100 mm
- X/Y steps per millimetre: 3,200
- X/Y maximum rate: 600 mm/min
- Laser PWM: 5 kHz on GPIO19
- Full wiring reference: [`media/diagrams/circuit-diagram.png`](../media/diagrams/circuit-diagram.png)
