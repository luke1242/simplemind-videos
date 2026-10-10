#!/bin/bash
# Quiet UI sounds generated locally with ffmpeg (no downloads).
set -e; mkdir -p assets/sfx; cd assets/sfx
ffmpeg -v error -y -f lavfi -i "anoisesrc=d=0.35:c=pink:r=44100" -af "highpass=f=800,lowpass=f=5000,afade=t=in:d=0.12,afade=t=out:st=0.12:d=0.23,volume=0.8" swoosh.wav
ffmpeg -v error -y -f lavfi -i "sine=f=620:d=0.14:r=44100" -af "afade=t=out:st=0.02:d=0.12,volume=0.9" pop.wav
ffmpeg -v error -y -f lavfi -i "anoisesrc=d=0.05:c=white:r=44100" -af "highpass=f=1500,afade=t=out:st=0.005:d=0.045,volume=0.7" click.wav
ffmpeg -v error -y -f lavfi -i "sine=f=1320:d=0.9:r=44100" -af "afade=t=in:d=0.01,afade=t=out:st=0.05:d=0.85,volume=0.6" ding.wav
