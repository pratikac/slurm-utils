#!/home/pratikac/anaconda2/bin/python

import os, sys, argparse, subprocess

parser = argparse.ArgumentParser('slurm cancel')
ap = parser.add_argument
ap('-u', type=str, help='username', default='pratikac')
opt = vars(parser.parse_args())
