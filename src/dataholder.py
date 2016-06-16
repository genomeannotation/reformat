#!/usr/bin/env python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

import os
import sys

class DataHolder:

    def __init__(self):
        self.SNPs = []
        self.SNP_labels = []
        self.output = []
        self.ind_names = []
        self.REF_ALT = []
        self.ped_status = []
        self.ped_ind = []
        self.ped_family = []
        self.ped_phenotype = []
        self.ped_sex = []
        self.ped_mom = []
        self.ped_dad = []
        self.SNPs_firsts = []
        self.plink_rejects = []
