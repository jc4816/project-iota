import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import linear_modeling

# Loading full model condition from 0 back and 2 back
beta_0 = np.loadtxt('../../../data/beta/task001_run001_betas_hat_full.txt')
beta_2 = np.loadtxt('../../../data/beta/task003_run001_betas_hat_full.txt')

# Loading design matrix for full model condition
design = np.loadtxt('../../../data/design_matrix/full_design_mat.txt')

# Calucate the difference of beta between two models
beta_0 = beta_0[:, 0:beta_2.shape[1]]
beta_df = np.subtract(beta_2, beta_0)

# Calucate the t-test on the beta1 and beta4
t, prob = stats.ttest_1samp(beta_df, 0.0)
print("There are", sum(prob<=0.05), "rejected the null hypothesis which means these voxels have high confidence to store the 2 second long memory.")

