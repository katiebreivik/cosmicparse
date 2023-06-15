import numpy as np
import pandas as pd
import argparse

# Create the parser
parser = argparse.ArgumentParser(description='Command line argument parser')

# Add arguments
parser.add_argument('--population_select', type=str, help='specifies which populations to select', nargs='+')
parser.add_argument('--dat_file', type=str, help='specify the datfile')
parser.add_argument('--counts', type=bool, help='do you want to count the specified population')
# Parse the arguments
args = parser.parse_args()

# Access the parsed arguments
pop_select = args.population_select 
dat_file = args.dat_file
counts = args.counts

bpp = pd.read_hdf(dat_file, key='bpp')

for pop in pop_select:
    if pop == 'DWD':
        if counts:
            print(len(bpp.loc[(bpp.kstar_1.isin([10,11,12])) & (bpp.kstar_2.isin([10,11,12]))].values))
    elif pop == 'DNS':
        if counts:
            print(len(bpp.loc[(bpp.kstar_1 == 13) & (bpp.kstar_2 == 13)].values))
    elif pop == 'BBH':
        if counts:
            print(len(bpp.loc[(bpp.kstar_1 == 14) & (bpp.kstar_2 == 14)].values))
