---
type: Property
title: "Kinetic energy preservation"
description: "A semi-discretization is kinetic-energy-preserving when its convective terms neither create nor destroy discrete kinetic energy, which Coppola and Veldman reduce to the skew-symmetry of C − ½diag(d_mass); the page gives that criterion, face-flux conditions, the second-order barrier, SBP proofs including the rotational form, correction terms, and DG two-point fluxes."
status: established
aliases: [KEP, kinetic-energy-preserving, KEEP, kinetic energy conservation, energy-preserving discretization]
tags: [kinetic-energy-preserving, finite-volume, finite-difference, dg, multiphase, turbulence]
timestamp: 2026-10-23T23:30:00Z
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

[Jain & Moin (2022)](/sources/jain-2022.md) prove the same face-flux
conditions as sufficient conditions for a second-order collocated scheme
on a uniform grid, with $\overline a_{i+1/2}$ the two-point average and
$\hat C$, $\hat M$, $\hat K$ the mass, momentum and kinetic-energy face
fluxes (page-local):

- **Theorem 3.1 (global).** Total kinetic energy is conserved by the
  convective terms if $\hat M_{i+1/2}=\hat C_{i+1/2}\,\overline v_{i+1/2}$
  (Eq. (43)).
- **Theorem 3.2 (local).** It is preserved locally if, in addition, the
  kinetic-energy flux is $\hat K_{i+1/2}=\hat C_{i+1/2}\,\tfrac12v_iv_{i+1}$
  (Eq. (50)).

These are Coppola & Veldman's momentum flux and kinetic-energy flux
*(compiler check, not in the sources: Jain & Moin do not cite Coppola &
Veldman 2023; they compare their condition with Jameson's KEP flux)*. Jain
& Moin extend both conditions to the interface-regularization fluxes of a
diffuse-interface two-phase model: the regularization momentum and
kinetic-energy fluxes must be the regularization mass flux times
$\overline v$ and times $\tfrac12v_iv_{i+1}$ (Eqs. (44), (51)). With
pressure, the pressure flux $\hat P$ and the pressure-work flux $\hat W$
(page-local) must satisfy the discrete product rule
$\hat P_{i+1/2}\overline v_{i+1/2}+p_i\overline v_{i+1/2}=\hat W_{i+1/2}$,
an idea they take from Kok and Kuya et al. (§3.3); their choice
$\hat P=\overline p$, $\hat W=\tfrac12(v_{i+1}p_i+v_ip_{i+1})$ meets it
(Eq. (58)). Each condition fails in their two-phase Taylor–Green vortex
when violated: an inconsistent momentum flux, a kinetic-energy flux with
face values $\tfrac12v_{i+1/2}^2$, or an inconsistent regularization
kinetic-energy flux each make the run diverge (App. D, Fig. 14).

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

## Induced equations and the energy variable

[De Michele & Coppola (2023a)](/sources/demichele-2023.md) define the
property through the induced equation: with
$\partial_t(\rho\phi)=-C_{\rho\phi}-P_{\rho\phi}$ and $\mathcal M=C_\rho$
(page-local convective and pressure terms), a scheme is KEP when
$C_{\rho\phi^2/2}=\phi\,C_{\rho\phi}-\tfrac12\phi^2\mathcal M$ is in conservation
form; the definition constrains only $C_{\rho\phi}$ and $\mathcal M$, the
pressure term being a central gradient (§3.1, Eqs. (10)–(11)). Their results
agree with the Coppola–Veldman criterion above and add three points:

- **Proof tools.** Central derivatives on periodic uniform meshes satisfy
  summation by parts but not the discrete product rule; global
  conservation for the $\zeta$ family follows from SBP and the
  skew-symmetry of the derivative matrix, which they identify with
  Veldman's Requirement 3.1 (§2.2, §3.2, Eqs. (17)–(19)).
- **Local flux.** In second-order flux form the induced kinetic-energy
  flux is $\tfrac12\phi_i\phi_{i+1}m_{i+1/2}$, the flux of Observation 7 above,
  and the weight of the family may vary from face to face without losing
  local conservation (§3.3–3.4, Eqs. (26)–(28);
  [split convective forms](/methods/split-convective-forms.md)). Applied to
  $G=\tfrac12\rho v_\alpha^2$, their induced-equation formula shows that each
  velocity component's kinetic energy is preserved separately (Eq. (31)).
- **KEP of the energy variable.** Using the KEP splitting also for the
  energy equation, so that $\rho E^2$, $\rho e^2$ or $\rho s^2$ are
  conserved, is the customary choice for total energy; they call it
  "exotic" and "not necessarily the best option". Preserving the square
  root instead, $\rho\sqrt e\propto\rho c$, gives similar robustness, and the
  internal-energy and entropy forms with the Kennedy–Gruber–Pirozzoli split
  are the most robust in their isentropic-vortex and Taylor–Green tests
  (§4.2, §5, §6, Table 3). A KEP internal-energy splitting cannot be
  [pressure-equilibrium preserving](/properties/pressure-equilibrium-preservation.md)
  (§4.2.2).

The same authors' later note, [De Michele & Coppola (2023b)](/sources/demichele-2023-b.md),
restates the two-point condition: a second-order two-point flux is KEP iff
the momentum flux is the mass flux times the arithmetic mean of the
velocity, $f_{\rho v}=f_\rho\{\!\{v\}\!\}$, also on non-uniform and
non-Cartesian meshes, and the induced kinetic-energy flux is
$\tfrac12f_\rho v_iv_{i+1}$ (§2, citing Veldman and Coppola & Veldman;
arXiv v2). Every flux of their asymptotically entropy-conservative family
has this form ([entropy-conservative fluxes](/methods/entropy-conservative-flux.md)).
They read the choice of the internal-energy flux through the induced
equations, consistently with the "KEP of the energy variable" point above:

- the arithmetic-mean flux $f_{\rho e}=f_\rho\{\!\{e\}\!\}$ (the KEEP scheme of
  Kuya et al., KGP($\rho e$)) makes the induced equation for $\rho e^2$
  conservative;
- the geometric-mean flux $f_{\rho e}=f_\rho\sqrt{e_ie_{i+1}}$ is a KEP
  discretization of the equation for $\rho\sqrt e$, inspired by Kok's
  sound-speed equation, and makes the balance of $\rho\sqrt e$
  conservative; the two are "dual" (§2, Eqs. (3)–(4)).

Neither is pressure-equilibrium preserving, and the arithmetic-mean flux
diverges at $t\approx22$ on their density-wave test while Aρ-He (harmonic
mean of $e$) and Gρ-Ge (geometric means of $\rho$ and $e$), both
pressure-equilibrium preserving, run to $t=100$ (§5, Fig. 1a).

## Summation-by-parts proofs and the rotational form

[Edoh (2022)](/sources/edoh-2022.md) proves kinetic-energy preservation of
split forms with diagonal-norm finite-difference
[summation-by-parts operators](/operators/summation-by-parts-operator.md):
the convective contribution to the discrete kinetic-energy balance
collapses to a boundary flux by $Q+Q^\top=B$ and the commutation of the
diagonal norm with diagonal data matrices (Eqs. (11)–(12), (22)–(24)).
Edoh's results (§3, Tables 1–3):

- **Incompressible.** The Morinishi (skew-symmetric) splitting, the author's
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

Edoh's tests show the practical side. Without filtering, Div-rot is more
robust than the divergence form but more prone to aliasing than the
Feiereisen and Kennedy–Gruber splittings on the isentropic vortex; on the
Taylor–Green vortex at $\mathrm{Re}=1600$ both Kennedy–Gruber and Div-rot
run severely under-resolved grids on which the divergence form fails
(§4, Figs. 1, 3).

## Kinetic energy and entropy in two-phase flows (KEEP)

Jain & Moin (2022) call a scheme KEEP when it preserves kinetic energy
exactly and entropy approximately, the entropy being the physical entropy
of each phase, not a Tadmor-type entropy (§1, §3). They state, after
Honein (2005) as recalled, that kinetic-energy conservation suffices for
stability in incompressible flow but not in compressible flow, where
entropy must also be controlled, and that for two-phase flows the
interface-equilibrium condition is a further requirement: uniform
velocity and pressure must stay uniform (Lemma 3.1;
[entropy stability](/properties/entropy-stability.md)). Their tests, all
inviscid, at $64^3$ (Taylor–Green vortex with a slab of a second fluid)
and $32^3$ (isotropic turbulence), with classical RK4 at CFL about 0.65:

- **Single phase.** All three internal-energy fluxes tested, their
  quadratic split, the Kennedy–Gruber/Kuya cubic split and Chandrashekar's
  harmonic-mean variant, conserve kinetic energy and are stable at initial
  Mach numbers 0.05 and 0.2, so the KEEP scheme "is not unique" (§4.1.1,
  Figs. 2–3).
- **Two phases, density ratio 10.** Only the quadratic split is stable;
  the other two cause "spurious mixing of internal energy at the
  interface" and diverge, in the Taylor–Green vortex and in isotropic
  turbulence (§4.1.2, §4.2, Figs. 4–5, 8).
- **Density ratio 1000.** The proposed scheme stays stable at initial
  Mach numbers 0.05, 0.2 and 0.4 up to $Mt=100$; the drift of kinetic
  energy at the larger Mach numbers is attributed to reversible pressure
  work (Fig. 7).

A $256^3$ droplet-laden decaying isotropic turbulence with density ratios
1–1000 reproduces the trends of incompressible reference data (§5).
The face fluxes of the scheme are on
[split convective forms](/methods/split-convective-forms.md) and
[entropy-conservative and kinetic-energy-preserving two-point fluxes](/methods/entropy-conservative-flux.md).

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
the Coppola–Veldman face-flux condition above, and for one component Renac's
flux reduces to the Chandrashekar flux *(compiler check, not in the
sources: compare with Observation 7; set the number of components $n_c$
(page-local) to 1 in Renac's Eq. (24), with
$p/T=\rho r_{\mathrm g}$, page-local gas constant $r_{\mathrm g}$)*. Renac does not say under which
discrete conditions the property fails.

Their formulas and a structural comparison with the Coppola–Veldman
face-flux condition are on
[entropy-conservative and kinetic-energy-preserving two-point fluxes](/methods/entropy-conservative-flux.md).

As recalled by Rueda-Ramírez et al. (2022), Rueda-Ramírez & Gassner found
that split-form DGSEM with the Chandrashekar flux plus subcell finite-volume
blending is more stable on under-resolved turbulence with shocks than
standard DGSEM/FV, and needs less low-order blending (§4).

## KEP fluxes inside shock-capturing hybrids

Two sources use a KEP central flux where the flow is smooth and switch in
dissipation elsewhere, so the full scheme is KEP only where the switch is
off:

- **Eight-point skew-symmetric flux with TENO.**
  [Liang & Fu (2024b)](/sources/liang-2024-b.md) take the Kennedy–Gruber
  triple-average two-point flux in Pirozzoli's high-order conservative form
  with dispersion-optimized sixth-order coefficients, and replace it by a
  characteristic-wise eight-point [TENO](/methods/targeted-eno.md) flux
  where a TENO-type indicator flags the stencil (§2.3, §3.1–3.2;
  [split convective forms](/methods/split-convective-forms.md),
  [hybrid schemes](/methods/hybrid-weno.md)). Its mass flux is
  $\overline\rho\,\overline v$ and its momentum flux
  $\overline\rho\,\overline v\,\overline v$ for every pair of the sum (Eq.
  (30)), i.e. mass flux times the arithmetic mean velocity, so each
  two-point term meets the face-flux condition above whatever the central
  weights *(compiler check, not in the sources)*. On the inviscid
  [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) at $64^3$ to
  $t=100$ the hybrid keeps the total kinetic energy, to plotting accuracy,
  while WENO-CU6, TENO6 and TENO8 dissipate it after $t\approx5$ (§4.10,
  Figs. 17–18). The authors attribute this to the "non-dissipative"
  skew-symmetric branch; the time integrator is SSP-RK3 at CFL 0.4 (§4).
- **KEP central flux with switched AUSM dissipation on unstructured
  meshes.** [Duronio & Di Mascio (2024)](/sources/duronio-2024.md) extend an
  OpenFOAM solver of Modesti & Pirozzoli to multi-species ideal and real
  gases. The convective face flux is Pirozzoli's triple product
  $\tfrac18(\rho_O+\rho_N)(\tilde q_O+\tilde q_N)(v_O+v_N)\cdot n$ between the
  owner and neighbour cell centres (page-local $O$, $N$ and transported
  vector $\tilde q=(1,v,H,Y_k)$), which they state preserves total kinetic
  energy semi-discretely, "as proved" by Pirozzoli, giving "strong nonlinear
  stability" (§2, Eq. (6)). AUSM$^+$-up dissipation is added to the
  convective part where a compression-only
  [Ducros-type sensor](/definitions/ducros-shock-sensor.md) exceeds 0.05
  (Eqs. (7)–(8)). They recall that earlier low-diffusion variants of
  OpenFOAM's central solver do not guarantee discrete kinetic-energy
  conservation (§1). The paper runs no kinetic-energy test.

## Qualifications

- Duronio & Di Mascio print the pressure dissipation
  $\mathbf F^D_p=I_P\mathbf F^{\mathrm{AUSM}}_p$ without the sensor factor
  that multiplies the convective dissipation (Eq. (8)); read as printed it
  acts everywhere, so the scheme as run would not be KEP even where the
  sensor is off *(compiler check, not in the sources)*. The species
  components extend the transported vector but leave mass and momentum
  fluxes, hence the kinetic-energy argument, unchanged.
- Liang & Fu's kinetic-energy conservation in the inviscid Taylor–Green
  vortex is shown as a plotted curve; their Eq. (30) and Algorithm 1 write
  the energy flux differently (see
  [split convective forms](/methods/split-convective-forms.md)), which does
  not affect the mass and momentum fluxes that the KEP property involves.
- Coppola & Veldman's theory is for periodic 1D grids and the convective
  terms only. It is not an entropy analysis: "kinetic energy" there is the
  generalized quadratic $\tfrac12\rho\phi^2$.
- Edoh's statement that Div-rot is the only KEP splitting whose
  kinetic-energy flux does not average velocities from both sides of an
  interface is qualified "to the author's knowledge" (§3.2, Remark 4).
- Jain & Moin's conservation statements exclude pressure work,
  viscosity, thermal diffusion and time-discretization errors (abstract,
  §6); "exact" kinetic-energy conservation refers to the convective
  terms. Their stability evidence is inviscid, shock-free and at Mach
  numbers up to 0.4.
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
- [Jain & Moin (2022)](/sources/jain-2022.md) — §1, §3.2 Thms. 3.1–3.2 Eqs. (43)–(52), §3.3 Lemma 3.1, §3.5 Eq. (58), §4.1–4.2 Figs. 2–8, §5, §6, App. D Fig. 14 (arXiv v1).
- [De Michele & Coppola (2023a)](/sources/demichele-2023.md) — §2.2, §3.1–3.4 Eqs. (10)–(28), §4.1 Eq. (31), §4.2, §4.2.2, §5, §6, Table 3 (arXiv v1).
- [De Michele & Coppola (2023b)](/sources/demichele-2023-b.md) — §2 Eqs. (2)–(4), §5 Fig. 1 (arXiv v2).
- [Liang & Fu (2024b)](/sources/liang-2024-b.md) — §2.3 Eqs. (25)–(30), §3.1–3.2 Algorithm 1, §4, §4.10 Figs. 17–18.
- [Duronio & Di Mascio (2024)](/sources/duronio-2024.md) — §1, §2 Eqs. (4)–(8).
