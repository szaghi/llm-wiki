# Methods

Algorithms and schemes.

* [Constrained transport (CT)](/methods/constrained-transport.md) — Evolves face magnetic fluxes from once-computed edge EMFs so the discrete divergence of the field is conserved identically.
* [MAC method (marker-and-cell)](/methods/mac-method.md) — Staggered primitive-variable scheme for incompressible flow: a pressure Poisson equation enforces the face-difference velocity divergence to zero each cycle.
* [Flux-CT and the Godunov CT variants](/methods/flux-ct.md) — Constrained transport driven by a shock-capturing base scheme: corner EMFs assembled from upwind fluxes (flux-CT) or interpolated fields (field-CT).
* [Projection method (divergence cleaning by Poisson solve)](/methods/projection-method.md) — Removes the divergence of the updated field by solving a Poisson problem and subtracting a gradient; constraint held to solver tolerance.
* [Yee scheme (FDTD)](/methods/yee-scheme.md) — Leapfrog update of Maxwell's curl equations on the Yee lattice: electric field on edges, magnetic field on faces, staggered in space and time.
* [Eight-wave formulation](/methods/eight-wave.md) — Powell's non-conservative source-term formulation: advects divergence errors with the flow, holding the constraint to truncation error only.
