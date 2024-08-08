. /disk/lhcb/scripts/lhcb_setup.sh
cd /disk/lhcb_data/sqasim/images
export SINGULARITY_TMPDIR=/disk/users/`whoami`/temp
export TMPDIR=/disk/users/`whoami`/tmp
singularity shell --nv -B /cvmfs -B /disk/users/`whoami` -B /run/user/21528 -B /home/hep/`whoami` simcontainer2.sif
