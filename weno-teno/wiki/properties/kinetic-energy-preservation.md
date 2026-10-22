---
type: Property
title: "Kinetic energy preservation"
description: "A semi-discretization is kinetic-energy-preserving when its convective terms neither create nor destroy discrete kinetic energy, which Coppola and Veldman reduce to the skew-symmetry of C − ½diag(d_mass); the page gives that criterion, face-flux conditions, the second-order barrier, SBP proofs including the rotational form, correction terms, and DG two-point fluxes."
status: established
aliases: [KEP, kinetic-energy-preserving, KEEP, kinetic energy conservation, energy-preserving discretization]
tags: [kinetic-energy-preserving, finite-volume, finite-difference, dg, turbulence]
timestamp: 2026-10-22T20:00:00Z
---

# Kinetic energy preservation

In the convective part of the compressible equations, the kinetic energy
$\kappa=\tfrac12\rho\lvert v\rvert^2$ is a secondary (quadratic) invariant. Its
evolution follows from the mass and momentum equations and is a pure
divergence. A semi-discretization is **kinetic-energy-preserving** (KEP)
when the same holds discretely: the convective terms change the discrete
total kinetic energy only through boundary fluxes, and locally only through
a kinetic-energy flux.
[Coppola & Veldman (2023)](/sources/coppola-2023.md) give the necessary and
sufficient algebraic condition. They state it for the generalized quadratic
$\tfrac12\rho\phi^2$ of a transported scalar $\phi$ (page-local), with
$\phi=v$ the kinetic energy (§2.1, §5).

## The criterion

The continuous kinetic-energy operator is (page-local $A$, not the flux
Jacobian)
$A\phi=\partial_x(\rho v\phi)-\tfrac12\phi\,\partial_x(\rho v)$. Global
conservation of $\tfrac12\rho\phi^2$ is the skew-symmetry of $A$, and locally
$\phi A\phi=\partial_x(\tfrac12\rho v\phi^2)$ (Eqs. (4)–(6)). Discretely, write
mass as $V\frac{d\rho}{dt}=-\mathbf d_m$ and momentum as
$V\frac{d}{dt}(\rho\phi)+\mathcal C\phi=0$, with page-local $V$ the diagonal
control-volume matrix, $\mathcal C$ the convective matrix and $\mathbf d_m$
the discrete mass transport. Then

$$V\frac{d}{dt}\big(\tfrac12\rho\phi^2\big)=-\mathrm{diag}(\phi)\Big(\mathcal C-\tfrac12\mathrm{diag}(\mathbf d_m)\Big)\phi .$$

Global kinetic-energy conservation holds **iff**
$\mathcal A=\mathcal C-\tfrac12\mathrm{diag}(\mathbf d_m)$ is skew-symmetric,
equivalently $\mathrm{diag}(\mathbf d_m)=\mathcal C+\mathcal C^\top$
(Eqs. (59)–(60)). The condition has two parts:

- the off-diagonal part of $\mathcal C$ is skew-symmetric;
- the diagonal of $\mathcal C$ equals half the discrete mass transport.

Coppola & Veldman call this "the mathematical proof of the necessity",
previously only observed by Pirozzoli and Morinishi, that continuity and
momentum be split consistently (§5.1). Two consequences follow:

- Under energy preservation, $\mathbf d_m=(\mathcal C+\mathcal C^\top)\mathbf 1$
  is fixed by the advective operator.
- If momentum is also conserved, then $\mathbf d_m=\mathcal C\mathbf 1$ and
  mass is conserved too (Eqs. (61)–(62)).

**Local form** (§5.3, Corollary A.4). A skew-symmetric banded matrix
$G=\sum_{k>0}\big(\mathrm{diag}(\mathsf c_k)\mathcal T^k-\mathcal T^{-k}\mathrm{diag}(\mathsf c_k)\big)$,
with page-local shift $\mathcal T$ and diagonals $\mathsf c_k$, satisfies
$\mathrm{diag}(\phi)G\phi=(I-\mathcal T^{-1})\mathbf f_\kappa$. The
kinetic-energy flux is
$\mathbf f_\kappa=\sum_{k>0}\sum_{h=0}^{k-1}\mathcal T^{-h}\mathrm{diag}(\mathsf c_k)\mathrm{diag}(\phi)\mathcal T^k\phi$.
Global kinetic-energy preservation therefore implies local preservation, in
the same way as for linear invariants
([local conservation and flux form](/results/local-conservation-flux-form.md)).

## Finite-volume face fluxes

For three-point finite-volume schemes, kinetic energy is conserved globally
and locally iff the momentum face flux is the mass flux times the
equal-weight mean, $m_{i+1/2}\,\tfrac12(\phi_i+\phi_{i+1})$
(Coppola & Veldman (2023), Observation 7, Eqs. (65)–(71)). Three features
of this condition stand out:

- The equal-weight mean is required "independent of the geometric position
  of the face", even on stretched grids.
- The mass flux $m_{i+1/2}$ is completely free, upwind-biased included,
  provided the same one is used in the mass equation.
- The local kinetic-energy flux is $\tfrac12m_{i+1/2}\phi_i\phi_{i+1}$. The
  source lists the same flux in Subbareddy–Candler, Chandrashekar and Kuya
  et al.

Unequal interpolation weights bias the flux and destroy the property.
Interpolating the product instead,
$(m\phi)_{i+1/2}=\tfrac12(m_i\phi_i+m_{i+1}\phi_{i+1})$, gives a zero-diagonal
advection matrix. That cannot be KEP for compressible flow (§5.2, §6.1). The
authors therefore regard the splitting of the mass flux, the focus of much
earlier work, as irrelevant to energy preservation (though it can affect
accuracy) (§6.1).

**Order barrier and its bypass** (§6).

- **Barrier.** Product-form face fluxes
  $m_{i+1/2}\sum_q c_q\phi_{i+q}$ (page-local interpolation weights $c_q$)
  that preserve kinetic energy are at most second order. The property forces
  the two central weights to $\tfrac12$ and the others to sum to zero
  (Observation 9).
- **Bypass.** Higher order needs sums of two-point products. Richardson
  extrapolation $(8\cdot\text{fine}-\text{coarse})/6$ of the second-order
  KEP scheme gives a fourth-order KEP finite-volume flux,
  $$(m\phi)^{\mathrm{4th}}_{i+1/2}=\tfrac13(m_{i+1}+m_i)(\phi_{i+1}+\phi_i)-\tfrac1{24}(m_{i+2}+m_i)(\phi_{i+2}+\phi_i)-\tfrac1{24}(m_{i+1}+m_{i-1})(\phi_{i+1}+\phi_{i-1}),$$
  with effective volume $(8V^{\mathrm{fine}}-V^{\mathrm{coarse}})/6$. This
  equals Pirozzoli's fourth-order flux (Eqs. (75)–(78)).
- **DG.** The high-order flux-differencing DG schemes follow the same
  bypass *(compiler check, not in the sources: Coppola & Veldman do not
  discuss DG, and Ranocha et al. do not discuss the barrier)*. Their volume term is a sum of symmetric two-point fluxes, and it
  keeps the order of the derivative operator
  ([Ranocha et al. (2023)](/sources/ranocha-2023.md), §2;
  [flux differencing](/methods/flux-differencing.md)).

**Pressure and total energy** (§8.1). The model problem has no pressure.
For Euler in the internal-energy formulation, total energy is conserved
when mass and momentum are discretized KEP and the pressure terms satisfy
$D^p=-(D^e)^\top$ (page-local pressure-gradient and pressure-work
operators). The source states this after Veldman and De Michele–Coppola.

## Finite-difference split forms

For the generalized split family, kinetic-energy preservation holds iff
the Coppola et al. weight conditions and the duality relations between
the four derivative matrices hold (Coppola & Veldman (2023), §5.3, Eq. (72)).
This admits non-uniform meshes and dual-sided (biased) operators. Details
are on [split convective forms](/methods/split-convective-forms.md). On
smooth tests, the KEP central members with $\zeta\in\{0,\tfrac12,1\}$ conserve
mass, momentum and energy to $O(10^{-15})$–$O(10^{-16})$, and members that
violate the weights lose energy at $O(10^{-3})$–$O(10^{-4})$ (§7.3, Fig. 2).

## Summation-by-parts proofs and the rotational form

[Edoh (2022)](/sources/edoh-2022.md) proves kinetic-energy preservation of
split forms with diagonal-norm finite-difference
[summation-by-parts operators](/operators/summation-by-parts-operator.md):
the convective contribution to the discrete kinetic-energy balance
collapses to a boundary flux by $Q+Q^\top=B$ and the commutation of the
diagonal norm with diagonal data matrices (Eqs. (11)–(12), (22)–(24)).
His results (§3, Tables 1–3):

- **Incompressible.** The Morinishi (skew-symmetric) splitting, his
  rotational-form splitting Div-rot and the derived Div-str are
  kinetic-energy preserving when the discrete velocity is solenoidal,
  $D_jv_j=0$. For Div-rot the proof relabels indices under the double sum
  over components, so the property holds only for the summed
  multi-dimensional kinetic energy, not component by component
  (Remark 3).
- **EMAC fails discretely.** The strain-based EMAC form of Charnyi et al.
  leaves an indefinite residual of the order of the operator, because the
  discrete product rule fails pointwise, and its compressible version of
  Both et al. likewise (Eqs. (16), (25)). The EMAC papers are finite
  element papers with a weakly imposed solenoidal constraint, so the
  disagreement concerns the discrete setting.
- **Compressible.** In square-root-density variables, compressible Div-rot
  and Div-str, and the one-parameter family that contains Rozema's
  splitting, are kinetic-energy preserving without any solenoidal
  condition (Eqs. (24), (26)). The KEP families are therefore not unique:
  Edoh's family with geometric density averages and Coppola et al.'s
  family with arithmetic ones (the $\zeta$ family above) are distinct
  ([split convective forms](/methods/split-convective-forms.md)).
- **Total energy.** Building the total-energy flux as internal energy plus
  the kinetic energy induced by mass and momentum (after Kuya et al.)
  gives a neutral-stability statement in the auxiliary variables
  $(\sqrt\rho,\sqrt\rho v,\sqrt{\rho e})$, as Edoh states after the
  literature (§4).
- **Time integration.** Exact preservation in time needs implicit
  symplectic or relaxation-type integrators; Edoh presumes the temporal
  error negligible at small $\Delta t$ and does not study it (§4.1.1).

His tests show the practical side. Without filtering, Div-rot is more
robust than the divergence form but more prone to aliasing than the
Feiereisen and Kennedy–Gruber splittings on the isentropic vortex; on the
Taylor–Green vortex at $\mathrm{Re}=1600$ both Kennedy–Gruber and Div-rot
run severely under-resolved grids on which the divergence form fails
(§4, Figs. 1, 3).

## Kinetic-energy correction terms

[Abgrall, Öffner & Ranocha (2022)](/sources/abgrall-2022.md) state the
kinetic-energy-preserving surface flux condition as a momentum flux
$\{\!\{v_m\}\!\}f_\rho+\{\!\{p\}\!\}n_m$ for any mass flux $f_\rho$ (Eq. (40)), the
Coppola–Veldman face condition with a central pressure added *(compiler
check, not in the sources: Coppola & Veldman treat no pressure)*. The
semi-discrete kinetic-energy balance of such a scheme contains the
volume pressure work $p^\top MD_jv_j$ and a surface term
$p^-\tfrac12(v^+_j-v^-_j)$ for $-p\,\partial_jv_j$ (Eq. (41)). Taking this
balance as a constraint, an element-wise
[correction term](/methods/entropy-correction-term.md) makes any
baseline DG or SBP scheme kinetic-energy preserving with the smallest
change in the mass-matrix norm (Eq. (42), Prop. 3.5), and it can be
combined with the entropy correction (Remark 3.6). On the inviscid 2D
Taylor–Green vortex the kinetic-energy correction removes the growth of
kinetic energy before the central scheme blows up, but does not prevent
the blow-up (on the sixth-order finite-difference grid it fails at about
the same time as the central scheme, App. A.3), while flux differencing with Pirozzoli's or Ranocha's
kinetic-energy-preserving flux survives much longer (§4.2.2, App. A.3;
[Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)).

## In DG: kinetic-energy-preserving volume fluxes

In split-form DGSEM the property is a choice of the symmetric two-point
volume flux ([Rueda-Ramírez, Pazner & Gassner (2022)](/sources/ruedaramirez-2022.md),
§2.1). The sources use these fluxes:

- the Shima et al. flux, KEP and pressure-equilibrium-preserving but not
  entropy-conservative;
- the Ranocha flux, KEP, pressure-equilibrium-preserving and
  entropy-conservative (Ranocha et al. (2023), §3.2, properties cited from
  the literature);
- the Chandrashekar flux, entropy-conservative and KEP (Rueda-Ramírez et
  al. (2022), §4);
- Renac's multicomponent flux, entropy-conservative and formally KEP "in
  Jameson's sense", a property that "can fail discretely"
  ([Renac (2021)](/sources/renac-2021.md), Remark 3.2, Eq. (24)).

Renac's momentum flux is the mixture mass flux times $\{\!\{v\}\!\}$ plus the
pressure mean $\{\!\{p/T\}\!\}/\{\!\{1/T\}\!\}$ times $n$, which has the structure of
the Coppola–Veldman face-flux condition above, and for one component his
flux reduces to the Chandrashekar flux *(compiler check, not in the
sources: compare with Observation 7; set the number of components $n_c$
(page-local) to 1 in his Eq. (24), with
$p/T=\rho r_{\mathrm g}$, page-local gas constant $r_{\mathrm g}$)*. He does not say under which
discrete conditions the property fails.

Their formulas and a structural comparison with the Coppola–Veldman
face-flux condition are on
[entropy-conservative and kinetic-energy-preserving two-point fluxes](/methods/entropy-conservative-flux.md).

As recalled by Rueda-Ramírez et al. (2022), Rueda-Ramírez & Gassner found
that split-form DGSEM with the Chandrashekar flux plus subcell finite-volume
blending is more stable on under-resolved turbulence with shocks than
standard DGSEM/FV, and needs less low-order blending (§4).

## Qualifications

- Coppola & Veldman's theory is for periodic 1D grids and the convective
  terms only. It is not an entropy analysis: "kinetic energy" there is the
  generalized quadratic $\tfrac12\rho\phi^2$.
- Edoh's statement that Div-rot is the only KEP splitting whose
  kinetic-energy flux does not average velocities from both sides of an
  interface is qualified "to the author's knowledge" (§3.2, Remark 4).
- Coppola & Veldman print a sign slip in their Eq. (6): the time derivative
  of $\tfrac12\rho\phi^2$ is $-\phi A\phi$, as their own Eqs. (4) and (59)
  give *(compiler check, not in the sources: re-derived from their
  Eqs. (1a,b))*.

# Citations

- [Coppola & Veldman (2023)](/sources/coppola-2023.md) — §2.1 Eqs. (4)–(6), §5.1 Eqs. (59)–(62), §5.2 Observation 7 Eqs. (64)–(71), §5.3 Eq. (72), Corollary A.4, §6 Observation 9 Eqs. (74)–(78), §7.3 Fig. 2, §8.1.
- [Ranocha et al. (2023)](/sources/ranocha-2023.md) — §2, §3.2.
- [Rueda-Ramírez, Pazner & Gassner (2022)](/sources/ruedaramirez-2022.md) — §2.1, §4.
- [Renac (2021)](/sources/renac-2021.md) — §3.1 Eq. (24), Remark 3.2 (arXiv v3).
- [Edoh (2022)](/sources/edoh-2022.md) — §3.1 Eqs. (11)–(18), Remark 3, Tables 1–2, §3.2 Eqs. (20)–(26), Remark 4, Table 3, §4, §4.1.1, Figs. 1, 3.
- [Abgrall, Öffner & Ranocha (2022)](/sources/abgrall-2022.md) — §3.3 Eqs. (38)–(42), Prop. 3.5, Remarks 3.4, 3.6, §4.2.2, App. A.3 (arXiv v4).
