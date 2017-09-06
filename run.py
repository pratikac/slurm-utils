import numpy as np
import os, sys, argparse, time

parser = argparse.ArgumentParser('slurm jobber')
ap = parser.add_argument
ap('-c', type=str, help='command', required=True)
ap('-n', type=int, help='num. nodes', default=1)
ap('--nt', type=int, help='tasks per node', default=1)
ap('--nc', type=int, help='num. cpus', default=2)
ap('--mem', type=int, help='mem (GB)', default=4)
ap('-g', type=int, help='num. gpus', default=4)
ap('-t', type=str, help='estimated time', default='01:00:00')
ap('-o', type=str, help='output', default='')
opt = vars(parser.parse_args())

if opt['g'] < 4:
    opt['g'] = 'gpu:%d'%opt['g']
else:
    opt['g'] = 'gpu:lgpu:%d'%opt['g']

opt['o'] = time.strftime('(%b_%d_%H_%M_%S)') + '.out'


cmd='''#!/bin/sh

#SBATCH --nodes=%d
#SBATCH --ntasks=%d
#SBATCH --tasks-per-node=%d
#SBATCH --cpus-per-task=%d
#SBATCH --mem=%dG
#SBATCH --gres=%s
#SBATCH --time=%s
#SBATCH --output=%s

%s'''%(opt['n'], opt['n'], opt['nt'], opt['nc'], opt['mem'], opt['g'], opt['t'],
    opt['o'], opt['c'])

s = u"echo '%s' | sbatch "%cmd
print s

#os.system(s)
