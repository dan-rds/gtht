#!/usr/bin/env python3
'''-------------------------------------
qr_maker.py

    by Daniel Richards (ddrichar@ucsc.edu)
       on 1-2-2019
-------------------------------------- 
'''
import os, sys
from PIL import Image

def main(tns_output_file):
	f = open(tns_output_file, "r+")
	print("f  [" ,type(f).__name__, "]   :", f)

	pic_matrix = []

	for line in f:
		if (chr(27) in line):
			char_list = line.split(chr(27)+ "[0m")
			pic_line = []
			for pix in char_list:
				pic_matrix.append(1 if '7' in pix else 0)

	img = Image.new('1', [32,32])
	img.putdata(pic_matrix)
	img.save('image.png',scale=2.0)

if __name__ == "__main__":
	if len(sys.argv) < 2:
		print("Must specify filename. E.g., `qr_maker.py filename.txt`")
	main(sys.argv[1])

	