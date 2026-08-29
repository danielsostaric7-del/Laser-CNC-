# 100 mm XY Laser CNC

A compact XY laser CNC system designed in SOLIDWORKS and controlled by FluidNC on a Wemos D1 R32 with a CNC Shield V3. The machine combines two 100 mm linear stages, DRV8825 stepper drivers, a custom enclosure, and a LaserTree 5 W optical module.

![Completed CNC machine](media/photos/machine-front.jpg)

## Highlights

- 100 mm X/Y travel configured at 3,200 steps/mm
- 1/32 microstepping with two DRV8825 drivers
- 600 mm/min configured maximum motion rate
- FluidNC v4 configuration for a Wemos D1 R32 + CNC Shield V3
- 5 kHz PWM laser control on GPIO19
- Custom SOLIDWORKS cage, slider, electronics enclosure, and adapter models

## CAD preview

| Isometric | Front | Right |
| --- | --- | --- |
| ![Cage isometric preview](media/cad-previews/cad-cage-isometric.png) | ![Cage front preview](media/cad-previews/cad-cage-front.png) | ![Cage right preview](media/cad-previews/cad-cage-right.png) |

The complete native assembly is [`cad/CNC Assembly.SLDASM`](cad/CNC%20Assembly.SLDASM). Additional views and component previews are in the [CAD gallery](docs/cad-gallery.md). The preview images are convenience renders from the STEP exports included with the project; the SOLIDWORKS files remain the design source of truth.

## Repository layout

| Folder | Contents |
| --- | --- |
| [`cad/`](cad/) | SOLIDWORKS assemblies, parts, STEP exports, and STL exports |
| [`firmware/`](firmware/) | FluidNC machine configuration |
| [`media/photos/`](media/photos/) | Cleaned photos of the completed machine and electronics |
| [`media/diagrams/`](media/diagrams/) | Wiring and circuit diagram |
| [`media/build/`](media/build/) | Short build/operation video and poster frame |
| [`docs/`](docs/) | CAD gallery, project notes, and working BOM |

## Build documentation

- [Working bill of materials](docs/BOM.md)
- [CAD preview gallery](docs/cad-gallery.md)
- [Build media notes](docs/build-media.md)
- [FluidNC configuration](firmware/config.yaml)
- [Circuit diagram](media/diagrams/circuit-diagram.png)

## Safety

This project uses a high-power laser module and mains-powered equipment. Use a suitable enclosure, interlocks, emergency-stop strategy, ventilation, and wavelength-rated laser eyewear. Validate grounding, polarity, current limits, and the PWM-off behavior before enabling the laser. Never operate the machine unattended.

## License

No license has been specified yet. Until one is added, the project remains all rights reserved.

