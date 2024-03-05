import numpy as np
import scipy
exp_data = np.load('./I_q_IPA_exp.npy','r')
theoretical_data = np.load('./I_q_IPA_model.npy','r')
mask = np.any(np.isnan(exp_data), axis=1)
mask_data = exp_data[~mask]
dim_exp = np.shape(exp_data)
dim_theo = np.shape(theoretical_data)

import matplotlib as mpl
from matplotlib import pyplot as plt
exp_model = scipy.interpolate.CubicSpline(mask_data[:,0],mask_data[:,1])
theo_model = scipy.interpolate.CubicSpline(theoretical_data[:,0],theoretical_data[:,1])
coord = np.linspace(np.min(mask_data[:,0]),np.max(mask_data[:,0]),num=1000)

def scale_param(a):
    return np.sum((exp_model(coord)-a*theo_model(coord))**2)/np.size(exp_model(coord))

coeff = scipy.optimize.minimize_scalar(scale_param)
scaled_theo_model = coeff.x*theo_model(coord)
    



fig, ax = plt.subplots()




ax.plot(coord,exp_model(coord),label='experimental model')
ax.scatter(mask_data[:,0],mask_data[:,1],c='r',marker='*',label='experimental data')
ax.plot(coord,scaled_theo_model,label='scaled theoretical model')
plt.legend()
plt.savefig('test_case.png',dpi=600)
plt.close()


