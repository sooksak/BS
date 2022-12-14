##

import arviz as az
import matplotlib.pyplot as plt
import numpy as np
import pymc3 as pm
import theano.tensor as tt

with pm.Model() as model:
    mu = pm.Normal("mu", mu=0, sigma = 1)
    obs = pm.Normal("obs", mu=mu, sigma=1, observed=np.random.randn(100))

model.basic_RV
