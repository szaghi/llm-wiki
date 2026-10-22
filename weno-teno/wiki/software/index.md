# Software

Codes and libraries embodying methods.

* [FLUXO](/software/fluxo.md) — FLUXO is an open-source Fortran code for split-form and entropy-stable DGSEM on 3D curved unstructured hexahedral meshes, with compile-time selection of flux and degree; the sources benchmark it against Trixi.jl and use it for subcell-limiting tests on Euler and GLM-MHD.
* [Trixi.jl](/software/trixi-jl.md) — Trixi.jl is an open-source Julia framework for DGSEM on Cartesian, structured and unstructured curved meshes; the sources use it for entropy-stable and kinetic-energy-preserving flux-differencing schemes, measure its serial performance against FLUXO, and run the KPP subcell-limiting test with it.
