---
type: Result
title: "Order of accuracy behind captured shocks"
description: "Shock-capturing schemes of any nominal order are stated to converge only at first order downstream of a moving shock, because a captured shock's position is known only to O(Δx), and to emit spurious oscillations behind slowly moving shocks; the page records the claim, its model-problem basis as recalled, steady nozzle runs with downstream orders near two and near four or above, and the remedies named (subcell resolution, shock fitting and tracking)."
status: established
aliases: [first-order convergence behind shocks, post-shock accuracy, downstream order of accuracy, global first order of shock capturing, globally first-order accurate, post-shock oscillations]
tags: [shock-capturing, weno, shock-tracking]
timestamp: 2026-11-17T08:44:05Z
---

# Order of accuracy behind captured shocks

A shock-capturing scheme reaches its design order in smooth regions measured away from a discontinuity:
for scalar problems "the full designed order of accuracy of the WENO scheme is achieved if we measure the
error away from the discontinuity" ([Shu (2009a)](/sources/shu-2009.md), §3.5.2). The review of [Pirozzoli (2011a)](/sources/pirozzoli-2011.md) (§3.5) states that this does
not extend to the region behind a moving shock: "even (nominally) uniformly high-order schemes yield
first-order accurate solutions downstream of moving shocks, mainly because shocks have zero measure, and
therefore their location is only known to $O(\Delta x)$ on a finite grid". Its Summary 5 states the
consequence for the whole domain: shock-capturing methods "are always globally first-order accurate for
unsteady problems, as the shock location is unknown to $O(\Delta x)$", and its conclusions that "the
global order of accuracy of shock-capturing schemes in unsteady problems is always reduced to unity"
(§6). The review calls this "a major flaw of shock-capturing schemes, often disregarded".

**Basis as recalled.** The review cites the loss as "highlighted in model scalar shock-sound interaction
problems" (Casper & Carpenter 1998; Engquist & Sjögreen 1998), relates it to "the slow convergence of
apparently simple shock/turbulence interaction calculations" (Larsson & Lele 2009), and points to
Efraimsson & Kreiss (1999) for "an interpretation of the pathology in terms of numerical viscosity"
(§3.5). None of these works is ingested. The review states that the pathologies are "apparently
unavoidable, unless one reverts to special techniques, such as subcell resolution (Harten 1989) or even
to shock-fitting" (§3.5), and that they "can only be overcome by some form of shock-fitting" (§6), while
calling shock fitting "only feasible in cases in which the shock topology is extremely simple and no
shock wave forms during the calculation" (§3).

**Later statements.** [Huang & Zahr (2022)](/sources/huang-2022.md) (§1) write that limiters, WENO and
artificial viscosity are first order near shocks, "which translates into a globally first-order accurate
scheme", as the motivation for [implicit shock tracking](/methods/implicit-shock-tracking.md); their own
evidence is one artificial-viscosity run on the quasi-1D nozzle at $N=2$, "limited to sub-first-order
convergence rate", against $O(\Delta x^{N+1})$ for their tracking method (§6.3, Table 3). Naudet & Zahr
(2024, §1) repeat the statement without naming a norm or a region (recorded on the shock-tracking page).

## A steady contrast: the standing shock of a nozzle

The claim above concerns moving shocks in unsteady problems; a standing shock is outside its scope. On
the steady quasi-1D nozzle, the run of Chou & Shu that [Shu (2009a)](/sources/shu-2009.md)
(§3.5.2, Table 3.1) reproduces measures the density error outside three cells around the standing shock
with a fourth-order residual-distribution WENO scheme. Downstream, the $L^1$ orders are 1.98–2.83 with
regular integration in the shock cell and 3.90–4.93 with "subcell separate integrations" there; Shu
states that the loss is a systems effect, "characteristics belonging to fields other than that of the
discontinuity may cross the discontinuity and carry the numerical error at the discontinuity into smooth
regions", avoided by "a subcell resolution technique" in the shock cells, and notes that even degenerate
downstream errors are "typically still much smaller than that of a lower order scheme on the same mesh"
([quasi-1D nozzle flow](/benchmarks/quasi-one-dimensional-nozzle-flow.md)). Shu adds that for a linear
scheme and a linear PDE "the designed high order accuracy is maintained in integrated quantities of the
numerical solution, such as moments against smooth functions", which post-processing can turn into
design-order point values (§3.5.2).

## Post-shock oscillations

For systems, captured shocks also emit spurious oscillations, "especially in the case of slowly moving
shock" (Arora & Roe 1997, as recalled by Pirozzoli 2011a, §3.5), which "may prevent the accurate
prediction of shock/sound and shock/turbulence interactions, as observed by Johnsen et al. (2010)". The
review lists their quantitative effect as unknown (§6, Future Issue 1). In steady computations,
[Fu (2023)](/sources/fu-2023.md) (§4.2) names slight post-shock oscillations as the reason the WENO and
TENO residuals stall ("an open problem"). [Liang & Fu (2026)](/sources/liang-2026.md) show post-shock
oscillations in WENO5-Z and TENO5 (§5.2, Fig. 7; §5.4, Fig. 17) and residual stalls (§§5.2–5.6), but
attribute the stall to the time variation of the reconstruction formula at fixed interfaces (§1, §3.2.3;
see [TENO](/methods/targeted-eno.md) and [steady shock problems](/benchmarks/steady-shock-problems.md)).

## Qualifications

- **Scope.** The result as scoped by the review concerns the region downstream of moving shocks in
  unsteady problems (after Casper & Carpenter 1998 and Engquist & Sjögreen 1998); "always globally
  first-order accurate" is the review's wording (Summary 5). The steady nozzle data above are a contrast
  outside that scope.
- **Norm and region.** None of the sources names the norm. *(Compiler check, not in the sources:
  "globally" is read as error norms over a domain that contains the region crossed by a moving shock;
  the pointwise error at a captured shock is $O(1)$ for any capturing scheme, and the smeared shock alone
  makes the $L^1$ error $O(\Delta x)$ even for a steady shock, which is why Shu's table excludes the
  cells around the shock.)*
- **Not a statement about smooth solutions.** The schemes concerned converge at design order on smooth
  solutions in the bundle's tests (e.g. [WENO-JS](/methods/weno-js-reconstruction.md)); the first-order
  statement concerns solutions with shocks.

# Citations

- [Pirozzoli (2011a)](/sources/pirozzoli-2011.md) — §3; §3.5; §6; Summary 5; Future Issue 1 (review).
- [Huang & Zahr (2022)](/sources/huang-2022.md) — §1; §6.3, Table 3, Fig. 26 (arXiv v2).
- [Shu (2009a)](/sources/shu-2009.md) — §3.5.2, Fig. 3.1, Table 3.1 (reproduced from Chou & Shu): design order away from discontinuities, systems effect, integrated quantities.
- [Fu (2023)](/sources/fu-2023.md) — §4.2: post-shock oscillations stall the steady residual.
- [Liang & Fu (2026)](/sources/liang-2026.md) — §1, §3.2.3: stall attributed to the time variation of the interface formula; §5.2, Fig. 7; §5.4, Fig. 17: post-shock oscillations of WENO5-Z and TENO5; §§5.2–5.6: residual stalls.
