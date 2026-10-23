---
type: Method
title: "Entropy projection"
description: "Entropy projection evaluates the nonlinear terms of a DG or FR scheme at conservative states mapped back from the L2 projection or interpolation of the entropy variables; it lets Tadmor's condition close the entropy balance on uncollocated or Gauss nodes, takes 4–14 % of the run time in Ranocha et al.'s tests, and cannot be built for kinetic-energy variables."
status: established
aliases: [entropy-projected variables, entropy-projected conservative variables, projected entropy variables, entropy-variable projection, STD entropy-projection scheme]
tags: [entropy-stable, dg, flux-reconstruction, kinetic-energy-preserving]
timestamp: 2026-10-23T15:20:00Z
---

# Entropy projection

An entropy projection replaces the conservative states at which a
high-order element scheme evaluates its nonlinear fluxes by states
recovered from the entropy variables $w=\eta'(u)$. With $u_h$ the
element solution of degree $N$ and $\Pi_N$ the $L^2$ projection onto
$\mathbb P^N$ (page-local symbol), the entropy-projected state is

$$\tilde u=u\big(\Pi_Nw(u_h)\big),$$

evaluated at volume and surface nodes, with $u(w)$ the inverse of the
entropy-variable map. Where the quadrature nodes are not collocated with
the solution, or do not include the element boundary (Gauss nodes), the
projected entropy variables are a polynomial whose traces and volume values
are consistent with one another, and this is what lets Tadmor's condition
$[\![w]\!]\cdot f^{\mathrm{ec}}=[\![\psi]\!]$ telescope into a discrete
entropy balance
([entropy-conservative fluxes](/methods/entropy-conservative-flux.md),
[entropy stability](/properties/entropy-stability.md)). On collocated
Legendre–Gauss–Lobatto nodes the projection at the volume nodes is the
identity and no projection is needed ([DGSEM](/methods/dgsem.md)).

## Constructions

The sources use three forms of the same idea.

- **Nodal, uncollocated (Chan's form).** As recalled by
  [Cicchino & Nadarajah (2025)](/sources/cicchino-2025.md): interpolate
  $u_h$ to the volume quadrature nodes, evaluate $w$ there, project onto the
  degree-$N$ basis, interpolate the projected entropy variables to the volume
  and surface nodes, and map back to conservative variables, $\tilde
  u(\xi)=u\big(\chi(\xi)\hat w\big)$ with $\hat w$ the projected modal
  coefficients and $\chi$ the basis (page-local) (Eq. (42)). The two-point
  volume and surface fluxes of their nonlinearly stable flux reconstruction
  take these states as arguments
  ([flux reconstruction](/methods/flux-reconstruction.md),
  [flux differencing](/methods/flux-differencing.md)).
- **Gauss collocation, face states only.**
  [Ranocha et al. (2023)](/sources/ranocha-2023.md) write
  $\tilde u=u(\mathcal Rw(\mathbf u))$, $\mathcal R$ the interpolation to the
  surface nodes, for the face states of entropy-stable Legendre–Gauss
  collocation with hybridized SBP operators (§6, Eqs. (6.1)–(6.3)).
  [Schwarz et al. (2025)](/sources/schwarz-2025.md) use the same
  construction in [FLEXI](/software/flexi.md): the entropy variables at the
  Gauss nodes are interpolated to the face with the Lagrange basis,
  $\ell_k(\pm1)$, and the face state is $u$ of that interpolant (§3.4,
  Eq. (25)), inside the hybridized operator of Chan (Eqs. (23)–(24);
  [summation-by-parts operator](/operators/summation-by-parts-operator.md)).
- **Modal, all operators.**
  [Alberti et al. (2025)](/sources/alberti-2025.md) solve for the modal
  coefficients of the conservative variables $u_h$ in an orthonormal,
  hierarchical physical-space basis, and evaluate every spatial operator,
  convective and viscous, from the projection $w_h$ defined by
  $\int_K\phi\,w_h\,dx=\int_K\phi\,w(u_h)\,dx$ for every basis function
  $\phi$ of the element (Eq. (7); orthonormality makes the mass matrix the
  identity, Eq. (15)). The scheme without further correction is their
  baseline "STD" (§2;
  [discontinuous Galerkin](/methods/discontinuous-galerkin.md)).

The inverse map needs positive density and pressure. For the Euler
entropy $\eta=-\rho s/(\gamma-1)$, Schwarz et al. write it with
$\tilde w=(\gamma-1)w$ (page-local, components $\tilde w_1$,
$\tilde w_{2:4}$, $\tilde w_5$) as (Eqs. (5)–(7))

$$\begin{aligned}
u(\tilde w)&=\Big(-\rho e\,\tilde w_5,\ \rho e\,\tilde w_{2:4},\ \rho e\Big(1-\frac{\lvert\tilde w_{2:4}\rvert^2}{2\tilde w_5}\Big)\Big),\\
\rho e&=\Big(\frac{\gamma-1}{(-\tilde w_5)^{\gamma}}\Big)^{1/(\gamma-1)}\exp\Big(\frac{-s}{\gamma-1}\Big),\qquad s=\gamma-\tilde w_1+\frac{\lvert\tilde w_{2:4}\rvert^2}{2\tilde w_5},
\end{aligned}$$

with $\rho e=p/(\gamma-1)$ the internal energy per unit volume; the map
returns $\rho$, $\rho v$ and $E$ *(compiler check, not in the sources)*.
Schwarz et al. call $\rho e$ the "specific internal energy" (§2.2).

## Why it is needed

Cicchino & Nadarajah (2025) state that the Tadmor shuffle substitution in
their entropy proof, after Chan, "is only possible" because the two-point
flux is built from conservative variables mapped from the projected entropy
variables (Thm. 6.3, Eqs. (57)–(58)). The entropy-conservative surface flux
must also act on entropy-projected left and right states, and entropy
dissipation is added through the jump of the projected entropy variables,
not of the conservative ones (§6.3).

The projection does not by itself remove the quadrature error of a modal
scheme. Alberti et al. show that the identity
$\sum_K\int_K\sum_d(\partial_{x_d}w_h)^\top f^{(d)}(w_h)\,dx=\sum_{\text{faces}}\int\sum_d[\![\psi_d(w_h)]\!]n_d$
($\psi_d$ the entropy flux potential of direction $d$, $n$ the face normal)
fails under quadrature because the integrand is not a polynomial, while
Gauss rules are exact only to degree $2N$; very high-order rules are, as
they recall from their earlier work, "unpractical and not very robust"
(§2.1.1, Eq. (18)). The elementwise residual, the integration error of the
entropy-flux potential, is $O(h^{2N+d})$ because entropy variables are
used, and they remove it with an
[entropy correction term](/methods/entropy-correction-term.md). For the
Euler entropy the error comes only from the pressure, since
$\psi_d=\rho v_d=p\,w_{d+1}$ is the product of the rational pressure and an
entropy variable (Eqs. (31)–(32)).

## Kinetic energy cannot be projected

Cicchino & Nadarajah's Theorem 6.4 states that an uncollocated high-order
discretization cannot be exactly discretely kinetic-energy preserving if
the surface quadrature nodes are not a subset of the volume nodes. The
kinetic-energy variables $\partial\kappa/\partial u=\big(-\tfrac12\lvert
v\rvert^2,\ v,\ 0\big)$ have a zero energy component, so no map back to
conservative variables exists, and the surface flux cannot be evaluated at
"kinetic-energy-projected" states; on nodes where surface ⊂ volume the
interpolation and projection are the identity and the obstruction
disappears (Eq. (59); Remark 6.2 exempts collocated Gauss schemes;
[kinetic-energy preservation](/properties/kinetic-energy-preservation.md)).

## Robustness and cost

- **Robustness.** Alberti et al. report the STD entropy-projection scheme
  "much more robust" than their conservative-variable modal DG, which, as
  recalled from their earlier work, completes the robustness tests only up
  to $N=1$ (§3.1.2). STD still fails for $N>1$ on fine triangular grids in
  the inviscid [Kelvin–Helmholtz](/benchmarks/kelvin-helmholtz-instability.md)
  test at Atwood number 0.75, where every entropy-correction variant
  completes up to $N=3$ (§3.1.2, a check run besides the $N=4$ to $7$
  tests of Fig. 4).
- **Accuracy.** Schwarz et al. find entropy-stable Gauss collocation more
  accurate than LGL collocation at equal $N$ on curved-mesh manufactured
  solutions, the Taylor–Green vortex at $M_0=0.1$ and $1.25$ and a 3D
  diffuser LES (§4; [DGSEM](/methods/dgsem.md)).
- **Cost.** Ranocha et al. (2023) measure the entropy projection at 11 % to
  4 % of the run time in 2D and 14 % to 6 % in 3D as $N$ grows, flux
  differencing being the dominant cost (§6, Fig. 3). Schwarz et al. find the
  Gauss scheme about twice as expensive as the LGL scheme at fixed $N$ in
  all their tests (27 890 against 62 080 CPU hours for the compressible
  diffuser, a ratio of 2.23 *(compiler check, not in the sources)*) and
  attribute the extra cost to the entropy projection and the additional
  surface fluxes (§4.4, §5).

## Qualifications

- The three constructions differ in where the projection acts (all volume
  and surface nodes; face states only; every operator of a modal scheme),
  not in the principle; the sources name it the same way.
- Alberti et al. find STD robust compared with conservative-variable DG in
  their modal setting; the comparison is with their own earlier scheme, and
  they do not test nodal SBP variants.
- Cicchino & Nadarajah's conclusion says discrete kinetic-energy
  preservation is achievable "only for the collocated case on
  Gauss-Legendre-Lobatto quadrature nodes" (§8), which is narrower than
  their Theorem 6.4 with Remark 6.2, which leave collocated Gauss schemes
  open.

# Citations

- [Cicchino & Nadarajah (2025)](/sources/cicchino-2025.md) — §3.3 Eq. (42), §6.3 Thms. 6.3–6.4, Eqs. (57)–(59), Remark 6.2, §8.
- [Schwarz et al. (2025)](/sources/schwarz-2025.md) — §2.2 Eqs. (4)–(7), §3.4 Eqs. (23)–(25), §4, §4.4, §5 (arXiv v1).
- [Alberti et al. (2025)](/sources/alberti-2025.md) — §2 Eqs. (7), (15), §2.1.1 Eqs. (18)–(21), (31)–(32), §3.1.2 Fig. 4.
- [Ranocha et al. (2023)](/sources/ranocha-2023.md) — §6 Eqs. (6.1)–(6.3), Fig. 3.
