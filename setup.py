import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
     name='multigaussampler',  
     version='0.1',
     scripts=[] ,
     author="Lucio Anderlini",
     author_email="Lucio.Anderlini@fi.infn.it",
     description="Sampling from a Maximum-Likelihood fitted Multi-Gaussian distribution in TensorFlow 2.1",
     long_description=long_description,
     long_description_content_type="text/markdown",
     install_requires = ['tensorflow==2.1.0', 'FastQuantileLayer'], 
     url="https://github.com/landerlini/multigaussampler",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )

