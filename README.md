# python_glue
Using Python as a glue to integrate with Stata, Fortran, and etc.

## Motivation

> We should forget about small efficiencies, say about 97% of the time: premature optimization is the root of all evil. 

> – Donald Knuth

As Sargent and Stachuski point out in the [Need for Speed](http://quant-econ.net/py/need_for_speed.html) section of the lecture notes for Python on Quant-econ, high productivity languages should be chosen over high speed languages for the great majority of scientific computing tasks as they can be used together with high-speed low-level languages.

Reference:

http://quant-econ.net/py/need_for_speed.html#speed-appendix-py

http://docs.scipy.org/doc/numpy/user/c-info.python-as-glue.html

## Stata
This section introduces how to run stata do file in python (IPython) in Windows and Mac OS X.

### 1. Write and execute stata commands in IPython

There is a nice module, [ipystata](https://github.com/TiesdeKok/ipystata), written Ties de Kok. You can find documentation about installation and usage in the GitHub page.

### 2. Run do files in IPython
#### Windows System
Prerequisites:
- Stata installed correctly.
- Stata installation directory: e.g. "C:\Program Files (x86)\Stata14\StataSE-64"

Reference: 
http://www.stata.com/support/faqs/windows/batch-mode/

#### Mac OS X
Prerequisites:
- Stata installed correctly.
- Install Stata(console) using the Terminal utility (this may not work with El Capatin as I have got error saying "The terminal utility could not be installed. ln: /usr/bin/stata-se: Operation not permitted" and I have El Capatin version 10.11.5)
- Installing Stata(console) by hand (if the previous step does not work) by adding "export PATH=$PATH:/Applications/Stata/StataSE.app/Contents/MacOS" in a .bash profile file. If there is no such file exists, make one and include the line in the previous quote. Make sure Stata is installed in the folder of Applications.

Reference: 

http://www.stata.com/manuals13/gsmc.pdf

#### How to run do files in IPython
- Use call method from subprocess model.  
- See example in runstata.py under stata folder

Reference: 

http://stackoverflow.com/questions/21263668/run-stata-do-file-from-python

