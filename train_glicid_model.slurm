#!/bin/bash
#SBATCH --job-name=glicid_model_training
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=96
#SBATCH --gres=gpu:2
#SBATCH --mem=64G
#SBATCH --time=24:00:00

# Load necessary modules
module load anaconda3

# Set up Conda environment
conda env create -f /jmir/git_repo/environment_setup.yaml
source activate glicid_model_env

# Navigate to your Python script directory
cd /jmir/git_repo/glicid_copilot

# Run your Python script for training the model
python glicid_support_transformer.py

# Deactivate the Conda environment
conda deactivate

# Cleanup Conda environment
conda env remove -n glicid_model_env

