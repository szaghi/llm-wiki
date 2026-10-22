# Software

Codes and libraries embodying methods.

* [FLUXO](/software/fluxo.md) — FLUXO is an open-source Fortran code for split-form and entropy-stable DGSEM on 3D curved unstructured hexahedral meshes, with compile-time selection of flux and degree; the sources benchmark it against Trixi.jl and use it for subcell-limiting tests on Euler, ideal and resistive GLM-MHD with non-conservative terms, up to a 20.7 M-DOF Io–plasma-torus run.
* [MFC](/software/mfc.md) — MFC (Multi-component Flow Code) is an open-source Fortran 90, MPI and Python solver for compressible multi-component, multiphase and bubbly flows: five- and six-equation diffuse-interface models, finite-volume WENO with HLLC and SSP Runge–Kutta, validated on shock–bubble and shock–water-column experiments and scaled to thousands of cores.
* [Trixi.jl](/software/trixi-jl.md) — Trixi.jl is an open-source Julia framework for DGSEM on Cartesian, structured and unstructured curved meshes; the sources use it for entropy-stable and kinetic-energy-preserving flux-differencing schemes, measure its serial performance against FLUXO, and run the KPP subcell-limiting test with it.
