import sys
import argparse
from src.controller import Controller

def main():
    parser = argparse.ArgumentParser(
    epilog="""
    Formatting tool for structure and pedigree output.
    """,
    formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument('-hmp', '--hapmap')
    parser.add_argument('-v', '--vcf')
    parser.add_argument('-p', '--plink_ped')
    parser.add_argument('-m', '--plink_map')
    parser.add_argument('-f', '--family')
    parser.add_argument('-o', '--out')
    args = parser.parse_args()
    controller = Controller()
    controller.execute(args)

if __name__ == '__main__':
    main()
