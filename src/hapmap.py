#!/usr/bin/env python

import os
import sys

class Hapmap:

	def __init__(self):
		"""nothing"""

	#read info from hapmap
	def read_hapmap(self, hapmap_filename, data):

		# Verify and read hapmap file
		if not os.path.isfile(hapmap_filename):
		    sys.stderr.write("Failed to find " + hapmap_filename + ".\n")
		    sys.exit()
		sys.stderr.write("Reading Hapmap...\n")

		fi = open(hapmap_filename, 'r')
		allLines = fi.readlines()

		i = 1
		for words in allLines:
			words = words.strip('\n')
			splits = words.split("\t")
			#take individual names
			if i == 1:
				for name in splits[12:]:
					data.ind_names.append(name.split(':')[0])
			#take SNP data
			else:
				#SNP label
				data.SNP_labels.append(splits[0])
				#SNP nucleotide
				data.SNPs.append([])
				data.SNPs[-1] = (splits[12:])
		
			#progress output
			sys.stdout.write('\r')
			sys.stdout.write("[reading " + hapmap_filename + ": " + str((i*100/len(allLines))) + "%]")
			sys.stdout.flush()
			i = i+1

		fi.close()
		sys.stdout.write('\n')
		print "number of names: ", len(data.ind_names)
		print "number of SNP locations: ", len(data.SNP_labels)

		sys.stderr.write("Done.\n")

