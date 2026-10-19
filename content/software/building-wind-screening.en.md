## From a site image to an inspection overview

Building Wind Screening is a local desktop prototype for annotating groups of buildings and exploring their relative wind-pressure exposure under different wind directions. It brings image calibration, editable building footprints, floor and height information, simplified pressure estimates and visual exports into one workflow.

The project is intended to support exploratory inspection planning for residential communities, campuses and multi-building sites. It helps organize which buildings, facades and floor bands deserve closer attention under a chosen scenario.

## What the current prototype does

- Loads a user-supplied site image and calibrates distances using two scale points.
- Creates and refines building footprints, including corner editing, additional vertices and rotation.
- Records building names, floors, heights and a selected target building.
- Annotates open areas and considers surrounding buildings in directional exposure estimates.
- Compares facade pressures, floor-band summaries and building-level rankings as wind direction changes.
- Saves and reloads project annotations in JSON, and exports static PNG figures and plan-view or pseudo-3D GIF animations.

## A practical workflow

Start with a site image and a known reference length. Calibrate the image, outline the buildings, enter their floors or heights, and mark relevant open areas. Set a wind-speed and incoming-direction scenario, then review the building overview and the selected building’s facade and floor-band outputs.

Annotations remain in the original image-pixel coordinate system. Zooming and panning change the desktop view rather than the stored building geometry.

## How to read the output

The model combines velocity pressure with height-dependent estimates, facade orientation and heuristic adjustments for building shape, surrounding exposure, shielding, open areas and nearby-building channels. Four floor bands provide a compact comparison across building height.

The pseudo-3D animation illustrates how this screening model’s surface-pressure estimates change with wind direction. Its colors describe relative modeled exposure; they are not a computed airflow field or observed damage measurements.

## Scope and current limitations

This is a development-stage screening model. The pressure coefficients and environmental corrections include empirical assumptions, and the project documentation identifies a need for comparison with measurements and established engineering methods. It does not estimate glass-breakage probability or certify structural or facade safety, and it does not replace CFD, wind-tunnel testing or professional engineering assessment.

## Development status and access

The reviewed working folder contains a Python/Tkinter desktop implementation, requirements and product notes, saved example projects, an earlier standalone HTML prototype and exported animations. PNG/GIF export uses Pillow. A public source release and downloadable software package have not been established for this project yet.

This page presents the current software and an existing output example. For a demonstration, collaboration or release enquiries, contact Yuming Su using the link above.
