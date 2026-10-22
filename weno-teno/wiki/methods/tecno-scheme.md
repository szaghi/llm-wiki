---
type: Method
title: "TeCNO schemes — entropy-stable reconstruction with the sign property"
description: "A TeCNO-type flux adds to an entropy-conservative flux a dissipation acting on jumps of reconstructed scaled entropy variables; it is entropy stable whenever the reconstruction has the sign property, which minmod has by construction and WENO reconstructions get from a componentwise sign switch."
status: established
aliases: [TeCNO, TVD-ES, sign property, entropy-stable reconstruction, ENO-based entropy-stable scheme, Fjordholm–Mishra–Tadmor scheme]
tags: [entropy-stable, reconstruction, numerical-flux, weno, dg]
timestamp: 2026-10-22T12:00:00Z
---

# TeCNO schemes — entropy-stable reconstruction with the sign property

A TeCNO-type scheme is a conservative scheme whose interface flux is an
[entropy-conservative two-point flux](/methods/entropy-conservative-flux.md)
plus a dissipation term. The dissipation is applied to the jump of
*reconstructed* scaled entropy variables, not to the jump of the cell
values. The reconstruction raises the order of the dissipation. Entropy
stability survives the reconstruction under one condition: every
reconstructed jump has the sign of the cell-value jump. This is the
**sign property**. Both sources trace the construction to
Fjordholm, Mishra & Tadmor (2012), as recalled by
[Rueda-Ramírez et al. (2021)](/sources/ruedaramirez-2021.md) (§4) and by
[Li, Duan & Tang (2022)](/sources/li-2022-c.md) (§3.4, after their ref. [19]).

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

**WENO with a sign switch.** Li, Duan & Tang (2022) reconstruct $\tilde w$
with fifth-order
[multi-resolution WENO](/methods/multi-resolution-weno.md) (App. A) and add
the componentwise switch of Biswas & Dubey "to ensure the sign property",
as they recall it (§3.4). In page-local notation,
$\mathcal Y=\mathrm{diag}(\mathcal Y_{ll})$ with $\mathcal Y_{ll}=1$ when the
$l$th components of $[\![\tilde w]\!]^{\mathrm{rec}}$ and $[\![\tilde w]\!]$ have the same
sign and $\mathcal Y_{ll}=0$ otherwise. The dissipation becomes
$-\tfrac12\tilde R\lvert\Lambda\rvert\mathcal Y[\![\tilde w]\!]^{\mathrm{rec}}$
(Eq. (3.21)). A component that fails the test gets no dissipation at that
interface.

The two sources differ in the dissipation matrix:

| | Rueda-Ramírez et al. (2021) | Li, Duan & Tang (2022) |
|---|---|---|
| $\lvert\Lambda\rvert$ | eigenvalue matrix; in the tests every entry set to the largest advective eigenvalue (ES Rusanov) | a scalar times the identity: the largest $\lvert\lambda_l\rvert$ along the computational direction, scaled by the metric terms and shifted by the mesh velocity (Rusanov-type) |
| reconstruction | minmod, second order | multi-resolution WENO, fifth order |
| sign property | by construction | by the switch $\mathcal Y$ |
| setting | LGL subcells of a DGSEM element, irregular grid | finite differences on a moving curvilinear mesh |

## High order

The order of a TeCNO scheme is the smaller of the orders of the
entropy-conservative part and of the reconstructed dissipation *(compiler
check, not in the sources)*.

- Li, Duan & Tang (2022) take the $2w$th-order entropy-conservative
  combination of LeFloch, Mercier & Rohde, as they recall it (Eq. (3.6)):
  $$f^{2w}_{i+1/2}=\sum_{m=1}^{w}\mathsf b_{w,m}\sum_{s=0}^{m-1}f^{\mathrm{ec}}(u_{i-s},u_{i-s+m}),\qquad \sum_{m=1}^wm\,\mathsf b_{w,m}=1,\quad \sum_{m=1}^wm^{2s-1}\mathsf b_{w,m}=0\ (s=2,\dots,w),$$
  with page-local coefficients $\mathsf b_{w,m}$. For $w=2$ the conditions
  give $\mathsf b_{2,1}=\tfrac43$ and $\mathsf b_{2,2}=-\tfrac16$ *(compiler
  check, not in the sources)*. The paper does not state the value of $w$
  it uses. The observed order is fifth, set by the WENO dissipation
  (Ex. 5.1, 5.5).
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

- **Entropy on a moving mesh.** Li, Duan & Tang (2022) compare the
  entropy-conservative and TeCNO versions on the 2D
  [isentropic vortex](/benchmarks/isentropic-vortex.md) ($N_x=160$). The
  first keeps the total entropy almost constant, and the second decays it
  to about $-4.2\times10^{-6}$ at $t=4$ (Ex. 5.1, Fig. 5.2). In the 3D
  vortex the decay is about $-1\times10^{-7}$ by $t=0.1$ (Ex. 5.5).
- **WENO choice.** The multi-resolution WENO dissipation resolves more
  structure than WENO-JS "with a slight increase in the computational
  cost" (Remark 3.2). *(Compiler check, not in the sources: the printed
  timings of the four runs that compare both give 0.1 % to 12 % extra.)*
  On the second 2D Riemann problem the moving-mesh runs take 2 min 50 s and 2 min 38 s on 4 cores
  (Ex. 5.4, Table 5.1; Remark 3.2). See
  [adaptive moving mesh](/methods/adaptive-moving-mesh.md).
- **TVD-ES against first-order subcells.** On Orszag–Tang, TVD-ES has
  higher resolution and fewer artefacts than first-order finite volumes.
  On the GEM reconnection challenge and the Io–plasma-torus problem the
  blended TVD-ES scheme runs where the entropy-stable DGSEM alone crashes
  (Rueda-Ramírez et al. (2021), §6.2–6.4).

## Qualifications

- Neither source proves the entropy inequality anew. Rueda-Ramírez et al.
  (2021) derive the production formula (75) from the sign property. Li,
  Duan & Tang (2022) state the inequality and refer to Duan & Tang for the
  proof (§3.4).
- The sign switch $\mathcal Y$ removes dissipation from components that
  fail the test. Li, Duan & Tang do not analyse how often this happens.
- Entropy stability does not give positivity. The blended TVD-ES scheme of
  Rueda-Ramírez et al. (2021) is robust on their tests, but the blending
  coefficient comes from a heuristic modal indicator
  ([troubled-cell indicator](/definitions/troubled-cell-indicator.md)).
- Rueda-Ramírez et al. (2021) print the "central slope" option (79) and
  the first argument of $\Theta_N$ in (80) with the node $0$ of the own
  element where symmetry with $\Theta_0$ calls for node $N$. The option
  in (79) is also one-sided despite its name. This is a slip in the
  arXiv v1 text and does not affect the option they finally use.

# Citations

- [Rueda-Ramírez et al. (2021)](/sources/ruedaramirez-2021.md) — §4 Eqs. (72)–(81), §6.2 Fig. 6, §6.3–6.4 (arXiv v1).
- [Li, Duan & Tang (2022)](/sources/li-2022-c.md) — §3.1 Eq. (3.6), §3.4 Eqs. (3.21)–(3.22), Remark 3.2, App. A, Ex. 5.1, 5.4, 5.5 (arXiv v1).
