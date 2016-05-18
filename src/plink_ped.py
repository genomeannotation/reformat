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
		sys.stderr.write("Reading Ped...\n")

		fi = open(ped_filename, 'r')
		allLines = fi.readlines()

		i = 1
		for line in allLines:
			line = line.strip('\n')
			splits = line.split("\t")

			if line[0] != "#":
		
				#individual ID
				data.ind_names.append(splits[1])
				#print ("%s" %len(SNPs_firsts))
				#first fill allele reference
				if len(data.SNPs_firsts) < 10:
					#print ("filling firsts")
					j = 1
					while j < len(splits[6:])+1:
						data.SNPs_firsts.append(splits[j+6:j+7])
						j = j + 1

				#get SNPs				
				j = 0
				data.SNPs.append([])
				while j < len(splits[6:]):
					#update allele reference
					if (data.SNPs_firsts[j] == ['0'] and splits[j+6:j+7] != ['0']):
						data.SNPs_firsts[j] = splits[j+6:j+7]
					if (data.SNPs_firsts[j+1] == ['0'] and splits[j+7:j+8] != ['0']):
						data.SNPs_firsts[j+1] = splits[j+7:j+8]
					#convert allele pairs to relative numbers
					if (splits[j+6:j+7] == ['0']):
						first = '0'
					elif (splits[j+6:j+7] == data.SNPs_firsts[j]):
						first = '1'
					else:
						first = '2'

					if (splits[j+7:j+8] == ['0']):
						second = '0'
					elif (splits[j+7:j+8] == data.SNPs_firsts[j+1]):
						second = '1'
					else:
						second = '2'

					thing = first, " ",second
					data.SNPs[-1].append(thing)
					j = j + 2
				#print ("%s %s %s %s %s\t" % (ind_names[-1], SNPs[-1][0], SNPs_firsts[0], SNPs_firsts[1], len(SNPs[-1])))
			#progress output
			sys.stdout.write('\r')
			sys.stdout.write("[reading " + ped_filename + ": " + str((i*100/len(allLines))) + "%]")
			sys.stdout.flush()
			i = i+1

		fi.close()	
		sys.stdout.write('\n')
