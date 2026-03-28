# usd2gltf

USD to GLTF/GLB converter

Current version `0.3.5`

## Usage

This package can be incorporated into a DCC tool (like Houdini) or used from the command-line.

### CLI

usage: usd2gltf [-h] [-i INPUT] [-o OUTPUT] [--interpolation INTERPOLATION] [-d] [-f]

Convert incoming USD(z) file to glTF/glb

optional arguments:

- -h, --help show this help message and exit
- -i INPUT, --input INPUT
  - Input USD (.usd, .usdc, .usda, .usdz)
- -o OUTPUT, --output OUTPUT
  - Output glTF (.gltf, .glb)
- --interpolation INTERPOLATION
  - Interpolation of animation (LINEAR, STEP, CUBIC)
- -d, --debug Run in debug mode
- -f, --flatten Flatten all animations into one animation

## Requirements

- **Python 3.9–3.13** — The [`usd-core`](https://pypi.org/project/usd-core/) wheels on PyPI do not support Python 3.14 yet, so `pip install usd-core` will not resolve on 3.14. Use 3.13 (or earlier) for the virtualenv, or supply your own USD build with `pxr` on `PYTHONPATH`.
- **OpenUSD (`pxr`)** — Usually via `pip install usd-core`; or a custom Pixar USD build whose Python bindings are on `PYTHONPATH`.
- gltflib
- numpy

## Features

- Mesh conversion
  - UV support (TEXCOORD_0, TEXCOORD_1)
  - displayColor support (COLORS_0)
  - Animated skeleton, weights, skinning
  - Normals and tangents supported
- Materials
  - UsdPreviewSurface -> PBRMetallicRoughness
- Camera conversion
- Light conversion
  - Point
  - Spot
  - Directional
- Xform conversion
  - Animated xforms supported
- Animations
  - Allows per object animation or single flat GLTF animation
- Export
  - GLB and GLTF options
- GLTF Extras
