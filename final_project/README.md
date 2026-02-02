# Final Project: Dataset Ideas and Links

This folder contains example datasets you can use for the final project. All datasets below are open and widely used for EM/analytical microscopy research.

## Example Datasets (Open and Accessible)

### General EM / Imaging
- **DOPAD (Dataset of nanoPArticle Detection)** — TEM nanoparticle detection dataset used in the course.  
  https://dopad.github.io/  
  (Useful for segmentation, detection, size distribution, and ML pipelines.)

### 4D-STEM / Diffraction
- **py4DSTEM Example Datasets** — curated 4D-STEM datasets used in tutorials and examples.  
  https://py4dstem.readthedocs.io/en/latest/tutorials.html  
  (Includes strain mapping, ptychography-style workflows, and diffraction analysis.)

- **CBED / 4D-STEM Data (EMD format)** — example 4D-STEM datasets in EMD format.  
  https://zenodo.org/record/3854690  
  (Good for beam-shift, phase retrieval, and diffraction-based analysis.)

### EELS
- **EELS Spectral Datasets (HyperSpy Examples)** — reference spectra and example EELS datasets.  
  https://hyperspy.org/hyperspy-doc/current/user_guide/data/index.html  
  (Good for denoising, PCA/NMF, peak fitting, and chemical mapping.)

- **Electron Energy-Loss Spectroscopy Databases** — open spectral references.  
  https://eelsdb.eu/  
  (Useful for building spectral classifiers or reference matching pipelines.)

### EDS / Spectrum Imaging
- **EDS Spectrum Image Examples (HyperSpy)** — EDS datasets in HyperSpy-friendly formats.  
  https://hyperspy.org/hyperspy-doc/current/user_guide/data/index.html  
  (Useful for elemental mapping, decomposition, and clustering.)

### Simulation / Synthetic Data
- **Prismatic (STEM simulations)** — open-source STEM simulation code with example datasets.  
  https://prism-em.com/  
  (Useful for comparing simulation vs experimental imaging.)

- **abTEM (TEM/STEM simulations in Python)** — simulation library with examples.  
  https://abtem.readthedocs.io/en/latest/  
  (Good for synthetic dataset generation and physics-informed ML.)

### Large Open Repositories
- **EMPIAR (Electron Microscopy Public Image Archive)** — large open EM datasets (cryo-EM, tomography, etc.).  
  https://www.ebi.ac.uk/empiar/  
  (Use if you want large-scale, realistic datasets.)

- **Zenodo EM Datasets** — searchable repository for EM datasets.  
  https://zenodo.org/search?q=electron%20microscopy  

## Suggested Project Directions
- ML-based segmentation and quantification of nanoparticles (DOPAD)
- 4D-STEM strain mapping or diffraction-based clustering (py4DSTEM datasets)
- EELS/EDS spectral decomposition using PCA/NMF
- Simulation–experiment matching (Prismatic or abTEM + real data)
- Physics-informed neural networks for electron microscopy data

## Note
If you use datasets outside this list, ensure they are properly cited and include a short data provenance section in your proposal and final README.