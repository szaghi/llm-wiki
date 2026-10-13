# Directory Update Log

## 2026-10-13

* **Frontier batch 10: ingested [Berger & Oliger (1984)](/sources/berger-1984.md),
  [Teyssier (2002)](/sources/teyssier-2002.md), [Colella & Glaz (1985)](/sources/colella-1985.md),
  [Hunter (2007)](/sources/hunter-2007.md), [Turk et al. (2011)](/sources/turk-2011-c.md) and
  [White et al. (2016)](/sources/white-2016.md)**, the user's downloads; 56 of 56.
  Teyssier read as the arXiv preprint (figures are placeholder pages). Stone & Norman's
  ZEUS-2D papers were not obtained and are dropped.
  * **New page:** [RAMSES](/software/ramses.md).
  * **Updated:** [AMR](/methods/adaptive-mesh-refinement.md) (Berger & Oliger's time refinement,
    Richardson estimate and rotated subgrids; Teyssier's octree and per-level stepping; the
    Open subcycling entry gains both as evidence), [approximate Riemann solvers](/methods/approximate-riemann-solvers.md)
    and [general EOS](/methods/general-equation-of-state.md) (Colella & Glaz's real-gas solver;
    White et al.'s frame-transformation solvers), [Athena++](/software/athena-plus-plus.md),
    [constrained transport](/methods/constrained-transport.md), [primitive-variable recovery](/methods/primitive-variable-recovery.md)
    (Noble's 1D_W in 2016), [Enzo](/software/enzo.md), [FLASH](/software/flash.md),
    [RAMSES-RT](/software/ramses-rt.md), [IDEFIX](/software/idefix.md),
    [Poisson solvers on adaptive meshes](/methods/multigrid-self-gravity.md) (RAMSES's one-way
    interface; the Open entry gains Teyssier's percent-level force errors, which neither confirm
    nor refute the estimate), [particle-mesh gravity](/methods/particle-mesh-gravity.md),
    [numerical floors](/methods/numerical-floors.md), [cell updates per second](/definitions/cell-updates-per-second.md),
    and the benchmarks Sod, Sedov–Taylor, Zeldovich pancake, double Mach reflection, MHD blast,
    linear waves and magnetized torus.
  * **No contradiction opened.** Qualifications: Teyssier's "no artefact" for shocks crossing
    level boundaries against FLASH's reflected shock at grazing incidence (his 3D evidence refines
    on concentric spheres, so incidence is near normal; compiler reading); refinement ratio 4
    (Berger & Oliger) against 2 (Enzo, Quokka), recommendations on different grounds; the 2016
    and 2020 Athena++ papers describe two epochs of the code. matplotlib and yt get Source pages
    only (analysis tooling is outside the bundle's scope); Hunter (2007) prints no reference list
    and stays on `--pending` by design.
  * **Bibliography** (2522 entries): 220 references merged. arXiv:1008.2801, cited as "Almgren et
    al. 2010" by Turk et al., is the SciDAC 2010 MAESTRO/CASTRO/SEDONA paper (arXiv API), new key
    almgren-2010-b; De Zeeuw's thesis, Kravtsov & Klypin and Collins et al. (arXiv) separated from
    same-key entries; Evans & Hawley printed ApJ 322:659 by White et al.; the note on turk-2011-b
    corrected (it is not the yt preprint, arXiv:1011.3514).

* **Deep lint #4** (15 ingestions since #3: frontier batches 6–9 and
  Truelove 1997). Two read-only audits (concept pages and registry; Source
  pages and every `Contradictions` entry), then fixes checked against the PDFs.
  * **Flags of batch 9 closed.** MHD blast wave: the 2005 arXiv v1 prints
    $t = 0.2$ twice (§5.6 and the Fig. 13 caption), so the transcription was
    right; the figure's front position and the ambient fast speed point to
    0.02 (compiler reading, recorded as printed). Berger & Colella's "factor
    of 4 increase in resolution" (p. 79, now quoted verbatim) is consistent:
    the double Mach reflection is self-similar, so resolution compares as
    $h/t$, giving $(1/120)/0.2 \div (1/800)/0.12 = 4.0$ (compiler computation;
    the Fig. 7.1 caption's $t = 0.12$ is the consistent value).
  * **Contradictions.** PPM order on non-uniform meshes (Open): Fryxell et al.'s
    fourth-order statement sits before their limiter (eqs. 20–24); a compiler
    note on Colella & Woodward's limited-slope context and Woodward &
    Colella's "the PPM remap is formally third-order accurate" (p. 165) added;
    still Open. Time subcycling (Open): Berger & Colella (1989) and Fryxell et
    al. (2000) evidence folded into the entry. Jeans criterion: the uncited
    commentary marked as a compiler note. Multigrid self-gravity entry flagged
    to the human as possibly below the bar (both sides agree the method is
    inconsistent); unchanged.
  * **Claims.** PLUTO's rotated tube: Mignone et al. (2012) eq. 55 rotates
    the Ryu–Jones 2a states with the matrix of Mignone et al. (2010); the
    earliest ingested 3D inclined 2a is Gardiner & Stone (2008) §5.4. The PPM
    detector constants 20, 0.05 and 0.1 are Colella & Woodward's statement,
    not printed in Woodward & Colella (1984). The 12/6-solve CFL pairing
    credited first to Gardiner & Stone (2008) on the integrator and Athena
    pages. Stone et al. (2020) print λ = 1 and k = 2π (checked), so the linear
    wave entry's recheck is done. Stale "not in the archive" / "not
    reproduced" lines replaced (Jeans criterion, Brio–Wu, FLASH); drafter
    scratch wording removed from four audit lists.
  * **Notation.** Registered $\lambda^\mp_{i+1/2}$, $\lambda_{\max}$ (HLL
    bounds; $\hat c$ was misused for them), $K_{\mathrm{Lap}}$, $\mathcal E^\circ$,
    $\mathcal E^c$, $L_1$, $L_2$, $L_\infty$, $c_{\mathrm{sl}}$ and $\mathsf I$;
    the GLM cleaning-pair face states rewritten in the $\mp$ convention;
    $\sqrt{-g}$, $v_d$, bare $J$ and paper-native $\Delta x$ removed.
  * **Bibliography.** Titles of gardiner-2008 and woodward-1984 taken from
    page 1; DOIs of truelove-1997, fryxell-2000, woodward-1984 and ryu-1995
    added (as verified at ingestion).

* **Frontier batch 9: ingested [Gardiner & Stone (2008)](/sources/gardiner-2008.md),
  [Woodward & Colella (1984)](/sources/woodward-1984.md),
  [Brio & Wu (1988)](/sources/brio-1988.md), [Dedner et al. (2002)](/sources/dedner-2002.md),
  [Godunov (1959)](/sources/godunov-1959.md), [Harten et al. (1983)](/sources/harten-1983.md)
  and [Ryu & Jones (1995)](/sources/ryu-1995.md)**, the bundle's most-cited works
  not yet ingested whose PDFs sat in sibling archives, copied into this
  bundle's archive (D17); 50 of 50. Godunov read in the Russian original;
  Ryu & Jones as the arXiv preprint.
  * **New pages:** [Godunov's method](/methods/godunov-method.md) and
    [interacting blast waves](/benchmarks/interacting-blast-waves.md).
  * **Updated:** [unsplit Godunov integrators](/methods/unsplit-godunov-integrators.md)
    and [Athena](/software/athena.md) (the 12-solve/CFL ≤ 1 and 6-solve/CFL < 1/2
    pairing is printed first by Gardiner & Stone 2008; "as accurate as the
    twelve-solve method" and "dramatically simpler" are Stone et al.'s words),
    [GLM cleaning](/methods/glm-divergence-cleaning.md) (the method in its primary
    source; Dedner's eq. 22 checked on the page image), [PPM](/methods/ppm.md) (the
    detector constants are not printed in Woodward & Colella 1984; the "not
    ingested here" phrase replaced), [approximate Riemann solvers](/methods/approximate-riemann-solvers.md),
    [constrained transport](/methods/constrained-transport.md), [FLASH](/software/flash.md),
    [PLUTO](/software/pluto.md) (the 3D rotated Ryu–Jones tube is not in the 1D paper),
    and the benchmarks [Brio–Wu](/benchmarks/brio-wu-shock-tube.md) (the output
    time $t = 0.1$ derived; the paper prints none),
    [double Mach reflection](/benchmarks/double-mach-reflection.md) (60° between
    shock and wall, the page's 30° being the normal's angle),
    [field loop](/benchmarks/field-loop-advection.md),
    [MHD blast wave](/benchmarks/mhd-blast-wave.md),
    [linear waves](/benchmarks/linear-wave-convergence.md),
    [circularly polarized Alfvén wave](/benchmarks/circularly-polarized-alfven-wave.md)
    and [Kelvin–Helmholtz](/benchmarks/kelvin-helmholtz-instability.md); notes on
    the Source pages of Stone et al. (2008), Berger & Colella (1989), Colella &
    Woodward (1984), Fryxell et al. (2000), Mignone et al. (2012) and Gardiner &
    Stone (2005).
  * **No contradiction opened.** Flagged, not resolved: the 2D MHD blast wave's
    $t = 0.2$ recorded for Gardiner & Stone (2005) against their 2008 run to
    $t = 0.02$ (a recheck of the 2005 PDF is due); Berger & Colella's "4 times
    finer" against $h = 1/120$ vs $1/800$ (about 6.7). A linear-wave damping rate
    credited to "Ryu et al. (1995)" is not in the 1D paper (qualification).
  * **Bibliography** (2407 entries): 187 references merged. Gropp printed 1:191
    (Crossref 10.1137/0901012; the entry had 4:191); Godunov et al. cited in the
    Russian original merged into godunov-1961; Bolstad's thesis "in preparation"
    is bolstad-1982; Brio & Wu printed 75:500 by Ryu & Jones; Harten & Hyman's
    LA-9105 report is harten-1983-c (Crossref 50:235); Dedner et al.'s fourth
    author corrected to C.-D. Munz from page 1.

* **Frontier batch 8: ingested [Fryxell et al. (2000)](/sources/fryxell-2000.md)
  and [Colella (1990)](/sources/colella-1990.md)**, the user's downloads
  (43 of 43).
  * **Updated:** [FLASH](/software/flash.md) (the code paper as primary
    source; the sentence "has not ingested a FLASH code paper" and the
    description updated), [PPM](/methods/ppm.md),
    [adaptive mesh refinement](/methods/adaptive-mesh-refinement.md),
    [unsplit Godunov integrators](/methods/unsplit-godunov-integrators.md),
    [Athena](/software/athena.md), [PLUTO](/software/pluto.md),
    [double Mach reflection](/benchmarks/double-mach-reflection.md),
    [Sod shock tube](/benchmarks/sod-shock-tube.md),
    [Sedov–Taylor blast wave](/benchmarks/sedov-taylor-blast-wave.md),
    [approximate Riemann solvers](/methods/approximate-riemann-solvers.md)
    and [general equations of state](/methods/general-equation-of-state.md).
  * **New Open `Contradictions` entry** on [PPM](/methods/ppm.md): Colella &
    Woodward (1984) call the interface interpolation "third-order accurate
    for variable mesh spacing"; Fryxell et al. (2000) §3.1.1 say it keeps
    "fourth-order accuracy even in the presence of nonuniform zoning".
  * Qualifications: the 12 and 6 Riemann solves per zone are Colella's,
    their pairing with Courant limits is Stone et al.'s; Colella's split and
    unsplit double Mach results are "essentially identical"; FLASH's first
    version has one global time step (no subcycling).
  * **Bibliography** (2314 entries): 96 references merged; Timmes & Arnett
    printed at their last page (125:294) merged into timmes-1999; Colella's
    MUSCL paper printed at 6:107 merged into colella-1985-c; van Leer's
    Computing Methods VI chapter is vanleer-1984-b; fryxell-2000 given its
    printed title.

* **Frontier batch 7: ingested [Evans & Hawley (1988)](/sources/evans-1988.md)
  and [Sod (1978)](/sources/sod-1978.md)**, cited by 9 and 8 of the
  bundle's sources, from PDFs copied out of sibling archives into this
  bundle's (41 of 41). Evans & Hawley is a scan with no text layer, read
  from page images.
  * **Updated:** [constrained transport](/methods/constrained-transport.md)
    (the original integral-form CT: edge EMFs used twice with opposite
    signs, the van Leer upwinded EMF, the divergence diagnostic values,
    kinematic tests only; the field layout relative to the hydro zones per
    Fig. 1, checked by the compiler on the figure: $B^x$ with $v^y$, the
    opposite of the later convention; "adaptive mesh" there is one moving
    grid, not AMR), [IDEFIX](/software/idefix.md) and the
    [Sod shock tube](/benchmarks/sod-shock-tube.md) (the problem as
    printed has no diaphragm position and no end time: for each recorded
    run, which values are Sod's and which are later conventions).
  * **No contradiction opened.**
  * **Bibliography** (2244 entries): 59 references merged; Hawley, Smarr &
    Wilson Paper I printed as Ap. J. 277:276 merged into hawley-1984-b
    (277:296 on Crossref; p. 276 lies inside another paper); the
    bibliography title of sod-1978 corrected to the printed one; Godunov,
    Zabrodin & Prokopov printed 1962 merged into godunov-1961.

* **Frontier batch 6: ingested [Colella & Woodward (1984)](/sources/colella-1984.md),
  [Berger & Colella (1989)](/sources/berger-1989.md) and
  [Gardiner & Stone (2005)](/sources/gardiner-2005.md)**, the bundle's
  most-cited works not yet ingested (cited by 15, 11 and 10 of its
  sources), from PDFs copied out of sibling archives into this bundle's
  (39 of 39). Gardiner & Stone read as the arXiv preprint.
  * **New page:** [piecewise parabolic method](/methods/ppm.md): the
    original method (reconstruction, monotonicity constraint, contact
    steepening, flattening, dissipation, characteristic averaging, its
    iterative Riemann solver, Lagrange-plus-remap and direct Eulerian
    forms) and how the bundle's codes use it, each from the code's own
    source. Linked from the reading guide.
  * **Updated** [approximate Riemann solvers](/methods/approximate-riemann-solvers.md)
    (PPM's own solver), [adaptive mesh refinement](/methods/adaptive-mesh-refinement.md)
    (the Berger–Colella design and every attribution to it checked),
    [Enzo](/software/enzo.md) and [FLASH](/software/flash.md) (where they
    depart from the paper), [constrained transport](/methods/constrained-transport.md),
    [unsplit Godunov integrators](/methods/unsplit-godunov-integrators.md),
    [Athena](/software/athena.md), and the benchmarks
    [field-loop advection](/benchmarks/field-loop-advection.md),
    [linear-wave convergence](/benchmarks/linear-wave-convergence.md) (the
    printed wavelength inconsistency recorded),
    [circularly polarized Alfvén wave](/benchmarks/circularly-polarized-alfven-wave.md)
    and [MHD blast wave](/benchmarks/mhd-blast-wave.md).
  * No contradiction opened: Katz et al. on PPM's time-step factor and the
    Enzo and FLASH departures are written as qualifications; Cholla's
    low-β instability against Gardiner & Stone's stable run stays the
    existing qualification (different integrator and dimension).
  * **Bibliography** (2200 entries): 67 references merged; references
    printed with no year keyed by the citing year (Berger & Colella's
    Adjerid & Flaherty, Chern & Colella, Dwyer, and Colella's LBL-17023),
    or by the published year when identified on Crossref (Colella's direct
    Eulerian MUSCL, SIAM 6:104, 1985); "Collela & Woodward, JCP 59, 264"
    is Colella & Glaz (Crossref); Evans & Hawley printed as ApJ 322:659 by
    Gardiner & Stone (332:659).

* **Ingested [Truelove et al. (1997)](/sources/truelove-1997.md)**, the
  origin of the Jeans condition, from the user's manual download (36 of
  36 archived sources). Published Letter, read with equations and numbers
  checked on page images.
  * **Updated** the [Jeans resolution criterion](/definitions/jeans-resolution-criterion.md)
    (a batch-5 section on what the original states: the Jeans number,
    the 0.25 threshold, artificial fragmentation, the evidence; the top
    line's "found sufficient" qualified, because the original calls the
    condition necessary but not in general sufficient; the description
    and its index line now attribute the collapse-only scope to Federrath
    et al.) and [adaptive mesh refinement](/methods/adaptive-mesh-refinement.md)
    (Jeans refinement in the original, and its regridding hazard).
  * **Contradiction opened** on the Jeans page: does the criterion apply
    only to bound, collapsing gas (Federrath et al. 2010, "by definition")
    or everywhere at all times (Truelove et al. 1997)?
  * **Bibliography** (2168 entries): 16 references merged; the printed
    self-citation "Truelove et al. 1997, ApJ, submitted" is the companion
    paper `truelove-1998`, not the Letter; the Letter's entry got its
    page-1 title and the fifth author L. H. Howell.

* **Source-page paths made absolute** on user instruction, as the repo
  schema asks: `local_file` in all 35 Source pages now reads
  `/home/stefano/...` instead of `~/...`. Every path was checked to exist.
  Citation lines in page bodies are unchanged.

## 2026-10-12

* **Batch 4: comparisons and applications** (6 sources). Ingested
  [Porth et al. (2019)](/sources/porth-2019.md) (EHT GRMHD code
  comparison), [Kim & Ostriker (2017)](/sources/kim-2017.md) (TIGRESS),
  [Villasenor et al. (2021)](/sources/villasenor-2021.md) (Cholla
  cosmology), [Ohlmann et al. (2016)](/sources/ohlmann-2016.md) (AREPO
  common envelope), [Bai (2017)](/sources/bai-2017.md) (Athena++ non-ideal
  MHD disk) and [Mathew & Federrath (2021)](/sources/mathew-2021.md)
  (FLASH star-cluster formation). All six were read as arXiv versions; the
  archive is now fully compiled (35 of 35).
  * **Created:**
    * Software: [FLASH](/software/flash.md), [TIGRESS](/software/tigress.md),
      [H-AMR](/software/h-amr.md);
    * Result: [EHT GRMHD code comparison](/results/eht-grmhd-code-comparison.md);
    * Methods: [density and pressure floors](/methods/numerical-floors.md),
      [particle-mesh N-body](/methods/particle-mesh-gravity.md);
    * Benchmarks: [Zel'dovich pancake](/benchmarks/zeldovich-pancake.md),
      [magnetized torus](/benchmarks/magnetized-torus-accretion.md).
  * **Rejected:**
    * An MRI quality-factor page: one source.
    * An AREPO Software page: it was drafted, then removed at the audit.
      The second source only lists AREPO, and no source presents it as a
      substantive contribution. AREPO content stays on the Ohlmann Source
      page and the Kelvin–Helmholtz page.
  * **Updated** (add-only, checked by a lost-lines diff):
    * Software: Athena, Athena++, Cholla, Enzo, Grackle.
    * Methods: AMR, Poisson solvers, Riemann solvers, constrained
      transport, unsplit integrators, primitive recovery, sinks, cooling,
      dual energy.
    * Definitions: cell-update throughput, the Jeans criterion.
    * Benchmarks: Kelvin–Helmholtz.
  * **Qualifications, not contradictions** (kept in the prose):
    * Ohlmann's Galilean-invariance attribution against Katz et al. on
      Kelvin–Helmholtz;
    * Kim's implicit cooling against Townsend;
    * Mathew's sink–gas gravity wording against Federrath et al.;
    * Villasenor's "third-order" PPM against Caddy & Schneider;
    * upwind CT dissipation against Stone et al. (2008).
  * **Open questions recorded:**
    * TIGRESS creates sinks without the Jeans and boundedness checks, in
      the regime where Federrath et al. call them necessary.
    * TIGRESS evolves collapsing gas below the Truelove condition before
      creating a sink.
  * **Later evidence on open entries, not closing them:**
    * FLASH sinks now carry intrinsic spin (Mathew & Federrath 2021); this
      says nothing about the 2004 Krumholz scheme.
    * H-AMR's locally adaptive time stepping (claimed factor 3–5) joins
      the subcycling side of the AMR entry.
  * **Bibliography:** 785 references merged; the record grew from 1509 to
    2157 entries, with `FLAGS: 0` and a clean `--dupes` sweep.
    * Two keys had to be freed for the ingested papers:
      * `kim-2017` was rekeyed `kim-2017-b` (Kim J.-G. et al., ApJ
        851:93), so the ingested Kim & Ostriker (2017) owns its key.
      * Mathew's bare `federrath-2010` (Highlights Astron. 15:404) would
        have taken the ingested key, like `zhang-2018` in batch 3. It is
        `federrath-2010-c`, and Mathew's "2010c" maps to the ingested
        paper.
    * Misprints folded with notes:
      * Zel'dovich (1970), printed A&A 500:13 (A&A 5:84);
      * Giacomazzo & Rezzolla, printed 24:235 (S235);
      * Lesur et al. (2014), printed A56.
    * Olivares et al.'s arXiv preprint was merged into its A&A version.
    * The venue sweep found two older duplicates, now folded:
      `abbott-2017b` into `abbott-2017-b`, and `pareshi-2005` into
      `pareschi-2005`. Three keys without a hyphen before the suffix were
      rekeyed: `abbott-2017-c`, `ciolfi-2020-b`, `ciolfi-2020-c`.
  * **Batch audit.** A read-only auditor checked about 65 numbers against
    the PDFs. Fixes:
    * A misattributed Kim & Ostriker quote: their "additional criteria"
      are the potential-minimum and convergence checks, not the Jeans and
      boundedness checks.
    * The spurious-sink paragraph now uses Federrath et al.'s own scope
      statements (opacity limit, magnetic effects).
    * KORAL's Table 4/Table 2 ratio is 1.6–2.7.
    * The H-AMR throughput "reconciliation" was removed: different
      hardware and years.
    * Cholla's dual-energy resynchronization runs both ways.
    * The EHT spread is non-monotone (8.6 at N = 128).
    * The Zel'dovich set-up is attributed to both sources.
    * The H-AMR library reference is §6.5.
  * **Deep lint #3 (35 ingestions).** A second read-only auditor re-read
    every concept page. Fixes:
    * Contradictions:
      * The AMR subcycling entry now lists the batch-3 and batch-4 codes
        on both sides.
      * The one-sided "level-dependent derived quantities" entry (deep
        lint #1) became an open question in prose.
      * The Poisson entry notes FLASH's block solver.
      * The RK2 stability entry paraphrases Athena++'s $C_0$ and cites
        AthenaK.
      * The sink angular-momentum algebra is marked as a compiler
        hypothesis.
    * Pages:
      * The Riemann-solver table gained FLASH, TIGRESS and H-AMR rows.
      * Software links were added on the particle-mesh, rotor,
        linear-wave, blast, Orszag–Tang, Brio–Wu and double-Mach pages.
      * Seven stale descriptions were refreshed: AMR, Poisson, M1, dual
        energy, reduced speed of light, Cholla, EHT.
      * Missing tags were added on 13 pages.
      * The duplicate AMR heading was suffixed.
      * Two `# Citations` headings that a batch-3 edit had dropped were
        restored (linear wave, reduced speed of light; the integrators
        page via its batch-4 draft).
    * Registry:
      * The seed relativistic section was moved up.
      * The $c_s$ row now covers the isothermal case.
      * $\beta_{\mathrm p}$ (plasma beta) was registered.
      * Proposed but not yet registered (pages use words): magnetization,
        black-hole spin, Mach number, polytropic index, error norms, and
        efficiency symbols for the two performance definitions.

* **Batch 3: the GPU codes** (9 sources). Ingested
  [Lesur et al. (2023)](/sources/lesur-2023.md) (IDEFIX),
  [Caddy & Schneider (2024)](/sources/caddy-2024.md) (Cholla MHD),
  [Stone et al. (2026)](/sources/stone-2026.md) (AthenaK),
  [Rossazza et al. (2026)](/sources/rossazza-2026.md) (gPLUTO),
  [Wibking & Krumholz (2022)](/sources/wibking-2022.md) (Quokka),
  [Shankar et al. (2023)](/sources/shankar-2023.md) (GRaM-X),
  [Zaghi et al. (2023)](/sources/zaghi-2023.md) (ADAM),
  [Bernardini et al. (2021)](/sources/bernardini-2021.md) (STREAmS) and
  [Jansson et al. (2024)](/sources/jansson-2024.md) (Neko). Same mode as
  batches 1–2: nine readers, seven drafters.
  * **Versions:**
    * Read as preprints: IDEFIX, Cholla, AthenaK, gPLUTO, Quokka, GRaM-X
      and Neko. Each Source page records the version.
    * Neko's preprint (2021) prints 65 references; the published version
      has 71.
    * AthenaK was published as ApJS 283:27 (2026), found on Crossref at
      ingestion, so its slug is `stone-2026`, not the planned
      `stone-2024`. Bundle law updated.
  * **Created:**
    * 9 Software pages: [AthenaK](/software/athenak.md),
      [IDEFIX](/software/idefix.md), [gPLUTO](/software/gpluto.md),
      [Cholla](/software/cholla.md), [Quokka](/software/quokka.md),
      [GRaM-X](/software/gram-x.md), [ADAM](/software/adam.md),
      [STREAmS](/software/streams.md), [Neko](/software/neko.md);
    * Methods: [porting to GPUs](/methods/gpu-porting.md),
      [super-time-stepping](/methods/super-time-stepping.md);
    * Definitions: [cell-update throughput](/definitions/cell-updates-per-second.md),
      [parallel scaling efficiency](/definitions/parallel-scaling-efficiency.md);
    * 8 Benchmarks: Shu–Osher, Liska–Wendroff implosion,
      Kelvin–Helmholtz, circularly polarized Alfvén wave, relativistic
      magnetic rotor, ambipolar C-shock, radiation shadow, subcritical
      radiative shock. Each is run by at least two sources.
  * **Updated** (add-only, checked by a lost-lines diff):
    * Software: Athena, Athena++, PLUTO, GAMER, Castro.
    * Methods: AMR, unsplit integrators, Riemann solvers, constrained
      transport, GLM cleaning, M1 transport, primitive recovery.
    * The reduced-speed-of-light definition.
    * Eight existing benchmarks. Rayleigh–Taylor is unchanged; no
      batch-3 source runs it.
  * **Contradictions opened**, on the auditor's recommendation:
    * [unsplit integrators](/methods/unsplit-godunov-integrators.md):
      whether RK2 at $\nu = 1$ is stable in 3D (Athena++ against Quokka's
      bound). It hinges on Athena++'s unprinted $\Delta t$ normalization.
    * [linear wave convergence](/benchmarks/linear-wave-convergence.md):
      Athena++ RK3+PPM keeps converging to $N = 256$ (Stone et al. 2020)
      against stalling in IDEFIX's Athena++ run.
    * [reduced speed of light](/definitions/reduced-speed-of-light.md):
      Skinner & Ostriker against Quokka on whether steady states depend on
      $\hat c$. A proposed resolution is attached; closing it is the
      human's call.
  * **Qualifications, not contradictions** (kept in the prose):
    * Brio–Wu PPM oscillations, Cholla against Athena++;
    * Cholla's low-β blast against Athena's CTU claim;
    * rotor Lorentz factor, PLUTO against GRaM-X;
    * IDEFIX's arithmetic EMF average against Stone et al. (2008);
    * AthenaK's $\nu \le 1/d$ usage;
    * GPU block-size advice against Athena++'s CPU advice.
  * **Notation:** registry section "Additions, batch 3": $a_{\mathrm r}$,
    the Planck, energy, flux and Rosseland mean opacities,
    $\Delta t_{\mathrm{hyp}}$, $\Delta t_{\mathrm{par}}$, $s_{\mathrm{RKL}}$.
  * **Bibliography:** 686 references merged; the record grew from 1049 to
    1509 entries, with `FLAGS: 0` and a clean `--dupes` sweep. The venue
    and fuzzy-title sweeps also ran.
    * Corrections verified on Crossref:
      * Powell et al. (1999) is JCP 154:284; Stone et al. (2008) printed
        153.
      * Crockett et al. (2005) is JCP 203:422; Stone et al. (2008)
        printed 203:255.
      * Ryu & Jones (1995) is ApJ 442:228; Caddy printed 422.
    * Other misprints folded with notes:
      * Caddy's Brio–Wu (75:40) and Einfeldt (92:213);
      * Caddy's Toro DOI, which does not resolve on Crossref;
      * K-Athena (arXiv:1905.04341), printed with year 2009 by Stone et
        al. (2020), rekeyed `grete-2019`.
    * Preprints merged into their published versions: AthenaK (cited by
      gPLUTO) and H-AMR (`liska-2022`).
    * Same key, different work, separated:
      * Rossazza's D. Zhang (2018, Galaxies) had merged by key into the
        ingested GAMER slug; it is now `zhang-2018-c`;
      * Jansson's Dongarra (2011) is `dongarra-2011-b`;
      * Zaghi's Berger & LeVeque (1989) is `berger-1989-b`;
      * Caddy's 2003 AIAA van Leer is `vanleer-2006-b`.
    * Two undated citations took the citing year (`amd-2026`,
      `mignone-2026`). Cholla's Zenodo archive is `caddy-2024-b`.
  * **Batch audit.** A read-only auditor spot-checked about 65 numbers
    against the PDFs. Fixes:
    * gPLUTO's printed SSP-RK3 last stage lacks a factor 2 on the
      operator term; the page now gives the standard form, and the Source
      page records the misprint.
    * IDEFIX's PPM error floor of $10^{-2}$ was wrongly called a misprint.
    * Cholla's "at most a 55% drop" is a loose bound, not a conflict.
    * One IDEFIX "GPU" is one MI250X module, so its per-node rate is about
      155 Mcell/s per GCD.
    * ADAM's block-size comparison now holds GPU count fixed.
    * Quokka's radiation throughput counting rule is now stated.
    * Smaller fixes: dimensionless $\mu$ on the two radiation benchmarks,
      $\nu$ for Cholla's printed $C_{CFL}$, the rotor's shared
      $\gamma = 5/3$, a missing `hydro` tag.
    * The audit verified the drafters' Orszag–Tang normalization mapping
      and the Cholla vector potential.

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
