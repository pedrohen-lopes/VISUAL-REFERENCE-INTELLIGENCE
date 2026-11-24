#!/usr/bin/env python3
"""Extrai quadros de vídeo com ffmpeg (verifica disponibilidade) e lista timestamps."""
import argparse
import os
import shutil
import subprocess
import sys

ap = argparse.ArgumentParser(description=__doc__)
ap.add_argument("video")
ap.add_argument("--fps", type=float, default=0, help="quadros por segundo a extrair (ex.: 10)")
ap.add_argument("--scene", type=float, default=0, help="limiar de mudança de cena (0.1-0.5) em vez de fps fixo")
ap.add_argument("--start", default="", help="início (s ou hh:mm:ss)")
ap.add_argument("--duration", default="", help="duração a extrair")
ap.add_argument("--out", default="frames")
args = ap.parse_args()

if not shutil.which("ffmpeg"):
    sys.exit("ffmpeg não encontrado. Instale (ex.: sudo apt install ffmpeg / pkg install ffmpeg) ou peça frames-chave ao usuário.")
if not os.path.exists(args.video):
    sys.exit(f"Arquivo não encontrado: {args.video}")
os.makedirs(args.out, exist_ok=True)
if shutil.which("ffprobe"):
    info = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
                           "stream=width,height,r_frame_rate,duration", "-of", "default=nw=1", args.video],
                          capture_output=True, text=True)
    print("Informações do vídeo:\n" + info.stdout.strip())
cmd = ["ffmpeg", "-y", "-hide_banner"]
if args.start:
    cmd += ["-ss", args.start]
if args.duration:
    cmd += ["-t", args.duration]
cmd += ["-i", args.video]
if args.scene > 0:
    vf = f"select='gt(scene,{args.scene})',showinfo"
    cmd += ["-vf", vf, "-vsync", "vfr"]
elif args.fps > 0:
    cmd += ["-vf", f"fps={args.fps},showinfo"]
else:
    cmd += ["-vf", "fps=5,showinfo"]
cmd += [os.path.join(args.out, "F%04d.png")]
proc = subprocess.run(cmd, capture_output=True, text=True)
if proc.returncode != 0:
    sys.exit("Falha no ffmpeg:\n" + proc.stderr[-800:])
times = []
for line in proc.stderr.splitlines():
    if "pts_time:" in line:
        t = line.split("pts_time:")[1].split()[0]
        times.append(t)
with open(os.path.join(args.out, "timestamps.txt"), "w") as fh:
    for i, t in enumerate(times, 1):
        fh.write(f"F{i:04d}\t{t}s\n")
print(f"{len(times)} quadros em {args.out}/ (timestamps.txt). Timestamps relativos ao início do trecho extraído.")
