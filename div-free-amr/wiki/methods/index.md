# Methods

Algorithms and schemes.

* [Constrained transport (CT)](/methods/constrained-transport.md) — Evolves face magnetic fluxes from once-computed edge EMFs so the discrete divergence of the field is conserved identically.
* [Flux-CT and the Godunov CT variants](/methods/flux-ct.md) — Constrained transport driven by a shock-capturing base scheme: corner EMFs assembled from upwind fluxes (flux-CT) or interpolated fields (field-CT).
* [Projection method (divergence cleaning by Poisson solve)](/methods/projection-method.md) — Removes the divergence of the updated field by solving a Poisson problem and subtracting a gradient; constraint held to solver tolerance.
* [Eight-wave formulation](/methods/eight-wave.md) — Powell's non-conservative source-term formulation: advects divergence errors with the flow, holding the constraint to truncation error only.
