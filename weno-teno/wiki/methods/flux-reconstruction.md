---
type: Method
title: "Flux reconstruction and energy-stable FR"
description: "Flux reconstruction corrects the discontinuous interpolated flux of each element with correction functions that carry the interface flux jumps, recovering nodal DG for one choice; energy-stable FR is a DG scheme filtered by a one-parameter correction operator, and Cicchino et al. make its split form nonlinearly stable by filtering the volume terms too."
status: established
aliases: [FR, CPR, correction procedure via reconstruction, ESFR, VCJH, Vincent–Castonguay–Jameson–Huynh schemes, energy-stable flux reconstruction, Huynh g2 lumped-Lobatto scheme]
tags: [flux-reconstruction, dg, entropy-stable, software, immersed-boundary]
timestamp: 2026-10-23T12:00:00Z
---

# Flux reconstruction and energy-stable FR

Flux reconstruction (FR) is a nodal, element-local discretization of
$\partial_tu+\nabla\cdot f(u)=0$ in differential form. In each element the
solution is a polynomial of degree $N$ through its solution points; the
flux evaluated at the solution points is interpolated into a
*discontinuous* flux polynomial, which is then corrected so that its
normal component at the interface points equals a common numerical flux
$h(u^-,u^+)$. The correction is a sum of the interface flux jumps times
*correction functions*, and the choice of correction functions decides
which scheme is obtained. With the DG correction functions FR is nodal
[DG](/methods/discontinuous-galerkin.md). Energy-stable FR (ESFR, also
VCJH) is the one-parameter family of correction functions that is
linearly stable in a broken Sobolev norm, and can be written as a filtered
DG scheme.

## Huynh's FR as implemented in PyFR

[Dzanic, Trojak & Witherden (2022)](/sources/dzanic-2022.md) and
[Dzanic & Witherden (2022)](/sources/dzanic-2022-b.md) state the
formulation of [PyFR](/software/pyfr.md) (Dzanic et al., §4.1, Eqs.
(31)–(38); Dzanic & Witherden, §2.2, §4.2, Eqs. (5)–(9), (25)–(26)).
Page-local symbols: $\ell_j$ the nodal (Lagrange) basis of solution point
$x_j$ (registry §10); $\mathbf g_k$ the vector correction function of
interface flux point $k$ with unit normal $n_k$.

- The discontinuous flux is $\tilde f(x)=\sum_jf(u_j)\ell_j(x)$.
- The corrected flux is
  $f(x)=\tilde f(x)+\sum_k\big(h_k-n_k\cdot\tilde f(x_k)\big)\mathbf g_k(x)$,
  with $h_k$ the common normal flux at interface point $k$, here a
  Rusanov flux with Davis wave speeds (Dzanic et al.) or HLLC (Dzanic &
  Witherden).
- The correction functions satisfy $n_k\cdot\mathbf g_l(x_k)=\delta_{kl}$
  and lie in the Raviart–Thomas space of degree $N$, and are chosen to
  recover nodal DG, after Huynh.
- The semi-discretization is $\frac{d}{dt}u_j=-(\nabla\cdot f)(x_j)$. Its
  interior and interface parts are fixed matrices: the interior one has
  entries $\nabla\ell_l(x_j)$, minus $\nabla\cdot\mathbf g_l(x_j)$ when $l$ is
  an interface point, and the interface one has entries
  $\nabla\cdot\mathbf g_l(x_j)$ (Dzanic & Witherden, Eqs. (25)–(26)).
- Viscous terms use a corrected gradient,
  $\nabla u\approx\nabla\tilde u+\sum_k(u^I_k-\tilde u_k)\nabla\mathbf g_k$
  with a common interface solution $u^I_k$, and a second correction for
  the viscous flux; the common values come from BR1 (Dzanic et al.,
  Eqs. (34)–(36)) or BR2 (Dzanic & Witherden).
- Solution points are Gauss–Lobatto points on tensor-product elements and
  $\alpha$-optimized points on simplices (Dzanic & Witherden, §4.2).

With DG correction functions the element mean evolves by the boundary
flux alone, which is the assumption under which Dzanic & Witherden prove
that their [entropy filtering](/methods/entropy-filtering.md) always
finds an admissible filter strength (§2.2, Eq. (10)). Dzanic et al. build
a reverse-time (downwind) divergence for their
[artificial viscosity](/methods/artificial-viscosity.md) simply by
flipping the sign of the dissipative part of the Rusanov flux (§4.2).

[Dzanic & Witherden (2023)](/sources/dzanic-2023.md) use the same
formulation for ideal MHD and write the interface part through an
interface basis $\ell^{\mathrm I}_k=n_k\cdot\mathbf g_k-\ell_k$ (page-local) on
the interface nodes, which are a subset of the solution nodes, with the
mean-value property stated for nodal DG with suitable quadrature and FR
with DG correction functions (§2.2, Eqs. (6)–(16)). They compute the
discrete divergence of $B$ for the Powell source from the same two parts,
interior and interface, the latter with the centred interface value
(Eqs. (18)–(19); [entropy filtering](/methods/entropy-filtering.md)).

## Huynh's correction function on Gauss points, with immersed walls

[Funada & Imamura (2023)](/sources/funada-2023.md) use Huynh's FR for the
Euler equations on hierarchical Cartesian grids, with $N+1$ solution points
at the Gauss points of each direction (the source counts points, $k=N+1$,
and calls the scheme $k$th order) (§2.1, Eqs. (1)–(12)). In 1D, on the
reference cell $\xi\in[-1,1]$ with $\ell_j$ the Lagrange basis,

$$f^c(\xi)=\sum_jf_j\ell_j(\xi)+\big[h_{i-1/2}-f(-1)\big]g_{\mathrm L}(\xi)+\big[h_{i+1/2}-f(1)\big]g_{\mathrm R}(\xi),$$

with $g_{\mathrm L}(-1)=1$, $g_{\mathrm L}(1)=0$, $g_{\mathrm R}(\xi)=g_{\mathrm L}(-\xi)$,
both of degree $N+1$ (Eqs. (7)–(9)). They take Huynh's function, chosen
for "a large upper bound on the Courant number",

$$g_{\mathrm L}=\frac{(-1)^{N+1}}{2}\Big[\frac{N\,P_{N+1}+(N+1)P_{N-1}}{2N+1}-P_N\Big]$$

with $P_n$ the Legendre polynomial of degree $n$ (page-local; Eq. (10),
written in their $k$). It satisfies $g_{\mathrm L}(-1)=1$, $g_{\mathrm L}(1)=0$
*(compiler check, not in the sources: use $P_n(\pm1)=(\pm1)^n$)*.
Multi-D is the tensor product of the 1D operator. Their other ingredients:

- the common flux is SLAU (Shima & Kitamura), an AUSM-family flux, at
  interior faces and at immersed-wall flux points (§2.1, §2.3);
- coarse–fine faces of the hierarchical grid, where flux points do not
  coincide, are handled by the mortar element method of Kopriva & Kolias:
  project the coarse-side states onto mortar points, compute common
  fluxes, project them back (§2.2, Fig. 3;
  [adaptive mesh refinement](/methods/adaptive-mesh-refinement.md));
- steady states are reached with the implicit matrix-free Gauss–Seidel
  method, whose dense FR Jacobian is replaced by a first-order
  finite-volume left-hand side on one sub-cell per solution point (defect
  correction on sub-cells, DECS) (§2.4).

The feature their immersed-boundary method exploits is that the FR
polynomial can be evaluated at any point of a cell, so wall data along a
wall-normal line can be interpolated to high order from fluid cells; with
it the observed order is the design order $N+1$ up to the wall, for
$N=1,2,3$, on a bump channel, a cylinder and a sphere
([immersed-boundary methods](/methods/immersed-boundary-method.md)). A
wall-free vortex advection on uniform grids confirms order $N+1$ in
$L_\infty$ of the transverse velocity (§3.1, Fig. 10).

## FR on Gauss points with LDG viscous terms

[Kou et al. (2022)](/sources/kou-2022.md) state Huynh's FR for the
compressible Navier–Stokes equations in seven stages (§3, Eqs.
(7)–(19), after Huynh, Vincent et al. and Williams et al.). On Cartesian
tensor-product elements the solution of degree $N$ lives at
$(N+1)^d$ solution points and the correction functions have degree
$N+1$; solution and flux points are Gauss points (Gauss–Lobatto named as
the alternative). The stages are:

1. interpolate the solution to the flux points;
2. form the common interface solution by LDG,
   $\{\!\{u\}\!\}-\beta_{\mathrm{LDG}}[\![u]\!]$, and the solution
   correction (Eqs. (9)–(10));
3. compute the corrected gradient from the interior gradient plus the
   correction functions times the solution corrections (Eqs. (11)–(13));
4. evaluate the inviscid and viscous fluxes at the solution points and
   interpolate them to the flux points (Eq. (14));
5. compute the interaction fluxes: Rusanov for the inviscid part, the LDG
   flux $\{\!\{f_v\}\!\}+\tau_{\mathrm{LDG}}[\![u]\!]+\beta_{\mathrm{LDG}}[\![f_v]\!]$
   for the viscous part, with $\beta_{\mathrm{LDG}}=0.5$ and
   $\tau_{\mathrm{LDG}}=0.1$ (page-local parameters and viscous flux $f_v$;
   Eq. (15));
6. add the flux correction, the jump between interaction and interpolated
   flux times the divergence of the correction functions (Eqs. (16)–(17));
7. advance $\frac{d}{dt}u=\mathcal L(u)$ (Eqs. (18)–(19)) with three-stage
   [SSP Runge–Kutta](/methods/ssp-runge-kutta.md) (Eqs. (20)–(22)).

Which member of the correction-function family is used is not stated.
Local p-refinement couples elements of different degrees through mortar
faces, on which the common and interaction fluxes are computed and
projected back (§5.2; [h- and hp-adaptation](/methods/hp-adaptation.md)).
Kou et al. add a volume-penalization source to this scheme to impose
walls on Cartesian grids ([immersed-boundary methods](/methods/immersed-boundary-method.md)).
In a 1D penalized advection–diffusion test the FR rate $O(h^{N+1})$ is
kept when the solid points are penalized towards the exact solution, but
falls to about first order over the fluid domain when they are penalized
towards the boundary value, while the rate away from the wall stays
$N+1$ (§5.1, Figs. 9–10). They recall that the explicit time step of
high-order methods scales with the inverse square of the order (§4.6).

## Energy-stable FR as filtered DG

[Cicchino, Nadarajah & Del Rey Fernández (2022)](/sources/cicchino-2022.md)
recall the background (§1–2). FR and the correction procedure via
reconstruction (CPR) coincide, as Jameson et al. proved; ESFR recovers DG,
spectral difference and spectral volume schemes through the choice of the
correction functions; and Allaneau–Jameson (1D) and Zwanenburg–Nadarajah
(3D, modal, uncollocated) recast ESFR as a filtered DG scheme. In that
form, with the element mass matrix $M$ (dense in general) and the stiffness
matrix $Q$ of a modal or nodal basis, the ESFR strong form reads (Eqs.
(14)–(17))

$$(M+K_{\mathrm{FR}})\frac{d}{dt}\hat{\mathbf u}+Q\hat{\mathbf f}+\text{(surface terms)}=0,\qquad K_{\mathrm{FR}}=c_{\mathrm{FR}}\,(D^N)^\top M\,D^N,\quad D=M^{-1}Q,$$

with $\hat{\mathbf u}$, $\hat{\mathbf f}$ the coefficient vectors of the
solution and of the projected flux, and page-local $K_{\mathrm{FR}}$ the
correction (filter) operator and $c_{\mathrm{FR}}\ge0$ its parameter.
Entry-wise, $K_{\mathrm{FR}}$ is $c_{\mathrm{FR}}$ times the reference-element
integral of $J$ times the product of the $N$th derivatives of two basis
functions. The named values are $c_{\mathrm{DG}}=0$
(DG), $c_{\mathrm{SD}}$ (spectral difference), $c_{\mathrm{HU}}$ (Huynh's
$g_2$) and $c_+$, the largest value before an order of accuracy is lost,
which has no closed form; the explicit time step grows with
$c_{\mathrm{FR}}$ (§2.2, after Castonguay). The values refer to a
normalized Legendre basis, and $K_{\mathrm{FR}}$ must be built with the
scheme's own derivative operator (Remark 2.1). Linear stability holds in
the broken Sobolev norm
$\tfrac12\lVert u\rVert^2_{M+K_{\mathrm{FR}}}$, using $K_{\mathrm{FR}}D=0$ (the
$(N+1)$th derivative of a degree-$N$ polynomial vanishes) (Eq. (22)).

**Inverse of the filtered mass matrix** (Cicchino et al., Lemma 3.1). On
affine elements, by Sherman–Morrison in a normalized Legendre basis,

$$(M+K_{\mathrm{FR}})^{-1}=M^{-1}-\frac{1}{1+c_{\mathrm{FR}}(2N+1)(N!\,\mathsf c_N)^2}\,M^{-1}K_{\mathrm{FR}}M^{-1},\qquad \mathsf c_N=\frac{(2N)!}{2^N(N!)^2},$$

with page-local $\mathsf c_N$ the leading coefficient of the Legendre
polynomial of degree $N$ (Eqs. (30)–(32)).

## Nonlinearly stable split form

Split forms make DG entropy (energy) stable for Burgers and Euler, but
earlier attempts to carry them to ESFR obtained a proof only for DG or for
Huynh's $g_2$ lumped-Lobatto scheme (Ranocha, Öffner & Sonar 2016; Abe et
al. 2018), as Cicchino et al. recall (§1). They explain why. With the
Burgers split
$\alpha_{\mathrm s}\,\partial_x(u^2/2)+(1-\alpha_{\mathrm s})\,u\,\partial_xu$
(page-local weight $\alpha_{\mathrm s}$, not the DG–FV blending
coefficient $\alpha$) applied through $D$, and the filter
$(M+K_{\mathrm{FR}})^{-1}$ applied to the surface terms only (the
"classical" ESFR split form, Eq. (21)), the energy balance contains the
term $-(1-\alpha_{\mathrm s})\,\mathbf u^\top K_{\mathrm{FR}}UD\mathbf u$ with
$U=\mathrm{diag}(\mathbf u)$, which is in general neither zero nor of one
sign. No nonlinear stability claim can then be made unless
$K_{\mathrm{FR}}=0$ or is diagonal (Eq. (23)).

Their remedy (§3.1, Eq. (28)):

1. split with respect to the stiffness operator $Q$, which satisfies a
   summation-by-parts property for any quadrature exact to degree $2N-1$,
   with dense norms and uncollocated nodes (Eq. (24);
   [summation-by-parts operator](/operators/summation-by-parts-operator.md));
2. apply $(M+K_{\mathrm{FR}})^{-1}$ to the conservative volume term, to the
   non-conservative volume term and to the face terms;
3. split the face term as well, because on non-LGL volume nodes the face
   value of the interpolated flux differs from the flux of the face value
   of the solution; on collocated LGL nodes the face splitting disappears
   ([DGSEM](/methods/dgsem.md)).

For DG ($c_{\mathrm{FR}}=0$) the scheme equals Chan's flux-differencing
scheme, and for collocated LGL DG Gassner's split form (§3.1;
[flux differencing](/methods/flux-differencing.md),
[split convective forms](/methods/split-convective-forms.md)). With
Lemma 3.1 and $K_{\mathrm{FR}}M^{-1}Q=0$ on linear elements, it is the DG
split form plus one extra volume term of design order, with coefficient
$(1-\alpha_{\mathrm s})/\big(1+c_{\mathrm{FR}}(2N+1)(N!\,\mathsf c_N)^2\big)$ (Eq. (33)). In
strong form it differs from the schemes of the ESFR literature, since the
correction now acts on the volume integral (abstract). It is valid for
modal or nodal bases, uncollocated volume and surface cubature, and
overintegration.

**Theorems** (Cicchino et al., 1D Burgers, affine elements):

- local and global conservation for every $\alpha_{\mathrm s}$ and any
  quadrature exact to degree $2N-1$ (§3.1.1, Eq. (42));
- energy stability in the $M+K_{\mathrm{FR}}$ norm for $\alpha_{\mathrm s}=2/3$, for
  which the volume terms cancel and only interface terms remain (Eq. (46)).
  The interface contribution is
  $(u^+-u^-)^2\big(\tfrac1{12}(u^+-u^-)-\lambda_{\mathrm s}\big)$ for the flux
  $\tfrac12\big(\tfrac12(u^-)^2+\tfrac12(u^+)^2\big)-\lambda_{\mathrm s}(u^+-u^-)$
  (page-local dissipation coefficient $\lambda_{\mathrm s}=a/2$ in the registry's
  Lax–Friedrichs form), so stability requires
  $\lambda_{\mathrm s}\ge\tfrac1{12}(u^+-u^-)$, with equality for the
  energy-conservative flux; local Lax–Friedrichs,
  $\lambda_{\mathrm s}=\tfrac12\max(\lvert u^-\rvert,\lvert u^+\rvert)$, satisfies it and is energy
  stable (Eqs. (47)–(50);
  [entropy-conservative two-point fluxes](/methods/entropy-conservative-flux.md),
  [entropy stability](/properties/entropy-stability.md)).

The authors state that the extension to 3D is straightforward (§1); the
proof is 1D and scalar.

**Huynh's $g_2$ scheme.** Huynh's lumped-Lobatto scheme chooses the
correction on Gauss nodes so that $M_{\mathrm{GL}}+K_{\mathrm{HU}}$ is the
lumped LGL mass matrix; with the flux evaluated on LGL nodes it is
collocated LGL DG in disguise. Cicchino et al. stress that it is *not*
equivalent to $c_{\mathrm{HU}}$ with $K_{\mathrm{FR}}$ and the volume flux on the
same node set, and that it cannot be run on uncollocated volume nodes
(Remark 3.1, footnotes 1–2). This is why Abe et al.'s stable case is DG.

## Evidence

Cicchino et al. (2022), PHiLiP code, 1D periodic Burgers on $[0,2]$, eight
elements, $N=4$ and $5$, RK4 with $\Delta t=10^{-4}$ (§4;
[Burgers equation tests](/benchmarks/burgers-equation-tests.md)):

- **Energy** ($u_0=\sin(\pi x)+0.01$, $t=3$, past shock formation). With
  $c_{\mathrm{DG}}$, $c_+$ and $c_{\mathrm{FR}}=10^4$, the new split form conserves
  energy to $O(10^{-12})$ with the energy-conservative flux and decreases
  it monotonically with Lax–Friedrichs, on collocated LGL, uncollocated
  Gauss ($N+1$ points) and overintegrated Gauss ($N+3$ points) nodes. The
  conservative DG scheme and the classical split form do neither, except
  Huynh's lumped-Lobatto scheme on collocated nodes (Tables 1–3). All
  schemes conserve the integral of $u$ to $O(10^{-16})$.
- **Accuracy** (manufactured solution, Lax–Friedrichs, $t=1$). $N=4$:
  orders 5.00–5.02 for DG and the new split form, 4.98 for the classical
  split with $c_+$ (Table 4). $N=5$: 6.02 for DG and the new split with
  $c_{\mathrm{DG}}$, but 5.70–5.76 for the new split with $c_+$ and
  5.60–5.73 for the classical split with $c_+$ (Table 5). The text says
  all schemes reach $N+1$ (§4.2); at $N=5$ with $c_+$ the tables show
  about 5.7, consistent with the definition of $c_+$ as the value at which
  an order is about to be lost (§2.2).

The PyFR implementation runs nodal DG through FR at $\mathbb P^2$–$\mathbb P^{14}$
on 1D, 2D and 3D Euler, MHD and Navier–Stokes problems, among them the
inviscid ONERA M6 wing and an LES of the VFE-2 delta wing at $\mathbb P^3$
with $1.04\times10^8$ degrees of freedom per component (Dzanic et al., §5;
Dzanic & Witherden, §5); see [PyFR](/software/pyfr.md).

## Qualifications

- The new split form is no longer an FR scheme in the sense of a
  surface-only correction; sources that define FR by the surface
  correction would not class it as FR.
- Cicchino et al.'s abstract stresses modal ESFR; all their tests use a
  nodal Lagrange basis, so the modal case is proved, not tested.
- The arXiv v1 read prints the weak form (29) without the face term that
  the integration by parts of the non-conservative volume term of (28)
  produces; the two are equivalent as printed only on collocated LGL
  nodes. The JCP version may differ.

# Citations

- [Cicchino, Nadarajah & Del Rey Fernández (2022)](/sources/cicchino-2022.md) — §1, §2 Eqs. (9)–(17), Remark 2.1, Eqs. (19)–(23), §3 Eq. (24), §3.1 Eqs. (26)–(33), Lemma 3.1, Remarks 3.1–3.2, §3.1.1 Eq. (42), §3.1.2 Eqs. (43)–(50), §4 Tables 1–5 (arXiv v1).
- [Dzanic, Trojak & Witherden (2022)](/sources/dzanic-2022.md) — §4.1 Eqs. (31)–(38), §4.2, §5 (arXiv v2).
- [Dzanic & Witherden (2022)](/sources/dzanic-2022-b.md) — §2.2 Eqs. (5)–(10), §4.2 Eqs. (25)–(26), §5 (arXiv v3).
- [Kou et al. (2022)](/sources/kou-2022.md) — §3 Eqs. (7)–(22), §4.6, §5.1 Figs. 9–10, §5.2.
- [Dzanic & Witherden (2023)](/sources/dzanic-2023.md) — §2.2 Eqs. (6)–(16), §2.3 Eqs. (18)–(19) (arXiv v2).
- [Funada & Imamura (2023)](/sources/funada-2023.md) — §2.1 Eqs. (1)–(12), §2.2 Fig. 3, §2.3, §2.4, §3.1 Fig. 10.
