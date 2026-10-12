---
type: Source
title: "Smith et al. (2017) — Grackle: a Chemistry and Cooling Library for Astrophysics"
description: "Method and software paper of Grackle, an open-source library extracted from Enzo that integrates non-equilibrium primordial chemistry and radiative cooling as a point-local, sub-cycled source step for a host code: sequential first-order backward-difference species updates under a 10% change limit, Cloudy metal-cooling tables, dust, UV backgrounds with self-shielding, a C/Fortran/Python API, unit and answer tests, and serial and OpenMP performance."
resource: "doi:10.1093/mnras/stw3291"
source_kind: paper
authors: [Smith B.D., Bryan G.L., Glover S.C.O., Goldbaum N.J., Turk M.J., Regan J., Wise J.H., Schive H.-Y., Abel T., Emerick A., O'Shea B.W., Anninos P., Hummels C.B., Khochfar S.]
year: 2017
venue: "Mon. Not. R. Astron. Soc. 466:2217–2234"
local_file: "~/papers/mosaic/astrophysical-simulation-codes/2017-MNRAS-Smith-101093mnrasstw3291.pdf"
tags: [software, cooling, chemistry, time-integration, cosmology, performance, verification]
timestamp: 2026-10-12T00:00:00Z
---

# Summary

Grackle is an open-source library, extracted in 2012 from Enzo's cooling and
chemistry solver (itself from Anninos et al. 1997), that integrates
non-equilibrium primordial (H, D, He) chemistry and radiative cooling and
heating for a host hydrodynamics code, one element at a time with no spatial
coupling (§2, §7.2.1). It offers 6-, 9- and 12-species networks (§3.1), a
tabulated equilibrium mode, Cloudy metal-cooling tables scaled by metallicity
(§4.2), a dust model (§4.3), redshift-dependent UV backgrounds with optional
self-shielding (§5), and hooks for host radiative-transfer rates (§5.2). Species
are advanced by a first-order backward-difference update applied sequentially
in a fixed order, sub-cycled under a 10% change limit inside the host time step
(§3.2, §4). The paper documents the API and the Python wrapper Pygrackle (§6),
a pytest unit and answer-test suite (§7.1), serial and OpenMP performance
(§7.2), validity ranges (§8.1) and 14 host codes (§8.2). Merged into
[Grackle](/software/grackle.md),
[integrating cooling and chemistry source terms](/methods/radiative-cooling-integration.md)
and [Enzo](/software/enzo.md).

# Key claims

1. **Rate equations** (§3.2, eqs. 5–6).
   $\partial_t n_i = \sum_j\sum_l k_{jl}n_jn_l + \sum_j I_jn_j$, regrouped as
   $\partial_t n_i = C_i(T, n_j) - D_i(T, n_j)\,n_i$.
2. **Backward-difference update** (§3.2, eq. 7).
   $n^{t+\Delta t} = (C^{t+\Delta t}\Delta t + n^t)/(1 + D^{t+\Delta t}\Delta t)$. A full BDF scheme
   is not implemented "due to the difficulty of evaluating the $C_i$ and $D_i$
   at the advanced time"; it is mimicked "through a set of partial updates
   combined with sub-cycling": species updated in a fixed order, each using the
   densities already updated in the step. Higher-order alternatives were not
   better "for the level of accuracy required" (Anninos et al. 1997; asserted,
   not shown).
3. **Update order** (§3.2). H, H$^+$, e$^-$, He, He$^+$, He$^{++}$ (empirical
   ordering of Anninos et al. 1997); nine species add H$_2$, H$^-$, H$_2^+$;
   twelve add D, D$^+$, HD.
4. **H$_2^+$ in equilibrium** (§3.2, eq. 8): its time scale is short enough that
   its density is set algebraically.
5. **Chemistry sub-cycle** (§3.2, eq. 9).
   $\Delta t = 0.1\min(n_{\mathrm H}/\dot n_{\mathrm H}, n_{\mathrm{e^-}}/\dot n_{\mathrm{e^-}})$: H and e$^-$
   change by at most 10% per sub-step. After more than 50 sub-cycles without
   completing the host step, analytic time derivatives are replaced by
   numerical ones, to stop the integrator "taking very small steps and
   regularly overshooting the equilibrium value".
6. **Energy** (§4, eqs. 10–11). $de/dt = -\dot e_{\rm cool} + \dot e_{\rm heat}$;
   chemistry and cooling "are solved together, using a simple first-order
   integrator", sub-cycled with $\Delta t \le 0.1\,e/\dot e$; the sub-step is the
   minimum of eqs. 9 and 11.
7. **Host coupling** (§3.2, §6.1, §7.2.1). Grackle receives a time step and the
   fields and updates species and internal energy in place
   (`solve_chemistry`); "each discretization point (particle or cell) can be
   evolved independently of the others". The calling stage within a host step
   and any conservation property of the sequential update are not stated.
8. **Temperature** (§4.1.2, eqs. 12–14). For the tabulated solver,
   $e = kT/((\gamma-1)\mu m_{\mathrm H})$ is solved iteratively from $\mu = 1$ with
   a damped update and a metal correction, converging "to within 1% in just a
   few iterations" (asserted). The non-equilibrium solver computes $T$ directly,
   "with no iterative processes" (§7.2.2).
9. **Tables** (§4.1.2, §4.2). Primordial tables 1D in $T$ or 2D/3D in
   $(z, \rho, T)$, interpolated linearly in log space; metal tables at Solar
   metallicity scaled by local metallicity, elements up to Zn, built with Cloudy
   via CIALoop, HDF5. UV backgrounds: Faucher-Giguère et al. (2009), Haardt &
   Madau (2012), or none.
10. **CMB floor** (eq. 15). $\Lambda_{\rm final}(T) = \Lambda(T) - \Lambda(T_{\rm CMB})$,
    also for metals.
11. **Dust** (§4.3, eqs. 16–18). Grain temperature from instantaneous balance,
    solved by Newton's method (no tolerance printed); gas–grain transfer after
    Hollenbach & McKee (1989); piecewise grain opacity; CMB-only grain heating.
12. **Self-shielding** (§5.1, eqs. 19–20). Rahmati et al. (2013) fit, three
    variants, off by default; no shielding correction for the metal tables,
    which "can cause large errors".
13. **API** (§6.1). `solve_chemistry`, `calculate_cooling_time`,
    `calculate_temperature`, `calculate_pressure`, `calculate_gamma`;
    `chemistry_data`, units and `grackle_field_data` structs (the 3.0 API);
    C, C++ and Fortran bindings; Python via Cython (Pygrackle, §6.2).
14. **Parallelism** (§7.2.1). No communication; "completely thread-safe after
    the initialisation step"; Fortran-ordered arrays; OpenMP over the outer
    $j, k$ loops; compute kernels in Fortran.
15. **Validity** (§8.1, Fig. 7). About 1 K to $10^9$ K; metal table
    $10^{-6} < n < 10^{12}$ cm$^{-3}$; no NLTE→LTE transition, so extrapolating
    above the table "may result in vast over-prediction"; optically thin only.
    The cooling length $c_s t_{\rm cool}$ (Fig. 8) must be resolved, else losses
    are over-predicted in a run-away cycle.
16. **Host codes** (§8.2). AREPO, ART-I, ART-II, CHANGA, Cosmos++, Enzo,
    Gadget-3, GAMER, GASOLINE, Gear, Gizmo, RAMSES, SPHS, SWIFT. The primordial
    chemistry is "closely based on" Enzo's, but includes processes absent from
    Enzo 2.5 (§3), e.g. tunnelling in H$_2$ collisional dissociation (§3.1).

**Tests** (§7; all through Pygrackle under py.test; answer tests compare with
stored outputs validated by manual inspection, i.e. regression, not
correctness). Unit-system invariance: cooling times agree to 4 decimal places
across unit systems; density units can differ by "roughly 31 orders of
magnitude" before that is lost (§7.1.1). Collisional ionization equilibrium
against analytic CIE, $10^4$–$10^9$ K, tolerance not printed (§7.1.2).
Cooling-rate answer test, 10 K to $10^9$ K, all solvers (§7.1.3, Fig. 2).
Constant-density cooling, $10^6$ K, 100 Myr, steps of 1% of the cooling time
(§7.1.4, Fig. 3). One-zone free-fall collapse at $Z = 0$ and $10^{-3}Z_\odot$
(§7.1.5, Fig. 4). Serial performance (§7.2.2, $64^3$ containers, one Xeon E5645
core): $8.6\times10^5$, $5.7\times10^5$, $3.2\times10^5$ updates/s (equilibrium,
6-species, 9-species); 6- and 9-species take 50% and 164% more time;
1.01 and 2.67 sub-cycles per solve; cost is set by total sub-cycles. OpenMP
(§7.2.3, 20 threads, two Xeon E5-2670 v2): efficiency ~60–90% at $16^3$ and
~80–90% at $64^3$ for the expensive routines. No convergence-order study, no
comparison with a stiff reference integrator, no code-to-code comparison.

# Notation map

| Smith et al. (2017) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $e$, $T$, $\rho$, $p$ | $e$, $T$, $\rho$, $p$ | |
| $\gamma$ | $\gamma$ | **collision:** in §6.2.2 (eq. 25) $\gamma \equiv \partial\ln p/\partial\ln\rho$ is an effective polytropic index of the one-zone model |
| $\Delta t$ (eqs. 7, 9, 11) | none (words: sub-cycle step) | registry $\Delta t$ is the host step |
| $n_i$, $C_i$, $D_i$, $k_{jl}$, $I_j$ | none (words) | species number density, creation rate, destruction coefficient, rate coefficients |
| $\Lambda$, $\Gamma$ | none (words) | cooling and heating rates; **paper-internal collision:** $\Gamma$ is also a photoionization or collisional ionization rate |
| $\dot e_{\rm cool}$, $\dot e_{\rm heat}$ | part of $s(u)$ | |
| $\mu$, $m_{\mathrm H}$, $k$ | none (words) | **collision:** $k$ (Boltzmann) against rate coefficients $k_{jl}$ |
| $t_{\rm cool}$, $c_st_{\rm cool}$ | none (words) | cooling time, cooling length |
| $T_{\rm gr}$, $\kappa_{\rm gr}$ | $\kappa$ with words | grain temperature, grain opacity |
| $z$ | none (words) | redshift; registry has $a$ |
| $G$ | $G$ | |
| $f$ (eq. 24), $t_{\rm ff}$, $t_{\rm col}$ | none (local) | one-zone collapse model; $f$ **collides** with flux $f$ |

# Pages created or updated

* Created [Grackle](/software/grackle.md),
  [Integrating cooling and chemistry source terms](/methods/radiative-cooling-integration.md).
* Updated [Enzo](/software/enzo.md).

# Citations

1. `~/papers/mosaic/astrophysical-simulation-codes/2017-MNRAS-Smith-101093mnrasstw3291.pdf`.
   * **Version.** arXiv:1610.09591v2 (14 Dec 2016), MNRAS LaTeX preprint
     ("Preprint 15 December 2016"), 20 pages; post-referee accepted manuscript
     (the acknowledgements thank the referee), not the typeset article; page
     numbers cited are the preprint's. Library versions in Table 2 run from 1.0
     (2014-01-10) to 3.0 (2016-11-01); the API described is 3.0. Repository:
     bitbucket.org/grackle/grackle (Table 1).
   * **Identity.** doi:10.1093/mnras/stw3291, checked on Crossref: title and 14
     authors as on page 1, Mon. Not. R. Astron. Soc. 466(2):2217–2234,
     published online 2016-12-17, issue 2017-04-11.
   * **How it was read.** Text extraction, all 20 pages (pdftotext reported an
     xref reconstruction but extracted completely); eq. 8 read from the
     rendered page 5. Figures read for captions and axes only.
   * **Recorded as printed.** Eq. 9 prints no absolute values on $\dot n$. Eq. 14
     has total $\rho$ in both left-hand terms. The $k$ indices of eq. 8 are
     internal Grackle numbering, undefined in the paper. 9-species "164%" more
     time, while $8.6/3.2 \approx 2.69$ gives ~169% (rounding of the printed
     rates, not corrected). The §6.1 listing accesses `grackle_data` with `.`
     although the text calls it a pointer. No tolerance for the dust Newton
     solve or the CIE test.
   * **Reference list:** 137 printed entries (matches the Crossref count), no
     titles (MNRAS style). Same-key suffixes: glover-2008 (AIP Conf., the only
     printed DOI, 10.1063/1.2905558) / glover-2008-b (Glover & Abel);
     revaz-2012 / revaz-2012-b; savin-2004 / savin-2004-b; turk-2011 (2011a) /
     turk-2011-b (2011b).
