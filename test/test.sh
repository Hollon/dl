#!/bin/bash -l
#SBATCH --job-name="Hollon"
#SBATCH --partition="RGZN2"
#SBATCH --qos=normal
#SBATCH --ntasks-per-node=1
#SBATCH --ntasks-per-core=1
#SBATCH --output=job.%j.out
#SBATCH --error=joberror.%j.out
#SBATCH --gpus=1

source activate yolo

module add cuda/11.2
python main.py >> test1.txt
