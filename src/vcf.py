#!/usr/bin/env python

import os
import sys

class Vcf:

	def __init__(self):
		"""nothing"""

	#read info from vcf
	def read_vcf(self, vcf_filename, data):

		# Verify and read VCF file
		if not os.path.isfile(vcf_filename):
		    sys.stderr.write("Failed to find " + vcf_filename + ".\n")
		    sys.exit()
		sys.stderr.write("Reading Vcf...\n")

		fi = open(vcf_filename, 'r')
		allLines = fi.readlines()

		g = 0
		for i, words in enumerate(allLines):
			words = words.strip('\n')
			splits = words.split("\t")
			#take individual names
			if splits[0] == "#CHROM":
				data.ind_names = splits[9:]
				g = 1
			#take SNP data
			elif g == 1:
				#SNP label
				data.SNP_labels.append("S" + splits[2] + "_" + splits[1])
				#SNP reference and alternative
				data.REF_ALT.append([])
				data.REF_ALT[-1].append(splits[3]+splits[4])
				#SNP data
				data.SNPs.append([])
				for snp in splits[9:]:
						data.SNPs[-1].append(snp.split(":")[0])
			#progress output
			sys.stdout.write('\r')
			sys.stdout.write("[reading " + vcf_filename + ": " + str(((i+1)*100/len(allLines))) + "%]")
			sys.stdout.flush()
			i = i+1
		fi.close()
		sys.stdout.write("\n")

