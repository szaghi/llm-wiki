---
type: Method
title: "THINC reconstruction"
description: "THINC reconstructs a cell's data by a hyperbolic-tangent jump profile fitted to the cell average and bounded by the neighbouring values; this page gives its finite-volume, finite-difference and normalised closed forms, the role of the steepness parameter (diffusive, nearly second order, anti-diffusive), a genuinely multi-dimensional form with time averaging for multi-stage Runge–Kutta, and how it is hybridized with polynomial reconstructions."
status: established
aliases: [THINC, tangent of hyperbola for interface capturing, tanh reconstruction]
tags: [interface-capturing, reconstruction, low-dissipation, finite-volume, finite-difference]
timestamp: 2026-10-23T11:06:00Z
---

# THINC reconstruction

**THINC** (tangent of hyperbola for interface capturing, Xiao et al., as recalled
by the sources) replaces the polynomial inside a cell by a monotone
hyperbolic-tangent profile that joins the two neighbouring values and whose
position is fixed by conservation of the cell average. With steepness
$\beta_{\mathrm T}$ the profile in cell $I_i$ is

$$u^{\mathrm T}(x)=u_{\min}+\frac{u_{\max}-u_{\min}}{2}\Big[1+\xi_{\mathrm T}\tanh\Big(\beta_{\mathrm T}\Big(\frac{x-x_{i-1/2}}{\Delta x}-x^c_i\Big)\Big)\Big],$$

$u_{\min,\max}=\min,\max(\bar u_{i-1},\bar u_{i+1})$,
$\xi_{\mathrm T}=\mathrm{sgn}(\bar u_{i+1}-\bar u_{i-1})$, the jump centre $x^c_i$
(page-local) fixed by $\frac1{\Delta x}\int_{I_i}u^{\mathrm T}dx=\bar u_i$; it is
used where the data are monotone, $(\bar u_{i+1}-\bar u_i)(\bar u_i-\bar u_{i-1})>0$,
and the face value is $\bar u_i$ otherwise
([Deng (2023)](/sources/deng-2023.md), §4.6, Eqs. (4.31)–(4.32)). The profile is
bounded by the two neighbours and cannot create new extrema, so it needs no extra
limiter ([Takagi et al. (2022)](/sources/takagi-2022.md), §2.3;
[Fu (2023)](/sources/fu-2023.md), §3.5).

## Finite-difference flux form

For a conservative finite-difference scheme the same construction is applied to
the split point fluxes, which are treated as cell averages of the Shu–Osher
function $\phi$ of the [conservative finite-difference scheme](/definitions/conservative-finite-difference-scheme.md) ([Takagi et al. (2022)](/sources/takagi-2022.md), §2.3,
Eqs. (15)–(17); [Fu (2023)](/sources/fu-2023.md), Eqs. (25)–(26)). With
page-local $f_{\mathrm m}=\tfrac12(f_{i-1}+f_{i+1})$, $f_{\mathrm j}=\tfrac12(f_{i+1}-f_{i-1})$,
$\varsigma=(f_i-f_{\mathrm m})/f_{\mathrm j}$ and $\mathcal T=\tanh(\beta_{\mathrm T}/2)$,
the interface flux for $\partial f/\partial u>0$ is

$$\hat f_{i+1/2}=f_{\mathrm m}+f_{\mathrm j}\,\frac{\mathcal A+\mathcal T}{1+\mathcal A\mathcal T},\qquad
\mathcal A=\frac{\mathrm{sgn}(\varsigma)}{\mathcal T}\,\frac{e^{\lvert\varsigma\rvert\beta_{\mathrm T}}-1}{e^{\lvert\varsigma\rvert\beta_{\mathrm T}}+1},$$

with the first-order fallback $\hat f_{i+1/2}=f_i$ where
$(f_{i+1}-f_i)(f_i-f_{i-1})\le10^{-15}$ (Takagi et al., Eq. (17)). The same closed form,
with $\beta_{\mathrm T}=1.6$ and the profile centred by the cell-average condition, is
printed by [Liang et al. (2022)](/sources/liang-2022.md) (§2.3, Eqs. (19)–(21)).
*(Compiler check, not in the sources: $\mathcal A=\tanh(\varsigma\beta_{\mathrm T}/2)/\mathcal T$,
and for $f_{i-1}=0$, $f_i=0.3$, $f_{i+1}=1$, $\beta_{\mathrm T}=1.6$ the formula
agrees to $10^{-13}$ with the value at $x_{i+1/2}$ of the tanh profile whose
average is computed by quadrature: the closed form is the exact face value.)*
Takagi et al. state that this $\mathrm{sgn}/\lvert\cdot\rvert$ form differs from
the one of Deng, Shimizu and Xiao (2019), a difference they relate to symmetry
breaking from floating-point errors (see
[symmetry preservation](/properties/symmetry-preservation.md)).

## Symmetric finite-volume closed form

[Wakimura et al. (2024)](/sources/wakimura-2024.md) (§3.2.3, Eqs. (29)–(34)) write the
finite-volume profile about the cell centre,
$u^{\mathrm T}(x)=u_{\mathrm m}+u_{\mathrm j}\tanh\big(\beta_{\mathrm T}((x-x_i)/\Delta x-x^c_i)\big)$,
with page-local $u_{\mathrm m}=\tfrac12(\bar u_{i-1}+\bar u_{i+1})$,
$u_{\mathrm j}=\tfrac12(\bar u_{i+1}-\bar u_{i-1})$, $\varsigma=(\bar u_i-u_{\mathrm m})/u_{\mathrm j}$,
$\mathcal T=\tanh(\beta_{\mathrm T}/2)$ and $\mathcal T_\varsigma=\tanh(\varsigma\beta_{\mathrm T}/2)$.
The cell-average condition gives
$x^c_i=\frac1{2\beta_{\mathrm T}}\ln\frac{1-\mathcal T_\varsigma/\mathcal T}{1+\mathcal T_\varsigma/\mathcal T}$, and the two
face values are

$$u^-_{i+1/2}=u_{\mathrm m}+u_{\mathrm j}\,\frac{\mathcal T+\mathcal T_\varsigma/\mathcal T}{1+\mathcal T_\varsigma},\qquad
u^+_{i-1/2}=u_{\mathrm m}-u_{\mathrm j}\,\frac{\mathcal T-\mathcal T_\varsigma/\mathcal T}{1-\mathcal T_\varsigma},$$

used where $(\bar u_{i+1}-\bar u_i)(\bar u_i-\bar u_{i-1})>10^{-20}$, with $\bar u_i$ at both
faces otherwise. They call it mathematically equivalent to the original formulation and
strictly symmetry-preserving, since the two faces are mirror images and $\mathcal T$ can be
precomputed for constant $\beta_{\mathrm T}$ (Appendix A). *(Compiler check, not in the sources:
$\tanh(\beta_{\mathrm T}x^c_i)=-\mathcal T_\varsigma/\mathcal T$, and with the registry's
$\mathcal A=\mathcal T_\varsigma/\mathcal T$ of the finite-difference form above the first face value
is Takagi et al.'s $(\mathcal A+\mathcal T)/(1+\mathcal A\mathcal T)$ exactly.)*

**Volume fractions with an oriented steepness.** [Zhang et al. (2024a)](/sources/zhang-2024.md)
(§3.3, Eqs. (35)–(46)) reconstruct only the volume fraction $\phi_1$ (page-local) by THINC in
interfacial cells, with profile $\tfrac12\big[1+\tanh\big(\beta_i(X+\mathsf c_i)\big)\big]$ on
$X=(x-x_{i-1/2})/\Delta x\in[0,1]$, an oriented steepness
$\beta_i=\beta_{\mathrm T}\lvert n_{1,i}\rvert+0.01$ ($n$ the interface normal) and the centre
in closed form,

$$\mathsf c_i=\frac1{2\beta_i}\ln\frac{e^{2\beta_i\bar\phi_{1,i}}-1}{e^{2\beta_i}-e^{2\beta_i\bar\phi_{1,i}}}$$

(page-local $\mathsf c_i$; Eq. (38)). *(Compiler check, not in the sources: for
$\beta_i=1.8$, $\bar\phi_{1,i}=0.3$ the profile with this centre averages to $0.3$ to
$10^{-10}$ by quadrature.)* The face values for increasing and decreasing $\phi_1$ collapse into
one formula with the gradient sign (Eq. (43)). Because the mirror relation between them fails in
floating point ($e^x\ne1/e^{-x}$ exactly), the implementation obtains the values for one sign by
mirror flipping those of the other, so the sign never enters $\mathsf c_i$. The partial densities
follow by proportionality, assuming constant phasic densities in the cell:
$(\phi_1\rho_1)^-_{i+1/2}=(\phi_1\rho_1)_i\,\phi^-_{1,i+1/2}/\bar\phi_{1,i}$ and
$(\phi_2\rho_2)^-_{i+1/2}=(\phi_2\rho_2)_i\,(1-\phi^-_{1,i+1/2})/(1-\bar\phi_{1,i})$ (Eq. (45));
velocity and pressure are not THINC-reconstructed "since pressure and velocity should be
continuous at the interface". They call this more concise and efficient than Shyue & Xiao, who
rebuild all conservative variables, and Garrick et al., who reconstruct the phase densities only.
Interfacial cells are those with $10^{-3}<\bar\phi_{1,i}<1-10^{-3}$ and locally monotone $\phi_1$
(Eq. (46)). Their steepness is $\beta_{\mathrm T}=1.8$ without and $1.3$ with surface tension.

## Normalised form and the steepness parameter

On the [normalised-variable diagram](/definitions/normalised-variable-diagram.md)
THINC has the closed form

$$\tilde u_{i+1/2}=\frac{\sinh\beta_{\mathrm T}+\cosh\beta_{\mathrm T}-e^{\beta_{\mathrm T}(1-2\tilde u_i)}}{2\sinh\beta_{\mathrm T}},\quad0<\tilde u_i<1,\qquad\tilde u_{i+1/2}=\tilde u_i\ \text{otherwise}$$

([Deng (2023)](/sources/deng-2023.md), Eq. (4.33)), so it is normalisable and
scale-invariant. Deng reads the effect of $\beta_{\mathrm T}$ off the diagram
(§4.6, Fig. 8): $\beta_{\mathrm T}=1.0$ lies entirely below the third-order line
(diffusive); $\beta_{\mathrm T}=1.3$ lies above it near $\tilde u=1/2$
(anti-diffusive, "as the SuperBee TVD limiter"); $\beta_{\mathrm T}=1.1$ passes
close to the accuracy point $(1/2,3/4)$, "almost" second order. This agrees with
the earlier finding, recalled by Deng, that $\beta_{\mathrm T}<1.1$ is diffusive
and $\beta_{\mathrm T}>1.2$ compressive, and with the adaptive THINC of Deng et
al. (2018) that uses $1.1$ in smooth regions and $1.6$ at discontinuities.
*(Compiler check, not in the sources: at $\tilde u_i=1/2$ the formula reduces to
$1/(1+e^{-\beta_{\mathrm T}})$, which equals $3/4$ exactly for
$\beta_{\mathrm T}=\ln3\approx1.0986$; $\beta_{\mathrm T}=1.1$ gives 0.7503.)*
[Wakimura et al. (2024)](/sources/wakimura-2024.md) (§3.2.3) recall the same regimes
from earlier works: $\beta_{\mathrm T}\approx1.1$ behaves like MUSCL with the van Leer
limiter, $\beta_{\mathrm T}=\ln3$ is "analytically second order", and
$\beta_{\mathrm T}$ between 1.6 and 2.0 resolves a discontinuity in about 3 to 4 cells;
their adaptive scheme uses $1.1$ and $1.6$.

**Steepness against surface tension.** [Zhang et al. (2024a)](/sources/zhang-2024.md)
(§4.9–4.10, Table 11) find that with surface tension the steepness must stay small. On a
static drop (Laplace law, $128^2$), $\beta_{\mathrm T}=1.3$, $1.8$, $2.3$ leave $\phi_1$
nearly unchanged ($L_1$ errors $0.81$, $0.78$, $0.72\times10^{-2}$), but the larger two add a
spurious pressure jump ($L_1$ pressure errors $0.99$, $1.66$, $1.81\times10^{-2}$); on an
oscillating ellipse a larger $\beta_{\mathrm T}$ damps the kinetic energy more and shifts
the period. Without surface tension they call the "mist" shed by a shocked water column a
pseudo-capillary effect of interface sharpening, not a physical one (§4.5).

At $\beta_{\mathrm T}=1.6$, the value used by Takagi et al. and recalled as
typical by Fu (2023, §3.5), THINC's modified wavenumber has a positive imaginary
part in some ranges, i.e. anti-diffusion that "squares" smooth profiles
([Takagi et al. (2022)](/sources/takagi-2022.md), §2.3, citing Deng et al.
2018); see [numerical dissipation](/definitions/numerical-dissipation.md). Every
scheme in the sources uses THINC only where a discontinuity is detected or
selected.

## The cell-average constraint and a point-interpolation alternative

[Liang et al. (2022)](/sources/liang-2022.md) (§3.2, Fig. 6) argue that the
cell-average constraint is itself a source of dissipation at a jump: for some
sub-cell positions of a step (their cases (c)–(e)) the face value of the fitted
profile deviates strongly from the exact flux, while for others ((a), (b)) the
deviation is negligible (schematic, not measured). Their remedy keeps the tanh
shape but fixes the shift by requiring the curve to pass through the point value
$f_i$ at the cell centre, with two steepness levels chosen by a TENO-flag detector;
see [TENO-THINC](/methods/teno-thinc.md). This is a dissipation claim at
discontinuities; the anti-diffusion recorded in the previous section concerns
smooth scales, a different regime.

## Multi-dimensional THINC for volume fractions

[Paula et al. (2023)](/sources/paula-2023.md) (§5.1, Eqs. (51)–(55),
Appendix B) reconstruct the volume fraction of each phase in a multiphase
[discrete equations method](/methods/discrete-equations-method.md) by a
genuinely multi-dimensional THINC function, after Ii et al. and Xie &
Xiao. In the unit cell $-\tfrac12\le X,Y,Z\le\tfrac12$, with interface
normal $n=\nabla\phi_k/\lvert\nabla\phi_k\rvert$, linear surface function
$\mathsf P(X)=n_1X+n_2Y+n_3Z$ and normalised distance $\mathsf d_i$, the
THINC profile $\Phi_i$ of the volume fraction is (page-local symbols;
$\Phi_i$ is the registry's $u^{\mathrm T}$ for $u=\phi_k$; quadratic surfaces
are not used)

$$\Phi_i(X)=\tfrac12\Big[1+\tanh\big(\beta_{\mathrm T}(\mathsf P(X)+\mathsf d_i)\big)\Big],$$

and $\mathsf d_i$ is fixed by requiring that the two-point Gauss
quadrature (tensor points $\pm\sqrt3/6$, weights $\tfrac12$) of $\Phi_i$
equal the cell average $\bar\phi_{k,i}$. With the addition formula for
$\tanh$ this is a scalar equation in $\tanh(\beta_{\mathrm T}\mathsf d_i)$,
solved by Newton's method with the shift of Kumar et al., which converges
quadratically to the unique solution from the stated initial guesses
(Eqs. (B.1)–(B.9); tolerance $10^{-6}$). Face values are taken at the same
Gauss points on each face (2 per face in 2D, 4 in 3D). They state that
applying the 1D THINC dimension by dimension gives severe grid effects,
citing earlier work. The default steepness is $\beta_{\mathrm T}=3$, with
$0.325$ and $1$ also tested (§6, §7.4.1).

**Normals from an inverted profile.** The normal is computed from an
approximate signed distance obtained by inverting the 1D profile at the
cell average, with a constant-offset correction:
$\mathsf d_i\approx\frac1{2\beta_{\mathrm T}}\ln\frac{\bar\phi_{k,i}}{1-\bar\phi_{k,i}}+\mathsf d_{\mathrm{corr}}(2\bar\phi_{k,i}-1)$,
$\mathsf d_{\mathrm{corr}}=\frac1{2\beta_{\mathrm T}}\ln\frac{\sinh\beta_{\mathrm T}}{\beta_{\mathrm T}}$,
the offset of the exact cell average far from the interface (Appendix D,
Eqs. (D.1)–(D.3)). Its maximum error is below $10^{-2}$ for
$\beta_{\mathrm T}=3$ (Fig. D.29). A Youngs-type vertex-averaged gradient
of this distance gives $n$ (Eqs. (D.4)–(D.6)). *(Compiler check, not in
the sources: for $\beta_{\mathrm T}=3$, $\mathsf d_{\mathrm{corr}}=0.2010$.)*

**Time averaging for multi-stage Runge–Kutta.** To keep the volume taken
from an upwind cell from exceeding its content, Paula et al. replace the
THINC function by its average over its own translation at the interface
velocity $v_{\mathrm I}$ (page-local; mass-weighted, Eq. (59)) during the
step, $\tilde\Phi(x)=\frac1{\Delta t}\int_0^{\Delta t}\Phi(x-v_{\mathrm I}t)\,dt$
(Eq. (56)), which holds for forward Euler (§5.2). For the three-stage SSP
Runge–Kutta method the averaging intervals of the three stages must be
$[0,\Delta t]$, $[-\Delta t,0]$ and $[-\tfrac12\Delta t,\tfrac12\Delta t]$,
each $\Phi$ built from that stage's data (Eq. (58)). They derive this by
rewriting the second stage as
$u^{(2)}=u^n+\tfrac14\Delta t\mathcal L(u^n)+\tfrac14\Delta t\mathcal L(u^{(1)})$,
a prediction at $t^{n+1/2}$ (Eq. (57)). In practice the average is a
three-point Gauss–Lobatto sum in time, i.e. a shift of $\mathsf d$ by
$-n\cdot v_{\mathrm I}\beta_{\mathrm T}\Delta t/\Delta x$ per quadrature
point (Appendix C, Eqs. (C.1)–(C.4)). They state that, to their knowledge,
time averaging had not been proposed for multi-stage integration or for
compressible flow; earlier works average the upwind volume flux of a
single-step incompressible scheme. They call the result
"positivity-preserving" but prove no theorem
([bound preservation](/properties/bound-preservation.md)). With more than
two phases the face values are normalised to sum to one, because the THINC
function is symmetric only for two phases, and this normalisation can
defeat the time averaging: the triple-point problem needed CFL 0.15
(§6, §7.5).

**Evidence.** Interfaces advected at uniform $p$ and $v$ keep the
velocity and pressure at round-off, $10^{-15}$–$10^{-14}$ in 1D and in 2D
with 2 and 5 materials (Table 1; see
[material-interface advection](/benchmarks/material-interface-advection.md)).
With a cut-off of $10^{-9}$ on the volume fractions, the diffuse interface
stays within about eight cells at $\beta_{\mathrm T}=3$ (§6). On a smooth
profile advected with an interface, the density error is about the same
with and without the interface (§7.3, Fig. 12).

## Hybrids

- **BVD**: per-cell selection between a polynomial (WENO, TENO) candidate and
  THINC by minimal interface jump; BVD-TENO5-THINC beats BVD-WENOZ-THINC (as
  recalled by Fu 2023, §3.6); see [BVD](/definitions/boundary-variation-diminishing.md).
- **TENO-THINC**: THINC where the TENO5 stencil flags show the pattern of a jump
  cell; see [TENO-THINC](/methods/teno-thinc.md).
- **MUSCL-THINC-BVD and Adaptive THINC-BVD in two-phase flow.**
  [Wakimura et al. (2024)](/sources/wakimura-2024.md) (§3.2.4) select by
  [BVD](/definitions/boundary-variation-diminishing.md) between MUSCL (van Leer) and
  THINC with $\beta_{\mathrm T}=1.6$, or between THINC with $1.1$ and $1.6$, in a
  six-equation model with phase change, and apply the switch to the volume fraction and
  the partial densities only; velocity and pressure always take the smooth candidate.
  Contacts are captured in about 3–4 cells, and vapour bubbles created by phase change
  are resolved on a $200\times200$ grid, which MUSCL reaches only on $400\times400$ or
  $800\times800$ (stated; §4.2, §4.4).
- **WENO5IS-THINC.** [Zhang et al. (2024a)](/sources/zhang-2024.md) (§3.3, Eq. (49),
  Algorithm 1) use the [incremental-stencil WENO](/methods/incremental-stencil-weno.md)
  everywhere and THINC for $\phi_1$ and the partial densities in interfacial cells, followed
  by a positivity- and boundedness-preserving interpolation limiter. Against MUSCL-THINC of
  Garrick et al. it resolves shocks, rarefactions and small vortices better and keeps the
  mirror symmetry of a Mach 10 shocked water column at every resolution
  ([symmetry preservation](/properties/symmetry-preservation.md)); both hybrids keep the
  interface width of an advected water block over ten periods, which WENO5IS alone smears
  (§4.1, §4.7).
- **Inside a Riemann solver.** [Hu, Yuan & Zhao (2022)](/sources/hu-2022.md) (§4.2,
  Eq. (4.9)) use THINC density values only in the dissipation term of their
  shock-stable HLLEM flux, selected against MUSCL values by a BVD-type minimal-jump
  rule over the four left/right combinations; the THINC formula and steepness are not
  given (see [BVD](/definitions/boundary-variation-diminishing.md),
  [HLL-family solvers](/methods/hll-riemann-solvers.md)).
- **Anti-dissipative design**: the behaviour of THINC above the third-order line
  is the precedent Huang et al. cite for the controlled anti-dissipation of
  LD-ROUND ([Huang et al. (2026)](/sources/huang-2026.md), §4.2; see
  [ROUND schemes](/methods/round-scheme.md)).

## Place among interface-sharpening methods

Nguyen, Phan, Duy, Kim & Park (2022, §1) list THINC twice in their review of interface capturing
for compressible multiphase flow: as an interface representation alongside level sets, front
tracking and VOF in ghost-fluid approaches, and as a sharpening technique of diffuse-interface
(five-, six- and seven-equation) models alongside level-set and VOF sharpening
([five-equation model](/definitions/five-equation-model.md),
[level-set method](/methods/level-set-method.md)). Their own model does without it: a MUSCL
reconstruction with the compressive "overbee" limiter of Chiapolino, Saurel & Nkonga on the volume
fractions keeps interfaces about three cells thick (§2.3, §3.1, Figs. 3–4), a limiter-based route to
sharp interfaces without a tanh profile ([TVD limiters](/definitions/total-variation-diminishing.md),
[multicomponent Euler equations](/definitions/multicomponent-euler-equations.md)).
[Huang & Johnsen (2023)](/sources/huang-2023.md) take a third route: a
[phase-field](/methods/phase-field-method.md) flux added to the equations
holds the diffuse interface at 4–7 cells with a second-order MUSCL
reconstruction (§4). They state that higher-order schemes "would only
delay" the unbounded thickening of material interfaces (§1); the paper
does not cite THINC-type reconstructions.

## Qualifications

- Fu (2023, Eq. (25)) and Takagi et al. (§2.3) print the conservation constraint
  without the factor $1/\Delta x$ (or with the integral meant in the local
  coordinate), and the profile of Fu (2023) has unbalanced parentheses.
- Paula et al.'s steepness $\beta_{\mathrm T}=3$ is far above the
  $1.1$–$1.6$ of the one-dimensional sources, and their fluxes are not
  integrated over cell faces, which limits the lateral order to two (§6).
- The finite-difference form applies a finite-volume construction to point fluxes
  read as cell averages of $\phi$; the sources use it this way without separate
  justification.

# Citations

- [Deng (2023)](/sources/deng-2023.md) — §4.6, Eqs. (4.31)–(4.33), Fig. 8.
- [Takagi et al. (2022)](/sources/takagi-2022.md) — §2.3, Eqs. (15)–(17).
- [Fu (2023)](/sources/fu-2023.md) — §3.5, Eqs. (25)–(26); §3.6.
- [Huang et al. (2026)](/sources/huang-2026.md) — §4.2: THINC as precedent for controlled anti-dissipation.
- [Nguyen et al. (2022)](/sources/nguyen-2022.md) — §1: THINC among interface-sharpening methods; §2.3, §3.1: limiter-based alternative.
- [Liang et al. (2022)](/sources/liang-2022.md) — §2.3, Eqs. (19)–(21); §3.2, Fig. 6: closed form restated, dissipation of the cell-average constraint.
- [Hu, Yuan & Zhao (2022)](/sources/hu-2022.md) — §4.2, Eq. (4.9): THINC density in the HLLEM dissipation term.
- [Paula et al. (2023)](/sources/paula-2023.md) — §5.1–5.2, Eqs. (51)–(59); §6; §7.1, §7.3, §7.5, Table 1, Fig. 12; Appendices B–D: multi-dimensional THINC, time averaging for SSP-RK3, inverted-profile normals.
- [Huang & Johnsen (2023)](/sources/huang-2023.md) — §1, §4: phase-field alternative to sharpening reconstructions (contrast only).
- [Wakimura et al. (2024)](/sources/wakimura-2024.md) — §3.2.3–3.2.4, Eqs. (29)–(36); §§4.2, 4.4; Appendix A: symmetric closed form, steepness regimes, BVD hybrids in two-phase flow.
- [Zhang et al. (2024a)](/sources/zhang-2024.md) — §3.3, Eqs. (35)–(49), Algorithm 1; §4.1, §4.5, §4.7, §4.9–4.10, Table 11: volume-fraction THINC with closed-form centre, mirror flipping, steepness against surface tension, WENO5IS-THINC.
