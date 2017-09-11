#!/home/pratikac/anaconda2/bin/python

import os, sys, argparse, subprocess

parser = argparse.ArgumentParser('slurm cancel')
ap = parser.add_argument
ap('-u', type=str, help='username', default='pratikac')
ap('-i', type=int, nargs='*', help='idx of jobs', default=[-1])
opt = vars(parser.parse_args())
#print opt

c = 'squeue -u %s'%(opt['u'])
p = subprocess.Popen(c, shell=True, stdout=subprocess.PIPE)
r, _ = p.communicate()
print r
r = r.strip().rstrip().split('\n')[1:]
idxs = []
for _r in r:
    i = int(_r.strip().split(' ')[0])
    idxs.append(i)
print 'Found jobs: ', idxs

for i in opt['i']:
    if i > len(idxs):
        print 'Cannot cancel job index: %d'%i
        continue
    if i >= 0:
        c = 'scancel %d'%(idxs[i])
        p = subprocess.Popen(c, shell=True, stdout=subprocess.PIPE)
        r, err = p.communicate()
        print 'Canceled: ', idxs[i]
