#!/usr/bin/env python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

import os
import sys
from src.hapmap import Hapmap
from src.vcf import Vcf
from src.family import Family
from src.plink_ped import Plink_Ped
from src.plink_map import Plink_Map
from src.output_struct import Output_struct
from src.output_ped import Output_ped
from src.dataholder import DataHolder

class Controller:

    def __init__(self):
        self.data = DataHolder()
        self.hapmap_mnger = Hapmap()
        self.family_mnger = Family()
        self.ped_mnger = Plink_Ped()
        self.map_mnger = Plink_Map()
        self.vcf_mnger = Vcf()
        self.output_struct_mnger = Output_struct()
        self.output_ped_mnger = Output_ped()

    def execute(self, args):

############################################### inputs ######################################################################

        # Read HapMap file
        if args.hapmap:
            hapmap_filename = args.hapmap
            Hapmap.read_hapmap(self.hapmap_mnger, hapmap_filename, self.data)

        # Read VCF file
        if args.vcf:
            vcf_filename = args.vcf
            Vcf.read_vcf(self.vcf_mnger, vcf_filename, self.data)

        # Read Family file
        if args.family:
            family_filename = args.family
            Family.read_family(self.family_mnger, family_filename, self.data)

        # Read Ped file
        if args.plink_ped:
            ped_filename = args.plink_ped
            Plink_Ped.read_ped(self.ped_mnger, ped_filename, self.data)

        # Read Ped file
        if args.plink_map:
            map_filename = args.plink_map
            Plink_Map.read_map(self.map_mnger, map_filename, self.data)

############################################### outputs ######################################################################

        # Create output directory
        out_dir = "reformat_output"
        if args.out:
            out_dir = args.out
        os.system('mkdir -p ' + out_dir)

        # Write structure file
        Output_struct.to_file(self.output_struct_mnger, out_dir, self.data)

        # Write ped file
        Output_ped.to_file(self.output_ped_mnger, out_dir, self.data)

