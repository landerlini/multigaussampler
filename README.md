# Multi-Gaussian Sampling 

The parametrization of conditional probability density function plays a crucial 
role in the simulations used to produce quickly large samples of data emulating 
real-life datasets. 

A very simple technique is based on the explicit modelling of the probability 
density function of the target dataset as a function of the conditions through 
the sum of kernel functions. 

The package`multigaussampler` offers a simple Python3 implementation of this 
simple algorithm. The model of the `pdf` is obtained through a maximum 
likelihood fit of a probability density function obtained as sum of 
Gaussians, optimized using the TensorFlow implementation of the Adam optimizer. 

The sampling of the `pdf` is also implemented in TensorFlow to provide 
efficient sampling on both CPU and GPU infrastructures. 

### Example code 
The code snippet below trains a sampler on a random dataset and generates
a random sample of y variables on top of the same X variables used for training.
```
import numpy as np

## Generate a random dataset as an example
nSamples = 1000 
X = np.random.uniform ( -20, 10,  (nSamples,4)).astype (np.float32) 
y = np.random.uniform ( 0, 1,     (nSamples,2)).astype (np.float32) 

#from multigaussampler import MGSampler
## Creates and configure the MGSampler object
gp = MGSampler(X,y) 

## Train the MGSampler on the training dataset
from tqdm import trange
progress_bar = trange ( 100 )
for iEpoch in progress_bar:
  l = gp.train ( X,y ) 
  progress_bar.set_description ( "Loss: %.1f " % l ) 

## Sample the obtained parametrization
gp.sample (X) 
```

### Author
Lucio Anderlini (Istituto Nazionale di Fisica Nucleare) 
