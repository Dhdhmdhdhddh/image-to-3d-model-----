# 🧊 Image → 3D

Convert photos to 3D models. Two modes, fully free, runs on Google Colab.

## Modes

| Mode | What it does | Best for |
|------|-------------|----------|
| **scene** | Whole photo → 3D terrain with photo texture | Landscapes, cityscapes, any photo |
| **subject** | Isolates main object → full 3D model | Cars, objects, animals |

## Quick Start

1. Go to [Google Colab](https://colab.research.google.com)
2. File → Upload notebook → pick `notebooks/image_to_3d.ipynb`
3. Runtime → Change runtime type → **T4 GPU**
4. Set `MODE = "scene"` or `MODE = "subject"` in Cell 1
5. Run all cells → download your files

## View Your Model

Open `viewer/3d_viewer.html` in any browser (no internet needed).  
Drop your downloaded OBJ or GLB onto it.

## Scripts

| Script | What it does |
|--------|-------------|
| `scripts/depthmap_to_obj.py` | Convert a depthmap PNG + photo → OBJ mesh locally |
| `scripts/brightness_to_obj.py` | Simple brightness-based heightmap (no AI, fast) |

## Files You Get

- **scene mode**: `scene_terrain.obj` + `texture.png` + `depthmap.png`
- **subject mode**: `output.glb` (textured 3D model)

## Requirements (local)
```
pip install pillow numpy
```
For scene mode on Colab: MiDaS runs automatically (needs GPU).  
For subject mode on Colab: InstantMesh runs automatically (needs GPU).
