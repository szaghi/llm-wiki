# Methods

Algorithms and schemes.

* [AMR projection method](/methods/amr-projection-method.md) — Subcycled projection-method incompressible flow on patch hierarchies: MAC-projected advection velocities, approximate nodal projections, and elliptic synchronization at interfaces.
* [Constrained transport (CT)](/methods/constrained-transport.md) — Evolves face magnetic fluxes from once-computed edge EMFs so the discrete divergence of the field is conserved identically.
* [GLM divergence cleaning](/methods/glm-divergence-cleaning.md) — Couples the divergence constraint to the induction equation via a generalized Lagrange multiplier; divergence errors propagate at finite speed and are damped.
* [MAC method (marker-and-cell)](/methods/mac-method.md) — Staggered primitive-variable scheme for incompressible flow: a pressure Poisson equation enforces the face-difference velocity divergence to zero each cycle.
* [Finite integration technique (FIT)](/methods/finite-integration-technique.md) — Discretizes Maxwell's integral equations exactly as topological matrix equations on a primal-dual grid pair, confining all error and material content to discrete Hodge matrices.
* [Flux-CT and the Godunov CT variants](/methods/flux-ct.md) — Constrained transport driven by a shock-capturing base scheme: corner EMFs assembled from upwind fluxes (flux-CT) or interpolated fields (field-CT).
* [Refluxing (coarse-fine flux correction)](/methods/refluxing.md) — Restores discrete conservation at AMR interfaces by replacing the coarse flux with the accumulated sum of fine fluxes on shared edges.
* [SBP-SAT technique](/methods/sbp-sat.md) — Imposes boundary and interface conditions weakly through penalty terms that preserve the SBP energy estimate, coupling multi-block high-order FD schemes stably and conservatively.
* [Mimetic spectral elements](/methods/mimetic-spectral-elements.md) — Arbitrary-order tensor-product elements whose reduction-reconstruction projection commutes with the exterior derivative, discretizing grad/curl/div exactly on curvilinear meshes.
* [Projection method (divergence cleaning by Poisson solve)](/methods/projection-method.md) — Removes the divergence of the updated field by solving a Poisson problem and subtracting a gradient; constraint held to solver tolerance.
* [Vector-potential evolution](/methods/vector-potential-evolution.md) — Evolves the magnetic vector potential instead of the field; B = curl A is exactly divergence-free on any grid, and AMR transfer acts on the unconstrained potential.
* [Yee scheme (FDTD)](/methods/yee-scheme.md) — Leapfrog update of Maxwell's curl equations on the Yee lattice: electric field on edges, magnetic field on faces, staggered in space and time.
* [Divergence-free reconstruction](/methods/divergence-free-reconstruction.md) — Reconstructs point values of the magnetic field from face data so that the interpolated field itself satisfies the divergence constraint to high order.
* [Electric-field correction](/methods/electric-field-correction.md) — Restores divergence-free consistency at AMR interfaces by replacing coarse edge EMFs with time-averaged sums of the subcycled fine edge EMFs.
* [Eight-wave formulation](/methods/eight-wave.md) — Powell's non-conservative source-term formulation: advects divergence errors with the flow, holding the constraint to truncation error only.
* [Upwind constrained transport (UCT)](/methods/upwind-constrained-transport.md) — CT design in which staggered face fields are primary data everywhere (reconstruction, Riemann solvers, fluxes) and the edge EMF is a four-state upwind flux, making the divergence condition built-in.
