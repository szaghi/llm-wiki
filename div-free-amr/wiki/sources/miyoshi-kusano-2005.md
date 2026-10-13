---
type: Source
title: "Miyoshi & Kusano (2005) — A multi-state HLL approximate Riemann solver for ideal magnetohydrodynamics"
description: "The HLLD solver: constant normal velocity over the Riemann fan gives four closed-form intermediate states separated by the entropy wave and two Alfvén waves, exact for isolated contact, tangential and rotational discontinuities, with a 1D positivity argument and Roe-level accuracy at lower cost; multi-D tests use mixed GLM cleaning."
resource: "doi:10.1016/j.jcp.2005.02.017"
source_kind: paper
authors: [Miyoshi T., Kusano K.]
year: 2005
venue: "J. Comput. Phys. 208:315-344"
local_file: "/home/stefano/papers/mosaic/div-free-amr/2005-JCP-Miyoshi-101016jjcp200502017.pdf"
tags: [riemann-solver, godunov, mhd, positivity, shock-capturing]
timestamp: 2026-10-13T00:00:00Z
---

# Summary

The paper builds **HLLD**
([HLLD Riemann solver](/methods/hlld-solver.md)), a four-intermediate-state
HLL-type approximate Riemann solver for 1D ideal MHD, from one assumption:
the normal velocity is constant over the Riemann fan, the HLLC assumption
(§5.1). That assumption forces constant total pressure across the fan,
excludes slow shocks inside it, and admits rotational (Alfvén)
discontinuities. The fan is therefore split by the entropy wave and two
Alfvén waves into four states; for vanishing normal field it collapses to
the two-state HLLC structure, and without a field it is HLLC (§5.1,
p. 328). All intermediate states follow in closed form from the
Rankine–Hugoniot conditions (eqs. 38–66). The solver resolves isolated
contact, tangential and rotational discontinuities exactly, and isolated
fast shocks exactly when the outer speeds equal the shock speed (§5.2).
Positivity of density and pressure is argued in 1D under a bound on the
outer speeds in terms of the fast speed, given two prerequisite
inequalities of which one is verified only for strong expansions (§5.3).
First-order tests show HLLD as accurate as Roe on 1D shock tubes and on
Orszag–Tang (with mixed GLM cleaning), more robust than Roe on a
super-fast expansion, and cheaper (§§6–7). Divergence: none in 1D; in
multi-D, CT is left "beyond the scope", and the Orszag–Tang runs use mixed
GLM without stated parameters or a divergence measurement.

# Key claims

1. **Founding assumption** (§5.1, p. 324; eqs. 39–40). Normal velocity
   constant over the fan, hence total pressure constant. "Slow shocks
   cannot be formed inside the Riemann fan. Rotational discontinuities
   propagating with the Alfvén waves, on the other hand, may be generated."
   Four intermediate states (Fig. 3).
2. **Middle-wave speed and total pressure** (eqs. 38, 41). The middle
   speed is the HLLC formula (eq. 14) with gas pressure replaced by total
   pressure; the fan's total pressure follows in closed form.
3. **Outer states** (eqs. 42–48) from the jump conditions across the outer
   waves: density scales by the ratio of relative speeds (eq. 43); the
   transverse velocity and field have closed forms (eqs. 44–47); energy
   eq. 48. These coincide with Gurski's "extended" HLLC-type states
   (p. 326).
4. **Degeneracy** (pp. 326, 328). A 0/0 appears in eqs. 44–47 when the
   middle speed equals the normal velocity, the outer speed equals the
   normal velocity plus or minus the fast speed, the transverse field
   vanishes and $B_n^2 \ge \gamma p$; the outer transverse values are then
   set to the unperturbed ones ("there is no shock across" that wave). No
   numerical tolerance is given. For $B_n = 0$ the Alfvén waves coincide
   with the middle wave and the inner states are not needed; the inner
   jump conditions (eq. 53) "become unsolvable" there.
5. **Inner states** (eqs. 49–63). Density and total pressure equal the
   outer ones (eqs. 49–50); the Alfvén speeds are the middle speed minus
   or plus $|B_n|$ over the square root of the outer density (eq. 51). The
   jump conditions across the Alfvén waves alone "appear not to be
   solvable"; with continuity of transverse velocity and field across the
   middle wave (eqs. 54–57) and the integral conservation law over the fan
   (eq. 58), the inner transverse velocity and field are
   square-root-density-weighted averages with a $\mathrm{sign}(B_n)$
   correction (eqs. 59–62); energy eq. 63. These satisfy the Alfvén-wave
   jump conditions (eq. 52).
6. **Flux** (eqs. 64–66): six cases selected by the signs of the five
   wave speeds.
7. **Outer speeds** (p. 328). Davis (eq. 12), Einfeldt (eq. 13), or the
   simple bounds of eq. 67 (extreme normal velocity plus or minus the
   larger fast speed). The tests use eq. 67: "indistinguishable from those
   by (13) in spite of not resolving isolate fast shocks exactly" (p. 332).
8. **Exact resolution** (§5.2, eqs. 68–87). Isolated tangential (eq. 71),
   contact (eq. 73) and rotational discontinuities (eqs. 75–80), for any
   outer-speed estimate; an isolated fast shock (eq. 87) only when the
   outer speed equals the exact shock speed, so eq. 13 is "appropriate …
   in this particular viewpoint" (p. 330). Slow shocks are not resolved
   exactly.
9. **Positivity in 1D** (§5.3, eqs. 88–100). Densities of all four states
   are positive (eq. 93). Positive outer pressure requires the right outer
   speed to exceed the right normal velocity by more than
   $\sqrt{(\gamma-1)/(2\gamma)}$ times the right fast speed, and the mirror
   bound on the left (eqs. 97–98, 100); the inner pressure then equals it
   (eq. 99). This is the HLLC condition (eq. 22) with the sound speed
   replaced by the fast speed. The derivation (eqs. 94–95) assumes that the
   outer speed exceeds the normal velocity by at least the fast speed,
   which eq. 67 assures, and that the outer speed exceeds the middle speed
   by at least the fast speed, of which the authors write "it is not so
   easy to confirm whether the other inequality … is satisfied or not at
   any situation"; they verify it only for strong expansions (p. 332).
   Two wordings coexist on p. 332: "since the HLLD solver for MHD clearly
   satisfies (98), our solver ensures the positivity preserving property
   (90)", and "the HLLD solver is thought to be a positively conservative
   scheme".
10. **HLL by averaging** (p. 332): "The present proof will also be
    applicable to the single-state HLL Riemann solver since the one
    intermediate state of the HLL solver is given by the average of the
    HLLD intermediate states contained in G" ($\mathcal G$).
11. **Against Gurski** (pp. 331–332): "Gurski [13] misled a 'stronger
    condition' for positivity in view of the inequality (95)"; "It is
    obvious that (98) and (100) are stronger than the conditions by
    Gurski [13]."
12. **Positivity is 1D only** (§1, p. 317; §7, p. 343): "discussions of
    positivity here are restricted to one-dimensional MHD"; "exact
    positivity preserving property in multi-dimensions may not be
    necessarily assured even in the HLLD solver."
13. **Cost** (§7, p. 343). Orszag–Tang at $N = 400$: CPU ratios
    HLL : HLLD : Roe $= 1 : 1.35 : 2.67$ in the flux calculation and
    $1 : 1.13 : 1.69$ for the whole run.
14. **Earlier HLLC-type MHD solvers** (§4.2, §6.1). Gurski's HLLC-G uses
    HLL averages of the transverse quantities when $B_n \ne 0$ and does not
    reduce to HLLC as $B_n \to 0$; Gurski's "extended" solver breaks the
    jump condition across the middle wave and oscillates; Li's HLLC-L is
    conservative over the fan but cannot reach the HLLC limit either. Their
    smeared rotational discontinuities are attributed to "the assumption
    that the magnetic field is constant over the Riemann fan" (p. 333).
15. **Extension remark** (§7): HLLD for a background-field-split system by
    subtracting the background magnetic pressure from the total pressure in
    eq. 41; "A detailed algorithm will be given in the future paper."
16. **Divergence treatment.**
    * 1D: the normal field is a constant parameter "due to the divergence
      free condition" (§2, p. 317).
    * Multi-D (§6.2, pp. 338–339): CT (Evans–Hawley) "can maintain the
      divergence free condition within machine accuracy, there are no
      general guidelines to apply any one-dimensional MHD solver properly.
      Thus, the application of the CT method to the HLLD solver is beyond
      the scope of this paper." Add-on alternatives listed: projection
      (Brackbill–Barnes), diffusion (Marder), transport (Dedner; Powell).
      **Mixed GLM** ([GLM cleaning](/methods/glm-divergence-cleaning.md);
      [Dedner et al. (2002)](/sources/dedner-2002.md)) is adopted for the
      Orszag–Tang runs as "easy to implement", "fast" and "conservative for
      the physical quantities"; $c_h$ and $c_p$ are not stated.
    * The $N = 800$ reference solution uses **projection** cleaning, called
      "one of the most accurate and reliable method at present"
      ([Tóth (2000)](/sources/toth-2000.md); p. 341).
    * No divergence measurement is reported.

# Tests

Common: $\gamma = 5/3$; first order in space and second order in time
unless stated; outer speeds by eq. 67; the Roe comparison uses Balsara's
Roe average.

1. **Dai–Woodward shock tube** (§6.1, Figs. 5–7). 800 points, CFL 0.8,
   $t = 0.2$; two fast shocks, two rotational discontinuities, two slow
   shocks and a contact
   ([Dai & Woodward (1994)](/sources/dai-woodward-1994.md)). HLLD is
   "indistinguishable" from Roe; HLL smears the contact and rotational
   discontinuities. HLLC-G and HLLC-L resolve the contact but smear the
   rotational discontinuities "extremely"; second-order HLLC-L (minmod)
   still does not reach first-order HLLD (Fig. 7).
2. **Brio–Wu shock tube with $\gamma = 5/3$** (Ryu–Jones version, Fig. 8;
   [Brio & Wu (1988)](/sources/brio-wu-1988.md),
   [Ryu & Jones (1995)](/sources/ryu-jones-1995.md)). $B_n = 0.75$,
   $t = 0.1$. HLLD ≈ Roe, slightly more smeared at the slow compound wave
   and slow shock; compound-wave density peak 0.820 (Roe) and 0.815
   (HLLD). Roe undershoots slightly at the tail of the compound
   rarefaction; HLLD does not.
3. **Slow switch-off shock** (Falle et al.; Fig. 9). HLLD resolves the
   slow shock as well as Roe "despite the loss of information on the slow
   waves"; HLL does not. Start-up error in every solver.
4. **Slow switch-off rarefaction** (Falle et al.; Fig. 10). HLL and HLLD
   fine; Roe violates the entropy condition at $x = 0$, cured by the
   Harten–Hyman entropy fix.
5. **Super-fast expansion** (Fig. 11). Symmetric outflow at fast Mach
   $u_0$, $B_n = 0$, $t = 0.05$. At $u_0 = 3$ all solvers stay physical; at
   $u_0 = 3.1$ Roe with entropy fix "fails after several time steps"; HLL
   and HLLD keep positivity.
6. **Orszag–Tang vortex** (§6.2, Tables 1–2, Figs. 12–13;
   [Orszag–Tang vortex](/benchmarks/orszag-tang-vortex.md)). Unit-wavenumber
   form on $[0,2\pi]^2$ with density $\gamma^2$ and pressure $\gamma$,
   periodic, $N^2$ with $N = 50$–$400$, CFL 0.4, first and second order
   (MC limiter), mixed GLM, temperature compared at $t = \pi$. Relative
   $L^1$ temperature difference from Roe (Table 1), $N = 50/100/200/400$:
   first-order HLL 0.0779/0.0579/0.0453/0.0353, first-order HLLD
   0.0054/0.0043/0.0034/0.0024; second-order HLL 0.0239/0.0143/0.0083/0.0046,
   second-order HLLD 0.0040/0.0028/0.0027/0.0011 — HLLD below 1% in every
   case. Difference from the $N = 800$ reference (Table 2): first order HLL
   0.4106/0.3340/0.2620/0.1960, HLLD 0.3661/0.2953/0.2257/0.1644, Roe
   0.3650/0.2950/0.2257/0.1647; second order HLL 0.1580/0.0844/0.0394/0.0172,
   HLLD 0.1365/0.0676/0.0308/0.0132, Roe 0.1357/0.0675/0.0315/0.0131.

# Notation map

| Miyoshi & Kusano | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $U$, $F$ | $U$; words for the flux | conserved state, physical flux |
| $B_x$ (constant normal field) | $B_n$ | |
| $\mathbf v = (u,v,w)$, $\mathbf B = (B_x,B_y,B_z)$ | words (normal and transverse components) | |
| $p_T = p + \lvert\mathbf B\rvert^2/2$ | words (total pressure) | no $4\pi$ |
| $c_a$, $c_f$, $c_s$ | words (Alfvén, fast, slow speeds) | |
| $\lambda_1,\dots,\lambda_7$ | $\lambda_k$ | |
| $S_L$, $S_R$, $S_M$, $S^*_L$, $S^*_R$ | words (outer, middle, Alfvén signal speeds) | **collision:** registry $S(U)$ is the Powell source vector |
| $U^*_\alpha$, $U^{**}_\alpha$, $F^*_\alpha$, $F^{**}_\alpha$ | words (outer and inner fan states) | **collision:** registry stars mark provisional base-scheme fields ($B_h^*$, $f^{x,*}$) |
| $G$ (set of physical states) | $\mathcal G$ | same definition |
| $\xi$, $\eta$, $\zeta$ | words | local to the positivity proof |
| $\gamma$ | $\gamma$ | |
| $T = p/\rho$, $\delta T_{Roe}$, $\delta T_{ref}$ | words | test metrics |

# Pages created or updated

* Created this Source page.
* Created [HLLD Riemann solver](/methods/hlld-solver.md).
* Updated [HLL Riemann solver](/methods/hll-solver.md): the HLLD-derived positivity statement for HLL, as a qualification next to Wu & Shu.
* Updated [Orszag–Tang vortex](/benchmarks/orszag-tang-vortex.md), [GLM cleaning](/methods/glm-divergence-cleaning.md) and [positivity–divergence coupling](/results/positivity-divergence-coupling.md).

# Citations

1. `/home/stefano/papers/mosaic/div-free-amr/2005-JCP-Miyoshi-101016jjcp200502017.pdf`.
   * **Version read.** The published journal version (Elsevier typeset,
     30 pp.). Received 15 November 2004, revised 7 February 2005, accepted
     18 February 2005.
   * **Identity.** doi:10.1016/j.jcp.2005.02.017, printed on page 1;
     checked on Crossref: title and authors match; J. Comput. Phys. vol.
     208, issue 1, pp. 315–344, issued September 2005; reference count 30.
   * **How it was read.** pdftotext loses minus signs, stars and primes;
     every formula cited was checked on page renders (pp. 324–328, 331–333,
     336, 338, 341). Not reproduced: the fast/slow speed formula eq. 3
     (garbled in the text layer, page not rendered) and the intermediate
     lines of eq. 94. The time integrator, the variables reconstructed at
     second order and the GLM parameters are not stated in the paper.
   * **Recorded as printed.**
     * "As found form (12), (13), or (67)" (p. 331).
     * "Gurski [13] misled a 'stronger condition'" (p. 331).
     * The reference list prints Orszag's first initial as "A.".
     * Batten et al. is printed "SIAM J. Sci. Statist. Comput. 18 (1997)
       1553".
   * **Reference list.** 30 entries, all merged. Harten & Hyman 1983 is
     `harten-1983-c`; Harten, Lax & van Leer is the ingested
     [Harten, Lax & van Leer (1983)](/sources/harten-lax-vanleer-1983.md);
     Orszag & Tang is `orszag-tang-1979`; Ryu & Jones and Dai & Woodward are
     the ingested `ryu-jones-1995` and `dai-woodward-1994`; the authors' own
     2001 JGR paper is `miyoshi-2001`. The entry's note records that
     stone-2008 prints the volume and page as "315, 344". Key renamed
     `miyoshi-2005` → `miyoshi-kusano-2005`. The bibliography holds 3834
     entries after this batch.
