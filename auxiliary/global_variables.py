from model import *

global network
global opt
global mesh_ref
global mesh_ref_LR
# load template at high and low resolution
mesh_ref = trimesh.load("/home/thibault/Downloads/MPI-FAUST/training/ref/reg_color_ref_HR.ply", process=False)
mesh_ref_LR = trimesh.load("/home/thibault/Downloads/MPI-FAUST/training/ref/reg_color_ref.ply", process=False)
