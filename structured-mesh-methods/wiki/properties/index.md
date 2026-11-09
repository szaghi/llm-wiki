# Properties

Constraints and invariants a method can hold.

* [Free-stream preservation](/properties/free-stream-preservation.md) — A scheme on a curvilinear grid preserves a uniform flow exactly only if its discrete metric terms satisfy the metric identities with the same discrete derivative operators; conservative evaluation of the metric terms achieves this, while analytic or averaged metrics leave spurious source terms.
* [Geometric conservation law](/properties/geometric-conservation-law.md) — On moving grids the volume element must change exactly as the swept volume of its moving faces: the differential law ∂J/∂t + Σ∂(Jξ^i_t)/∂ξ^i = 0 solved with the same discrete operators as the flow equations makes the Jacobian consistent with the scheme's effective volume and keeps a uniform flow uniform.
