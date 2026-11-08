# Definitions

Precise domain terms.

* [Immersed boundary method](/definitions/immersed-boundary-method.md) — A family of methods that solve the flow equations on a grid that does not conform to the body or interface, representing the boundary through forcing, modified stencils, ghost values or cut cells; the hub page that separates continuous from discrete forcing and diffuse from sharp interfaces.
* [Sharp and diffuse interface representations](/definitions/sharp-and-diffuse-interface.md) — The classification of immersed boundary methods by whether the boundary is smeared over a band of grid cells (diffuse: regularized delta functions, Gaussian spreading, penalization masks) or kept a codimension-one set that the discrete equations see exactly (sharp: jump-corrected stencils, ghost values, cut cells, reconstruction at forcing points).
* [Small-cell problem](/definitions/small-cell-problem.md) — The stability defect of explicit cut-cell (embedded-boundary) finite-volume schemes: a cell clipped by the boundary can have an arbitrarily small volume fraction, so a conservative update with a time step set by the full cells is unstable; the remedies are cell merging, redistribution, large-time-step and rotated schemes, and smaller local time steps.
