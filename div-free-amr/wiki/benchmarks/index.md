# Benchmarks

Standard test problems.

* [Field-loop advection](/benchmarks/field-loop-advection.md) — Passive advection of a weak magnetic loop; the standard detector of divergence-constraint violations and stencil inconsistency in MHD schemes.
* [Orszag–Tang vortex](/benchmarks/orszag-tang-vortex.md) — Compressible 2D MHD vortex on a periodic box that steepens into interacting shocks; the standard robustness test of divergence control, where uncontrolled high-order schemes lose pressure positivity.
* [Rotated shock tube](/benchmarks/rotated-shock-tube.md) — 1D MHD Riemann problems rotated obliquely to the grid; the exactly constant normal field makes its deviation a direct measure of divergence errors and of non-conservative jump defects.
* [Sod shock tube](/benchmarks/sod-shock-tube.md) — 1D Euler Riemann problem with a left rarefaction, a contact and a right shock, from Sod's 1978 scheme survey; the hydrodynamic base of the Brio-Wu MHD tube, with no divergence content of its own and no output time in the original.
