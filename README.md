# 100 mm XY Laser CNC

A compact XY laser CNC system designed in SOLIDWORKS and controlled by FluidNC on a Wemos D1 R32 with a CNC Shield V3. The machine combines two 100 mm linear stages, DRV8825 stepper drivers, a custom enclosure, and a LaserTree 5 W optical module.

<p align="center">
  <img src="media/cad-previews/cnc-assembly-isometric.png" width="720" alt="Full 100 mm XY laser CNC assembly in SOLIDWORKS">
</p>

<p align="center"><em>Full machine assembly from <code>cad/CNC Assembly.SLDASM</code>.</em></p>

## Highlights

- 100 mm X/Y travel configured at 3,200 steps/mm
- 1/32 microstepping with two DRV8825 drivers
- 600 mm/min configured maximum motion rate
- FluidNC v4 configuration for a Wemos D1 R32 + CNC Shield V3
- 5 kHz PWM laser control on GPIO19
- Custom SOLIDWORKS cage, slider, electronics enclosure, and adapter models

## Completed build

![Completed CNC machine](media/photos/machine-front.jpg)

## CAD files

| Design source | File |
| --- | --- |
| Complete machine | [`CNC Assembly.SLDASM`](cad/CNC%20Assembly.SLDASM) |
| Native component library | [`cad/`](cad/) — organized by subsystem |
| Retained neutral models | [`IEC320-C14.STEP`](cad/AC%20Plug/IEC320-C14.STEP) · [`Laser Tree 40W AA.step`](cad/Laser%20Tree%20Slider/Laser%20Tree%2040W%20AA.step) |

Intermediate STEP and STL exports are intentionally omitted; the native SOLIDWORKS files are the design source of truth. Cage subassembly views and component previews remain available in the [CAD gallery](docs/cad-gallery.md).

## Repository layout

| Folder | Contents |
| --- | --- |
| [`cad/`](cad/) | Native SOLIDWORKS assemblies and parts, plus two retained vendor STEP models |
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
