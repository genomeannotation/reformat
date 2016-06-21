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

		fi = open(map_filename, 'r')
		allLines = fi.readlines()

		i = 1
		j = 0
		for words in allLines:
			words = words.strip('\n')
			splits = words.split("\t")
			data.cleaned_map.append([])
			if words[0] != "#":
				#SNP label
				if splits[0].split("|")[3][:-2] + "_" + splits[3] not in data.SNP_labels:
					data.SNP_labels.append(splits[0].split("|")[3][:-2] + "_" + splits[3])
				else:
					data.plink_rejects.append(j)

				data.cleaned_map[-1].append(splits[0].split("|")[3])
				data.cleaned_map[-1].append(splits[1])
				data.cleaned_map[-1].append(splits[2])
				data.cleaned_map[-1].append(str(int(splits[3])-1))
				j = j + 1
			else: 
				data.cleaned_map[-1].append(words)

			#progress output
			sys.stdout.write('\r')
			sys.stdout.write("[reading " + map_filename + ": " + str(round((i*100/len(allLines)))) + "%]")
			sys.stdout.flush()
			i = i+1

		fi.close()
		sys.stdout.write('\n')
