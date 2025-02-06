#!/bin/sh


for d in *; do
    [ ! -d $d ] && continue
    [ -f $d/SUBMITTED ] && continue
    [ -f $d/RUNNING? ] && continue
    [ -f $d/conv_loop3 ] && continue
    #[ -f $d/conv_loop5 ] && continue

    # ignore existing(?)
    #[ -f $d/slurm-* ] && continue

    echo
    echo "$d: submitting..."

    cd $d
    chmod u+x jobfile
    #echo "missing job for $d"
    sbatch jobfile | tee SUBMITTED
    cd - >/dev/null

done

#qstat -u $USER

squeue -u $USER -o '%.7i %.18j %.9M %.10l %.5D %.6P %.2t %R'
