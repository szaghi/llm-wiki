---
type: Source
title: "Taheri et al. (2022) — Time-discretization of a plasma-neutral MHD model with a semi-implicit leapfrog algorithm"
description: "Compares Crank–Nicolson (linearized and Jacobian-free Newton–Krylov) and Strang-split (per-field, and interleaved into the leapfrog with a Douglas–Rachford-inspired coupling source) treatments of ionization, recombination and charge exchange in NIMROD's semi-implicit leapfrog on 0D and 1D tests, finding that the leapfrog-interleaved splitting matches CN-JFNK accuracy at about one third of its cost."
resource: "doi:10.1016/j.cpc.2022.108288"
source_kind: paper
authors: [Taheri S., King J.R., Shumlak U.]
year: 2022
venue: "Comput. Phys. Commun. 274:108288"
local_file: "/home/stefano/papers/mosaic/fusion-mhd-simulation/2022_Crossref_Computer_Physics_Communications_Taheri_Time-discretization_of_a_plasma-neutral_MHD_model_with_a_sem.pdf"
tags: [mhd, neutrals, time-integration, finite-elements, spectral, edge, verification, numerics]
timestamp: 2026-10-16T16:51:00Z
---

# Summary

The paper adds the Meier–Shumlak single-species hydrogenic plasma–neutral
model (electron-impact ionization, radiative recombination, resonant charge
exchange; separate neutral continuity, momentum and temperature equations)
to [NIMROD](/software/nimrod.md) and asks how to fit its atomic source terms
into NIMROD's mixed implicit/[semi-implicit leapfrog](/methods/semi-implicit-leapfrog.md).
In the leapfrog the velocity is staggered against $(n,T,\mathbf B)$, which are
advanced one after another; temperature-dependent rate coefficients in the
density equation and relative-velocity terms in the energy equations break
that dependency structure. Four schemes are compared:
(i) CN-linear, Crank–Nicolson centring of the linearized atomic terms inside
each field solve; (ii) CN-JFNK, the same plus an approximate Jacobian-free
Newton–Krylov iteration on the nonlinear remainder, which also carries the
inter-species velocity coupling; (iii) SS-field, per-field Strang splitting
(ODE half-step with lsode, unchanged PDE advance, ODE half-step); and (iv)
SS-leapfrog+DR, full-system ODE half-steps interleaved into the leapfrog with
a limited Douglas–Rachford-inspired coupling source added to the ODE step and
subtracted from the PDE step. Errors are classified as nonlinear, CN
centring, "T-in-n", field staggering, and ODE/PDE splitting
([operator splitting of atomic sources](/methods/operator-splitting-of-atomic-sources.md)).
Tests: four 0D cases and two 1D cases (neutral expansion into a fixed tokamak
pedestal; a planar snowplow plasma accelerator). SS-field shows a large
$\Delta t$-dependent splitting error in the pedestal steady state;
SS-leapfrog+DR matches or beats CN-JFNK, which costs about 3 times SS-field.
There is no formal stability analysis; the second-order claim for
SS-leapfrog+DR is asserted without derivation.

# Key claims

1. **Leapfrog dependency structure** (§3, p. 4). Without atomic physics the
   single-fluid dependencies are $n(\mathbf v)$, $\mathbf v(n,\mathbf B,T)$, $T(n,\mathbf v)$, $\mathbf B(\mathbf v)$,
   which allows $\mathbf v$ to be staggered and the other fields to be solved in
   sequence. Stated (attributed to Sovinec et al.).
2. **Semi-implicit operator is essential** (§3, p. 4; Eqs. 44–45) to stabilize
   wave propagation in the leapfrog (Schnack et al. 1987); the ideal-MHD force
   operator "limits spectral-pollution time-discretization error" (Lütjens &
   Luciani 1996); a staggered neutral species likewise needs a sound-wave
   operator. Stated.
3. **Centring** (§3.1, p. 5). $\theta_{\mathrm t}=1/2$ for advection "is required to
   maintain numerical stability" (Sovinec & King 2010). Stated; no proof here.
4. **T-in-n error** (§3.1 p. 6; §3.5). Temperature-dependent rate coefficients
   centred explicitly in the density advance produce an error named here.
   Stated and shown in 0D.
5. **CN-linear is not robust** (§5, p. 15): it "can give spurious results at
   large time-step sizes" in 1D and is dropped there, consistent with Knoll et
   al. (2007) on linear-implicit versus implicitly balanced schemes. Stated; no
   1D CN-linear results shown.
6. **Second order of SS-leapfrog+DR** "regardless of the choice" of the
   coupling source (§3.4, p. 8). Stated ("Analysis shows…"), no analysis
   given.
7. **0D reduction** (§4, p. 11). In 0D SS-leapfrog+DR is an adaptive ODE
   integration of the whole system with error at the solver tolerance
   ($10^{-12}$), so it is left out of the 0D tests. Stated.
8. **Error decomposition in 0D** (Fig. 4a, §4.1). CN-linear − CN-JFNK = nonlinear
   error; CN-JFNK − SS-field = CN centring error; SS-field − tolerance = T-in-n
   error; "not strictly additive". Shown.
9. **Tokamak edge** (Fig. 4c,d). Dropping the nonlinear terms errs at every
   $\Delta t$; beyond a cost "tipping point" CN-JFNK beats CN-linear in accuracy
   per cost. Shown.
10. **Nonlinear ionization** (Fig. 4e,f, §4.3). CN-linear is most accurate by a
    "fortuitous" cancellation of its overshoot against the T-in-n error.
    Shown.
11. **Flow relaxation** (Fig. 4g, §4.4). Field staggering dominates; T-in-n and
    CN errors are negligible. Shown.
12. **Pedestal steady state** (Figs. 6a–c, 7; §5.1.1). The SS-field steady state
    depends on $\Delta t$ (ODE/PDE splitting error, cf. LeVeque 2002) and
    underestimates the neutral flux; CN-JFNK and SS-leapfrog+DR agree, errors
    about $10^{-8}$–$10^{-6}$ against about $10^{-2}$ for SS-field. Shown.
13. **Cost** (§5.1.1, p. 16; 40 × 4 bi-quintic elements). CN-JFNK about 3 ×
    SS-field wall clock at equal $\Delta t$; SS-field about 10% slower than
    SS-leapfrog+DR. GMRES counts are a poor cost proxy in 1D because of
    periodic matrix refactorization. Shown (numbers in text, no table).
14. **Snowplow** (Fig. 11, §5.2). All methods share an error at large $\Delta t$,
    "likely from the PDE Crank-Nicolson and leapfrog discretization itself";
    at small $\Delta t$ the splitting error flattens SS-field's convergence.
    Shown; attribution inferred.
15. **Robustness** (§6). Strang-split methods are more robust; some snowplow
    permutations failed to converge with CN-JFNK, "potentially because our
    JFNK is approximate". Stated.
16. **Decoupling** (§3.3, §6). Splitting decouples the species in the global
    solves (smaller systems, less fill-in, possible species parallelism, "not
    presently explored"). Stated.

# Models and numerics

**Model** (Eqs. 1–6, 18), resistive MHD plus a hydrogenic neutral fluid,
quasi-neutral ($n_e=n_i$), no displacement current, no electron–neutral or
elastic neutral–ion scattering; NIMROD's extended Ohm's law is not used:

$$\begin{aligned}
&\partial_tn_i+\nabla\cdot(n_i\mathbf v)=\mathcal R_{\mathrm{ion}}-\mathcal R_{\mathrm{rec}},\qquad \partial_tn_{\mathrm N}+\nabla\cdot(n_{\mathrm N}\mathbf v_{\mathrm N})=\mathcal R_{\mathrm{rec}}-\mathcal R_{\mathrm{ion}},\\
&m_in_i(\partial_t+\mathbf v\cdot\nabla)\mathbf v=\mathbf J\times\mathbf B-\nabla p-\nabla\cdot\mathsf\Pi+\mathbf f_{\mathrm{cx}}+m_i(\mathcal R_{\mathrm{ion}}+\mathcal R_{\mathrm{cx}})(\mathbf v_{\mathrm N}-\mathbf v),\\
&m_in_{\mathrm N}(\partial_t+\mathbf v_{\mathrm N}\cdot\nabla)\mathbf v_{\mathrm N}=-\nabla p_{\mathrm N}-\nabla\cdot\mathsf\Pi_{\mathrm N}-\mathbf f_{\mathrm{cx}}+m_i(\mathcal R_{\mathrm{rec}}+\mathcal R_{\mathrm{cx}})(\mathbf v-\mathbf v_{\mathrm N}),\\
&\partial_t\mathbf B=-\nabla\times(\eta\mathbf J-\mathbf v\times\mathbf B),\qquad\mu_0\mathbf J=\nabla\times\mathbf B,
\end{aligned}$$

with ionization, recombination and charge-exchange rate densities
$\mathcal R_{\mathrm{ion}}=\langle\sigma v\rangle_{\mathrm{ion}} n_in_{\mathrm N}$, $\mathcal R_{\mathrm{rec}}=\langle\sigma v\rangle_{\mathrm{rec}} n_i^2$,
$\mathcal R_{\mathrm{cx}}=\sigma_{\mathrm{cx}}n_in_{\mathrm N}\sqrt{\tfrac4\pi(v_{th,i}^2+v_{th,\mathrm N}^2)+|\mathbf v-\mathbf v_{\mathrm N}|^2}$, and
$\mathbf f_{\mathrm{cx}}$ the net charge-exchange friction (Eqs. 10–11, both
$\propto\sigma_{\mathrm{cx}}n_in_{\mathrm N}(\mathbf v-\mathbf v_{\mathrm N})$). The plasma and neutral temperature
equations (Eqs. 5–6) carry compression, conduction, atomic heat exchange
($\tfrac32T_{\mathrm N}\mathcal R_{\mathrm{ion}}$, $\tfrac32T_i\mathcal R_{\mathrm{rec}}$, charge-exchange terms), the radiative loss
(ionization energy times $\mathcal R_{\mathrm{ion}}$), particle-exchange terms and the frictional
heating $\tfrac{m_i}2(\cdot)|\mathbf v-\mathbf v_{\mathrm N}|^2$; prefactor $n/(\Gamma-1)$. Rate
coefficients come from DEGAS2 tables (bi-cubic spline). Isotropic closures:
$\mathsf\Pi=-m_in\nu[\nabla\mathbf v+\nabla\mathbf v^T-\tfrac23\mathsf I\nabla\cdot\mathbf v]$, $\mathbf q=-\kappa\nabla T$. See
[fluid neutral models](/methods/fluid-neutral-models.md).

**Discretization.** NIMROD: 2D nodal spectral (C⁰ Lagrange) elements, bi-quintic
in the tests, times a 1D Fourier direction. The 1D tests use a radial slab
(pedestal) and an axial coordinate (snowplow); no toroidal geometry is
exercised.

**Leapfrog** (§3, Fig. 1). $\mathbf v$, $\mathbf v_{\mathrm N}$ at integer levels; $n_i$, $n_{\mathrm N}$,
$T$, $T_{\mathrm N}$, $\mathbf B$ at half-integer levels. Per step: (1) $\Delta\mathbf v$ and
$\Delta\mathbf v_{\mathrm N}$, solved separately; (2) $[\Delta n_i,\Delta n_{\mathrm N}]$ together; (3)
$[\Delta T,\Delta T_{\mathrm N}]$ together; (4) $\Delta\mathbf B$. This is the mixed
implicit/semi-implicit leapfrog of Sovinec & King (2010); NIMROD's
predictor–corrector variants are not treated.

**Semi-implicit operators** (App. A, Eqs. 44–45). The plasma velocity advance
contains $(m_in-\Delta t^2\mathcal L_{\mathrm{si}})\Delta\mathbf v/\Delta t$ with

$$\mathcal L_{\mathrm{si}}(\Delta\mathbf v)=C_0\Big\{\tfrac1{\mu_0}[\nabla\times\nabla\times(\Delta\mathbf v\times\mathbf B)]\times\mathbf B+\mathbf J\times\nabla\times(\Delta\mathbf v\times\mathbf B)+\nabla\big(\Delta\mathbf v\cdot\nabla p+\tfrac53p\nabla\cdot\Delta\mathbf v\big)\Big\}+C_1p_{\mathrm{nl}}\nabla^2\Delta\mathbf v,$$

the ideal-MHD force operator plus an isotropic Laplacian scaled by a
"nonlinear pressure" $p_{\mathrm{nl}}$; the neutral operator keeps only the
sound-wave part. No values of $C_0$, $C_1$ or $p_{\mathrm{nl}}$ are given.

**Density advance** (Eqs. 19–21). Crank–Nicolson ($\theta_{\mathrm t}=1/2$) for
hyperbolic and atomic terms; each rate is expanded as start-of-step value +
$\theta_{\mathrm t}$ × linear part + nonlinear remainder, the rate-coefficient
derivative left in the remainder ("the functional form of the cross section
may not be known a priori").

**CN-JFNK** (§3.2, Eqs. 22–26). For $\mathrm dx/\mathrm dt=g(x)$, solve
$\Delta x-\Delta t[g(x^n)+\tfrac12\Delta x\,g'(x^n)+g_{\mathrm{nl}}(x^n,\Delta x)]=0$ with
$g_{\mathrm{nl}}=g(x^n+\tfrac12\Delta x)-g(x^n)-\tfrac12\Delta x\,g'(x^n)$, i.e. the implicit-midpoint
form. Newton iterates with a finite-difference Jacobian of $g_{\mathrm{nl}}$
(increment $\epsilon\Delta x$), relative-residual stopping, a dynamic positivity floor
on $n$ and $T$, and under-relaxation; GMRES for the linear solves. The two
species' velocities are still solved separately; their coupling is centred
through the Newton iteration.

**SS-field** (§3.3, Eq. 27). For each field separately: ODE half-step (local
atomic rates, lsode/Adams), PDE full step (transport, unchanged), ODE
half-step. Keeps the T-in-n error.

**SS-leapfrog+DR** (§3.4, Eqs. 30–35). $\mathrm d\mathbf u/\mathrm dt=\mathcal A_1(\mathbf u)+\mathcal A_2(\mathbf u)$, with
$\mathcal A_1$ the local nonlinear atomic physics and $\mathcal A_2$ the linearized fluid
system. Strang sequence ODE($\Delta t/2$) – PDE($\Delta t$) – ODE($\Delta t/2$) on the full
state, the ODE step solving $\mathcal A_1+\mathbf u_0'$ and the PDE step $\mathcal A_2-\mathbf u_0'$, with
the coupling source $\mathbf u_0'$ designed to vanish when the ODE and PDE tendencies
have the same sign and limited to the smaller magnitude (Eq. 34; see
Citations for the printed form). $\mathcal A_2$ is lagged from the previous step to
avoid an extra mass-matrix solve for second derivatives in C⁰ elements
(Eq. 35). The half-steps are interleaved with the staggered velocity and
$(n,T,\mathbf B)$ advances (Fig. 3).

**Error metric** (Eq. 36): mean relative error over fields and 10 output
times. **Cost proxy**: total GMRES iterations (0D), wall clock (1D); codes "not
optimized"; no parallel or GPU data.

# Tests and results

| Case (0D) | Initial plasma / neutral | $t_{\mathrm{end}}$ | Finding |
|---|---|---|---|
| Tokamak core (Tab. 1) | $10^{20}$ m⁻³, 1241.7 eV / $10^{16}$, 1.2417 eV | $2\times10^{-7}$ s | three separated error levels: SS-field ≈ $10^{-7}$–$10^{-6}$, CN-JFNK ≈ $10^{-7}$–$5\times10^{-4}$, CN-linear ≈ $10^{-4}$–$3\times10^{-3}$ |
| Tokamak edge (Tab. 2) | $10^{17}$, 2.4834 / $10^{20}$, 0.025 | $2\times10^{-6}$ s | nonlinear error at every $\Delta t$; cost tipping point |
| Nonlinear ionization (Tab. 3) | $10^{20}$, 2.4834 / $10^{20}$, 2.4834 | $2\times10^{-5}$ s | CN-linear best by fortuitous cancellation |
| Flow relaxation (Tab. 4) | $10^{19}$, 1.2417, $10^4$ m/s / $1.492\times10^{19}$, 1.2417, 0 | $10^{-5}$ s | field staggering dominates |

In 0D the ionization energy loss is ignored so energy is conserved; all runs
end before equilibrium; references use a fine $\Delta t$.

**1D pedestal** (§5.1). Frozen plasma profiles; neutrals start at local
ionization–recombination balance and are fed through a thin diffusive layer
with a Dirichlet density condition at the wall (0.8 m from the core);
neutral viscous and thermal diffusivities 0.1 and 0.01 m² s⁻¹ at
$10^{19}$ m⁻³. Neutral flux down to about $-2.4\times10^{18}$ m⁻² s⁻¹. Steady state:
SS-field strongly $\Delta t$-dependent, flux underestimated; SS-leapfrog+DR more
accurate than CN-JFNK below $\Delta t\approx5\times10^{-7}$ s. Dynamics: both split
schemes underpredict the core-penetration speed, SS-field much more;
SS-leapfrog+DR error about $10^{-6}$ at $\Delta t=5\times10^{-8}$ s, SS-field about
$10^{-2}$.

**1D snowplow** (§5.2). Acceleration region of a sheared-flow-stabilized
Z-pinch: background plasma $10^{19}$ m⁻³, neutral slug $10^{21}$ m⁻³ near
0.3–0.5 m, boundary field ramped to 0.02 T in 10 µs, Braginskii (plasma) and
Sutherland (neutral) transport, Dirichlet field and zero-Neumann density and
velocity boundaries; to 20 µs at $\Delta t=10^{-8}$ s. All methods agree
qualitatively; convergence (reference $\Delta t=10^{-10}$ s) as in Key claim 14.

No code-to-code comparison: all comparisons are among the four NIMROD
schemes.

# Notation map

| Taheri et al. (2022) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $n$, $n_n$ | $n_i$ ($=n_e$), $n_{\mathrm N}$ | |
| $\mathbf V$, $\mathbf V_n$ | $\mathbf v$, $\mathbf v_{\mathrm N}$ | |
| $T$ ($T_i$ in Eqs. 9–15), $T_n$ | $T$, $T_i$, $T_{\mathrm N}$ | single plasma temperature |
| $m$ | $m_i$ | hydrogenic, $=$ neutral mass |
| $p$, $p_n$ | $p$, $p_{\mathrm N}$ | relation to $nT$ not stated |
| $\Gamma$ | $\Gamma$ | ratio of specific heats |
| $\Gamma^{ion}$, $\Gamma^{rec}$, $\Gamma^{cx}$ | $\mathcal R_{\mathrm{ion}}$, $\mathcal R_{\mathrm{rec}}$, $\mathcal R_{\mathrm{cx}}$ | **collision:** native rates share the symbol of the adiabatic index $\Gamma$ |
| $\langle\sigma_{ion}v\rangle$, $\langle\sigma_{rec}v\rangle$, $\sigma_{cx}$ | $\langle\sigma v\rangle_{\mathrm{ion}}$, $\langle\sigma v\rangle_{\mathrm{rec}}$, $\sigma_{\mathrm{cx}}$ (cross-section, page-local) | $v$ inside the brackets is a particle speed |
| $\mathbf R^{cx}_{in}$, $\mathbf R^{cx}_{ni}$ | $\mathbf f_{\mathrm{cx}}$ (net, page-local) | |
| $Q^{ion}$, $Q^{rec}$, $Q^{cx}$, $\phi_{ion}$ | words | **collision:** $\phi_{ion}$ vs toroidal angle $\phi$ |
| $v_{T*}^2=2T_*/m$ | $v_{th,s}^2$ | convention here $v_{th,s}^2=2T_s/m_i$ (factor 2, unlike §10's default) |
| $\underline\Pi_*$, $\chi_*$ | $\mathsf\Pi$, $\nu$ | **collision:** native $\chi$ is a viscous diffusivity; registry $\chi$ is the vacuum scalar potential |
| $\mathbf q_*$, $\kappa_*$ | $\mathbf q$, $\kappa$ | isotropic |
| $\mathbf B$, $\mathbf J$, $\eta$, $\mu_0$ | same | SI |
| $j$ (step label) | words | **collision:** registry $j$ is the reduced-MHD current |
| $\theta$, $\theta_v$, $\theta_{visc}$ | $\theta_{\mathrm t}$, words | $\theta_v$, $\theta_{visc}$ undefined in the paper |
| $\mathbf L$, $\mathbf L_n$, $C_0$, $C_1$, $p_{nl}$ | $\mathcal L_{\mathrm{si}}$ (page-local), $C_0$, $C_1$, $p_{\mathrm{nl}}$ | |
| $g$, $g'$, $g_{nl}$ | same | generic right-hand side |
| $\mathcal A_1$, $\mathcal A_2$, $\mathcal S_{ode}$, $\mathcal S_{pde}$ | same | operators of the splitting |
| $\mathbf u$, $\mathbf u_0'$ | $\mathbf u$, $\mathbf u_0'$ | registry $\mathbf u$ = discrete state |
| $\|\mathcal E\|_2$ | words | an $l^1$-type mean relative error |

# Pages created or updated

Chunk 1 (2026-10-16) created every page of the bundle; chunks 2 and 3 (2026-10-16) extended many. This source is cited on:

* [Bézier–Hermite finite elements with toroidal Fourier harmonics](/methods/bezier-finite-elements.md)
* [Divergence-free magnetic field](/properties/divergence-free-magnetic-field.md)
* [Fluid neutral models and plasma–neutral atomic sources](/methods/fluid-neutral-models.md)
* [NIMROD](/software/nimrod.md)
* [Operator splitting and Newton–Krylov treatment of atomic-physics sources](/methods/operator-splitting-of-atomic-sources.md)
* [Semi-implicit leapfrog](/methods/semi-implicit-leapfrog.md)
* [Single-fluid visco-resistive MHD model](/methods/visco-resistive-mhd-model.md)

# Citations

1. `/home/stefano/papers/mosaic/fusion-mhd-simulation/2022_Crossref_Computer_Physics_Communications_Taheri_Time-discretization_of_a_plasma-neutral_MHD_model_with_a_sem.pdf`
   * **Version.** arXiv:2110.02328v1 [physics.plasm-ph], 5 October 2021
     (page 1 dated 7 October 2021), 24 pp. (main text 19 pp., Appendix A pp.
     21–23, references pp. 23–24); not the publisher version, despite
     "Crossref" in the filename.
   * **Identity.** doi:10.1016/j.cpc.2022.108288, checked on Crossref: Comput.
     Phys. Commun. 274:108288, print issue May 2022; authors Taheri S., King J.R.,
     Shumlak U.
   * **How read.** Full text including Appendix A; Eqs. 19–20 (p. 5) and 37
     (p. 21) checked on rendered pages; plot values are approximate readings.
   * **Recorded as printed.**
     * Eq. 34 as typeset is identically zero: $|\mathcal A_2|/|\mathcal A_1|\ge0$, so
       $\max(-|\mathcal A_2|/|\mathcal A_1|,0)=0$ and $\mathbf u_0'\equiv0$. The stated intent (vanish
       for same-sign tendencies, limit to the lesser magnitude) needs a signed
       ratio. The CPC version should be checked.
     * "Second-order accurate in time regardless of the choice of $\mathbf u_0'$"
       (§3.4): "Analysis shows", none given.
     * ODE integrator named "lsode, with Adams methods" (§3.3), "time adaptive
       Adam-Bashforth" (Eq. 32, §3.5) and "multi-step ODE solver" (§6); lsode's
       Adams option is Adams–Moulton predictor–corrector.
     * §4 calls the 0D tests "optically thick" (ionization loss ignored),
       against the optically-thin assumption of §2.
     * §4.1 reference step printed "$\Delta t=2\times10^{12}$ s", for $2\times10^{-12}$ s.
     * Table 1: plasma $\Delta T=+0.1$ eV while the text describes dilution
       cooling. Compiler's check, not a source claim: with plasma internal
       energy $3n_iT$ a −0.1 eV change is nearly energy-conserving and +0.1 is
       not, and Tables 2–3 conserve energy within 1%; with $\tfrac32n_iT$, implied
       by the $n/(\Gamma-1)$ prefactor of Eq. 5, they do not. The paper never
       states $p$ versus $nT$.
     * Colour and marker descriptions in §4.1, §5.1 and §5.1.2 do not match
       Figs. 4, 5 and 6(d–f).
     * Eq. 38 left side prints $-\mathbf R^{cx}_{ni}(\cdot)+\mathbf R^{cx}_{ni}(\cdot)$, which
       cancels; by analogy with Eqs. 4 and 37 one term should be $\mathbf R^{cx}_{in}$.
     * Eqs. 39–40 (App. A) drop $\theta$ on the atomic linear terms and the $T$
       arguments, and use superscript $j+1$ where Eqs. 19–20 use $j+1/2$.
     * Undefined: $\theta_v$, $\theta_{visc}$, $\bar n$, $\bar n_n$, values of $C_0$,
       $C_1$, $p_{nl}$; $T$ and $T_i$ used interchangeably; Eq. 37 has a fixed $\tfrac12$
       on $\nabla\cdot\mathsf\Pi(\Delta\mathbf v)$.
     * Eq. 24 writes $\Delta x_k$, Eq. 26 $\Delta x^k$.
     * Eqs. 22–23 are called Crank–Nicolson but evaluate $g$ at the midpoint;
       equivalent only for linear $g$.
     * Eq. 36 is called an $l_2$ norm but $\sqrt{(\cdot)^2}=|\cdot|$; relative to the
       reference it is ill-defined for fields crossing zero (velocity in flow
       relaxation).
     * §5.2 prints identical plasma and neutral diffusivities (400 m² s⁻¹
       viscous, 500 m² s⁻¹ thermal) attributed to Braginskii and Sutherland
       respectively; resistivity "100µ0 Ω·m" has inconsistent units
       (presumably $\eta/\mu_0=100$ m² s⁻¹).
     * §5.1: the thin diffusive layer's parameters are not given.
     * Typos: abstract "that exploited by", "As the computationally cost",
       "tempearture" (Fig. 3), "pick" for peak (§5.2), "time-sidcretization"
       (Fig. 11), "Crank-Nicholson" (App. A title).
   * **Reference list.** 29 printed references, merged into the bibliography
     under `taheri-2022` (29 entries); no DOIs printed, none added. [27], the
     lsode reference, prints a garbled corporate author ("Livermore Nationai")
     and is `livermore-1993`. [29] is the unpublished King et al. 2021
     manuscript (`king-2021`). [16] (Braams, NET report 1987) has an incomplete
     author list. [21], [22] and [23] are cited as the HiFi, PSI-Tet and WARPXM
     code references but are application papers (spectral-element anisotropic
     conduction; HIT-SI injector dynamics).
