#!/usr/bin/env python

import os
import sys

class Output_struct:

	def __init__(self):
		"""nothing"""

	#nucleotide to Corresponding number
	def nucleo_to_numbers(self, letter, iteration):
	    switcher = {
		'A': '\t1' if iteration==1 else '\t1',
		'C': '\t2' if iteration==1 else '\t2',
		'G': '\t3' if iteration==1 else '\t3',
		'T': '\t4' if iteration==1 else '\t4',
		'R': '\t1' if iteration==1 else '\t3',
		'Y': '\t2' if iteration==1 else '\t4',
		'S': '\t2' if iteration==1 else '\t3',
		'W': '\t1' if iteration==1 else '\t4',
		'K': '\t3' if iteration==1 else '\t4',
		'M': '\t1' if iteration==1 else '\t2',
		'N': '\t-9' if iteration==1 else '\t-9',
	    }
	    return switcher.get(letter, "\nOops\n")

	#binary to letter
	def bin_to_letter(self, duo, ref_alt):
		letter_to_num = {
			'A': '1',
			'C': '2',
			'G': '3',
			'T': '4',	 
		}
		switcher1 = {
			'0': letter_to_num.get(ref_alt[0][0]),
			'1': letter_to_num.get(ref_alt[0][1]),
			'.': 'N'
		}
		phase2 = switcher1.get(duo[0], "\nOops\n") + switcher1.get(duo[2], "\nOops\n")
		switcher2 = {
			'11': 'A',
			'22': 'C',
			'33': 'G',
			'44': 'T',
			'13': 'R',
			'31': 'R',
			'42': 'Y',
			'24': 'Y',
			'23': 'S',
			'32': 'S',
			'14': 'W',
			'41': 'W',
			'34': 'K',
			'43': 'K',
			'12': 'M',
			'21': 'M',
			'NN': 'N',
		}
		return switcher2.get(phase2, "\nOops\n")

	#struct output
	def to_file(self, out_dir, data):
		output = []
		temp_SNPS = []

		if len(data.REF_ALT) == 0:
			return #do not print struct output when there is no reference/alternative for genome

		fo = open(out_dir + '/output.struct', 'w')

		for i, snps in enumerate(data.SNPs):
			temp_SNPS.append([])
			for snp in snps:
				temp_SNPS[-1].append(self.bin_to_letter(snp, data.REF_ALT[i]))
			#progress output
			sys.stdout.write('\r')
			sys.stdout.write("[processing .struct output: " + str(round(((i+1)*100/len(data.SNPs)))) + "%]")
			sys.stdout.flush()

		trans_SNPs = list(zip(*temp_SNPS)) #transpose the SNPs

		#format output
		output.append(data.SNP_labels)

		for i, name in enumerate(data.ind_names):
			output.append([])
			output[-1].append(name)
			output[-1].append('A') #start SNP list with 1's
			for snp in trans_SNPs[i]: 
				output[-1].append(snp) 

			#progress output
			sys.stdout.write('\r')
			sys.stdout.write("[processing .struct output: " + str(round(((i+1)*100/len(data.ind_names)))) + "%]")
			sys.stdout.flush()
		sys.stdout.write('\n')
	
		#write output to file
		for i, line in enumerate(output):
			#first line for individual
			for j, word in enumerate(line):
				if i == 0:
					fo.write("%s\t" % word)#SNP_labels
				elif j == 0:
					fo.write("%s" % word)#ind_name
				else:
					fo.write(self.nucleo_to_numbers(word, 1))
		
			#second line for individual
			if i != 0: fo.write("\n")
			for j, word in enumerate(line):
				if i == 0: break #skip SNP_labels 
				elif j == 0:
					fo.write("%s" % word)#ind_name
				else:
					fo.write(self.nucleo_to_numbers(word, 2))			
			
			fo.write("\n")

			#progress output
			sys.stdout.write('\r')
			sys.stdout.write("[writing " + fo.name + ": " + str(round(((i+1)*100/len(output)))) + "%]")
			sys.stdout.flush()

		fo.close()
		sys.stdout.write('\n')
