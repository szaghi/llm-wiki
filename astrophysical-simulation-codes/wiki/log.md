# Directory Update Log

## 2026-10-12

* **Batch 2: the physics modules** (10 sources). Ingested
  [Krumholz, McKee & Klein (2004)](/sources/krumholz-2004.md) and
  [Federrath et al. (2010)](/sources/federrath-2010.md) (sink particles),
  [Townsend (2009)](/sources/townsend-2009.md) (exact cooling integration),
  [Smith et al. (2017)](/sources/smith-2017.md) (Grackle),
  [Jiang et al. (2013)](/sources/jiang-2013.md) (Athena self-gravity),
  [Siegel et al. (2018)](/sources/siegel-2018.md) and
  [Kastaun, Kalinani & Ciolfi (2021)](/sources/kastaun-2021.md)
  (relativistic primitive recovery),
  [Tejeda & Rosswog (2013)](/sources/tejeda-2013.md) (pseudo-Newtonian
  potential), [Coleman (2020)](/sources/coleman-2020.md) (general EOS in
  Athena++) and [Katz et al. (2016)](/sources/katz-2016.md) (Castro
  self-gravity energy conservation). Same mode as batch 1.
  * **Created:**
    * Software: [Grackle](/software/grackle.md);
    * Methods: [sink particles](/methods/sink-particles.md),
      [cooling and chemistry integration](/methods/radiative-cooling-integration.md),
      [primitive-variable recovery](/methods/primitive-variable-recovery.md),
      [pseudo-Newtonian potentials](/methods/pseudo-newtonian-potentials.md),
      [general equations of state](/methods/general-equation-of-state.md);
    * Definition: [Jeans resolution criterion](/definitions/jeans-resolution-criterion.md);
    * Benchmarks: [singular isothermal sphere collapse](/benchmarks/singular-isothermal-sphere-collapse.md),
      [self-gravitating polytrope](/benchmarks/self-gravitating-polytrope.md),
      [hydrostatic white dwarf](/benchmarks/hydrostatic-white-dwarf.md).
  * **Updated** (add-only, checked by a lost-lines diff): Athena, Athena++,
    Castro, Enzo; conservative self-gravity, approximate Riemann solvers,
    dual energy, adaptive mesh refinement; Jeans wave.
  * **Contradictions opened:**
    * [sink particles](/methods/sink-particles.md): whether the 2004
      Krumholz scheme conserves angular momentum without a sink spin
      (Federrath et al. App. B against Krumholz et al. §2.4.2);
    * [primitive-variable recovery](/methods/primitive-variable-recovery.md):
      the cost of the temperature inversion (Siegel against Kastaun).
  * **Not a contradiction:** Stone et al. (2020) say Athena++ extends HLLE
    to a general EOS; Coleman (2020) shows that HLLE runs with one but
    fails to converge on general-EOS double shocks. The drafted
    Contradictions entries on three pages were turned into qualifications
    in the prose.
  * **Notation:** registry section "Additions, batch 2" (Jeans length and
    $N_{\mathrm J}$, free-fall time, sink symbols, Bondi radii and
    $\lambda_{\mathrm B}$, cooling function and times, number densities,
    $\mu$ family, $\Gamma_1$, $\eta_{\mathrm{tab}}$, $h_{\mathrm{rel}}$,
    $Y_{\mathrm e}$, $\mu_{\mathrm r}$, $f_{\mathrm m}$, black-hole radii,
    the four point-mass potentials, $\mathbf F_{\mathrm g}$, and the grid
    resolution $N$, which the batch-1 benchmarks already used). The
    Truelove number is written in words, because $J$ is the current
    density. Tag `relativistic` merged into `relativity`.
  * **Bibliography:** 544 references merged; the record grew from 629 to
    1049 entries, with `FLAGS: 0` and a clean `--dupes` sweep.
    * [Siegel et al. (2018)](/sources/siegel-2018.md) owns `siegel-2018`;
      Siegel & Metzger is `siegel-2018-b` and the Zenodo code release
      `siegel-2018-c`.
    * Coleman's "in preparation" companion is `coleman-2020-b`; Coleman's
      "Stone et al. 2019" is the published `stone-2020`.
    * Misprints were folded with notes:
      * Ebert (Z. Astrophys. 37:217), printed by Krumholz as 317;
      * Toro (1997), printed as "Reimann";
      * Miyoshi & Kusano (JCP 208:315).
    * Distinct works under one first-author year were kept apart: Krumholz
      & Bonnell proceedings, First Stars III, a submitted SISC paper, and
      the Fortran edition of *Numerical Recipes*.
  * **Batch audit (deep lint #2, 20 ingestions).** A read-only auditor
    spot-checked 46 numbers against the reader notes and PDFs; all
    matched. Fixes:
    * Two recovery tables now explain that their 1D Brent unknowns differ
      by the factor $D$.
    * Newman's recovery is "most robust" only in Siegel's
      Lorentz-factor–magnetization sweep.
    * Mullen §4.3.2 is cited as measured support for Katz's objection to
      the stress tensor.
    * Notation slips fixed: bare Truelove $J$, $c_\infty$ for
      $c_{s,\infty}$, $e^{3/2}$ for $\exp(3/2)$, Townsend's dimensional
      $\mu$ rewritten as $\mu m_{\mathrm H}$, $df_{\mathrm m}$, "polytropic
      index 3", constant-entropy subscript.
    * Athena++ now says that the EOS-call and root-finder-step counts
      measure different things.
    * Missing tags were added, and `gravity` was merged into
      `pseudo-newtonian`.

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
