#!/usr/bin/env python

import os
import sys

class Family:

	def __init__(self):
		"""nothing"""

	#read family.txt file 
	def read_family(self, family_filename, data):

		# Verify and read family file
		if not os.path.isfile(family_filename):
		    sys.stderr.write("Failed to find " + family_filename + ".\n")
		    sys.exit()
		sys.stderr.write("Reading Family...\n")

		fi = open(family_filename, 'r')
		allLines = fi.readlines()

		i = 1
		for words in allLines:
			words = words.strip('\n')
			splits = words.split("\t")
			if (splits[0][0] != '#'):
				#status = mom or dad or offspring
				data.ped_status.append(splits[0].strip())
				#get ped_ind
				data.ped_ind.append(splits[1].strip())	
				#family number
				data.ped_family.append(splits[2].strip())
				#get ind phenotype
				data.ped_phenotype.append(splits[3].strip())
				#get sex
				data.ped_sex.append(splits[4].strip())
			#progress output
			sys.stdout.write('\r')
			sys.stdout.write("[reading " + family_filename + ": " + str((i*100/len(allLines))) + "%]")
			sys.stdout.flush()
			i = i+1
		fi.close()
		sys.stdout.write('\n')	
