========
PhasorPy
========

PhasorPy is an open-source Python library for the analysis of luminescence
lifetime and hyperspectral images using the phasor approach.

The phasor approach represents time-resolved and spectral signals as
phasor coordinates (normalized Fourier coefficients at harmonic frequencies)
for intuitive visualization and analysis.

PhasorPy enables reproducible phasor-based fluorescence lifetime imaging
(FLIM) and hyperspectral imaging (HSI) workflows in scientific Python.
It provides tools to read microscopy data in many file formats and to
calculate, calibrate, filter, visualize, and interconvert phasor coordinates,
lifetimes, and signals. Phasor coordinates can be exported to standard
formats and analyzed through cursor-based region-of-interest selection,
cluster detection, multi-component unmixing, FRET efficiency and concentration
estimation.

.. container:: sphx-glr-thumbnails

  .. gallery-tile:: phasorpy_introduction
    :title: Introduction to PhasorPy
    :description: Demonstrate key features of the PhasorPy library.

  .. gallery-tile:: phasorpy_lifetime_geometry
    :title: Geometric interpretation of lifetimes
    :description: Illustrate the geometric interpretation of lifetimes in the phasor plot.

  .. gallery-tile:: api/phasorpy_io
    :title: File input/output
    :description: Read and write phasor-related data in various file formats.

  .. gallery-tile:: api/phasorpy_fret
    :title: Förster resonance energy transfer
    :description: Calculate and plot phasor coordinates of FRET donor and acceptor channels.

  .. gallery-tile:: misc/phasorpy_apps
    :title: Interactive applications
    :description: Explore phasor concepts using interactive educational applications.

  .. gallery-tile:: applications/phasorpy_component_fit
    :title: Multi-component fit
    :description: Spectral unmixing using multi-component analysis in phasor space.

  .. gallery-tile:: applications/phasorpy_nadh_concentration
    :title: Absolute NADH concentration
    :description: Determine absolute NADH concentration using intensity-calibrated phasor FLIM.

  .. gallery-tile:: https://www.phasorpy.org/docs/stable/tutorials/
    :title: All tutorials...
    :img: https://www.phasorpy.org/docs/stable/_images/sphx_glr_phasorpy_logo_thumb.png
    :description: Browse all PhasorPy tutorials.

Documentation
=============

The `PhasorPy documentation <docs/stable/>`_ thoroughly documents all aspects
of the library, including:

- `Phasor approach <docs/stable/phasor_approach/>`_
- `Tutorials <docs/stable/tutorials/>`_
- `API reference <docs/stable/api/>`_
- `Release notes <docs/stable/release/>`_
- `Contributing guide <docs/stable/contributing/>`_
- `Acknowledgments <docs/stable/acknowledgments/>`_
- `MIT License <docs/stable/license/>`_

Other versions: `latest development <docs/dev>`_, :doc:`all <docs>`

Resources
=========

- `Source code <https://github.com/phasorpy/phasorpy>`_ is maintained on GitHub.com.
- `Releases <https://pypi.org/project/phasorpy/>`_ are published on PyPI.org and `conda-forge <https://anaconda.org/conda-forge/phasorpy>`_.
- `Data files <https://zenodo.org/communities/phasorpy>`_ are shared on Zenodo.org.
- `Ask questions and report issues <https://github.com/phasorpy/phasorpy/issues>`_ on the GitHub issue tracker.

News
====

- May 12, 2026: `PhasorPy 0.10 <https://pypi.org/project/phasorpy/>`_ is released to PyPI.

- Jan 1, 2026: `PhasorPy 0.9 <https://pypi.org/project/phasorpy/>`_ is released to PyPI.

- Oct 10, 2025: `PhasorPy 0.8 <https://pypi.org/project/phasorpy/>`_ is released to PyPI.

- Aug 22, 2025: `PhasorPy 0.7 <https://pypi.org/project/phasorpy/>`_ is released to PyPI.

- Aug 16, 2025: The new `PhasorPy logo <https://www.phasorpy.org/_static/phasorpy_logo.svg>`_ is live.

- June 22, 2025: `PhasorPy 0.6 <https://pypi.org/project/phasorpy/>`_ is released to PyPI.

- June 16, 2025: `200th commit <https://github.com/phasorpy/phasorpy/graphs/contributors>`_ to the PhasorPy source code.

- Apr 11, 2025: `PhasorPy 0.5 <https://pypi.org/project/phasorpy/>`_ is released to PyPI.

- Jan 30, 2025: `PhasorPy 0.4 <https://pypi.org/project/phasorpy/>`_ is released to PyPI.

- Jan 25, 2025: The `liffile library <https://github.com/cgohlke/liffile>`_ for reading Leica LIF files is released.

- Jan 8, 2025: PhasorPy is available on `conda-forge <https://anaconda.org/conda-forge/phasorpy/>`__.

- Dec 16, 2024: `PhasorPy 0.3 <https://pypi.org/project/phasorpy/>`_ is released to PyPI.

- Nov 30, 2024: `PhasorPy 0.2 <https://pypi.org/project/phasorpy/>`_ is released to PyPI.

- Oct 22, 2024: PhasorPy project update and practical are presented at the `18th LFD Workshop <https://www.lfd.uci.edu/workshop/>`_.

- Sept 30, 2024: `PhasorPy 0.1 <https://pypi.org/project/phasorpy/>`_ is released to PyPI.

- Sept 23, 2024: `100th commit <https://github.com/phasorpy/phasorpy/graphs/contributors>`_ to the PhasorPy source code.

- June 12, 2024: PhasorPy is featured at the `CZI Open Science 2024 <https://chanzuckerberg.com/science/programs-resources/open-science/>`_ meeting.

- Feb 16, 2024: First `tutorial <https://www.phasorpy.org/docs/stable/tutorials/>`_ added to the documentation.

- Nov 1, 2023: The `ptufile library <https://github.com/cgohlke/ptufile>`_ for reading PicoQuant PTU files is released.

- Oct 26, 2023: The PhasorPy project is introduced at the `17th LFD Workshop <https://www.lfd.uci.edu/workshop/2023/>`_.

- Oct 5, 2023: The PhasorPy `community on Zenodo <https://zenodo.org/communities/phasorpy>`_ is used to share data files.

- Sept 1, 2023: `Bruno Pannunzio <https://github.com/bruno-pannunzio>`_ joins the PhasorPy project.

- Aug 22, 2023: The library documentation is published at `www.phasorpy.org <https://www.phasorpy.org/docs/stable>`_.

- Aug 21, 2023: First PhasorPy developer meeting, to be held remotely every two weeks.

- July 6, 2023: PhasorPy's `organization and repository on GitHub <https://github.com/phasorpy/phasorpy>`_ are live.

- July 1, 2023: `Christoph Gohlke <https://github.com/cgohlke>`_ joins the PhasorPy project.

- Sept 2022: A `grant from the Chan Zuckerberg Initiative
  <https://chanzuckerberg.com/eoss/proposals/phasorpy-a-python-library-for-phasor-analysis-of-flim-and-spectral-imaging/>`_
  is awarded to Leonel Malacrida and Enrico Gratton for the development of the PhasorPy library and community.

Events
======

The PhasorPy project is presented at the following events:

- Bruno Pannunzio.
  PhasorPy and napari-phasors: open source tools for FLIM-phasor analysis.
  `F-Techniques Worskhop Series: FLIM
  <https://ppbi.pt/wordpress/index.php/f-techniques-worskhop-series-flim-january-13-15-2026/>`_.
  January 13-15, 2026. Portuguese Platform of BioImaging (PPBI), Portugal.

- Bruno Schüty.
  PhasorPy hands-on training.
  `LFD/AIM Workshop on Fluorescence Advanced Imaging Research (FLAIR)
  <https://sites.uci.edu/aimlfdworkshop/>`_.
  January 12-15, 2026. University of California, Irvine, USA.

- Bruno Pannunzio and Leonel Malacrida.
  The PhasorPy library for FLIM and HSI phasor analysis.
  `6th Workshop in Advanced Microscopy and Biophotonics
  <https://pasteur.uy/cursos-y-charlas/6th-workshop-in-advanced-microscopy-and-biophotonics/>`_.
  November 23-28, 2025. Institut Pasteur de Montevideo, Uruguay.

- Leonel Malacrida.
  PhasorPy library for open-source phasor analysis of FLIM and HSI: present, future and some applications in biological fluorescence.
  `12th International Weber Symposium
  <https://www.webersymposium.com/>`_.
  June 15-20, 2025. Genoa, Italy.

- Bruno Pannunzio, Bruno Schuty Teske, Michelle Digman, Christoph Gohlke, and Leonel Malacrida.
  PhasorPy: an open-source Python library for the analysis of fluorescence lifetime and hyperspectral images using the phasor approach.
  `69th Annual Meeting of the Biophysical Society
  <https://biophysics.cld.bz/BPS2025-Full-Program-Abstracts/125/>`_.
  February 15-19, 2025. Los Angeles, USA.

- Leonel Malacrida.
  Introduction to PhasorPy.
  Third LFD around the world meeting.
  December 9, 2024. Online.

- Leonel Malacrida.
  The PhasorPy library for FLIM and HSI phasor analysis.
  `Optica Webinar Series
  <https://www.optica.org/events/webinar/2024/11_november/the_phasorpy_library_for_flim_and_hsi_phasor_analysis/>`_.
  November 25, 2024. Online.
  `Recording <https://www.optica.org/events/webinar/2024/11_november/the_phasorpy_library_for_flim_and_hsi_phasor_analysis/>`__.

- Bruno Schüty.
  Phasor Analysis in fluorescence lifetime imaging and spectral imaging with PhasorPy.
  `GloBIAS Bioimage Analysts Workshop
  <https://www.globias.org/activities/past-activties/annual-workshop-gothenburg-2024>`_.
  November 5-8, 2024. Gothenburg, Sweden.
  `Recording <https://www.youtube.com/watch?v=5qURI2NVkzg/>`__.

- Bruno Pannunzio.
  PhasorPy: an open-source Python library for the analysis of fluorescence lifetime and hyperspectral images using the phasor approach.
  `Virtual I2K 2024: Online tutorials on image analysis
  <https://www.i2kconference.org/workshops>`_.
  October 29, 2024. Online.
  `Recording <https://www.youtube.com/watch?v=VGKGF8Zj3tY>`__.

- Leonel Malacrida.
  Unlocking the phasor approach for FLIM and HSI: Insights from PhasorPy, a comprehensive Python library for phasor plot analysis.
  `Euro-Bioimaging Virtual Pub
  <https://www.eurobioimaging.eu/events/phasor-plots-for-hyperspectral-imaging-and-flim/>`_.
  October 25, 2024. Online.
  `Recording <https://www.youtube.com/watch?v=cI7WydgIG00>`__.

- Bruno Schüty.
  PhasorPy hands-on training.
  `18th LFD Workshop in Advanced Fluorescence Imaging and Dynamics
  <https://www.lfd.uci.edu/workshop/>`_.
  October 21-24, 2024.
  Laboratory for Fluorescence Dynamics, University of California, Irvine, USA.

- Christoph Gohlke.
  Introduction to PhasorPy.
  `18th LFD Workshop in Advanced Fluorescence Imaging and Dynamics
  <https://www.lfd.uci.edu/workshop/>`_.
  October 21-24, 2024.
  Laboratory for Fluorescence Dynamics, University of California, Irvine, USA.

- Bruno Pannunzio, Bruno Schüty, Christoph Gohlke, and Leonel Malacrida.
  PhasorPy: un nuevo software abierto para el análisis de imágenes espectrales y tiempo de vida por gráficos de fasores.
  `Semana Académica del Hospital de Clínicas
  <https://www.semanacademica.hc.edu.uy/index.php/galeria2024/681>`_.
  September 23-27, 2024. Montevideo, Uruguay.

- Leonel Malacrida.
  Phasor analysis for FLIM & STED.
  `Montreal Light Microscopy Course (MLMC). In-Focus: STimulated Emission Depletion (STED) Microscopy
  <https://www.canadabioimaging.org/mlmc-infocus-sted>`_.
  July 22-26, 2024. Montreal, Canada.

- Leonel Malacrida.
  The phasor approach for biophysical studies of condensates and membranes using DAN probes.
  `XXVII Congreso Nazionale SIBPA
  <https://www.sibpa.it/CongressoNazionaleSIBPAGenova/>`_.
  June 16-20, 2024. Genoa, Italy.

- Leonel Malacrida.
  PhasorPy: a Python open-source library for phasor analysis of FLIM and HSI data.
  `CZI Open Science 2024
  <https://chanzuckerberg.com/science/programs-resources/open-science/>`_.
  June 11-14, 2024. Boston, USA.

- Leonel Malacrida.
  The phasor plots for time-resolved and hyperspectral imaging: fundamentals and new developments.
  `Sociedad Argentina de Microscopia
  <https://www.samictucuman2024.com/>`_.
  May 29-31, 2024. Tucuman, Argentina.

- Leonel Malacrida.
  The phasor plot analysis for hyperspectral imaging and time-resolved imaging: PhasorPy developments and its applications.
  `Latin American Hub for Bioimaging Through Open Hardware (LIBRE Hub) Seminars
  <https://librehub.github.io/2024/04/03/leonel-malacrida.html>`_.
  May 15, 2024. Online.
  `Recording <https://www.youtube.com/watch?v=CbmDNjwo_sg>`__.

- Leonel Malacrida.
  PhasorPy: a Python open-source library as SimFCS legacy for phasor analysis of FLIM and HSI data.
  `Frontiers in Biological Fluorescence 2024
  <https://www.lfd.uci.edu/frontiers/>`_.
  May 10, 2024. University of California, Irvine, USA.

- Leonel Malacrida.
  Microscopía no lineal en Uruguay: 2P-FLIM y microscopio DIVER para estudiar procesos in vivo en la profundidad del tejido.
  `Simposio en Microscopía y Bioimágenes: avances y desafíos
  <https://cicada.uy/simposio-en-microscopia-y-bioimagenes-avances-y-desafios/>`_.
  April 4-5, 2024. University of the Republic (UdelaR). Montevideo, Uruguay.

- Leonel Malacrida.
  Microscopy techniques applied to the analysis of biosensors performance.
  `1st Latin-American Workshop: Development and applications of biosensors: from fluorescent proteins to synthetic biology
  <https://pasteur.uy/cursos-y-charlas/1st-latin-american-workshop-development-and-applications-of-biosensors-from-fluorescent-proteins-to-synthetic-biology/>`_.
  Nov 27 - Dec 1, 2023. Institut Pasteur de Montevideo, Uruguay.

- Bruno Schüty, Bruno Pannunzio, and Leonel Malacrida.
  Practical section 3: PhasorPy and Napari plugin for FLIM & HSI analysis.
  `5th Workshop in Advanced Microscopy and Biophotonics
  <https://pasteur.uy/2023/5th-workshop-in-advanced-microscopy-and-biophotonics/>`_.
  November 19-24, 2023. Institut Pasteur de Montevideo, Uruguay.

- Christoph Gohlke and Leonel Malacrida.
  Introduction to PhasorPy.
  `17th LFD Workshop in Advanced Fluorescence Imaging and Dynamics
  <https://www.lfd.uci.edu/workshop/>`_.
  October 23-27, 2023. Laboratory for Fluorescence Dynamics,
  University of California, Irvine, USA.

Publications
============

**Using PhasorPy**

#. Schuty B, Garcia MJ, Khuon S, Malacrida L.
   `Phasor analysis of RGB camera data enables fluorescence microscopy unmixing
   and brightfield segmentation in a commercial microscope
   <https://doi.org/10.1016/j.sbsr.2026.101014>`__.
   *Sensing and Bio-Sensing Research*. 52: 101014 (2026)

#. Prieto D, Rehermann MI, Fabbiani G, Vitar M, Trujillo-Cenoz O, Falco MV,
   Cuparo M, Trigo FF, et al.
   `A filopodia-based dendritic mechanosensory compartment in CSF-contacting
   neurons <https://doi.org/10.64898/2026.04.09.713694>`__.
   *bioRxiv* (2026)

#. Halbers LP, Brennan CK, Scipioni L, Tedeschi G, Torrey ZR, Parag-Sharma K,
   Labra B, Gohlke C, et al.
   `Expanded applications of bioluminescence microscopy with phasor analysis
   <https://doi.org/10.1016/j.crmeth.2026.101344>`__.
   *Cell Reports Methods*. 6(4): 101344 (2026)

#. Fuller EB, Cole KH, Halbers LP, Chan CET, Ng KK, Scipioni L, Gohlke C,
   Digman MA, et al.
   `Bioluminescent probes for multiplexed RNA imaging
   <https://doi.org/10.1021/jacs.5c16597>`__.
   *Journal of the American Chemical Society*. 148(11): 11521-11530 (2026)

#. Pannunzio B, Cespedes P, Diaz M, Ali D, Rial A, Malacrida L.
   `High-throughput single-cell spectroscopy using phasor analysis of spectral
   flow cytometry <https://doi.org/10.64898/2026.02.27.708623>`__.
   *bioRxiv* (2026)

#. Zhao W, Samimi K, Skala MC, Datta R.
   `FLIM playground: an interactive, end-to-end graphical user interface for
   analyzing single cells with fluorescence lifetime imaging microscopy
   <https://doi.org/10.1101/2025.09.30.679625>`__.
   *bioRxiv* (2025)

**Mentioning PhasorPy**

#. Harkhoe R, Ferrari G, Dmitriev RI, Kuhl M.
   `Luminescence lifetime imaging: Key concepts and advances in the image
   acquisition, processing, and analysis pipeline
   <https://doi.org/10.1021/acsmeasuresciau.5c00209>`__.
   *ACS Measurement Science Au*. acsmeasuresciau.5c00209 (2026)

#. Georgakoudi I, Skala MC, Quinn KP, Stringari C, Sorrells JE, Heikal AA,
   Li LZ, Xu HN, et al.
   `Consensus guidelines for cellular label-free optical metabolic imaging:
   ensuring accuracy and reproducibility in metabolic profiling
   <https://doi.org/10.1117/1.JBO.30.S2.S23901>`__.
   *Journal of Biomedical Optics*. 30(S2): S23901 (2025)

#. Wetzker C, Zoccoler ML, Iarovenko S, Okafornta CW, Nobst A, Hartmann H,
   Muller-Reichert T, Haase R, et al.
   `A fluorescence lifetime separation approach for FLIM live-cell imaging
   <https://doi.org/10.1111/jmi.70036>`__.
   *Journal of Microscopy*. 301(1): 91-106 (2025)

#. Michalet X.
   `AlliGator: open source fluorescence lifetime imaging analysis in G
   <https://doi.org/10.1101/2025.05.22.655640>`__.
   *bioRxiv* (2025)

#. Kapsiani S, Laubli NF, Ward EN, Shehata M, Kaminski CF, Kaminski Schierle GS.
   `FLIMPA: a versatile software for fluorescence lifetime imaging microscopy
   phasor analysis <https://doi.org/10.1021/acs.analchem.5c00495>`__.
   *Analytical Chemistry*. 97(22): 11382-11387 (2025)

#. Vallmitjana A, Torrado B, Durkin AF, Dvornikov A, Rajil N, Ranjit S, Balu M.
   `GSLab: open-source platform for advanced phasor analysis in fluorescence
   microscopy <https://doi.org/10.1093/bioinformatics/btaf162>`__.
   *Bioinformatics*. 41(4): btaf162 (2025)

#. Weber F, Iskrak S, Ragaller F, Schlegel J, Plochberger B, Sezgin E,
   Andronico LA.
   `VISION - an open-source software for automated multi-dimensional image
   analysis of cellular biophysics <https://doi.org/10.1242/jcs.262166>`__.
   *Journal of Cell Science*. 137(20): jcs262166 (2024)

Cite
====

Please cite `doi: 10.5281/zenodo.13862586 <https://dx.doi.org/10.5281/zenodo.13862586>`_
if PhasorPy contributes to research that leads to a publication.

Contact
=======

PhasorPy is a community-maintained project.

`Contributions <docs/stable/contributing/>`_
in the form of bug reports, bug fixes, feature implementations, documentation,
datasets, and enhancement proposals are welcome.

Report issues and ask questions about PhasorPy on the GitHub
`issue tracker <https://github.com/phasorpy/phasorpy/issues>`_.

Alternatively, contact the
`PhasorPy developers <https://github.com/orgs/phasorpy/people>`_ directly.
