#!/bin/sh

set -e

for d in *; do
    [ ! -d $d ] && continue
    [ -f $d/SUBMITTED ] && continue
    [ -f $d/RUNNING? ] && continue
    [ -f $d/conv_loop3 ] && continue

    # ignore existing(?)
    [ -f $d/POTCAR ] && continue

    echo
    echo $d

    cp -f puhti.py jobfile $d/.

    #sed "s/^#PBS -N .*/#PBS -N $d/" jobfile >$d/jobfile
    sed "s/^#SBATCH --job-name=.*/#SBATCH --job-name=$d/" jobfile >$d/jobfile
    chmod +x $d/jobfile

    #makepot $d
#    makekpoints $d
done
