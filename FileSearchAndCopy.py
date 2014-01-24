#!/usr/bin/python

import os, shutil, argparse

parser = argparse.ArgumentParser()
parser.add_argument("directory", type=str, help="The directory to retrieve files from")
parser.add_argument("extension", type=str, help="The extension of the files to recieve")
parser.add_argument("destination", type=str, help="The Directory to copy the files to")
parser.add_argument("-o", "--open", help="Open the directory where you copied the files to")
args = parser.parse_args()

toCopy = []
for root, dirs, files in os.walk(args.directory):
	for file in files:
		if file.endswith(args.extension):
			toCopy.append(os.path.join(root, file))

if len(toCopy)==0:
	print "No such files"

for i in toCopy:
	shutil.copy(i, args.destination)

if args.open:
	os.system('open ' + args.destination)


