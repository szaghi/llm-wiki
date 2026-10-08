# Software

Codes embodying methods.

* [HOW-MHD (high-order WENO MHD code with high-order constrained transport)](/software/how-mhd.md) — Public Cartesian ideal-MHD code (adiabatic and isothermal) built on Jiang–Wu fifth-order finite-difference WENO, five-stage fourth-order SSP Runge–Kutta at CFL 1.5, and a fourth- or sixth-order staggered constrained transport that lifts the code's convergence on multi-D MHD waves from second to fifth order.
* [PLUTO (astrophysical gas-dynamics and MHD code)](/software/pluto.md) — Multi-physics finite-volume and finite-difference code for classical and relativistic MHD in which two high-order capturing schemes of this corpus are implemented: cell-centred finite-difference GLM-MHD with WENO-Z and MP5 (third and fifth order), and fourth-order finite volume with pointwise reconstruction and upwind constrained transport.
* [STREAmS (compressible wall-turbulence DNS on GPUs)](/software/streams.md) — Open-source Fortran/CUDA Fortran finite-difference DNS code for supersonic and hypersonic channel, boundary-layer and shock/boundary-layer flows: a kinetic-energy-preserving central flux of order 2–8, switched by a Ducros-type sensor to characteristic WENO of order 1–7, low-storage RK3, and GPU porting at 97% weak-scaling efficiency on 1024 GPUs.
