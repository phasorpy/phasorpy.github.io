"""
Multi-harmonic phasor coordinates
=================================

An introduction to handling multi-harmonic phasor coordinates.

This tutorial is an adaptation of
:ref:`sphx_glr_tutorials_phasorpy_introduction.py`, focusing on the
calculation, calibration, filtering, thresholding, storage, and visualization
of multi-harmonic phasor coordinates.

"""

# %%
# Import required modules and functions:

import numpy
import tifffile  # TODO: from phasorpy.io import read_ometiff

from phasorpy.datasets import fetch
from phasorpy.io import phasor_from_ometiff, phasor_to_ometiff
from phasorpy.phasor import (
    phasor_calibrate,
    phasor_filter,
    phasor_from_signal,
    phasor_threshold,
)
from phasorpy.plot import PhasorPlot

# %%
# Read signal from file
# ---------------------
#
# Read a time-correlated single photon counting (TCSPC) histogram,
# acquired at 80.11 MHz, from a file:


signal = tifffile.imread(fetch('Embryo.tif'))
frequency = 80.11  # MHz; from the XML metadata in the file

# %%
# Calculate phasor coordinates
# ----------------------------
#
# Phasor coordinates at multiple harmonics can be calculated at once
# from the signal. The histogram samples are in the first dimension of the
# signal (`axis=0`).
# The first and second harmonics are calculated in this example:

mean, real, imag = phasor_from_signal(signal, harmonic=[1, 2], axis=0)

# %%
# The two harmonics are in the first dimension of the phasor coordinates,
# `real` and `imag`:

print(mean.shape, real.shape, imag.shape)

# %%
# To calculate all harmonics, use ``harmonic='all'``:

_ = phasor_from_signal(signal, harmonic='all', axis=0)

# %%
# Calibrate phasor coordinates
# ----------------------------
#
# A homogeneous solution of Fluorescein with a fluorescence lifetime of 4.2 ns
# was imaged as a reference for calibration:

reference_signal = tifffile.imread(fetch('Fluorescein_Embryo.tif'))

# %%
# Calculate phasor coordinates from the measured reference signal at
# the first and second harmonics:

reference_mean, reference_real, reference_imag = phasor_from_signal(
    reference_signal, harmonic=[1, 2], axis=0
)

# %%
# Calibration can be performed at all harmonics simultaneously. Calibrate the
# raw phasor coordinates with the reference coordinates of known lifetime
# (4.2 ns), at the first and second harmonics:

real, imag = phasor_calibrate(
    real,
    imag,
    reference_real,
    reference_imag,
    frequency=frequency,
    harmonic=[1, 2],
    lifetime=4.2,
    skip_axis=0,
)

# %%
# If necessary, the calibration can be undone/reversed using the
# same reference:

uncalibrated_real, uncalibrated_imag = phasor_calibrate(
    real,
    imag,
    reference_real,
    reference_imag,
    frequency=frequency,
    harmonic=[1, 2],
    lifetime=4.2,
    reverse=True,
    skip_axis=0,
)

numpy.testing.assert_allclose(
    (uncalibrated_real, uncalibrated_imag),
    phasor_from_signal(signal, harmonic=[1, 2], axis=0)[1:],
    atol=1e-3,
)

# %%
# Filter phasor coordinates
# -------------------------
#
# Applying median filter to the calibrated phasor coordinates,
# often multiple times, improves contrast and reduces noise.
# This is done at multiple harmonics simultaneously by excluding the
# harmonic axis from the filter:

real, imag = phasor_filter(
    real, imag, method='median', size=3, repeat=2, skip_axis=0
)

# %%
# Pixels with low intensities are commonly excluded from analysis and
# visualization of phasor coordinates. For now, harmonics must be treated
# separately when thresholding:

real1, real2 = real
imag1, imag2 = imag
mean, real1, imag1 = phasor_threshold(mean, real1, imag1, mean_min=1)
mean, real2, imag2 = phasor_threshold(mean, real2, imag2, mean_min=1)

# %%
# Store phasor coordinates
# ------------------------
#
# Write the calibrated and filtered phasor coordinates at multiple harmonics,
# and the fundamental frequency to an OME-TIFF file:

phasor_to_ometiff(
    'phasors.ome.tif',
    mean,
    real,
    imag,
    frequency=frequency,
    harmonic=[1, 2],
    description=(
        'Phasor coordinates at first and second harmonics of a zebrafish '
        'embryo at day 3, calibrated, median-filtered, and thresholded.'
    ),
)

# %%
# Read the phasor coordinates and metadata back from the OME-TIFF file:

mean_, real_, imag_, attrs = phasor_from_ometiff(
    'phasors.ome.tif', harmonic='all'
)

numpy.allclose(real_, real)
assert real_.dtype == numpy.float32
assert attrs['frequency'] == frequency
assert attrs['harmonic'] == [1, 2]
assert attrs['description'].startswith(
    'Phasor coordinates at first and second'
)

# %%
# Plot phasor coordinates
# -----------------------
#
# Visualize the 2D histogram of the calibrated and filtered phasor coordinates
# at the second harmonic:

phasorplot = PhasorPlot(
    frequency=frequency,
    title='Calibrated, filtered phasor coordinates at second harmonic',
)
phasorplot.hist2d(real2, imag2)
phasorplot.show()

# %%
# For comparison, the uncalibrated, unfiltered phasor coordinates at the
# second harmonic:

phasorplot = PhasorPlot(
    allquadrants=True, title='Raw phasor coordinates at second harmonic'
)
phasorplot.hist2d(uncalibrated_real[1], uncalibrated_imag[1])
phasorplot.show()

# %%
# Component analysis
# ------------------

# TODO

# %%
# sphinx_gallery_thumbnail_number = -1
# mypy: allow-untyped-defs, allow-untyped-calls
# mypy: disable-error-code="arg-type"
