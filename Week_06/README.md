# Week 6: Dynamical Diffraction and Bloch Waves
February 9-13, 2026

## Overview

This week introduces **dynamical electron diffraction theory** using the **Bloch-wave method**. Unlike kinematic theory (Week 5), dynamical theory accounts for multiple scattering events and provides accurate predictions for thick crystals and zone-axis diffraction patterns.

### Key Concepts:
- **Bloch waves**: Eigenstates of electron propagation in periodic crystals
- **Pendellösung**: Periodic exchange of intensity between beams
- **Structure matrix**: Encodes crystal potential and beam coupling
- **Absorption**: Energy loss from inelastic scattering
- **CBED**: Convergent beam patterns revealing crystal structure

---

## Lecture Topics

### Monday: Dynamical Diffraction Theory
- Two-dimensional channeling and Bloch-wave concepts
- Ewald sphere construction and reciprocal lattice mapping
- Diffraction contrast mechanisms
- Introduction to eigenvalue formulation

### Wednesday: Computational Implementation
- Bloch-wave eigenvalue method (4-step workflow)
- Multi-beam calculations (25 beams)
- Real crystal structures: Si and GaAs
- Friedel's law and crystal symmetry
- Absorption effects and CBED simulation

---

## Lecture Notebooks

### 📓 Lecture 6.1: Dynamical Diffraction Introduction
**Files:** 
- `lecture_6.1a_dynamical_diffraction.ipynb`
- `lecture_6.1b_practical_dynamical_applications.ipynb`

**Topics:**
- Ewald sphere construction
- Reciprocal lattice and zone axes
- Introduction to Bloch waves
- Comparison with kinematic theory
- Practical applications and examples

---

### 📓 Lecture 6.2: Bloch-Wave Computational Workflow
**File:** `lecture_6.2_bloch_wave_computation.ipynb`

**Topics:**
- **Step 1**: Crystal structure and Fourier coefficients
- **Step 2**: Structure matrix construction
- **Step 3**: Eigenvalue decomposition (Bloch waves)
- **Step 4**: Boundary condition matching
- **Multi-beam simulation**: 25 beams (5×5 grid)
- Comprehensive visualizations (12+ figures)

**Learning Outcomes:**
- Understand the complete Bloch-wave solution procedure
- Build structure matrices from structure factors
- Solve eigenvalue problems for Bloch states
- Match boundary conditions for incident beams
- Visualize beam intensity evolution with thickness

**Key Features:**
- Pedagogical step-by-step approach
- Two-beam and multi-beam examples
- Eigenvalue/eigenvector analysis
- Pendellösung oscillations
- Reciprocal space mapping

---

### 📓 Lecture 6.3: Real Crystal Structures
**File:** `lecture_6.3_bloch_wave_real_crystals.ipynb`

**Topics:**
- **Si [110]**: Diamond cubic (centrosymmetric)
- **GaAs [110]**: Zincblende (non-centrosymmetric)
- Atomic scattering factors (real values)
- Zone axis diffraction ([110] orientation)
- **Friedel's law violation** in GaAs

**Physical Insights:**
- Centrosymmetric crystals: F(g) = F(-g)
- Non-centrosymmetric crystals: F(g) ≠ F(-g)
- Asymmetric intensity in CBED from GaAs
- Crystal polarity determination
- Structure factor calculations

**Applications:**
- Polar semiconductors (GaAs, GaN, ZnO)
- Crystal structure determination
- Phase identification
- Direct demonstration of symmetry breaking

---

### 📓 Lecture 6.4: Absorption and CBED Simulation
**File:** `lecture_6.4_bloch_wave_absorption_cbed.ipynb`

**Topics:**
- **Part 1**: Absorption (imaginary potential)
  - Complex structure factors
  - Complex eigenvalues and damping
  - Total intensity decay
  
- **Part 2**: Systematic row analysis ([001] row)
  - 1D diffraction along reciprocal lattice line
  - Structure factor analysis
  - Absorption effects on pendellösung
  
- **Part 3**: CBED disk simulation
  - Convergent beam geometry
  - Angular intensity distribution
  - Rocking curves
  
- **Part 4**: Thickness series
  - CBED evolution with thickness
  - Quantitative comparison

**Key Physics:**
- Absorption from inelastic scattering
- Complex potential: V = V_real + i·V_imag
- Anomalous absorption (Bloch-wave dependent)
- CBED features for structure determination

**Visualizations:**
- Actual (002) CBED disk (64×64 angular sampling)
- Direct beam (000) disk
- Rocking curves across convergence angle
- Thickness-dependent disk evolution
- Absorption damping effects

---

## Assignment 6

**Topic:** Compute diffraction intensities using Bloch-wave model

**Tasks:**
1. Implement Bloch-wave solver for given crystal
2. Calculate intensity vs thickness for multiple beams
3. Compare with kinematic theory predictions
4. Analyze convergence with number of beams
5. Explore effect of crystal orientation

**Skills Developed:**
- Eigenvalue problem solving
- Complex matrix operations
- Numerical propagation
- Scientific visualization
- Physical interpretation

---

## Computational Tools

### Required Libraries:
```python
import numpy as np              # Linear algebra, eigenvalues
import matplotlib.pyplot as plt # Visualization
from matplotlib.gridspec import GridSpec  # Multi-panel layouts
```

### Key Functions Implemented:
- `calculate_structure_factor()`: Compute F_g from atomic positions
- `build_structure_matrix()`: Construct eigenvalue matrix
- `solve_bloch_waves()`: Eigenvalue decomposition
- `match_boundary_conditions()`: Determine wave amplitudes
- `propagate_beams()`: Calculate intensity vs thickness
- `calculate_cbed_disk()`: Simulate convergent beam patterns

---

## Learning Objectives

By the end of Week 6, students will be able to:

1. **Explain** the physical basis of dynamical diffraction
2. **Construct** structure matrices from crystal data
3. **Solve** Bloch-wave eigenvalue problems numerically
4. **Predict** beam intensities for thick crystals
5. **Interpret** pendellösung oscillations
6. **Analyze** effects of absorption on diffraction
7. **Simulate** CBED patterns for material identification
8. **Distinguish** centrosymmetric vs non-centrosymmetric crystals
9. **Apply** Bloch-wave method to real materials (Si, GaAs)
10. **Visualize** reciprocal space and beam coupling

---

## Key Equations

**Bloch-Wave Eigenvalue Equation:**
```
A · C = γ · C
```

**Structure Matrix Elements:**
```
A_gg' = s_g·ξ_g           (diagonal: excitation error)
A_gg' = (π/λE)·U_g-g'     (off-diagonal: coupling)
```

**Beam Amplitude Evolution:**
```
ψ_g(z) = Σ_j C_gj · α_j · exp(iπγ_j·z/ξ_g)
```

**Intensity:**
```
I_g(z) = |ψ_g(z)|²
```

---

## Resources

### Textbooks:
- Williams & Carter, *Transmission Electron Microscopy*, Ch. 17-18
- Spence & Zuo, *Electron Microdiffraction*, Ch. 6-8
- Hirsch et al., *Electron Microscopy of Thin Crystals*

### Papers:
- Bethe (1928): Original dynamical theory
- Cowley & Moodie (1957): Multislice method
- Zuo (1993): CBED for structure determination
- Allen & Rossouw (1990): Absorption in CBED

### Software:
- JEMS (CBED simulation)
- CrystalMaker (structure visualization)
- QSTEM (multislice calculations)

---

## Directory Structure
```
Week_06/
├── README.md                                         # This file
├── lectures/                                         # Lecture notebooks
│   ├── lecture_6.1a_dynamical_diffraction.ipynb     # Introduction
│   ├── lecture_6.1b_practical_dynamical_applications.ipynb
│   ├── lecture_6.2_bloch_wave_computation.ipynb     # 4-step workflow
│   ├── lecture_6.3_bloch_wave_real_crystals.ipynb   # Si & GaAs
│   └── lecture_6.4_bloch_wave_absorption_cbed.ipynb # Absorption & CBED
├── code_examples/                                    # Code examples and practice
│   ├── example_01_ewald_sphere_basics.ipynb         # Ewald sphere construction
│   ├── example_02_bloch_wave_analysis.ipynb         # Bloch-wave calculations
│   ├── example_03_thickness_fringes.ipynb           # Pendellösung analysis
│   └── example_04_dynamical_vs_kinematic.ipynb      # Theory comparison
├── exercises/                                        # (Empty - see code_examples)
├── assignments/                                      # Assignment materials
└── resources/                                        # References
```

---

## Important Notes

⚠️ **Computational Complexity:**
- N-beam calculation scales as O(N²) for matrix construction, O(N³) for eigenvalue solution
- 25-beam calculation is reasonable; 100+ beams can be slow
- CBED simulation with full angular sampling is computationally intensive

💡 **Physical Intuition:**
- Bloch waves are like "modes" of electron propagation
- Pendellösung is analogous to beat frequency in coupled oscillators
- Absorption breaks reciprocity and intensity conservation
- CBED disks are "rocking curves" in 2D

🔬 **Experimental Connection:**
- These simulations match real TEM/STEM diffraction experiments
- Thickness measurements from pendellösung are practical
- CBED is used for space group determination
- Friedel's law breaking enables polarity mapping

---

**Next Week:** Multislice method and STEM imaging simulation
