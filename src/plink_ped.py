#!/usr/bin/env python

import os
import sys

class Plink_Ped:

	def __init__(self):
		"""nothing"""

	#read plink.ped file
	def read_ped(self, ped_filename, data):

		# Verify and read ped file
		if not os.path.isfile(ped_filename):
		    sys.stderr.write("Failed to find " + ped_filename + ".\n")
		    sys.exit()

		fi = open(ped_filename, 'r')
		allLines = fi.readlines()

		for i in enumerate(data.ped_family):
			data.SNPs_firsts.append([])
		
		i = 1
		for line in allLines:
			line = line.strip('\n')
			splits = line.split("\t")

			if line[0] != "#":

				#select individuals that appear in families text
				try:
					location = data.ped_ind.index(splits[1])
					location = int(data.ped_family[location])	
				except ValueError:
					location = -1

				if (location >= 0):
	
					current_snps = splits[6:]
					#individual ID
					data.ind_names.append(splits[1])
					#first fill allele reference
					for p, e in enumerate(data.plink_rejects):
						del current_snps[p]
					if len(data.SNPs_firsts[location]) < 1:
						for j, m in enumerate(current_snps):
							data.SNPs_firsts[location].append(current_snps[j])

					#get SNPs			
					j = 0
					data.SNPs.append([])
					while j < len(current_snps):
						#update allele reference/alternate
						if (data.SNPs_firsts[location][j] == '0' and current_snps[j] != '0'):
							data.SNPs_firsts[location][j] = current_snps[j]
						if (data.SNPs_firsts[location][j+1] == '0' and current_snps[j+1] != '0'):
							data.SNPs_firsts[location][j+1] = current_snps[j+1]

						#convert allele pairs to relative numbers
						if (current_snps[j] == '0'):
							first = '0'
						elif (current_snps[j] == data.SNPs_firsts[location][j]):
							first = '1'
						else:
							first = '2'

						if (current_snps[j+1] == '0'):
							second = '0'
						elif (current_snps[j+1] == data.SNPs_firsts[location][j+1]):
							second = '1'
						else:
							second = '2'

						thing = first, " ",second
						data.SNPs[-1].append(thing)
						j = j + 2

			#progress output
			sys.stdout.flush()
			sys.stdout.write("[reading " + ped_filename + ": " + str(round((i*100/len(allLines)))) + "%]")
			sys.stdout.write('\r')			
			i = i+1

		fi.close()	
		sys.stdout.write('\n')
