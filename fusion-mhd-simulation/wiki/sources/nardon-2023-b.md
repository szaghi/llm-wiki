---
type: Source
title: "Nardon et al. (2023b) — Non-linear dynamics of the double tearing mode"
description: "JOREK reduced-MHD simulations of a 4/1 double tearing mode in a JET runaway-beam-like plasma, showing that a violent, helicity-conserving global relaxation with a large current spike occurs only at intermediate resistivity, and explaining this by how fast secondary 11/3 and 7/2 tearing modes, destabilized at the outer island edge, grow relative to the primary mode."
resource: "doi:10.1063/5.0162608"
source_kind: paper
authors: [Nardon E., Bandaru V., Hoelzl M., Artola F.J., Maget P., JOREK Team, JET Contributors]
year: 2023
venue: "Phys. Plasmas 30:092502"
local_file: "/home/stefano/papers/mosaic/fusion-mhd-simulation/2023_Crossref_Physics_of_Plasmas_Nardon_Non-linear_dynamics_of_the_double_tearing_mode.pdf"
tags: [tearing, reduced-mhd, disruption, runaway-electrons, tokamak]
timestamp: 2026-10-16T20:00:00Z
---

# Summary

The paper runs 3D nonlinear [JOREK](/software/jorek.md) simulations of an
$m/n=4/1$ double tearing mode (DTM) in the setup of the JET runaway-electron
benign-termination study of Bandaru et al. (2021), without runaway electrons.
The model is pressureless [reduced MHD](/methods/reduced-mhd.md) without
parallel flow and with flat constant density, in a nearly circular limiter
plasma ($R_0=2.6$ m, $a=0.67$ m, $B_\phi=3.5$ T, $I_p=0.75$ MA) whose
non-monotonic $q$ profile has two $q=4$ surfaces. The Kadomtsev model
generalized to the DTM predicts a reconnection region from almost the axis to
the edge, unlike the partial region of earlier Tore Supra DTM studies. At
normalized $\eta=\nu=10^{-6}$ (Spitzer at 27 eV) the two 4/1 island chains
overlap, the field becomes stochastic, a secondary 7/2 mode acts as a
"magnetic trigger", a macroscopic 4/1 flow stirs the plasma, all flux surfaces
are destroyed, and $J_\phi/B$ flattens almost completely at nearly constant
magnetic helicity, giving a large $I_p$ spike (≈+30%) and a strong $l_i$ drop.
This violent relaxation occurs only for $5\cdot10^{-7}\le\eta\le3\cdot10^{-6}$
(Spitzer 47–13 eV). The authors explain the window by the relative growth of
secondary tearing modes destabilized by the steep current gradient at the
outer 4/1 island edge: at low $\eta$ an 11/3 mode in its linear phase
($\propto\eta^{3/5}$) outpaces the primary in its Rutherford phase
($\propto\eta$), relaxes the current gently and removes the 7/2 drive; at high
$\eta$ the 7/2 mode never grows much. Two numerical experiments (switching
$\eta$ mid-run, truncating to $n\le2$) support this. An appendix derives the
helicity and its purely resistive dissipation in this model. The authors
speculate that background temperature explains the different outcomes of D$_2$
and high-Z injection into runaway beams.

# Key claims

Registry symbols (§10): $\mathcal H=\int\mathbf A\cdot\mathbf B\,dV$ the magnetic
helicity; $w$ an island width. Page-local: $j_0$ the initial $j$.

1. **Qualitative $\eta$ dependence** (Abstract, §IV, §V). Attributed to "how
   fast secondary, non-linearly destabilized, tearing modes grow relative to the
   primary mode". Dependence Shown (Fig. 5); mechanism supported by the
   numerical experiments of Figs. 11–12 and hedged in the paper ("appears",
   "likely").
2. **Violent-relaxation window** (§I, §IV, Fig. 5). Only for
   $5\cdot10^{-7}\le\eta\le3\cdot10^{-6}$ (JOREK units), i.e. Spitzer
   $T_e\simeq13$–47 eV. Shown; the $\eta=3\cdot10^{-7}$ and $10^{-7}$ runs were
   stopped, so "it is not known for sure whether a large $I_p$ spike would arise
   later" (Fig. 6 suggests saturation at $3\cdot10^{-7}$).
3. **Generalized Kadomtsev prediction** (§II, Fig. 2; §V). Matching helical flux
   predicts a reconnection region "extending from almost the very centre up to
   the edge of the plasma". Derived; consistency with the simulation Shown
   qualitatively.
4. **Role of edge proximity and limiter** (§II). The outer $q=4$ surface near the
   edge is key; in a divertor plasma $q\to\infty$ at the edge might keep the
   region from reaching the edge, though large shear favours overlap. Stated.
5. **Fixed boundary suppresses 5/1** (§II). Fixing $\psi$ at the boundary zeroes
   perturbations there, which "probably explains" the negligible 5/1 role
   although $q\approx5$ at the edge. Stated.
6. **Sequence at $\eta=10^{-6}$** (§III, Fig. 3). Two 4/1 chains (3.62 ms);
   overlap and small-scale stochasticity with an intact core (4.30 ms); a strong
   macroscopic 4/1 flow "violently 'stirs' the plasma" (4.35 ms); the core
   shrinks with a skin current until all surfaces are destroyed; the flow decays,
   $J_\phi$ homogenizes, surfaces "promptly reform" (4.40, 4.57 ms). Shown.
7. **Spike signature** (§III, Fig. 4). The spike at 4.36 ms comes with a strong
   $l_i$ drop, a small magnetic-energy release and nearly constant $\mathcal H$,
   "as expected from the theory of fast MHD relaxations"; later spikes at 5.35
   and 6.08 ms because the source $\eta(j-j_0)$ restores an unstable state. Shown;
   $I_p/I_p(0)\approx1.3$, $l_i/l_i(0)\approx0.58$ (plot readings).
8. **Near-complete flattening** (§V). "An almost complete flattening of the
   $j_\phi/B$ profile at fixed magnetic helicity". Shown qualitatively.
9. **Quasi-linear early phase** (§IV.A, Fig. 6). The 4/1 mode grows
   quasi-linearly until $W_{\mathrm{mag}}^{(1)}\simeq10^{-6}$ (a.u.); higher
   harmonics grow by beating "with growth rates adding up"; then the Rutherford
   phase. Shown.
10. **Rutherford invariance** (§IV.A, Fig. 7). The Rutherford phase is invariant
    under $t\to\alpha t$, $\eta\to\eta/\alpha$ ($dw/dt\propto\eta$); with
    $t'=t/3.3+1.13$ ms the $3\cdot10^{-7}$ run matches the $10^{-6}$ run for
    $n=1,2$. Derived (theory) / Shown (match).
11. **Earlier 11/3 secondary at low $\eta$** (§IV.A, Figs. 7–9). In rescaled time
    the 11/3 mode grows earlier and faster at $3\cdot10^{-7}$, producing
    stochasticity at the outer edge of the outer 4/1 island. Shown.
12. **Drive of the 11/3 mode** (§IV.A, Fig. 10). The radial $J_\phi$ gradient at the
    outer island edge (radius ≈0.57 m), formed because $J_\phi/B$ tends to be
    constant on helical surfaces inside the island; the two runs' profiles are
    "remarkably" similar before the 11/3 grows. Shown/Stated.
13. **Scaling argument** (§IV.A). Linear 11/3 ($\propto\eta^{3/5}$) against
    Rutherford 4/1 ($\propto\eta$) gives a ratio $\propto\eta^{-2/5}$, larger at
    small $\eta$. Finite-layer-width effects lowering the linear rate below
    $\eta^{3/5}$ at large $\eta$ (Militello) can reinforce it; a critical
    $\Delta'\propto\eta^{1/6}\nu^{1/6}$ (Grasso) differs by only ≈20% between the
    cases, and a run with 10× lower viscosity shows "almost no effect". Derived
    (heuristic) / Shown (viscosity test).
14. **7/2 trigger at $\eta=10^{-6}$** (§IV.A, Fig. 6). Excited at ≈4 ms when the
    $J_\phi$ gradient crosses $q=7/2$, it boosts stochasticity ("magnetic trigger",
    Lichtenberg 1992); at $3\cdot10^{-7}$ early 11/3 stochasticity relaxes the
    current first and gives "gentle saturation". Shown/Stated ("plausible
    explanation").
15. **Mid-run switch** (§IV.A, Fig. 11). $\eta$ lowered from $10^{-6}$ to
    $3\cdot10^{-7}$ at 3.83 ms, after the gradient has passed $q=11/3$, still
    gives a large spike. Shown.
16. **$n\le2$ truncation** (§IV.A, Fig. 12). Both resistivities behave much more
    alike and neither relaxes violently, "probably because $n\ge3$ harmonics are
    required". Shown.
17. **High $\eta$** ($10^{-5}$–$10^{-4}$; §IV.B, Figs. 13–14). The 7/2 mode never
    grows much, no large stochastic region forms; at rescaled 4.2 ms
    $\eta=10^{-6}$ is almost fully stochastic for $\sqrt{\psi_N}\ge0.3$ while
    surfaces remain at $10^{-5}$. Shown; detailed mechanism "beyond the scope".
18. **Helicity theorem** (App. A, Eq. A4). In this model
    $d\mathcal H/dt=2F_0\int\eta(j-j_0)R^{-1}\,d\phi\,dS$, "recovering the
    classical result that helicity is dissipated at a resistive rate only".
    Derived (with the Jacobian caveat under Citations).
19. **Runaway-beam termination hypothesis** (§V). After D$_2$ injection the
    colder, more resistive plasma ($\eta$ probably above $10^{-5}$, ≈6 eV) lets the
    primary mode grow larger before stochasticity, giving a more violent
    relaxation and benign termination; after high-Z injection the plasma is
    hotter. Stated ("may be hypothesized").
20. **Caveats on missing runaways** (§V). Helander et al. (2007): linear tearing
    with runaways is set by the cold bulk, so the study is relevant; but the
    finite-resistivity correction to $\eta^{3/5}$ is absent when runaways carry
    the current, which weakens claim 13. In DIII-D the relevant mode is the
    resistive external kink ($q_{\mathrm{edge}}\to2$), which also involves primary and
    secondary islands ([Liu et al. (2021)](/sources/liu-2021.md), Fig. 10). Stated.

# Models and numerics

* **Model.** JOREK pressureless reduced MHD without parallel flow; flat
  $n_e=10^{19}$ m$^{-3}$, $\rho=m_{\mathrm D}n_e=3.3\cdot10^{-8}$ kg m$^{-3}$; $\eta$,
  $\nu$ constant. Fields $\psi$, $u$. JOREK normalized units ($\mu_0=1$). With
  $j=\Delta^*\psi$, $\varpi=\nabla\cdot\nabla_{\mathrm{pol}}u$,
  $[f,g]=\mathbf e_\phi\cdot(\nabla f\times\nabla g)$:
  $$\begin{aligned}
  \partial_t\psi&=R[\psi,u]-F_0\partial_\phi u+\eta(j-j_0),\\
  \nabla\cdot\big(R^2\rho\nabla_{\mathrm{pol}}\partial_tu\big)&=\frac1R[R^4\rho\varpi,u]-\frac1{2R}[R^2\rho,R^2|\nabla_{\mathrm{pol}}u|^2]+\frac1R[\psi,j]-\frac{F_0}{R^2}\partial_\phi j+\nu\,\Delta\varpi,
  \end{aligned}$$
  where $\Delta$ in the viscous term is not defined in the paper. The source
  $\eta(j-j_0)$ keeps the initial profile in the absence of MHD. The signs of the
  $\psi$ equation ($+\eta(j-j_0)$, $-F_0\partial_\phi u$, $+R[\psi,u]$) are those of
  [Hu et al. (2021b)](/sources/hu-2021-b.md) and
  [Bandaru et al. (2024)](/sources/bandaru-2024.md), opposite to
  [Hoelzl et al. (2021)](/sources/hoelzl-2021.md) Eq. 28 and
  [Nikulsin et al. (2022)](/sources/nikulsin-2022.md) Eq. 3d.
* **Field and helicity** (App. A). $\mathbf B=\nabla\psi\times\nabla\phi+F_0\nabla\phi$,
  $\mathbf A=\psi\nabla\phi-F_0(Z/R)\nabla R$,
  $\mathbf A\cdot\mathbf B=(F_0/R^2)(\psi-Z\partial_Z\psi)$; boundary terms vanish
  because $\partial_t\psi=0$ and $u=0$ on the boundary; the
  $\partial_\phi u$ term vanishes on toroidal integration.
* **Equilibrium.** $B_\phi=3.5$ T at $R_0=2.6$ m ($F_0=9.0$ T m), $I_p=0.75$ MA,
  $a=0.67$ m, nearly circular limiter; non-monotonic $q$ with
  $q_{\min}\approx3.5$ near $\sqrt{\psi_N}\approx0.6$, $q\approx5$ at the edge and
  ≈7 near the axis (plot readings); two $q=4$ surfaces, plus $q=11/3$, 7/2.
* **Boundary conditions.** Fixed boundary: $\psi=\psi(t=0)$, $u=\varpi=j=0$.
* **Discretization.** [Bézier finite elements](/methods/bezier-finite-elements.md)
  on a flux-surface-aligned grid of 120 radial × 64 poloidal cells (7680);
  toroidal harmonics $n=0$–15 ($n=0$–2 in Fig. 12). Time integration and solver
  not described. Marconi-Fusion; low-$\eta$ runs "very expensive".
* **Units (as printed).** $\eta_{\mathrm{SI}}=\sqrt{\mu_0/\rho}\,\eta\simeq6.1\cdot10^{-6}$ Ω m
  at $\eta=10^{-6}$ (Spitzer 27 eV); $\nu_{\mathrm{SI}}=\sqrt{\mu_0/\rho}\,\nu/R^2\simeq9.0\cdot10^{-7}$
  kg m$^{-1}$s$^{-1}$, a momentum diffusivity of 27 m²/s; $3\cdot10^{-6}$ ↔ 13 eV,
  $5\cdot10^{-7}$ ↔ 47 eV, $10^{-5}$ ↔ ≈6 eV.
* **Scan.** $\eta\in\{10^{-7},3\cdot10^{-7},5\cdot10^{-7},10^{-6},3\cdot10^{-6},10^{-5},3\cdot10^{-5},10^{-4}\}$
  with $\nu=\eta$; an $\eta$ scan at fixed $\nu$ is "qualitatively similar" (not
  shown); one run at $\eta=10^{-6}$, $\nu=10^{-7}$.

# Tests and results

No code-to-code benchmark; a physics parameter scan.

| $\eta$ (JOREK units) | Spitzer $T_e$ | Outcome (Fig. 5) |
|---|---|---|
| $3\cdot10^{-6}$ | 13 eV | large spike |
| $10^{-6}$ | 27 eV | large spike at 4.36 ms ($I_p$ ≈0.94–0.98 MA, plot reading) |
| $5\cdot10^{-7}$ | 47 eV | rise 0.75 → 0.77 MA, plateau, then large spike |
| $3\cdot10^{-7}$, $10^{-7}$ | – | moderate rise and plateau; runs stopped |
| $10^{-5}$, $3\cdot10^{-5}$, $10^{-4}$ | ≈6 eV at $10^{-5}$ | much smaller spike, faster dynamics |

* Reference run: $W_{\mathrm{mag}}^{(0)}$ drops by a few percent, $\mathcal H$ flat,
  secondary spikes at 5.35 and 6.08 ms.
* Rescalings $t'=t/3.3+1.13$ ms ($3\cdot10^{-7}$) and $t''=10t-6.3$ ms
  ($10^{-5}$). The $n=3$ mode at $3\cdot10^{-7}$ is identified as 11/3 (Fig. 8,
  $t'=3.40$ ms).
* Critical $\Delta'$ differs by ≈20% between $10^{-6}$ and $3\cdot10^{-7}$.

# Notation map

| Nardon et al. (2023b) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $R$, $Z$, $\phi$, $\mathbf e_\phi$ | same | right-handed $(R,Z,\phi)$ implied by Eq. A2; COCOS not stated |
| $\psi$, $\psi_n$ | $\psi$ (per radian), $\psi_N$ | |
| $\Psi_n$ | $\psi_{t,N}$ | |
| $\psi_*=\int(1/q-1/4)\,d\Psi_n$ | $\psi_h$ for $m/n=4/1$ | integrated over the normalized $\psi_{t,N}$, not $\psi_t$ |
| $u$ | $u$ | called "electric potential", equal to the flow potential |
| $\omega$ | $\varpi$ | **collision:** registry $\omega$ is a frequency |
| $j_\phi\equiv\Delta^*\psi$ | $j$ | **collision:** named "toroidal current density"; registry $J_\phi$ is the physical component |
| $j_{\phi0}$ | $j_0$ (page-local) | |
| $\Delta_{pol}$, $\Delta$ | $\nabla\cdot\nabla_{\mathrm{pol}}$; $\Delta$ undefined | |
| $\nabla_{pol}$, $[A,B]$ | $\nabla_{\mathrm{pol}}$, $[f,g]$ | same definitions |
| $\mu$ | $\nu$ | **collision:** registry $\mu$ is the magnetic moment |
| $\eta$ | $\eta$ | JOREK units |
| $H$ | $\mathcal H$ | |
| $l_{i3}$ | $l_i$ ($l_i(3)$ presumed) | definition not given |
| $E_{mag,n}$ | $W_{\mathrm{mag}}^{(n)}$ | a.u. |
| $m_D$ | $m_i$ (deuterium) | |
| $w$ | $w$ | island width |
| $\alpha$, $t'$, $t''$ | page-local | |

# Pages created or updated

Chunk 2 (2026-10-16) created or updated the pages below; chunk 3 extended some. This source is cited on:

* [Bézier–Hermite finite elements with toroidal Fourier harmonics](/methods/bezier-finite-elements.md)
* [Disruption: phases, current quench and current spike](/definitions/disruption.md)
* [Double tearing mode](/definitions/double-tearing-mode.md)
* [JOREK](/software/jorek.md)
* [Modified Rutherford equation](/definitions/modified-rutherford-equation.md)
* [Reduced MHD for tokamaks](/methods/reduced-mhd.md)
* [Resistive tearing mode](/definitions/tearing-mode.md)
* [Runaway current reconstitution after an MHD flush](/results/runaway-reconstitution-after-mhd-flush.md)
* [Runaway electrons and their generation mechanisms](/definitions/runaway-electrons.md)
* [Sawtooth crash and Kadomtsev reconnection](/definitions/sawtooth-crash.md)

# Citations

1. `/home/stefano/papers/mosaic/fusion-mhd-simulation/2023_Crossref_Physics_of_Plasmas_Nardon_Non-linear_dynamics_of_the_double_tearing_mode.pdf`.
   * **Version.** HAL accepted manuscript cea-04193695v1 (deposited 1 Sep 2023,
     manuscript dated 1 September 2023); 11 PDF pages (HAL cover + 10 paper
     pages); not the typeset version of record.
   * **Identity.** doi:10.1063/5.0162608, checked on Crossref: Phys. Plasmas
     30(9), article 092502, issued 2023-09-01; five personal authors plus JOREK
     Team and JET Contributors as group authors; 27 references, matching the
     printed list. The `-b` suffix follows `nardon-2023` (Nardon et al., NF 63,
     current spike and stochasticity), published earlier in 2023.
   * **How read.** Full text; Eqs. 1–2 checked on rendered p. 2 and App. A on
     rendered p. 10; curve values are plot readings.
   * **Recorded as printed.**
     * The HAL cover names the journal "Journal of Plasma Physics, In press";
       the journal is Physics of Plasmas (DOI correct).
     * App. A: text extraction garbles $\mathbf A\cdot\mathbf B$; the rendered
       $(F_0/R^2)(\psi-Z\partial_Z\psi)$ is confirmed for right-handed $(R,Z,\phi)$
       (compiler's check).
     * Eq. A3 integrates $(F_0/R^2)(\dots)\,d\phi\,dS$ but A4 has
       $F_0/R$; with $dV=R\,d\phi\,dS$ the A3 integrand should carry $F_0/R$,
       which is what makes A4 and the vanishing of the $R[\psi,u]$ term follow
       (compiler's check).
     * $j_\phi\equiv\Delta^*\psi$ is called "the toroidal current density",
       dropping the factor $-R$ (and $\mu_0$); Fig. 1's colorbar "j (MA/m^2)" is
       positive, presumably a converted physical $J_\phi$.
     * $\mu_{SI}=\sqrt{\mu_0/\rho}\,\mu/R^2$ is dimensionally unusual (the $R^2$,
       presumably $R_0$); the number checks out. "Constant magnetic Prandtl
       number, $\mu=\eta$" holds in normalized units only: the SI magnetic
       diffusivity ≈4.9 m²/s against 27 m²/s momentum diffusivity is a Prandtl
       number ≈5.5 (compiler's check).
     * $5\cdot10^{-7}$ ↔ 47 eV against ≈43 eV from pure $T^{-3/2}$; plausibly the
       $\ln\Lambda$ dependence (minor).
     * The rescaling factor 3.3 stands for $10/3$; $t'=7.49/3.3+1.13=3.40$ ms is
       consistent with Fig. 9.
     * The spike is not quantified in the text (Figs. 4 and 5 give ≈1.3 and
       ≈1.25–1.3).
     * $\Delta$ in $\mu\Delta\omega$ and $l_{i3}$ are undefined; Kadomtsev's
       original paper is not cited; "Huysmans" (refs. 10, 16, 17, 20) and
       "Huijsmans" (ref. 15) for the same author; "We precise quasi-linear",
       "consistent to".
   * **Reference list.** 27 printed entries, merged into the bibliography under
     `nardon-2023-b`. Key decisions: Paz-Soldan et al. NF 61:116058 (ref. 24) is
     `pazsoldan-2021-b`; Maget et al. Phys. Plasmas 14:052509 (ref. 10) is
     `maget-2007-b`; ref. 27 (PPCF 63:125031) is the ingested `liu-2021`; ref. 14
     Wesson *Tokamaks* 4th ed. (2011) is `wesson-2011`, distinct from
     `wesson-2004`; Militello (ref. 20) printed 2003, Crossref 2004, kept as
     `militello-2003`; the cited JOREK overview is the ingested
     [Hoelzl et al. (2021)](/sources/hoelzl-2021.md) (`hoelzl-2021`). Printed defects: DOIs of refs. 2 and 25 only
     inside URLs; collaboration authors garbled in refs. 12–13 ("J.
     contributors", "J. Team"); refs. 19, 21, 23 print volume, DOI and article
     number in irregular order. This source is cited by
     [Hoelzl et al. (2024)](/sources/hoelzl-2024.md) (its ref. [58]).
