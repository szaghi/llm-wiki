# Sources

One page per ingested source, with verified metadata, a notation map, and an
audit list of pages touched.

* [Harlow & Welch (1965) — Numerical calculation of time-dependent viscous incompressible flow with free surface](/sources/harlow-welch-1965.md) — Introduces the MAC method: the original staggered grid and pressure-Poisson enforcement of a face-difference discrete divergence of velocity.
* [Yee (1966) — Numerical solution of initial boundary value problems involving Maxwell's equations in isotropic media](/sources/yee-1966.md) — Introduces the Yee lattice and leapfrog FDTD scheme: E on edges, H on faces, curl-form updates chosen so conducting-boundary conditions are imposed naturally.
* [Chorin (1968) — Numerical solution of the Navier-Stokes equations](/sources/chorin-1968.md) — Introduces the projection method: advance an auxiliary velocity, then Hodge-decompose it into a discretely divergence-free field plus a discrete pressure gradient.
* [Evans & Hawley (1988) — Simulation of MHD flows: a constrained transport method](/sources/evans-hawley-1988.md) — Introduces constrained transport (CT): staggered flux-based induction-equation update preserving the divergence constraint to machine roundoff.
* [Tóth (2000) — The ∇·B = 0 constraint in shock-capturing MHD codes](/sources/toth-2000.md) — Systematic comparison of seven divergence-control schemes; proves CT variants are pure finite-volume schemes and that conservation excludes exact Lorentz-force orthogonality.
