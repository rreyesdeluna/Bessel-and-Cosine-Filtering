# Bessel and Cosine Filtering Approaches for Electromechanical Modes Identification

Authors:

Rodrigo David Reyes de Luna, José Antonio de la O Serna, Alejandro Zamora-Mendez, Mario R. Arrieta Paternina (@marioap7) and Antonino López Rios.

The real-time system monitoring of electromechanical oscillations in power grids
is essential to maintain operational control in an optimal state and to make the
right decisions in any adverse situation. In this context, this investigation proposes
two filtering approaches to identify modal patterns (damping and frequency) from
multivariate and multi-modal oscillation signals stemming from multiple PMUs and
locations. The key idea behind this proposal lies in introducing the Cosine- and
Bessel-based filtering to conduct a time-frequency analysis for dealing with the modal
identification of nonlinear signals that arise after disturbance in the grid. Thereby,
this research develops the theoretical foundations of both filtering perspectives form-
ing bi-orthogonal bases that support their analysis and synthesis equations. Then,
mono-component signals are extracted by spectral analysis, and their modal patterns
are extracted via Hilbert transform. Numerical experiments conducted on synthetical
oscillating signals, simulated-based signals extracted from a well-known power grid,
and synchrophasors captured by the Mexican WAMS, demonstrate the applicability
of the proposal.

Requirements:

  * Python V3 
  * Packages: Numpy, Scipy, Plotly, Matplotlib
  
Instructions:

  * Download both folders: single_channel and multi_channel.
  * Run programs in folders separately (single-cannel and multi-channel):
  * The script signal_data.py contain the signal(s) to be analyzed. Here you can add or modify the signal or signals for your study.
  * Calculate L using calc_Lb.py and calc_Lc.py
  * Calculate monocomponents and modal parameters with fourier_bessel_1.py and fourier_cosine_1.py. These programs command the following scripts: signal_data.py, fft.py, ht.py.

The results and charts are obtained directly from the previous programs, however, for better editing in charts, there are the scripts hilbert_plot_b.py, hilbert_plot_c.py, L_plot.py, modes_plot.py, multi_fourier_plot.py
