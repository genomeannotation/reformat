#!/usr/bin/env python

import os
import sys

class Output_ped:

	def __init__(self):
		"""nothing"""

	#genotype conversion
	def ped_genotype(self, snp):
		switcher = {
			'.': '0',
			'0': '1',
			'1': '2',
		}
		return (switcher.get(snp[0], "\nOops\n") + " " + switcher.get(snp[2], "\nOops\n"))

	#convert sex to number
	def sex_to_number(self, ind_sex):
		return_num = 0
		if (ind_sex == "Female"):
			return_num = 1
		if (ind_sex == "Male"):
			return_num = 2
		return return_num

	#ped output
	def to_file(self, out_dir, data):	
		output = []

        	fo = open(out_dir + '/output.ped', 'w')

		trans_SNPs = zip(*data.SNPs) #transpose the SNPs

		#begin formatting output
		output.append([])

		#format top line (labels)
		output[-1].append("#Family\tID\tMom\tDad\tSex\tPhenotype")
		for label in data.SNP_labels:
			output[-1].append("\t%s" % label)

		#format text body
		for i, name in enumerate(data.ped_ind):

			#select individuals that appear in families text
			try:
				location = data.ind_names.index(name)	
			except ValueError:
				location = -1

			if (location >= 0):
				output.append([])
				output[-1].append(data.ped_family[i])
				output[-1].append(data.ped_ind[i])

				#family decicions
				if (data.ped_status[i] == "Mom"):
					output[-1].append("0\t0")
				elif (data.ped_status[i] == "Dad"):
					output[-1].append("0\t0")
				elif (data.ped_status[i] == "Parent"):
					output[-1].append("0\t0")
				else:
					#find mom of individual
					for parent_location in range(len(data.ped_family)):
						if (data.ped_status[parent_location] == "Mom" and data.ped_family[parent_location] == data.ped_family[i]): 
							output[-1].append(data.ped_ind[parent_location])
						elif (data.ped_status[parent_location] == "Parent" and data.ped_sex[parent_location] == "Female" and \
							 data.ped_family[parent_location] == data.ped_family[i]): 
							output[-1].append(data.ped_ind[parent_location])
					#find dad of individual
					for parent_location in range(len(data.ped_family)):
						if (data.ped_status[parent_location] == "Dad" and data.ped_family[parent_location] == data.ped_family[i]): 
							output[-1].append(data.ped_ind[parent_location])
						elif (data.ped_status[parent_location] == "Parent" and data.ped_sex[parent_location] == "Male" and \
							 data.ped_family[parent_location] == data.ped_family[i]): 
							output[-1].append(data.ped_ind[parent_location])

				output[-1].append(self.sex_to_number(data.ped_sex[i]))

				if (data.ped_phenotype[i] == "Brown"):
					output[-1].append("1")
				elif (data.ped_phenotype[i] == "White"):
					output[-1].append("2")

				#TODO this may be a wrong decision
				if len(data.REF_ALT) == 0: #output in non-ddrad form
					for snp in data.SNPs[location]:
						output[-1].append(snp[0] + " " + snp[2] + "\t")
				else:
					for snp in trans_SNPs[location]:
						output[-1].append(self.ped_genotype(snp))
	
			#progress output
			sys.stdout.write('\r')
			sys.stdout.write("[processing .ped output: " + str(((i+1)*100/len(data.ped_ind))) + "%]")
			sys.stdout.flush()


		sys.stdout.write('\n')
	
		#write output to file
		fo = open(fo.name, 'w')
		i = 0
		for line in output:
			j=0
			#first line for individual
			for word in line:
				if i == 0:
					fo.write("%s" % word)#SNP_labels
				else:
					fo.write("%s\t" % word)
				j=j+1

			i=i+1	
			fo.write("\n")

			#progress output
			sys.stdout.write('\r')
			sys.stdout.write("[writing: " + fo.name + " " + str((i*100/len(output))) + "%]")
			sys.stdout.flush()

		fo.close()
		sys.stdout.write('\n')

