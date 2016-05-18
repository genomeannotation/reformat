#!/usr/bin/env python

import os
import sys

class Plink_Map:

	def __init__(self):
		"""nothing"""

	#read plink.map file 
	def read_map(self, map_filename, data):	

		# Verify and read map file
		if not os.path.isfile(map_filename):
		    sys.stderr.write("Failed to find " + map_filename + ".\n")
		    sys.exit()
		sys.stderr.write("Reading Map...\n")

		fi = open(map_filename, 'r')
		allLines = fi.readlines()

		i = 1
		for words in allLines:
			words = words.strip('\n')
			splits = words.split("\t")
			if words[0] != "#":
				#SNP label
				data.SNP_labels.append(splits[0].split("|")[3][:-2] + "_" + splits[3])
				#print(SNP_labels[-1])
		

			#progress output
			sys.stdout.write('\r')
			sys.stdout.write("[reading " + map_filename + ": " + str((i*100/len(allLines))) + "%]")
			sys.stdout.flush()
			i = i+1

		fi.close()
		sys.stdout.write('\n')
