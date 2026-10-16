---
type: Source
title: "Wright & Ferraro (2024) — Investigating nonlinear magnetohydrodynamics in an optimized, reactor-scale quasi-axisymmetric stellarator"
description: "First nonlinear M3D-C1 simulations of a reactor-scale two-field-period quasi-axisymmetric stellarator optimized at β = 2.5% without a stability target: edge pressure-driven high-n modes destroy the flux surfaces within about 1500 Alfvén times for every resistivity model, only even toroidal harmonics are destabilized, and Spitzer resistivity gives a secondary nonlinear acceleration of growth."
resource: "doi:10.1063/5.0215594"
source_kind: paper
authors: [Wright A.M., Ferraro N.M.]
year: 2024
venue: "Phys. Plasmas 31:082509"
local_file: "/home/stefano/papers/mosaic/fusion-mhd-simulation/2024_Crossref_Physics_of_Plasmas_Wright_Investigating_nonlinear_magnetohydrodynamics_in_an_optimized.pdf"
tags: [mhd, full-mhd, stellarator, equilibrium, finite-elements]
timestamp: 2026-10-16T20:00:00Z
---

# Summary

A letter-length article applying the stellarator capability of
[M3D-C1](/software/m3d-c1.md) (Zhou et al. 2021) to the first nonlinear MHD
study of a reactor-scale [quasi-axisymmetric](/definitions/quasi-symmetry.md)
(QA) equilibrium with $N_{\mathrm{fp}}=2$, taken from Landreman, Buller &
Drevlak (2022, §VI C therein). The equilibrium was optimized with SIMSOPT for
$\beta=2.5\%$, quasi-symmetry, energetic-particle confinement and a
self-consistent [bootstrap current](/definitions/bootstrap-current.md), but not
for MHD stability. The model is single-fluid
[visco-resistive MHD](/methods/visco-resistive-mhd-model.md) with continuity
and anisotropic heat conduction ($\kappa_\perp/\kappa_\parallel=10^{-6}$,
perpendicular diffusivity 2.18 m² s⁻¹), dynamic viscosity
$3.65\times10^{-4}$ kg m⁻¹ s⁻¹, a conducting wall on the initial plasma
boundary and no imposed symmetry; 72 toroidal planes and $8.64\times10^5$
elements, about $4\times10^5$ CPU-h (14 days) per run. Four resistivity models
are compared: constant, and Spitzer scaled by 1, 10 and 100. High-$(m,n)$ modes
appear almost at once at the edge; a chaotic layer covers 5–10% of the minor
radius by about $500\tau_A$, about 25% by $800\tau_A$, and engulfs the core by
about $1500\tau_A\approx700$ µs (constant $\eta$). Temperature gradients
survive in the chaotic region because the relaxation time $a^2/\chi_\perp=1.33$
s is far longer. The evolution is qualitatively the same for every resistivity
model, which the authors read as ideal instability. Kinetic-energy growth
rates of the even harmonics $6\le n\le30$ are all positive, largest for
$20\le n\le28$; the restriction to even $n$ is explained by
[toroidal mode families](/definitions/toroidal-mode-family.md). With constant
$\eta$ the $n=30$ growth rate plateaus and decays toward saturation; with
Spitzer $\eta$ it accelerates a second time, interpreted as nonlinear drive.
The authors conclude that field periodicity and MHD stability should enter
stellarator optimization, and that linear predictions should be used with
caution.

# Key claims

1. **Stellarator M3D-C1** (§II). The code handles strongly shaped
   non-axisymmetric domains and has been compared with PIES (Zhou et al. 2021)
   and with W7-X sawtooth-like crashes ([Zhou et al. 2023](/sources/zhou-2023.md)).
   Attributed.
2. **Magnetic well on all surfaces** of the optimized QA by a posteriori
   analysis (§II). Stated; no figure or method.
3. **Alfvénic instability** (§III, Figs. 1, 6). The equilibrium is "highly
   unstable to multiple MHD modes that grow on Alfvénic timescales";
   high-$(m,n)$ modes appear "almost immediately near the plasma edge". Shown.
4. **Chaotic-layer growth** (§III, Figs. 1, 2, 6). 5–10% of $a$ within about
   $500\tau_A$, "nearly 25%" by about $800\tau_A$, until "the core is
   enveloped by a sea of chaotic magnetic fields". Shown (constant-$\eta$
   sequence $0\le t\le1425\tau_A$; Fig. 2 at $1500\tau_A$).
5. **Resistivity-independent evolution** (§III, §IV). "Qualitatively
   identical, regardless of resistivity model", which "is indicative of an
   ideally unstable plasma". Evolution Shown; the ideal character is
   inferred, with no ideal linear stability calculation.
6. **"Interchange-like pressure-driven"** edge instabilities (abstract, §IV).
   Stated; no mode-structure, Mercier or ballooning analysis
   ([interchange modes](/definitions/interchange-mode.md)).
7. **Core modes** $m=5$ and $m=3$ grow much more slowly and stay small (§III).
   Stated, not shown.
8. **"Internal in character"**, hence "unaffected by the boundary conditions
   chosen" (§III). Stated; no boundary-condition variation.
9. **Gradients persist in chaotic field** (§III, Fig. 1e–f). Relaxation time
   $a^2/\chi_\perp=1.33$ s ($a=1.704$ m) against $1500\tau_A\approx700$ µs,
   consistent with Reiman (2021). Derived (order of magnitude) and Shown. The
   break-up is "mechanistically distinct" from equilibrium pressure-driven
   stochastization. Stated.
10. **Even-$n$ spectrum** (§III, Figs. 3–4). All even $6\le n\le30$ have
    positive maximum growth rates, largest for $20\le n\le28$, about
    $(0.1$–$1.1)\times10^{-2}\tau_A^{-1}$ (Fig. 3; time traces to about
    $1.5\times10^{-2}\tau_A^{-1}$, Fig. 4); many modes start near
    $200\tau_A$. Shown. The rates are of the kinetic energy, i.e. twice the
    amplitude growth rate $\gamma$ (not stated by the paper).
11. **Mode coupling by field periodicity** (§III, §IV). A harmonic $n_0$
    couples to $n_0+lN_{\mathrm{fp}}$ for integer $l$; for
    $N_{\mathrm{fp}}=2$ "a single unstable eigenmode will be composed of
    numerous even-numbered toroidal Fourier modes, which is consistent with
    what is observed". Selection rule standard; consistency Shown; that a
    single eigenmode is responsible is asserted (no odd-$n$ data or eigenmode
    analysis shown).
12. **Constant versus Spitzer $\eta$ at $n=30$** (§III, Fig. 5; §IV).
    Constant: the growth rate rises, plateaus near $500\tau_A$
    ("characteristic of the linear growth phase") and falls toward zero near
    $700\tau_A$ ("tending toward nonlinear saturation"). Spitzer (×1, ×10,
    ×100): no plateau, a slowing then "a significant increase" before peaking,
    "suggestive of strong nonlinear interactions, which are accelerating the
    growth". Curves Shown; interpretation Stated; energy-transfer analysis
    left to future work.
13. **Linear predictions and optimization** (§I, §III, §IV). "Proceed with
    caution when using linear approximations to predict nonlinear MHD
    behavior in stellarators"; "field-periodicity plays an important role in
    nonlinear MHD stability"; MHD stability is "at least as important a
    target for optimization" for finite-$\beta$ QA equilibria. Stated
    (conclusion from claims 3–12).
14. **Viscosity** about 100 times experimental "does not negatively impact the
    simulations", since it damps high-$(m,n)$ modes; convergence studies
    "were performed" (§II). Stated, not shown.

# Models and numerics

**Equations** (App. A, reproduced from Jardin et al. 2012; checked on the
rendered page), in registry notation:

$$\begin{aligned}
&\partial_tn_i+\nabla\cdot(n_i\mathbf v)=0,\\
&n_im_i(\partial_t\mathbf v+\mathbf v\cdot\nabla\mathbf v)=\mathbf J\times\mathbf B-\nabla p-\nabla\cdot\mathsf\Pi+\mathbf S_{\mathbf v},\\
&\partial_tp+\mathbf v\cdot\nabla p+\Gamma p\nabla\cdot\mathbf v=(\Gamma-1)\big[S_p-\nabla\cdot\mathbf q_T+\eta J^2-\mathbf v\cdot\mathbf S_{\mathbf v}-\mathsf\Pi:\nabla\mathbf v\big],\\
&\mu_0\mathbf J=\nabla\times\mathbf B,\qquad \partial_t\mathbf B=\nabla\times(\mathbf v\times\mathbf B)-\nabla\times(\eta\mathbf J),\\
&\mathbf q_T=-\kappa_\perp\nabla T_e-\kappa_\parallel\mathbf b\mathbf b\cdot\nabla T_e,\qquad
\eta=\eta_{\mathrm{norm}}\big[\eta_c+\eta_{\mathrm{Sp},0}T_e^{-3/2}\big],
\end{aligned}$$

with $\mathbf q_T$ the conductive heat flux (page-local), $\mathbf S_{\mathbf v}$
and $S_p$ the external force and heat source, and $\eta_c$,
$\eta_{\mathrm{Sp},0}$ page-local multipliers. No $\mathbf J_x$, no bootstrap
term, no two-fluid terms; the form of $\mathsf\Pi$ is not given. The
perpendicular heat flux uses the full gradient, as in
[Zhou et al. (2023)](/sources/zhou-2023.md).

* **Coefficients.** $\kappa_\perp/\kappa_\parallel=10^{-6}$; perpendicular
  diffusivity $\chi_\perp=2.18$ m² s⁻¹, chosen as representative of measured
  QS transport (HSX, Canik et al. 2007). $\eta_{\mathrm{norm}}=2.74$ Ω m;
  constant model $\eta_c=10^{-6}$, $\eta_{\mathrm{Sp},0}=0$
  ($\eta=2.74\times10^{-6}$ Ω m); Spitzer models $\eta_c=0$,
  $\eta_{\mathrm{Sp},0}\in\{1,10,100\}$; units of $T_e$ in the Spitzer term
  not stated. Dynamic viscosity $\nu=3.65\times10^{-4}$ kg m⁻¹ s⁻¹,
  "comparable to the values used in the MIPS code" (Futatani & Suzuki 2019).
  No hyper-diffusion.
* **Normalization** (compiler's inference, consistent with every printed
  number): M3D-C1 units with $B=1$ T, $n=10^{20}$ m⁻³, proton mass and 1 m give
  $v_A\approx2.18\times10^6$ m s⁻¹, $\tau_A\approx0.46$ µs, resistivity unit
  2.74 Ω m, diffusivity unit $2.18\times10^6$ m² s⁻¹, viscosity unit 0.364
  kg m⁻¹ s⁻¹; hence $\chi_\perp=10^{-6}$ and $\nu=10^{-3}$ in code units, and
  $1500\tau_A\approx690$ µs. The paper does not define $\tau_A$.
* **Boundary conditions.** No vacuum region; the domain is the initial plasma
  boundary (limited plasma) with a conducting wall; $T$ and $\mathbf J$ vanish
  there; density held at its initial wall value (an implicit source).
* **Initial state.** The Landreman et al. (2022) QA at $\beta=2.5\%$ (type of
  average not stated), nested surfaces assumed; $a=1.704$ m; $R$ about
  7.3–10.6 m and peak $T_e\approx2.2\times10^4$ eV (Fig. 1 readings). Full
  torus, no symmetry imposed.
* **Discretization.** Semi-structured 3D mesh, 72 toroidal planes,
  $8.64\times10^5$ elements (≈12 000 per plane); element type, time
  integration and solvers not restated. "M3D-C1 itself is not a spectral
  code": the toroidal Fourier decomposition is a diagnostic.
* **Cost.** About $4\times10^5$ CPU-h, 14 days wall clock (≈1200 cores on
  average, compiler's arithmetic); no GPU.
* **Diagnostics.** Poincaré sections (angle not stated); $T_e$ at
  $\phi=45^\circ$; kinetic energy per toroidal harmonic and its logarithmic
  derivative, smoothed by a Gaussian kernel of standard deviation $5\tau_A$.

# Tests and results

No verification benchmark; one case, four resistivity variants.

| Quantity | Value | Location |
|---|---|---|
| Edge chaos visible | ≈450–525 $\tau_A$ | Fig. 6 |
| Chaotic width | 5–10% of $a$ at ≈500 $\tau_A$; ≈25% at ≈800 $\tau_A$ | §III |
| Core reached | 1125–1425 $\tau_A$; almost all surfaces lost at 1500 $\tau_A$ ≈ 700 µs | Figs. 2, 6 |
| Relaxation time $a^2/\chi_\perp$ | 1.33 s | §III |
| Max growth rate, $n=6$ | ≈0.07 (constant), 0.17 (Spitzer ×10), 0.28 (×100), ×10⁻² $\tau_A^{-1}$ | Fig. 3 |
| Max growth rate, $20\le n\le30$ | Spitzer ≈0.93–1.02, ×10 ≈0.8–0.92, ×100 ≈1.0–1.11, constant ≈0.8–0.85 (0.70 at $n=30$) | Fig. 3 |
| $n=30$ peak | constant ≈1.2 at 600–700 $\tau_A$; Spitzer ×1, ×10, ×100 ≈1.45, 1.6, 1.55 at ≈700, 650, 550 $\tau_A$ (×10⁻² $\tau_A^{-1}$) | Fig. 5 |

Growth-rate values are figure readings. The ordering in resistivity is not
monotonic (Spitzer ×1 above ×10 for most $n$), and higher Spitzer multipliers
peak earlier at $n=30$. Spitzer runs end at ≈700–900 $\tau_A$, the constant
run continues to ≈1500 $\tau_A$.

Relation to [Saxena et al. (2025)](/sources/saxena-2025.md), same group and the
same QA family ($a=1.70$ m, $\eta_{\mathrm{norm}}=2.74$ Ω m, same viscosity):
Saxena et al. state that "instability growth still increases with
resistivity, supporting Wright & Ferraro (2024a)". This paper's own conclusion
stresses resistivity independence, and its Fig. 3 shows no monotonic increase
of the maximum growth rate with resistivity. The supporting reading is
therefore not a result stated here (compiler's comparison; for the concept
pages to weigh). Saxena et al. give a central temperature of 9.45 keV for
their QA case against the ≈22 keV peak of Fig. 1 here, unresolved.

# Notation map

| Wright & Ferraro (2024) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $n$ (App. A) | $n_i$ | **collision:** native $n$ is also the toroidal mode number (§III) |
| $m$, $n$ (§III) | $m$, $n$ | |
| $\mathbf v$, $m_i$, $\mathbf J$, $\mathbf B$, $B$, $p$ | $\mathbf v$, $m_i$, $\mathbf J$, $\mathbf B$, $B$, $p$ | |
| $\Pi$ | $\mathsf\Pi$ | single-fluid viscous stress |
| $\mathbf F$, $Q$ | $\mathbf S_{\mathbf v}$, $S_p$ | |
| $\gamma$ | $\Gamma$ | **collision:** registry $\gamma$ is a growth rate |
| unnamed growth rate $d\ln E_k/dt$ | $2\gamma$ | kinetic-energy rate |
| $\eta$, $\eta_{\rm norm}$, $\eta_c$, $\eta_0$ | $\eta$; $\eta_{\mathrm{norm}}$, $\eta_c$, $\eta_{\mathrm{Sp},0}$ (page-local) | |
| $T_e$ | $T_e$ | eV in Fig. 1; unit in Eq. 2 unstated |
| $\mathbf q$ | $\mathbf q_T$ (page-local) | **collision:** registry $q$ is the safety factor |
| $\kappa_\parallel$, $\kappa_\perp$, $\chi_\perp$ | $\kappa_\parallel$, $\kappa_\perp$, $\chi_\perp$ | |
| $\nu$ | $\nu$ | dynamic |
| $\tau_A$ | $\tau_A$ | undefined in the paper; ≈0.46 µs inferred |
| $\tau_{\rm relaxation}$ | words | |
| $a$, $\beta$ | $a$, $\beta$ | |
| $N$ | $N_{\mathrm{fp}}$ | |
| $n_0$, $n_l$, $l$ | words (seed harmonic, coupled harmonics, integer) | the coupled set is one mode family $N_f$ (§10) |
| $R$, $\phi$, $Z$ ($u$/$\varphi$ in §I) | $R$, $\phi$, $Z$ | orientation not stated |

# Pages created or updated

Chunk 3 (2026-10-16) created or updated the pages below. This source is cited on:

* [Bootstrap current and its MHD implementation](/definitions/bootstrap-current.md)
* [Edge instabilities of an optimized quasi-axisymmetric reactor stellarator](/results/stellarator-edge-instability-qa.md)
* [Interchange modes and the Mercier criterion](/definitions/interchange-mode.md)
* [M3D-C1](/software/m3d-c1.md)
* [MIPS](/software/mips.md)
* [Quasi-symmetry](/definitions/quasi-symmetry.md)
* [Single-fluid visco-resistive MHD model](/methods/visco-resistive-mhd-model.md)
* [Soft β limit of stellarators](/definitions/soft-beta-limit.md)
* [Three-dimensional inverse equilibrium solvers](/methods/inverse-equilibrium-solvers.md)
* [Toroidal mode families in stellarators](/definitions/toroidal-mode-family.md)

# Citations

1. `/home/stefano/papers/mosaic/fusion-mhd-simulation/2024_Crossref_Physics_of_Plasmas_Wright_Investigating_nonlinear_magnetohydrodynamics_in_an_optimized.pdf`
   * **Version.** Publisher version of record (AIP, CC BY-NC-ND 4.0), 8 PDF
     pages: AIP cover plus article pages 082509-1 to -7; Special Collection
     "2024 Early Career Collection". Submitted 24 April 2024, accepted 24 July,
     online 13 August 2024.
   * **Identity.** doi:10.1063/5.0215594, checked on Crossref: title, authors,
     Phys. Plasmas 31(8), article 082509, August 2024, 28 references. It is the
     work already keyed `wright-2024` in the bibliography (cited by
     saxena-2025 as "Wright & Ferraro 2024a").
   * **How read.** Full text; App. A and Eqs. 1–2 checked on the rendered
     page; growth rates and geometry are figure readings.
   * **Recorded as printed.**
     * The coupling rule is printed "$n_l=ln_0\pm N$ for $l\in\mathbb Z$"
       (p. 082509-4, rendered page); the rule used in the text (all even
       harmonics) is $n_0+lN$.
     * "Even-numbered toroidal Fourier modes with $n>6$ have positive maximum
       growth rates", but Fig. 3 shows positive maxima at $n=6$ for all four
       models.
     * Fig. 1 caption announces "initial, intermediate, and final time"; the
       panels show $t=0$ and $t_{final}=825\tau_A$, although the constant-$\eta$
       run continues to $1500\tau_A$ (Fig. 2).
     * Fig. 6 is the "full sequence" to $1425\tau_A$; Fig. 2 shows the same
       run at $1500\tau_A$.
     * §II lists "one that is constant and three Spitzer-resistivity models",
       §IV "a temperature dependent Spitzer model, and two others that are
       scaled versions" (consistent, four in all).
     * Parameters printed in braces, "$\eta_c=\{0\}$"; units of $T_e$ in
       $T_e^{-3/2}$ not given, so the Spitzer magnitude cannot be
       reconstructed.
     * The magnetic well is defined as "the average curvature on a magnetic
       surface" and equated with linear stability to local pressure-gradient
       perturbations (imprecise; the paper then finds pressure-driven
       instability despite a well on all surfaces).
     * Modes "near the plasma edge" are also called "internal in character"
       and unaffected by boundary conditions, with the wall on the plasma
       boundary; untested.
     * Growth rates are kinetic-energy rates, not stated as such.
     * Eq. A3 contains $-\mathbf v\cdot\mathbf F$, with $\mathbf F$
       unspecified for these runs.
     * $n$ is both density and mode number; $\gamma$ is the adiabatic index;
       $\mathbf q$ is the heat flux.
     * $\tau_A$ undefined; type of $\beta$ average and Poincaré-section angle
       not stated; the introduction writes $\partial_u\ne0$ with $u$ the
       toroidal angle.
     * "Convergence studies were performed", no results shown.
   * **Reference list.** 28 printed entries, no garbled ones, merged into the
     bibliography under `wright-2024`. Key decisions: the source of the
     equilibrium, Landreman, Buller & Drevlak (2022) Phys. Plasmas 29:082501,
     is the existing `landreman-2022`; Landreman's (2022) J. Plasma Phys.
     near-axis paper is `landreman-2022-c` and Futatani & Suzuki (2019) is
     `futatani-2019-c` (the `-b` and unsuffixed keys are other works); Zhou et
     al. (2023) is the ingested `zhou-2023` and Zhou et al. (2021) is
     `zhou-2021`; other reused keys are `helander-2014`, `jardin-2012`,
     `landreman-2021`, `freidberg-2014`. Ref.
     3 is arXiv:1908.05360 printed with year 2020; ref. 13 prints 33 authors
     (kept as the first 10 plus others); ref. 16's "Bräuer" is written
     Brauer.
