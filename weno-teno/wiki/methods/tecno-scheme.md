---
type: Method
title: "TeCNO schemes — entropy-stable reconstruction with the sign property"
description: "A TeCNO-type flux adds to an entropy-conservative flux a dissipation acting on jumps of reconstructed scaled entropy variables; it is entropy stable whenever the reconstruction has the sign property, which minmod and ENO have by construction and WENO reconstructions get from a componentwise sign switch or from constrained weights."
status: established
aliases: [TeCNO, TVD-ES, sign property, entropy-stable reconstruction, ENO-based entropy-stable scheme, Fjordholm–Mishra–Tadmor scheme]
tags: [entropy-stable, reconstruction, numerical-flux, weno, dg, relativistic]
timestamp: 2026-10-23T20:29:00Z
---

# TeCNO schemes — entropy-stable reconstruction with the sign property

A TeCNO-type scheme is a conservative scheme whose interface flux is an
[entropy-conservative two-point flux](/methods/entropy-conservative-flux.md)
plus a dissipation term. The dissipation is applied to the jump of
*reconstructed* scaled entropy variables, not to the jump of the cell
values. The reconstruction raises the order of the dissipation. Entropy
stability survives the reconstruction under one condition: every
reconstructed jump has the sign of the cell-value jump. This is the
**sign property**. The sources trace the construction to
Fjordholm, Mishra & Tadmor (2012), as recalled by
[Rueda-Ramírez et al. (2021)](/sources/ruedaramirez-2021.md) (§4), by
[Duan & Tang (2022)](/sources/duan-2022.md) (§1, §4) and by
[Li, Duan & Tang (2022)](/sources/li-2022-c.md) (§3.4, after their ref. [19]).
As recalled by Duan & Tang, Bhoriya & Kumar extended TeCNO schemes to
relativistic hydrodynamics with ENO-based dissipation, and their own
earlier uniform-mesh scheme already combined fifth-order WENO with the
Biswas–Dubey switch (§1, §4). [Bhoriya et al. (2023)](/sources/bhoriya-2023.md) carry the
ENO-based construction to the two-fluid relativistic plasma equations with 3D velocities
(§4.1).

## The flux and the entropy condition

Let $w=\eta'(u)$ be the entropy variables. Let page-local $\tilde R$ be
the right-eigenvector matrix of $A$ scaled so that
$\partial u/\partial w=\tilde R\tilde R^\top$ (Barth's scaling), and let
$\Lambda=\mathrm{diag}(\lambda_l)$. Both are frozen at the interface
$x_{i+1/2}$. The page-local *scaled entropy variables* are
$\tilde w=\tilde R^\top w$. Let page-local $[\![\tilde w]\!]^{\mathrm{rec}}_{i+1/2}=\tilde w^+_{i+1/2}-\tilde w^-_{i+1/2}$
be the jump between the two reconstructed values at the interface, while
$[\![\tilde w]\!]_{i+1/2}=\tilde R^\top(w_{i+1}-w_i)$ is the jump of the
cell values. The flux is

$$h_{i+1/2}=f^{\mathrm{ec}}(u_i,u_{i+1})-\tfrac12\,\tilde R\,\lvert\Lambda\rvert\,[\![\tilde w]\!]^{\mathrm{rec}}_{i+1/2}.$$

The entropy-conservative part is evaluated on the cell (or subcell)
values, not on reconstructed states (Rueda-Ramírez et al. (2021), Eq. (72)).
With Tadmor's condition $[\![w]\!]\cdot f^{\mathrm{ec}}=[\![\psi]\!]$, the
entropy production at the interface is

$$[\![w]\!]\cdot h_{i+1/2}-[\![\psi]\!]=-\tfrac12\,[\![\tilde w]\!]^\top\lvert\Lambda\rvert\,[\![\tilde w]\!]^{\mathrm{rec}}.$$

**Sign property.** If there is a diagonal matrix $\mathcal B\ge0$
(page-local) with $[\![\tilde w]\!]^{\mathrm{rec}}=\mathcal B[\![\tilde w]\!]$,
that is, if each component of the reconstructed jump has the sign of the
cell-value jump, the production is non-positive and the scheme is
[entropy stable](/properties/entropy-stability.md). Rueda-Ramírez et al.
(2021) state the condition with $\mathcal B$ diagonal and positive
(Eqs. (73)–(75)). Their production is
$-\tfrac12[\![w]\!]^\top R\lvert\Lambda\rvert\mathcal Z\mathcal BR^\top[\![w]\!]\le0$,
with page-local diagonal $\mathcal Z>0$ from $\partial u/\partial w=R\mathcal ZR^\top$. This
is the formula above with $\tilde R=R\mathcal Z^{1/2}$ *(compiler check, not in the
sources: diagonal matrices commute)*. They note that $(R^\top)^{-1}$ never
has to be computed.

## Choices of reconstruction

**Minmod on the variables $\tilde w$ (TVD-ES).** Rueda-Ramírez et al. (2021)
reconstruct each component of $\tilde w$ linearly with the minmod slope
(Eqs. (76)–(77), (81)). Minmod returns zero unless the two one-sided slopes
share a sign, so the reconstructed jump at an interface keeps the sign of
the cell jump *(compiler check, not in the sources)*. They state, citing Fjordholm et al., that minmod is the only
symmetric TVD limiter with the sign property (§4;
[total variation diminishing](/definitions/total-variation-diminishing.md)).

**ENO on the variables $\tilde w$.** [Bhoriya et al. (2023)](/sources/bhoriya-2023.md)
(§4.1.2, Eq. (22), Thm. 4.3) reconstruct $\tilde w$ with ENO, which has the sign property
(Fjordholm, Mishra & Tadmor, as they recall it), so no switch is needed: minmod at second
order, ENO-3 and ENO-4 at third and fourth order. The scaled variables are formed per
interface, $\tilde R^\top_{i\pm1/2}w_m$ for the stencil cells $m$, reconstructed, and mapped back
with $(\tilde R^\top)^{-1}$ before the jump is taken. Entropy stability is proved for each fluid
block of their two-fluid system, and holds whatever the discretization of the Maxwell block,
because the Lorentz sources produce no entropy
([relativistic hydrodynamics](/definitions/relativistic-hydrodynamics.md)).

**WENO with a sign switch.** Duan & Tang (2022) reconstruct $\tilde w$
with fifth-order [WENO-JS](/methods/weno-js-reconstruction.md), and Li,
Duan & Tang (2022) with fifth-order
[multi-resolution WENO](/methods/multi-resolution-weno.md) (App. A); both
add the componentwise switch of Biswas & Dubey "to ensure the sign
property", as Li, Duan & Tang recall it (§3.4). On a curvilinear mesh the
variables are rotated first into the frame of the face normal: Duan &
Tang reconstruct $\tilde w=\tilde R^\top(T_{\mathrm{rot}}u)\,T_{\mathrm{rot}}w$, with page-local
$T_{\mathrm{rot}}$ the rotation of the velocity (and magnetic-field)
components into the direction of the metric vector
$(J\partial_{x_j}\xi_k)_j$, set by two angles (§4). In page-local notation,
$\mathcal Y=\mathrm{diag}(\mathcal Y_{ll})$ with $\mathcal Y_{ll}=1$ when the
$l$th components of $[\![\tilde w]\!]^{\mathrm{rec}}$ and $[\![\tilde w]\!]$ have the same
sign and $\mathcal Y_{ll}=0$ otherwise. The dissipation becomes
$-\tfrac12\tilde R\lvert\Lambda\rvert\mathcal Y[\![\tilde w]\!]^{\mathrm{rec}}$
(Li, Duan & Tang, Eq. (3.21); Duan & Tang, Eq. (4.1)). A component that
fails the test gets no dissipation at that interface. Duan & Tang prove
the semi-discrete entropy inequality of the resulting moving-mesh scheme
(Thm. 4.1): the key inequality is
$[\![\tilde w]\!]^\top\mathcal Y[\![\tilde w]\!]^{\mathrm{rec}}\ge0$, and the numerical
entropy flux is the entropy-conservative one minus
$\tfrac12\hat a\,\{\!\{\tilde w\}\!\}^\top\mathcal Y[\![\tilde w]\!]^{\mathrm{rec}}$, with
$\hat a$ (page-local) the scalar dissipation speed (Eqs. (4.2)–(4.4)). The
dissipation vanishes for a constant state, so the scheme keeps the free
streams of its entropy-conservative part (Remark 4.1;
[free-stream preservation](/properties/free-stream-preservation.md)).

**Third-order WENO with the property built in.**
[Charles & Ray (2025)](/sources/charles-2025.md) use four-point
third-order WENO reconstructions whose weights are constrained to have
the sign property, so no switch is needed. These are SP-WENO
(Fjordholm & Ray), SP-WENOc (Ray) and their learned DSP-WENO, detailed on
[sign-preserving WENO](/methods/sign-preserving-weno.md) (§3–4; arXiv v2).
Their scheme "TeCNO4" is the fourth-order LeFloch–Mercier–Rohde
entropy-conservative flux ($c_1=\tfrac43$, $c_2=-\tfrac16$, see High
order) plus $-\tfrac12R\lvert\Lambda\rvert[\![\tilde w]\!]^{\mathrm{rec}}$. Here
$R$ is the right-eigenvector matrix of the flux Jacobian, for which no
scaling is stated, the scaled variables are $R^\top_{i+1/2}w$, and
$\lvert\Lambda\rvert=\mathrm{diag}(\lvert\lambda_l\rvert)$ is Roe-type (Eqs.
(6)–(11)). They also run a Rusanov-type $\lvert\Lambda\rvert=(\lvert v\rvert+c)I$.
They state the entropy condition as Lemma 1, after Fjordholm, Mishra &
Tadmor. Their central claim is that the *size* of the reconstructed jump
governs the dissipation. SP-WENO gives a zero or near-zero jump at most
shock interfaces, hence too little dissipation and overshoots (§3.2,
§5.3).

The sources differ in the dissipation matrix:

| | Rueda-Ramírez et al. (2021) | Duan & Tang (2022) | Li, Duan & Tang (2022) | Bhoriya et al. (2023) |
|---|---|---|---|---|
| $\lvert\Lambda\rvert$ | eigenvalue matrix; in the tests every entry set to the largest advective eigenvalue (ES Rusanov) | a scalar times the identity: $\hat a=\max_l\lvert J\partial_t\xi_k+L_k\lambda_l\rvert$, page-local $L_k$ the length of the metric vector (Rusanov-type) | a scalar times the identity: the largest $\lvert\lambda_l\rvert$ along the computational direction, scaled by the metric terms and shifted by the mesh velocity (Rusanov-type) | a scalar times the identity: the largest $\lvert\lambda_l\rvert$ of the fluid block (Rusanov-type, Eq. (21)) |
| reconstruction | minmod, second order | WENO-JS, fifth order | multi-resolution WENO, fifth order | minmod, ENO-3, ENO-4 |
| sign property | by construction | by the switch $\mathcal Y$ | by the switch $\mathcal Y$ | by construction (ENO) |
| setting | LGL subcells of a DGSEM element, irregular grid | finite differences on a moving curvilinear mesh, relativistic HD and MHD | finite differences on a moving curvilinear mesh, stiffened gas | finite differences on a uniform Cartesian grid, two-fluid relativistic plasma with stiff sources |

The Rusanov-type magnitude of the three finite-difference schemes is not
the Roe-type $\tilde R\lvert\Lambda\rvert\tilde R^\top$ of Fjordholm–Mishra–Tadmor's
general form: the eigenvector matrix enters only through the scaling
(Duan & Tang, §4). Bhoriya et al. call their form "similar to the Roe diffusion operator",
since $\tilde R\Lambda\tilde R^{-1}[\![u]\!]\approx\tilde R\Lambda\tilde R^\top[\![w]\!]$ (§4.1.2); with a
scalar $\Lambda$ its magnitude is still Rusanov-type.

## High order

In both finite-difference schemes of the sources the entropy-stable flux
has the order of its reconstructed dissipation, one below that of the
entropy-conservative part (Duan & Tang, §4; Li, Duan & Tang, Exs. 5.1, 5.5).

- Li, Duan & Tang (2022) take the entropy-conservative combination of
  LeFloch, Mercier & Rohde of order $2n_{\mathrm o}$, as they recall it
  (Eq. (3.6); page-local $n_{\mathrm o}$ and coefficients $c_n$, the
  source's $w$ and $\mathsf c_{w,m}$, the notation of
  [flux differencing](/methods/flux-differencing.md)):
  $$f^{(2n_{\mathrm o})}_{i+1/2}=\sum_{n=1}^{n_{\mathrm o}}c_n\sum_{s=0}^{n-1}f^{\mathrm{ec}}(u_{i-s},u_{i-s+n}),\qquad \sum_{n=1}^{n_{\mathrm o}}n\,c_n=1,\quad \sum_{n=1}^{n_{\mathrm o}}n^{2s-1}c_n=0\ (s=2,\dots,n_{\mathrm o}).$$
  For $n_{\mathrm o}=2$ the conditions give $c_1=\tfrac43$ and
  $c_2=-\tfrac16$ *(compiler check, not in the sources)*. The paper does
  not state the value of $n_{\mathrm o}$ it uses. The observed order is
  fifth, set by the WENO dissipation (Ex. 5.1, 5.5).
- Duan & Tang (2022) state the bookkeeping explicitly: the
  entropy-stable flux has order $2n_{\mathrm o}-1$ for an
  entropy-conservative flux of order $2n_{\mathrm o}$ and a WENO
  reconstruction of order $2n_{\mathrm o}-1$ (the source's $p$ is
  $n_{\mathrm o}$). Their MM-O5 scheme is the sixth-order entropy-conservative
  flux ($n_{\mathrm o}=3$) plus fifth-order WENO dissipation, and it reaches
  fifth order on the relativistic-MHD vortex in 2D and 3D, while the
  entropy-conservative MM-O6 reaches sixth (§4, §6, Exs. 6.1, 6.7;
  [flux differencing](/methods/flux-differencing.md)). The source-term
  flux and the volume conservation law keep the order of the
  entropy-conservative part, with no dissipation (§4).
- Bhoriya et al. (2023) (§4.1.1–4.1.2, Remarks 4.1–4.2) use the second-order closed-form
  entropy-conservative flux or its fourth-order LeFloch–Mercier–Rohde combination
  ($c_1=\tfrac43$, $c_2=-\tfrac16$ above). Only even orders are available, so a scheme of odd
  order $q$ takes the flux of order $q+1$: their third-order scheme is the fourth-order
  entropy-conservative flux with ENO-3 dissipation, and the fourth-order one the same flux with
  ENO-4, so the entropy-stable flux has the order of its reconstruction, equal to or one below
  that of the conservative part *(compiler check, not in the sources)*. With SSP Runge–Kutta of matching order the observed orders on a
  forced smooth solution are 1.94, 3.21 and 3.81 at 3200 cells (Table 2).
- Rueda-Ramírez et al. (2021) make no order claim. They cite Winters &
  Gassner that the entropy-conservative flux is second order only on
  regular meshes, and the LGL subcell grid is irregular (§4). Their
  reconstruction still reduces the mesh imprinting of the first-order
  subcell scheme on the Orszag–Tang vortex (Fig. 6).

## TVD-ES inside a DGSEM element

Rueda-Ramírez et al. (2021) use TVD-ES as the low-order partner of the
[subcell finite-volume blending](/methods/subcell-finite-volume-limiting.md)
of the [DGSEM](/methods/dgsem.md). The reconstruction is done in reference
space on the LGL subcells, with slopes divided by $\xi_{j+1}-\xi_j$. The
boundary values of the finite-volume scheme equal those of the DGSEM, so
the blending lemma still applies and the blend is entropy stable
([entropy stability](/properties/entropy-stability.md)).

For the two boundary subcells of an element they test three options:

- no reconstruction (piecewise constant), Eq. (78);
- a one-sided slope inside the element, Eq. (79);
- minmod with the neighbour element's nodal value, Eq. (80).

On the [Orszag–Tang vortex](/benchmarks/orszag-tang-vortex.md) (pure
finite volumes, $256^2$ degrees of freedom, $N=7$) the option without
boundary reconstruction gives the best result, and it is used in all later
tests (§6.2, Fig. 6). The stencil of Eq. (80) needs only the DGSEM's element
connectivity. The authors state that TVD-ES can be added to a DGSEM code
"by only replacing the volume integral and without any additional MPI
communication" (§4).

## Evidence

- **Entropy on a moving mesh, relativistic flows.** Duan & Tang (2022)
  show the discrete total entropy constant for MM-O6 and decaying
  monotonically for MM-O5 on the 2D ($N_x=160$, $t=4$) and 3D ($t=0.1$)
  relativistic-MHD vortices (Figs. 6.4, 6.14). MM-O5 runs relativistic
  Riemann problems, a relativistic-MHD blast, shock–cloud interactions in
  2D and 3D and a 3D shock–bubble without reported failure (Exs.
  6.2–6.10).
- **Entropy on a moving mesh.** Li, Duan & Tang (2022) compare the
  entropy-conservative and TeCNO versions on the 2D
  [isentropic vortex](/benchmarks/isentropic-vortex.md) ($N_x=160$). The
  first keeps the total entropy almost constant, and the second decays it
  monotonically up to $t=4$ (Ex. 5.1, Fig. 5.2); the 3D vortex shows the
  same behaviour up to $t=0.1$ (Ex. 5.5). The paper gives the curves, not
  printed values.
- **WENO choice.** The multi-resolution WENO dissipation resolves more
  structure than WENO-JS "with a slight increase in the computational
  cost" (Remark 3.2). *(Compiler check, not in the sources: the printed
  timings of the four runs that compare both give 0.1 % to 12 % extra.)*
  On the second 2D Riemann problem the moving-mesh runs take 2 min 50 s and 2 min 38 s on 4 cores
  (Ex. 5.4, Table 5.1; Remark 3.2). See
  [adaptive moving mesh](/methods/adaptive-moving-mesh.md).
- **Entropy decay with order, two-fluid plasma.** On the relativistic two-fluid
  [Brio–Wu tube](/benchmarks/brio-wu-shock-tube.md), Bhoriya et al. (2023) find almost the same
  entropy decay for explicit and IMEX schemes of the same order, and less entropy dissipated at
  third than at second order and at fourth than at third (Fig. 1); the third- and fourth-order
  schemes capture the dispersive two-fluid waves already at 400 cells. At the stiffest
  charge-to-mass ratios on 400 cells the small-scale oscillations are unresolved but the run is
  stable, which the authors credit to "the built in entropy stability" (Fig. 2). The 2D
  relativistic Orszag–Tang, blast and reconnection runs are stable at 200×200 and 512×256
  (§6.2).
- **Third-order WENO and ENO dissipation, Cartesian finite differences.**
  Charles & Ray (2025) report that with TeCNO4, ENO3 loses order on
  $\sin^4x$ advection ($L^1$ rate 1.32 at $N=1000$), which they attribute
  to the linear instability of ENO. On the 2D isentropic vortex ENO3
  reaches about 2.2, while the sign-preserving WENO variants keep third
  order (Tables 3–4). On a Burgers Riemann problem every reconstruction
  oscillates, minmod included. The authors call this "a fundamental
  problem with high-order TeCNO schemes" (Remark 6). On 2D Riemann
  configuration 3 a carbuncle-like artefact appears with SP-WENO and
  DSP-WENO under Roe-type dissipation, and Rusanov-type dissipation
  weakens it. Entropy stability does not prevent it (§5.3, Fig. 10;
  [carbuncle phenomenon](/definitions/carbuncle-phenomenon.md)).
- **TVD-ES against first-order subcells.** On Orszag–Tang, TVD-ES has
  higher resolution and fewer artefacts than first-order finite volumes.
  On the GEM reconnection challenge and the Io–plasma-torus problem the
  blended TVD-ES scheme runs where the entropy-stable DGSEM alone crashes
  (Rueda-Ramírez et al. (2021), §6.2–6.4).

## Qualifications

- Rueda-Ramírez et al. (2021) derive the production formula (75) from
  the sign property. Li, Duan & Tang (2022) state the inequality and refer
  to Duan & Tang for the proof (§3.4); Duan & Tang (2022) print it for
  the high-order moving-mesh finite-difference scheme (Thm. 4.1).
- The sign switch $\mathcal Y$ removes dissipation from components that
  fail the test; those components then carry the pure high-order
  entropy-conservative flux, which Duan & Tang themselves say "may produce
  serious nonphysical oscillations near the discontinuities" (§4).
  Entropy stability is proved, the absence of oscillations is not, and
  neither Duan & Tang nor Li, Duan & Tang analyse how often the switch
  fires.
- Entropy stability does not give positivity. The blended TVD-ES scheme of
  Rueda-Ramírez et al. (2021) is robust on their tests, but the blending
  coefficient comes from a heuristic modal indicator
  ([troubled-cell indicator](/definitions/troubled-cell-indicator.md)).
- Rueda-Ramírez et al. (2021) print the "central slope" option (79) and
  the first argument of $\Theta_N$ in (80) with the node $0$ of the own
  element where symmetry with $\Theta_0$ calls for node $N$. The option
  in (79) is also one-sided despite its name. This is a slip in the
  arXiv v1 text and does not affect the option they finally use.
- Bhoriya et al. (2023) prove entropy stability of the semi-discrete scheme; neither the SSP
  nor the IMEX time integration is claimed entropy stable; the Maxwell block, reconstructed
  with third- or fifth-order WENO, needs no entropy property, since the argument holds for any
  Maxwell discretization (Remark 4.3).

# Citations

- [Rueda-Ramírez et al. (2021)](/sources/ruedaramirez-2021.md) — §4 Eqs. (72)–(81), §6.2 Fig. 6, §6.3–6.4 (arXiv v1).
- [Li, Duan & Tang (2022)](/sources/li-2022-c.md) — §3.1 Eq. (3.6), §3.4 Eqs. (3.21)–(3.22), Remark 3.2, App. A, Ex. 5.1, 5.4, 5.5 (arXiv v1).
- [Duan & Tang (2022)](/sources/duan-2022.md) — §1, §4 Eqs. (4.1)–(4.4), Thm. 4.1, Remark 4.1, §6 Exs. 6.1–6.10, Figs. 6.4, 6.14 (arXiv v1).
- [Bhoriya et al. (2023)](/sources/bhoriya-2023.md) — §4.1 (Eqs. (18)–(22), Thms. 4.2–4.3, Remarks 4.1–4.3), §4.2, §6 (Table 2, Figs. 1–2), App. B (arXiv v2).
- [Charles & Ray (2025)](/sources/charles-2025.md) — §2 Eqs. (6)–(11), Lemma 1, §3.2, §5 Tables 3–4, Fig. 10, Remark 6 (arXiv v2).
