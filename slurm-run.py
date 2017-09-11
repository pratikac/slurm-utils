#!/home/pratikac/anaconda2/bin/python

import numpy as np
import os, sys, argparse, time

parser = argparse.ArgumentParser('slurm jobber',
            formatter_class=argparse.ArgumentDefaultsHelpFormatter)
ap = parser.add_argument
ap('-c', type=str, help='command', required=True)
ap('--name', type=str, help='job name', default'sbatch')
ap('-n', type=int, help='num. nodes', default=1)
ap('--nt', type=int, help='tasks per node', default=1)
ap('--nc', type=int, help='cpus per task', default=2)
ap('-m', type=int, help='mem (GB)', default=4)
ap('-g', type=int, help='gpus per node', default=4)
ap('-t', type=str, help='estimated time', default='01:00:00')
ap('-o', type=str, help='output', default='')
opt = vars(parser.parse_args())

if opt['g'] < 4:
    opt['g'] = 'gpu:%d'%opt['g']
else:
    opt['g'] = 'gpu:lgpu:%d'%opt['g']

loc = '/home/pratikac/local2/pratikac/results/'
opt['o'] = loc + time.strftime('%b_%d_%H_%M_%S_') + opt['name'] + '.out'

cmd='''#!/bin/sh

#SBATCH --job-name=%s
#SBATCH --nodes=%d
#SBATCH --ntasks=%d
#SBATCH --tasks-per-node=%d
#SBATCH --cpus-per-task=%d
#SBATCH --mem=%dG
#SBATCH --gres=%s
#SBATCH --time=%s
#SBATCH --output=%s

%s'''%(opt['name'], opt['n'], opt['n'], opt['nt'], opt['nc'], opt['m'], opt['g'], opt['t'],
    opt['o'], opt['c'])

s = u'''echo \"%s\" | sbatch '''%cmd
print s

os.system(s)
