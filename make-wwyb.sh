#!/bin/sh

text2wave -mode singing tmp/$1.xml -o tmp/$1.wav -eval "(voice_us1_mbrola)"
ffmpeg -hide_banner -loglevel error -y -i tmp/$1.wav -i wwyg-instruments.wav -filter_complex amix=inputs=2:duration=longest tmp/$1-mixed.wav
ffmpeg -hide_banner -loglevel error -y -loop 1 -i img.jpg -i tmp/$1-mixed.wav -c:v libx264 -tune stillimage -c:a aac -b:a 192k -pix_fmt yuv420p -shortest tmp/$1.mp4
