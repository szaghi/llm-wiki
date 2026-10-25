# Software

Codes and libraries embodying methods.

* [CharLES](/software/charles.md) — CharLES is Cascade Technologies' compressible, low-dissipation, second-order finite-volume LES code on Voronoi grids; this page records its scheme, meshing, GPU cost and the wall-modelled LES of aircraft, juncture flows, bumps and compressible channels run with it.
* [FLEXI](/software/flexi.md) — FLEXI is an open-source high-order DGSEM framework for compressible scale-resolving simulation, with the HOPR mesh generator and POSTI post-processing; this page records its numerics, turbulence features, parallel performance and the LES studies run with it.
* [LESGO](/software/lesgo.md) — LESGO is an open-source incompressible LES code, pseudo-spectral in the wall-parallel directions and second-order finite-difference on a staggered wall-normal grid, used as the host of wall-model studies: the LaRTE model and an a posteriori comparison of machine-learning wall models.
* [RAMSES](/software/ramses.md) — RAMSES is an octree adaptive-mesh-refinement code with a second-order Godunov MHD solver and constrained transport; in the sources it hosts cosmological galaxy-formation runs whose dissipation is purely numerical, a one-equation subgrid turbulence model, a subgrid dynamo, and a comparison of refinement strategies for the turbulent dynamo.
* [elsA](/software/elsa.md) — ONERA's compressible cell-centred finite-volume solver for structured multi-block grids, as used in the sources: host of the zonal detached-eddy simulation of a turbofan fan stage, and the structured Spalart–Allmaras RANS reference against which mesh-adaptive RANS of NASA Rotor 37 is compared.
