[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/wOo27OxG)

This repository is public so that Binder can find it. All code and data is based on the original [LIGO Center for Open Science Tutorial Repository](https://github.com/losc-tutorial/LOSC_Event_tutorial). This repository is a class exercise that restructures the original LIGO code for improved reproducibility, as a homework assignment for the [Fall 2025 installment of UC Berkeley's Stat 159/259 course, _Reproducible and Collaborative Data Science](https://ucb-stat-159-f25.github.io/site/). Authorship of the original analysis code rests with the LIGO collaboration._

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/UCB-stat-159-f25/hw3-yauchristy/HEAD?urlpath=%2Fdoc%2Ftree%2FLOSC_Event_tutorial.ipynb)

This repository contains the data files and Jupyter notebook used to detect gravitational waves in the LIGO project. The project relied on gravitation-waves software packages (https://www.gwosc.org/software/) to analyze strain data from three binary black hole events.

The data files uploaded from the original repository include the IPython notebook, parameter file (json format), readligo.py utility file, and two data file for the GW150914 event (hdf5 format). The ligotools package contains functions used in the notebook in the readligo.py and utils.py files. The tests folder contains four small tests for the output of these functions.  The ai_documentation.txt file contains a record of the prompts and outputs from ChatGPT used for this homework assignment. 

