---
type: Source
title: "Kastaun, Kalinani & Ciolfi (2021) — Robust recovery of primitive variables in relativistic ideal magnetohydrodynamics"
description: "Builds primitive-variable recovery for ideal GRMHD with an arbitrary EOS as the root of one scalar master function, proves a root exists in an explicit bracket for any input and is unique whenever the sound speed is subluminal, derives linear error bounds on all recovered quantities, and releases the RePrimAnd library, which never fails in stand-alone tests and needs at most 23 EOS calls."
resource: "doi:10.1103/PhysRevD.103.023018"
source_kind: paper
authors: [Kastaun W., Kalinani J.V., Ciolfi R.]
year: 2021
venue: "Phys. Rev. D 103:023018"
local_file: "~/papers/mosaic/astrophysical-simulation-codes/2021-PRD-Kastaun-101103physrevd103023018.pdf"
tags: [mhd, relativity, primitive-recovery, equation-of-state, verification]
timestamp: 2026-10-12T00:00:00Z
---

# Summary

The paper constructs conservative-to-primitive recovery for ideal GRMHD with an
arbitrary EOS $p(\rho, e)$ as the root of a single scalar master function
$f(\mu) = \mu - \hat\mu(\mu)$, $\mu = 1/(Wh_{\mathrm{rel}})$ (§II D–E, eqs. 26,
44–48). It **proves** that $f$ has a root in an explicitly constructed bracket
$(0, \mu_+]$, even for unphysical conserved input (§II F), and that the root is
unique whenever $c_s < 1$ plus a mild condition on the upper EOS validity bound
(§II G, App. A). It derives, to linear order, error bounds on every recovered
primitive and on the recomputed conserved variables (§II H), and builds a
classification and projection of invalid states into the recovery (§III). The
C++ library RePrimAnd (TOMS748 bracketing root finder, no EOS derivatives) is
tested stand-alone with zero failures and at most 23 EOS calls at
$\Delta = 10^{-8}$ (§IV). §V analyses how evolution errors in the conserved
variables are amplified into $e$ and $p$, and the spurious heating caused by
the zero-temperature floor. Merged into
[primitive-variable recovery](/methods/primitive-variable-recovery.md) and
[dual-energy formalism](/methods/dual-energy-formalism.md).

# Key claims

1. **Setting** (§II A–C). Ideal MHD with $\boldsymbol{\mathcal E} = -\mathbf v\times\mathbf B$
   (eq. 21); $\mathbf B$ known before recovery (evolved directly, by constrained
   transport, or through a vector potential, §II C); EOS $p(\rho, e)$ with
   extra variables (electron fraction) as fixed parameters. EOS validity box
   $\rho_{\min} \le \rho \le \rho_{\max}$, $e_{\min}(\rho) \le e \le e_{\max}(\rho)$
   (eqs. 5–6), $e_{\min}$ the zero-temperature value. Physical constraints
   $0 \le c_s^2 < 1$ (eq. 7), $0 \le p/\rho_E \le 1$ (dominant energy condition,
   eq. 10), and a global lower enthalpy bound $h_0$. $e > 0$ and
   $h_{\mathrm{rel}} \ge 1$ are not assumed.
2. **Rescaled variables** (eqs. 15–27). Conserved $D$, $S_i$, $\tau$ split into
   fluid and electromagnetic parts; the metric volume element is omitted.
   Rescaled by $D$: $q = \tau/D$, $r_i = S_i/D$, $b_i = B_i/\sqrt D$. The
   relevant field scale is $b$, not the magnetization; $\mathcal O(b) = 1$ is
   already a very large magnetization (§II C).
3. **Master function** (§II E, eqs. 40–48). From a trial $\mu$ the scheme
   computes $\hat{\mathbf v}$ (limited by $v_0$, eqs. 32–33), $\hat W$,
   $\hat\rho = D/\hat W$ and $\hat e$ (eq. 42, written to avoid round-off in
   $W - 1$), clamps $(\hat\rho, \hat e)$ to the validity box, and returns
   $\hat\mu = 1/(\hat\nu + \bar r^2\mu)$ with $\hat\nu = \max(\nu_A, \nu_B)$.
   Design goals: one-dimensional, continuous, exactly one root even for
   unphysical input, well behaved in the Newtonian and $B = 0$ limits, known
   bracket, no EOS derivatives. The "straightforward" choice
   $\hat\mu = 1/(\hat W\hat h_{\mathrm{rel}})$ was rejected because clamping
   produces severe kinks (found "by trial and error"). Newtonian limit:
   $f(\mu) \approx \mu - 1$ (§V A).
4. **Existence** (proved, §II F, eqs. 49–54). An EOS-free, strictly increasing
   auxiliary function has exactly one root $\mu_+ \in (0, h_0^{-1}]$, with
   $f(\mu_+) \ge 0 > f(0)$; $f$ is continuous, so a root lies in
   $(0, \mu_+]$. The proof holds for invalid conserved input and uses no EOS
   property except $h_0$.
5. **Uniqueness** (proved, §II G, App. A, eq. 65). At a root
   $\mathrm df/\mathrm d\mu \ge 1 - \hat v^2 > 0$ when $c_s < 1$, at all
   velocities and fields; with superluminal $c_s$, only if $v^2c_s^2 < 1$.
   Where $e$ hits $e_{\max}$, uniqueness needs condition eq. 66; an isentropic
   upper bound always satisfies it, and constant-$T$ or constant-$e$ bounds
   caused no problems in practice. For density out of range, uniqueness on
   the whole bracket is **not proved**; a sub-bracket on which $D/\hat W$ is
   valid is found instead (App. A, Fig. 2).
6. **Accuracy bounds** (derived to linear order, §II H, eqs. 69–74). With
   $\Delta \equiv \hat W^2\delta\mu/\mu$, every primitive's relative error is
   bounded by a multiple of $\Delta$ (e.g. $\delta\hat\rho/\hat\rho \le \hat v^2\Delta$,
   eq. 70); for the conserved variables $\vert\delta S_i\vert/\vert S_i\vert \le \Delta$
   and $\delta(1+q)/(1+q) \le 4v^2\Delta$ (eq. 74). The required $\delta\mu$
   tightens with $W$; $b$ does not enter; the entropy error is zero to linear
   order; $D$ is reproduced **exactly**. Round-off is excluded.
7. **Invalid states** (§III A). The scheme returns a projection onto the valid
   region by recomputing conserved variables from clamped primitives. If
   $e < e_{\min}$, **only $\tau$ changes**; if $e > e_{\max}$ all conserved
   variables can change, a correction meant only at fluid–vacuum boundaries
   or inside horizons.
8. **Implementation** (§IV A). RePrimAnd, C++, EOS-agnostic interface that
   enforces validity ranges. Root finder TOMS748 (Alefeld–Potra–Shi) from
   Boost: bracketing, inverse cubic interpolation, bounded step count,
   derivative-free; stopping criterion $\Delta$ with $\delta\mu$ the current
   bracket width. $\mu_+$ by Newton–Raphson on the smooth auxiliary function.
   A fully tabulated 3D nuclear EOS is not tested (§IV D).
9. **Round-off** (§IV B, measured and estimated). For $\Delta \lesssim 10^{-7}$
   the bounds are exceeded at high $W$ or very small $e$ and $\vert\mathbf v\vert$:
   at $W = 10^3$ and about 16 digits, $\Delta > 10^{-10}$; cancellation in $e$
   loses digits of order $z^2/e$ and $b^2W/e$, $z = W\vert\mathbf v\vert$.
   Including these, measured accuracy lies within the bounds (Fig. 3).
10. **Efficiency** (§IV C, measured). At most **23 EOS calls** for
    $\Delta = 10^{-8}$ over the test space; flat up to $W = 1000$ and $b = 10$
    (Fig. 4); about 40 steps at $b = 10^4$, $W = 10^3$, still without failure
    (Fig. 5). An average below 10 calls "in practice" is asserted.
11. **Comparison** (§IV D, Table I). Unlike the schemes of Noble, Siegel et al.
    (2018) and Cerdá-Durán ("Duran"), which use EOS derivatives, unbounded
    steps and an initial guess, this scheme and those of Neilsen and Newman
    need neither derivatives nor guesses and have bounded steps. Citing Siegel
    et al. (2018): all existing schemes fail somewhere for $W = 10$–$1000$,
    even for the ideal gas, and only Newman needs fewer than about 10 steps
    consistently. The success tolerance of Siegel et al. (2018) is, per the
    authors, unattainable by any scheme at $W \gtrsim 2\times10^3$ (small $B$)
    or $p/p_{\mathrm{mag}} \gtrsim 5\times10^8$ (small $\vert\mathbf v\vert$)
    because of cancellation in $e$; "all schemes shown in [33] exceed the
    tolerance already below $W<10^3$ at small $B$, where our scheme succeeds"
    — a comparison against the figures of Siegel et al., not a re-run. The
    authors concede a $T$-based scheme "might indeed be faster" with a
    $T$-based table.
12. **Error amplification** (§V B–C, measured by finite differences). In the
    Newtonian limit the relative error in $e$ amplifies the relative errors
    of $q$ and $b$ by factors of order $b^2/e$, and those of $q$ and $r_i$ by
    factors of order $\vert\mathbf v\vert^2/e$ (eq. 79, text-layer reading). In magnetically dominated regions perpendicular momentum is not
    amplified, but $e$ suffers cancellation. With $B = 10^{15}$ G a relative
    error $10^{-4}$ in $b$ or $q$ dominates $e$ at densities near
    $10^8$ g cm$^{-3}$ (Fig. 6). The loss is accepted as "a fundamental
    consequence of evolving the conserved variables"; no dual-energy or
    entropy fallback is proposed.
13. **Floor effects** (§V D). The zero-temperature floor biases the energy
    upward and causes **spurious heating** until the thermal energy reaches
    the width of the energy-error distribution; momentum does not drift
    because only $\tau$ changes. A random-walk test gives average momentum
    errors orders of magnitude below eq. 74.
14. **Coupling** (§I, §II C, §IV C). Point-wise algebraic inversion after each
    evolution step; no time-step constraint; no host code tested —
    benchmarks within GRMHD simulations are "reserved for future work".

**Tests** (§IV–V, all stand-alone, no hydrodynamic evolution). Robustness and
accuracy sweep (§IV B, Fig. 3): $z = W\vert\mathbf v\vert \in [0, 1000]$,
$b \in [0, 5]$, thermal $e \in [10^{-4}, 50]$, velocity parallel and
orthogonal to $\mathbf B$; ideal gas with $\gamma = 2$ and a hybrid MS1 EOS
with thermal index 1.8 (densities $10^6$–$10^{15}$ g cm$^{-3}$);
$\Delta = 10^{-8}$; recovery succeeds "without any exception" for valid input
and classifies out-of-range energies as invalid. Efficiency (§IV C,
Figs. 4–5): EOS calls against thermal energy, $z$ and $b$ up to $10^4$.
Siegel et al. tolerance (§IV D): reached in $W \le 10^3$, $b < 5$ for both
EOSs, except the ideal gas with $e \lesssim 0.005(W/10^3)^2$. Error
amplification (§V C, Fig. 6) and a random-walk floor-correction test (§V D)
with $\Delta \in \{10^{-7}, \dots, 10^{-10}\}$: no problematic behaviour of
$\mathbf v$, $W$, $e$, $p$ or $\mu$.

# Notation map

| Kastaun et al. (2021) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $D$, $\tau$, $S_i$ | $D$, $\tau$, $S_i$ | the $\sqrt\gamma$ volume element is omitted (§II C) |
| $\bar D$, $\bar\tau$, $\bar S_i$ | none (words) | fluid-only parts |
| $\rho$, $P$, $T$ | $\rho$, $p$, $T$ | |
| $\epsilon$ | $e$ | specific internal energy; the paper also uses $\epsilon^{ljk}$ (Levi-Civita) |
| $h$, $h_0$ | none; written $h_{\mathrm{rel}}$, $h_0$ on this page | relativistic specific enthalpy and its lower bound; **collision** with cell size $h$ |
| $W$, $v^i$ | $W$, $\mathbf v$ | |
| $z = Wv$ | local | |
| $E^i$ | $\boldsymbol{\mathcal E}$ | eq. 21 matches the registry definition |
| $B^i$ | $\mathbf B$ | Heaviside–Lorentz-type units ($\tfrac12(E^2+B^2)$ in $\tau$) |
| $c_s$ | $c_s$ | relativistic, $c_s^2 = \mathrm d\ln h/\mathrm d\ln\rho\vert_s$ (eq. 8) |
| $\Gamma$, $\Gamma_{\mathrm{th}}$ | $\gamma$, none (words) | ideal-gas index; thermal index of the hybrid EOS |
| $a = P/\rho_E$ | none (words) | **collision** with the scale factor $a$ |
| $\rho_E$ | none (words) | rest-frame fluid energy density |
| $\mu$, $x$, $q$, $r_i$, $b_i$, $f$, $\hat\mu$, $\hat\nu$, $\mu_+$ | local | master-function variables |
| $\Delta$ | local | root-finding accuracy $\hat W^2\delta\mu/\mu$; not a step size |
| $\epsilon_{\min}(\rho)$, $\epsilon_{\max}(\rho)$ | $e_{\min}(\rho)$, $e_{\max}(\rho)$ (words) | EOS validity box |
| $A_q$, $A_b$, $A_r$ | local | amplification factors (eqs. 80–82); $A$ collides with $A(u)$ |

# Pages created or updated

* Created [Primitive-variable recovery](/methods/primitive-variable-recovery.md).
* Updated [Dual-energy formalism](/methods/dual-energy-formalism.md).
* Also cited on [Athena++ (block-based AMR framework for astrophysical MHD)](/software/athena-plus-plus.md).
* Also cited on (batch 3) [AthenaK (performance-portable Kokkos version of the Athena++ AMR framework)](/software/athenak.md).

# Citations

1. `~/papers/mosaic/astrophysical-simulation-codes/2021-PRD-Kastaun-101103physrevd103023018.pdf`.
   * **Version.** arXiv:2005.01821v2 [gr-qc], 24 Jan 2021, 18 pages,
     REVTeX two-column: the preprint posted after publication, not the
     publisher PDF. Software: RePrimAnd V1.1, C++,
     doi:10.5281/zenodo.4075317 (ref. [34]).
   * **Identity.** doi:10.1103/PhysRevD.103.023018, checked on Crossref: title
     exact, three authors, Phys. Rev. D 103(2):023018, issued 2021-01-20.
   * **How it was read.** Text extraction, all sections; the text layer drops
     every $\epsilon$, so the equations on pp. 4, 5, 7, Table I and the
     $\epsilon_{\max}$ value (p. 9) were checked on rendered pages. Eqs. 51–62
     and App. A from the text layer; eq. 79 transcribed from the text layout
     and not reproduced here; Figs. 1–6 read from captions and text only.
   * **Recorded as printed.** No internal inconsistency flagged. Ref. [30]
     prints "L. D. Zanna" for L. Del Zanna.
   * **Reference list:** 42 printed entries (Crossref deposits 41; plausibly
     the Zenodo item [34] is not counted). No article titles printed; only
     [34] prints a DOI. Same-author-year suffixes in printed order
     (abbott-2017/-b/-c, ciolfi-2020/-b/-c). The printed Siegel & Metzger
     (2018, ApJ 858:52) maps to `siegel-2018-b`, and Siegel, Mösta, Desai &
     Wu (2018, ApJ 859:71) to the ingested [siegel-2018](/sources/siegel-2018.md).
