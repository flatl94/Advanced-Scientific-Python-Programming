import os
import numpy as np
import math
import sys
from sklearn.utils.extmath import cartesian
import copy
import random

from plot_tools import General2DPlotter
from geometrical_tools import CircleGenerator, PolygonGenerator, LatticeEnumeration, CenterToPolygon

"""
This exercise aims to sketch a fuel assembly 17 by 17 of a nuclear reactor.
https://www.pinterest.jp/pin/411797959670187978/

"""

# --- # BEGINNING OF THE SCRIPT # --- #

# --- # INPUT PARAMETERS # --- #
pin_diameter = 0.95
pitch_pin = 1.26
fa_dimenion = 21.40

x1_dim = 17
x2_dim = 17

guide_rod_diameter = 1.15

output_dir = '.'
name_figure = 'test_FA'
# --- # EVALUATION OF GEOMETRICAL DIMENSION # --- #
lat_coordinates = np.zeros((x1_dim,x2_dim),dtype=object)
idx=1
idx_grod = [40,43,46,55,65,88,91,94,97,100,139,142,145,148,151,190,193,196,199,202,225,235,244,247,250]
for i1 in range(x1_dim):
    for i2 in range(x2_dim):
        lat_coordinates[i1,i2]={'coord':((-(x1_dim-1)/2+i1)*pitch_pin,(-(x2_dim-1)/2+i2)*pitch_pin),
                                'type':'pin',
                                'power':random.uniform(0, 1),
                                'square_verts':np.array([[(-(x1_dim-1)/2+i1+0.5)*pitch_pin,(-(x2_dim-1)/2+i2+0.5)*pitch_pin],
                                                         [(-(x1_dim-1)/2+i1-0.5)*pitch_pin,(-(x2_dim-1)/2+i2+0.5)*pitch_pin],
                                                         [(-(x1_dim-1)/2+i1-0.5)*pitch_pin,(-(x2_dim-1)/2+i2-0.5)*pitch_pin],
                                                         [(-(x1_dim-1)/2+i1+0.5)*pitch_pin,(-(x2_dim-1)/2+i2-0.5)*pitch_pin],
                                                         ],dtype=object)}
        if idx in idx_grod:
            lat_coordinates[i1,i2]['type']='guide_rod'
            lat_coordinates[i1,i2]['power']=0.0
        idx= idx + 1



CG = CircleGenerator()
list_power = []
PG = PolygonGenerator()
for i1 in range(x1_dim):
    for i2 in range(x2_dim):
        if lat_coordinates[i1,i2]['type'] == 'pin':
            CG.add_circle(lat_coordinates[i1,i2]['coord'],pin_diameter/2)
            list_power.append(lat_coordinates[i1,i2]['power'])
        elif lat_coordinates[i1,i2]['type'] == 'guide_rod':
            PG.add_polygon(lat_coordinates[i1,i2]['square_verts'])
box_verts=np.array([[-fa_dimenion/2,-fa_dimenion/2],[fa_dimenion/2,-fa_dimenion/2],[fa_dimenion/2,fa_dimenion/2],[-fa_dimenion/2,fa_dimenion/2]])           
PG.add_polygon(box_verts)

cg_patches=CG.return_patches()
pg_patches=PG.return_patches()
# --- # PLOTTING THE FA # --- #

G2DP = General2DPlotter()
G2DP.add_label('x (cm)','y (cm)')
G2DP.add_data_patches(cg_patches, list_power,'power (normalized)')
G2DP.add_boundary_patches(cg_patches)
G2DP.add_boundary_patches(pg_patches)
for i1 in range(x1_dim):
    for i2 in range(x2_dim):
        if lat_coordinates[i1,i2]['type'] == 'pin':
            G2DP.add_symbols(lat_coordinates[i1,i2]['coord'],'o','pin')
        elif lat_coordinates[i1,i2]['type'] == 'guide_rod':
            G2DP.add_symbols(lat_coordinates[i1,i2]['coord'],'x','guide rod')
G2DP.add_legend()
G2DP.save_plot(output_dir,name_figure)

