"""
brightness_to_obj.py
--------------------
Simple brightness-based heightmap. No AI, no GPU, instant.
Not as accurate as MiDaS but works offline.

Usage:
    python brightness_to_obj.py --photo photo.jpg --out output.obj
"""

import argparse
import numpy as np
from PIL import Image, ImageFilter

def brightness_to_obj(photo_path, out_path, scale=4, height_scale=0.3):
    photo = Image.open(photo_path).convert("RGB")
    W, H = photo.size
    MW, MH = W // scale, H // scale

    gray = np.array(photo.resize((MW, MH)).convert("L"), dtype=np.float32) / 255.0
    photo_small = np.array(photo.resize((MW, MH)), dtype=np.float32) / 255.0

    positions, colors, uvs, indices = [], [], [], []

    for y in range(MH):
        for x in range(MW):
            positions.append(((x/(MW-1))*2-1, -((y/(MH-1))*2-1), float(gray[y,x])*height_scale))
            r,g,b = photo_small[y,x,:3]
            colors.append((float(r), float(g), float(b)))
            uvs.append((x/(MW-1), 1-y/(MH-1)))

    for y in range(MH-1):
        for x in range(MW-1):
            a=y*MW+x; b=y*MW+x+1; c=(y+1)*MW+x+1; d=(y+1)*MW+x
            indices.extend([(a,b,c),(a,c,d)])

    with open(out_path, "w") as f:
        f.write("# Brightness heightmap OBJ\n\n")
        for v,c in zip(positions,colors):
            f.write(f"v {v[0]:.4f} {v[1]:.4f} {v[2]:.4f} {c[0]:.3f} {c[1]:.3f} {c[2]:.3f}\n")
        f.write("\n")
        for uv in uvs:
            f.write(f"vt {uv[0]:.4f} {uv[1]:.4f}\n")
        f.write("\n")
        for tri in indices:
            a,b,c=tri[0]+1,tri[1]+1,tri[2]+1
            f.write(f"f {a}/{a} {b}/{b} {c}/{c}\n")

    print(f"✅ {out_path} — {len(positions):,} verts, {len(indices):,} tris")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--photo", required=True)
    parser.add_argument("--out", default="output.obj")
    parser.add_argument("--scale", type=int, default=4)
    parser.add_argument("--height", type=float, default=0.3)
    args = parser.parse_args()
    brightness_to_obj(args.photo, args.out, args.scale, args.height)
