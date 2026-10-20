---
type: Method
title: "Parallel-in-time integration"
description: "Parallel-in-time methods distribute the time direction over processes: across the steps (Parareal, pipelined SDC), through an all-at-once space-time solve (ParaDiag), or across the method (diagonal SDC). The page gives the taxonomy and how each source's speedup was measured, modelled or only predicted."
status: established
aliases: [PinT, time-parallel time integration, parallel in time, space-time parallelism, parallelism across the steps, parallelism across the method]
tags: [parallel, linear-algebra, stiff, verification]
timestamp: 2026-10-20T10:00:00Z
---

# Parallel-in-time integration

**Parallel-in-time (PinT) integration** assigns different parts of the time
direction, or of one time step, to different processes. The motivation shared by
the sources is that spatial parallelism saturates: once a spatially distributed
solver stops scaling, the only remaining direction is time
([Gander & Palitta (2024)](/sources/gander-2024.md), §1;
[Muralikrishnan & Speck (2025)](/sources/muralikrishnan-2025.md), §1). Time and space
parallelism multiply: 1000 spatial cores times 4 time-parallel threads give 4000
cores ([Čaklović et al. (2025)](/sources/caklovic-2025.md), §1.1). Muralikrishnan &
Speck (App. A.4) move processes to the time direction only once the spatial parallel
efficiency falls below 50 %. Throughout, the interval is cut into $N$ time slices
$T_0<\dots<T_N$ of length $\Delta T$, with $h$ the step inside a slice.

## Taxonomy

Čaklović et al. (2025, §1.1) follow Gear's split into parallelism **across the
steps** and **across the method**; Gander & Palitta (2024, §1) list multiple shooting
and Parareal, domain decomposition and waveform relaxation, multigrid (MGRIT), and
direct time-parallel solvers. The sources of this bundle cover three groups:

| group | idea | members in the sources |
|---|---|---|
| across the steps, iterative | a cheap serial coarse solve corrects accurate fine solves run on all slices at once | [Parareal](/methods/parareal.md) and its variants; PFASST, MGRIT (recalled) |
| across the steps, pipelined | consecutive steps iterate concurrently, each starting after one sweep of its predecessor | block Gauss–Seidel SDC (GSSDC), RIDC, PIRKAS (recalled); see [diagonal SDC](/methods/parallel-sdc.md) |
| all at once | the time-stepping equations of all steps form one space-time system, diagonalized in time | [ParaDiag](/methods/paradiag.md) |
| across the method | the stages or nodes of one implicit step are solved in parallel | [diagonal (parallel) SDC](/methods/parallel-sdc.md); diagonalized collocation, diagonally iterated Runge–Kutta (recalled) |

Čaklović et al. (2025, §1.1) recall that diagonalization approaches for the
stages of one step "struggle to outperform sequential time-stepping" for large
problems, and that pipelined Block Gauss–Seidel SDC coincides with PIRKAS.
[Saupe et al. (2025)](/sources/saupe-2025.md) (§2.3) describe GSSDC: the steps of a
block, one per process, are solved in pipelined fashion, a new step starting after one sweep of the
previous one; it is the core of PFASST, and RIDC is a similar pipeline. Its order
equals that of single-step SDC (as recalled).

## Where each family works

- **Diffusive versus non-diffusive problems.** Parareal "has been mostly successful for
  diffusive problems" (Muralikrishnan & Speck 2025, §1), works well for parabolic and
  worse for hyperbolic problems ([Carrel et al. (2023)](/sources/carrel-2023.md), §2.1,
  as recalled), and on non-diffusive problems either needs a coarse propagator close to
  the fine one or converges only for low-frequency modes
  ([Buvoli & Minion (2024)](/sources/buvoli-2024.md), §1, §5.7). For Vlasov–Maxwell,
  Muralikrishnan & Speck (§7) suggest ParaExp or ParaDiag for the field part instead.
- **Linear problems with constant steps.** ParaDiag needs a time-stepping matrix that is
  diagonalizable or circulant plus low rank, which holds for backward Euler and BDF with
  uniform steps; Gander & Palitta (2024, §7) state that all-at-once Runge–Kutta
  discretizations lead to a comparable structure.
- **Stiff problems with expensive implicit stages.** Diagonal SDC turns the
  [fully implicit collocation step](/methods/fully-implicit-runge-kutta.md) into $\mathsf M$
  independent node solves per sweep; it is the only family here that changes the
  [implicit stage solve](/methods/implicit-stage-solvers.md) rather than the time slicing.
- **Combinations.** Combining diagonal SDC with GSSDC did not help: GSSDC works best with
  implicit-Euler sweeps, and a diagonal preconditioner inside GSSDC raised the iteration
  count, with very large errors or crashes on Allen–Cahn (Saupe et al. 2025, §4.1, Fig. 9).
- **Adaptivity.** Saupe et al. (2025, §1) find no earlier adaptive step selection for
  SDC-type PinT methods and only a few for Parareal. Their adaptive GSSDC uses one step
  size per block; see [step-size control](/methods/step-size-control.md).

## How speedup is measured

The sources report three kinds of evidence, and a number of one kind is not comparable
with a number of another:

1. **Measured wall-clock speedup on parallel hardware.**
   - Muralikrishnan & Speck (2025, §6.3): Parareal on up to 1536 A100 GPUs, 32 in space
     times 48 in time; speedups of 4.2, 4.7 and 2.4 over space-only parallelization for
     Landau damping, two-stream instability and Penning trap (5.8, 5.6, 4.4 with an order-7
     B-spline fine shape function); no speedup with 2 and 4 time-parallel GPUs, crossover
     at 8. The Parareal runs are timed, but the space-only reference is extrapolated: one
     Penning-trap run of 768 steps, scaled by 8 to the 6144 steps and used for all three
     test cases (§6.3). Parareal stops at a tolerance chosen to match serial energy and
     charge errors, not at a fixed iteration count (App. A.2).
   - Buvoli & Minion (2024, §4): 10.4 against serial ERK4 on 2048 cores, a quarter of the
     value 38.5 of the model formula, because communication dominated; the iteration count
     behind 38.5 is not printed (the formula gives 38.6 at $K=5$ with stage counts as costs,
     *compiler check, not in the source*).
     On Vlasov–Poisson (§6.3) the measured run on 2048 cores reaches fine accuracy after
     $K=8$ iterations 24 times faster than serial ERK4, with model and measured speedup
     in close agreement.
   - Saupe et al. (2025, §4.1, Fig. 9): measured wall-clock times on JUSUF, with
     adaptive steps and iterations; diagonal SDC with three processes "roughly halved" the
     time, and four-process GSSDC gave good speedup on van der Pol and Allen–Cahn.
   - Čaklović et al. (2025, §4.4, Fig. 17): MPI timings for Allen–Cahn only, measured
     parallel efficiency 74–93 %.
2. **Cost models or extrapolations.**
   - Čaklović et al. (2025, §4.1): cost $=$ Newton iterations plus right-hand-side
     evaluations, divided by $\mathsf M P_{\mathrm{eff}}$ with an assumed parallel
     efficiency $P_{\mathrm{eff}}=0.8$ (page-local) for parallel SDC.
   - Jin et al. (2025, §4): Parareal cost simulated as sequential coarse time plus the
     largest fine time per iteration, communication ignored; iteration counts 3–11 to the
     target accuracy (Tables 4.2–4.3).
   - Buvoli & Minion (2024, §6.1–6.2): the KP-equation speedups 9.09–11.71 at $K=28$
     iterations are extrapolated from a shortened parallel run on 64 nodes; the convergence
     curves were computed serially.
3. **Counts of parallel operations, or no number at all.**
   - Gander & Palitta (2024, §6) count parallel-in-time loops (#PinT): all runs were on a
     laptop with the block solves applied sequentially, and no timings are given.
   - Carrel et al. (2023, §5) report no parallel run and only expect good speedup from the
     cost gap between coarse and fine rank.

Muralikrishnan & Speck (App. A.2) warn, after Götschel et al., that mismatched
tolerances produce "bloated speedups", and choose the Parareal tolerance so that energy
and charge errors match those of serial stepping.

## Qualifications

- **Reference solver.** Speedups are measured against different baselines: serial ERK4
  with the same fine step (Buvoli & Minion), spatial parallelization alone
  (Muralikrishnan & Speck), serial SDC or Runge–Kutta methods under a cost model
  (Čaklović et al.), or embedded order-5 Runge–Kutta pairs in wall-clock time (Saupe et
  al.). None compares against the best serial method at equal error on parallel hardware
  for every problem.
- **Versions read.** All sources on this page were read as arXiv preprints; their
  numbering is that of the preprints.

# Citations

- [Gander & Palitta (2024)](/sources/gander-2024.md) — arXiv v2: §1, §6, §7.
- [Čaklović et al. (2025)](/sources/caklovic-2025.md) — arXiv v2: §1, §1.1, §4.1, §4.4 (Fig. 17).
- [Saupe et al. (2025)](/sources/saupe-2025.md) — arXiv v2: §1, §2.3, §4.1 (Fig. 9).
- [Buvoli & Minion (2024)](/sources/buvoli-2024.md) — arXiv v2: §1, §4, §5.7, §6.1–6.2.
- [Carrel et al. (2023)](/sources/carrel-2023.md) — arXiv v2: §2.1, §5.
- [Jin et al. (2025)](/sources/jin-2025.md) — arXiv v2: §4.
- [Muralikrishnan & Speck (2025)](/sources/muralikrishnan-2025.md) — arXiv v2: §1, §6.3, §7, App. A.2, A.4.
