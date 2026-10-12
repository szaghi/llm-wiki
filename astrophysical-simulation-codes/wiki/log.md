# Directory Update Log

## 2026-10-12

* **Batch 1: the frameworks** (10 sources). Ingested
  [Stone et al. (2008)](/sources/stone-2008.md) (Athena),
  [Stone et al. (2020)](/sources/stone-2020.md) (Athena++),
  [Mignone et al. (2012)](/sources/mignone-2012.md) (PLUTO-Chombo),
  [Almgren et al. (2010)](/sources/almgren-2010.md) (Castro),
  [Bryan et al. (2014)](/sources/bryan-2014.md) (Enzo),
  [Zhang, Schive & Chiueh (2018)](/sources/zhang-2018.md) (GAMER MHD),
  [Rosdahl et al. (2013)](/sources/rosdahl-2013.md) (RAMSES-RT),
  [Skinner & Ostriker (2013)](/sources/skinner-2013.md) (Athena's Hyperion
  module), [Tomida & Stone (2023)](/sources/tomida-2023.md) (Athena++
  multigrid) and [Mullen, Hanawa & Gammie (2021)](/sources/mullen-2021.md)
  (conservative self-gravity). Reader notes by parallel subagents; pages
  drafted by subagents from the notes, then reviewed, installed and linted
  by the compiler.
  * **Created:**
    * 7 Software pages (Athena, Athena++, PLUTO, Castro, Enzo, GAMER,
      RAMSES-RT);
    * 9 Method pages (unsplit integrators, Riemann solvers, constrained
      transport, GLM cleaning, dual energy, AMR, M1 transport, Poisson
      solvers on AMR, conservative self-gravity);
    * the reduced-speed-of-light Definition;
    * 10 Benchmarks. Each benchmark lists only sources that actually run
      it; the drafters dropped five planned source–test pairs the papers
      do not contain.
  * **Recorded as printed:** Athena's corner-EMF eq. 79 prints indices
    $j+1$ and $i+1$ where the faces touching the corner are $j-1$ and
    $i-1$ (checked on the page image). It is not reproduced; the
    [constrained-transport](/methods/constrained-transport.md) page describes
    it in words.
  * **Notation:** registry section "Additions, batch 1" ($P^*$, $\mathbf J$,
    $\boldsymbol{\mathcal E}$, $\psi$, $c_h$, $c_p$, $\hat c$, $f_c$,
    $f_{\mathrm r}$, $\chi_{\mathrm E}$, $\hat{\mathbf n}$, $N_{\mathrm{ph}}$,
    $\mathbf F_{\mathrm{ph}}$, $\mathsf T_{\mathbf g}$, $E_{\mathrm g}$, $a$,
    $\eta_1$, $\eta_2$, $\omega_{\mathrm{SOR}}$, $\hat f^{\rho}$).
  * **Bibliography:** 812 references merged into 629 entries. AAS and MNRAS
    lists print no titles, so all 51 same-stem pairs were resolved by
    journal, volume and page; every pair was distinct. Misprints were
    folded with notes, and the correct venue kept:
    * Woodward & Colella (JCP 54:115), printed with page 174;
    * Liska & Wendroff (SISC 25:995), printed as 25:3;
    * Stone & Gardiner (Phys. Fluids 19:094104);
    * Commerçon (A&A 529:A35);
    * Parker (JGR 62:509), printed with volume 4;
    * Colella & Woodward (PPM), printed with the authors reversed.

    The ingested PLUTO-AMR paper owns `mignone-2012`; Stone et al.'s A&A
    Mignone 2012 is `mignone-2012-b`.
  * **Deep lint (10 ingestions, run with this batch).** A read-only auditor
    checked the 27 concept pages against the reader notes and PDFs. About 150
    numbers and references matched. Fixes:
    * Bryan's Sedov eq. 104 gives the spherical $t^{2/5}$ law for a
      cylindrical blast; flagged as printed.
    * The 2D relativistic MHD blasts of Mignone and Stone are different
      set-ups; they were wrongly attributed to units.
    * RAMSES-RT's GLF bound is $\hat c$, not $c$.
    * Mullen's discrete Poisson identity now carries its $1/h$ and its sum
      over directions.
    * Rosdahl's Table 1 and text disagree on the ISM's $f_c$.
    * Tomida's level-by-level estimate is marked as a hypothesis.
    * Four notation slips were fixed (theta weight, isothermal sound speed,
      gas step, photon-number reduced flux). Missing tags were added.
    * **Two contradictions opened** on
      [AMR](/methods/adaptive-mesh-refinement.md): whether subcycling is
      worth its cost, and whether patch AMR suffers level-dependent derived
      quantities.
    * **One contradiction opened** on
      [Poisson solvers](/methods/multigrid-self-gravity.md): whether
      level-by-level solvers are adequate.

* **Bundle scaffolded** on user instruction: the code-design bundle for
  classes 7 and 8 of the ADAM paper collection (astrophysics codes and
  physics modules; GPU and HPC frameworks), "codes of both kinds",
  independent of every other bundle (D12, D17, D18). Created the folder
  indexes, an empty `bibliography.bib`, and the
  [notation registry](/notation.md), seeded once with the conservation
  laws, mesh, time-stepping, self-gravity, radiation and relativistic
  symbols the first batches need. Corpus archive:
  `~/papers/mosaic/astrophysical-simulation-codes/` (35 PDFs; Truelove
  et al. 1997 awaits a manual download).
