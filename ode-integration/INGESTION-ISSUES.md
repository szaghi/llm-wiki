# Ingestion issues — ode-integration

Reviewer's digest, one section per chunk, newest first: contradictions
opened (the normative record is the `## Contradictions` section of the
named page), printed inconsistencies, identity and metadata problems,
bundle-fit suggestions, and questions left to the human. Not part of the
OKF wiki; maintained by the compiler at every chunk.

## Chunk 3 — multistep and BDF methods, IMEX for relaxation and low-Mach problems, implicit stage solvers (2026-10-19)

Sources (20): boscheri-2021, akrivis-2021, song-2022, garciaarchilla-2023,
glandon-2022, abulabdeh-2023, munch-2024, akrivis-2024, kemm-2024,
southworth-2024, birke-2024, boscheri-2024, hu-2025, conte-2024,
gonzaleztabernero-2024, orlando-2025-b, orlando-2025, ma-2026, taddei-2026,
toh-2026. 19 new concept pages (97 in all, 158 with the Source pages and
the registry), 28 extended, 2234 bibliography entries. Deep lint (D26) over
the chunk's pages before staging.

### Decisions for the human

1. **Contradiction opened (Open): explicit stages in the implicit tableau of
   an AP IMEX pair** ([asymptotic-preserving scheme](wiki/definitions/asymptotic-preserving-scheme.md)).
   Southworth et al. (2024, §5.1, attributing to Pareschi & Russo 2005) say
   an AP IMEX scheme must not have one; Hu & Shu (2025, App. 7.3) state that
   ARS(2,2,2) and ARS(4,4,3), which have one, are GSA and hence AP on the
   same problem class. The deep lint confirmed it as a genuine conflict.
   Deciding it needs the Pareschi–Russo proof (not ingested): keep Open, or
   close by fiat as an over-broad paraphrase by Southworth et al.
2. **Lobatto IIIC stage order** stays a qualification: Abu-Labdeh et al.
   (2023) and Farrell et al. (2021) both print $s$; the standard $s-1$ is
   supported on the pages only by a compiler check of the two-stage tableau.
   Promote to a contradiction, or keep?
3. **Bibliography calls to confirm:** glandon-2022 ref [36] ("in print",
   arXiv 1910.14079, 2020) merged onto the existing preprint `roberts-2019-b`
   (same arXiv id) rather than a separate 2020 pre-publication entry;
   Karniadakis–Sherwin printed as 2005 folded onto `karniadakis-2013` (same
   2nd-edition DOI); `gresho-2021` (Part 2, no venue or year printed) keeps
   the citing year although the work is from 1990.
4. **Docs build headroom:** with chunk 3 the full site build peaks at
   13.5 GB RSS (12.6 GB with chunk 2), under the 14 GB heap cap of the
   pending `fix(docs)` commit but growing about 0.9 GB per chunk; chunk 4
   will likely exceed it. A structural fix is needed before chunk 4 is
   pushed (static bibliography pages, or a per-bundle build).
5. **Bundle-fit candidates for a D17 copy** (none made): birke-2024,
   boscheri-2024, toh-2026 (MHD finite volumes, all-Mach and
   asymptotic-preserving) for `fusion-mhd-simulation` or
   `high-order-capturing-schemes`; boscheri-2021, orlando-2025,
   orlando-2025-b (all-Mach compressible solvers) for
   `high-order-capturing-schemes`; taddei-2026 (model reduction for FSI) has
   no fitting bundle; song-2022 (structural dynamics) neither.

### Identity and version problems

- 14 of 20 files are preprints: arXiv (akrivis-2021 v1 is 15 pages against
  24 published; abulabdeh-2023, birke-2024, boscheri-2021, boscheri-2024,
  conte-2024, garciaarchilla-2023, hu-2025, ma-2026, munch-2024,
  orlando-2025-b, song-2022, taddei-2026), HAL (orlando-2025, v2 of a v5
  record) or a review manuscript (glandon-2022, supplement missing, "??"
  references). Versions of record: akrivis-2024, gonzaleztabernero-2024,
  kemm-2024, southworth-2024, toh-2026.

### Printed slips (recorded on the Source pages)

- boscheri-2021 Eq. (80) SA DIRK(3,4,3): $a_{44}$ and the explicit row sums
  are wrong as printed (the type-I first row is not a slip).
- orlando-2025 Table 1: missing minus sign on $\tilde a_{32}$ (restored, row
  sums and $R(\infty)=0$ hold); orlando-2025-b Table 20: the explicit
  tableau fails $b^\top A^{\mathrm E}c^{\mathrm E}=1/6$ (0.19885; compiler check).
- akrivis-2021: Eq. (3.11) missing $\tau$; the constant of Eq. (2.2) does not
  match the stated angle; a step of the proof of Prop. 2.3 does not follow as
  printed. akrivis-2024: $p(y^\star)$ evaluated at the rounded ratio.
- ma-2026 Table 4.2: exponents e-05 for e-04; conte-2024: $\mu_4^*$ fourth
  digit; hu-2025: §5.2 cross-reference; glandon-2022: index slips in (3.6),
  (3.7), (3.14), (3.17b).
- munch-2024: sign of the stage-system right-hand side, index slips, "786"
  for 768 processes; abulabdeh-2023: Reynolds number list, table rates.
- toh-2026: the model scheme analysed is not Heun's method, so the "first
  order in time" verdict follows from the model, not necessarily from the
  algorithm.

### Contradictions opened

| Name | Page | Status |
|---|---|---|
| Explicit stage in the implicit tableau of an AP IMEX pair | definitions/asymptotic-preserving-scheme | Open |

Qualifications recorded: Ma et al.'s "many IMEX-RK degrade" vs Hu & Shu's
uniform accuracy (different classes and regimes); Southworth et al.'s
"hard limit of second order" for splitting (real nonnegative coefficients
only); Kemm's "unstable first stage" thesis (a hypothesis of the source);
Glandon et al. calling damping at infinity L-stability; the step-ratio bounds
of variable-step BDF2 bound different estimates; the CFL-type conditions
$h\le c/N^2$ of the uniform-accuracy proofs are sufficient conditions.

## Chunk 2 — relaxation, stabilized and paired-explicit methods, step-size control (2026-10-19)

Sources (20): koyaguerebo-2022, dawes-2021, bassenne-2021, aljahdali-2022,
belardo-2026, croci-2022, hedayatinasab-2022, kang-2022, gaburro-2023,
ranocha-2025, vermeire-2023, bencomo-2023, biswas-2023-b, doehring-2024,
zhang-2024, doehring-2025, deleon-2025, bleecke-2026, bazavov-2026,
faleichik-2026. 15 new concept pages (78 in all, 119 with the Source pages
and the registry), 22 pages extended, 1622 bibliography entries. Deep lint
(D26) run over the chunk's pages before staging.

### Decisions for the human

1. **Reclassification applied by the deep lint (veto possible):** the
   drafter opened "who first combined relaxation with IMEX methods" on
   [relaxation Runge–Kutta](wiki/methods/relaxation-runge-kutta.md):
   Biswas & Ketcheson (2023, §7) claim to be first; Kang & Constantinescu
   (arXiv 2021, J. Sci. Comput. 2022) did it before and are not cited by
   them. Moved to `## Qualifications` as a priority claim settled by the
   publication record, not a conflict of technical results.
2. **Slug convention for double surnames:** deleon-2025 follows Crossref's
   family name "de León"; page 1 prints "Gabriel A. Barrios de León", which
   under the bundle rule (particles joined) would give `barriosdeleon-2025`.
   Pages cite "de León et al. (2025)". Keep, or re-slug?
3. **Bibliography rules to confirm:**
   - book printings with different years stay separate entries, as in
     chunk 1 (Butcher 2002/2003, Lambert 1991/1992);
   - `fernandez-2020` (chunk 1) does not join the surname particles of Del
     Rey Fernández while the new entry is `delreyfernandez-2020`: re-key the
     old one (I can do it on your word);
   - applied without asking, as plain identity fixes: `vermeire-2020` →
     `vermeire-2021` (the future Source slug, printed with its online year),
     `dematte-2019` → `dematte-2020`, `wanner-1991` → `hairer-1991`,
     `kennedy-1994` → `carpenter-1994` (NASA TM-109112 is by Carpenter and
     Kennedy), and `fekete-2022` restored to the published author order
     after a citing list had overwritten it with the preprint order.
4. **Registry choices you may want to veto:** §8 $\eta(y)$ (entropy or
   invariant) and $\gamma_n$ (relaxation parameter, joining the $\gamma$
   family); the P-ERK active-stage count stays page-local as $e$ (the
   sources write $E$).
5. **Bundle-fit candidates for a D17 copy** (none made): gaburro-2023
   (entropy-stable ADER-DG) and kang-2022 (entropy-stable DG time
   stepping) for `high-order-capturing-schemes`; doehring-2024,
   doehring-2025 and hedayatinasab-2022 (P-ERK on DG/FR with Trixi.jl)
   likewise; croci-2022 (mixed precision) has no bundle elsewhere.
6. **Unverified items left as stated by the readers:** the E5 system printed
   by Koyaguerebo-Imé & Bourgault (§6.4) seems to differ from the standard
   E5 (comparison from memory, not in the wiki); doehring-2025's file is
   probably arXiv 2408.05470v1 (not printed in the file).

### Identity and version problems

- aljahdali-2022 and belardo-2026 sit under wrong filenames (Vermeire 2021
  and Izgin 2022); both are versions of record.
- 14 of 20 files are preprints (arXiv, or the authors' preprint for
  doehring-2025); versions of record: aljahdali-2022, belardo-2026,
  bleecke-2026, dawes-2021, hedayatinasab-2022, vermeire-2023, zhang-2024.
- gaburro-2023: the preprint's title is "…ADER scheme", the published one
  "…ADER-DG schemes".

### Printed slips (recorded on the Source pages)

- bazavov-2026: Eq. (95) sign of the linear coefficient ($z_2+z_1$), Table 8
  $a_{51}=2053/11172$, Table 9 $A_5=-261/625$ (checked in exact
  arithmetic); the paper itself corrects Williamson (1980)'s conversion
  formula for $b_i=0$, recorded as Bazavov's correction on
  [low-storage methods](wiki/methods/low-storage-runge-kutta.md).
- belardo-2026: Fig. 2b embedded weights violate order 2; midpoint
  $\rho_{\max}$ is 8 at $k=3\sqrt2/4$, not 7 at $k=1$.
- dawes-2021: four-step RKL2 threshold printed "∼0.18" (closed form 0.2073);
  four formula slips in Appendix D; Eqs. (35)–(36).
- deleon-2025: abscissae $c_3$, $c_4$ of PEP(4,2,5) swapped; constants in
  Eq. (9); sign in Eq. (21).
- faleichik-2026: Eq. (23) error estimate lacks $h$ and has constant 1/20
  rather than 1/10.
- hedayatinasab-2022: Eq. 40 sum start, Eq. 33, Table 2 exponents; the
  claim "$2^{p-1}$ order conditions" (wrong for $p\ge5$); consistent and
  conservative swapped against Doehring et al. (2025).
- vermeire-2023: Eq. (21) missing $\hat b_6$; Table 1 entries contradict
  "always slightly smaller"; speedup "in excess of 7".
- doehring-2024: Table 5 $\Delta t$ at $S=112$; doehring-2025: (A.1d)
  abscissae, (4.6b) $c_4$ for $c_5$.
- aljahdali-2022: evaluation counts inconsistent with 600 steps; identical
  counts for five schemes in Table 4.
- zhang-2024: none in the coefficients (all 1205 order conditions recomputed
  to $10^{-118}$); garbled DOIs in the reference list.
- koyaguerebo-2022: B-stability announced, only B-convergence proved;
  Corollary 4.1 drops $\mu h\ge-2$; Remark 3.1 transform.
- kang-2022, gaburro-2023, bencomo-2023, croci-2022, bassenne-2021,
  biswas-2023-b, bleecke-2026, ranocha-2025: index, caption and typo slips
  listed on their pages.

### Contradictions opened

None. Qualifications recorded: the IMEX-relaxation priority claim; opposite
design goals for embedded stability regions (Vermeire 2023 smaller vs
Ranocha et al. 2022 containing); the stored-register count of third-order
P-ERK (three stage derivatives vs two registers); Farrell et al.'s cubic
BBM invariant (compiler inference: not conserved independently).

## Chunk 1 — founding chunk: reviews, software and Runge–Kutta theory (2026-10-19)

Sources (20): farrell-2021, ranocha-2022, sun-2021, hanveiga-2021,
hedayatinasab-2021, roberts-2021, chinomona-2021, gardner-2022, jin-2022,
fekete-2022, gottlieb-2022, sun-2022, southworth-2022, ketcheson-2023,
reynolds-2023, steinebach-2023, biswas-2023, blanes-2024, biswas-2024,
biswas-2025. 63 concept pages (84 with the Source pages and the registry),
1084 bibliography entries from 1299 printed references. Deep lint (D26) run
over the whole bundle before staging.

### Decisions for the human

1. **Contradiction kept Open: reduced order of Gauss methods on stiff PDEs**
   ([order reduction](wiki/definitions/order-reduction.md)). Farrell et al.
   (2021) say an $s$-stage Gauss method drops to order $s$ (= stage order $q$)
   and observe 2 for two stages; Southworth et al. (2022) and Biswas et al.
   (2025) give $\approx\min\{p,q+1\}$, i.e. $s+1$. Both are generic statements
   over the same class; the true rate depends on the problem, the boundary
   data and the norm (Ostermann–Roche theory, recalled by Biswas et al.
   2024). Recommended: keep Open until a source analyses Gauss methods on a
   parabolic problem with time-dependent boundary data in a stated norm.
2. **Reclassification applied by the deep lint (veto possible):** the drafter
   recorded "suitability of the Conde–Fekete–Shadid SSP embeddings for
   adaptive control" (Fekete et al. 2022 vs Ranocha et al. 2022) as a
   contradiction. Checked on the Ranocha PDF (§5): Ranocha et al. do not say
   which of the eight SSPRK(10,4) embeddings they tested, they assess
   step-size-control stability while Fekete et al. assess efficiency, and on
   SSPRK(4,3) the two agree. Moved to `## Qualifications` on
   [embedded pairs](wiki/methods/embedded-runge-kutta-pair.md).
3. **Tag vocabulary** (not changed, your call): `geometric-integration` (14)
   and `structure-preserving` (12) overlap; `strong-stability` and
   `energy-method`; `implicit-stage-solvers` (a tag equal to a page slug),
   `linear-algebra` and `preconditioning`; `embedded-pair`,
   `error-estimation` and `step-size-control`; `sundials` beside `software`.
   Proposal: keep `geometric-integration` for symplectic/splitting/BEA pages
   and `structure-preserving` for discrete invariants (energy, entropy,
   positivity); drop `sundials` and `implicit-stage-solvers` in favour of
   `software` and `linear-algebra`; fold `error-estimation` into
   `step-size-control`. Applied already: `dae`, `ssp`, `embedded-pair`,
   `stability`, and `runge-kutta` + `explicit`/`implicit` replaced their
   synonyms.
4. **Archive (Layer 1), done with your authorization (2026-10-19):** the bad
   files of Abdulle 2022, Goswami 2023, Maurya 2021 and Wei 2026 were
   overwritten with the papers from `~/papers/re-download`; Buvoli 2023
   (main paper, `..._Part_I_main_paper.pdf`), Vermeire 2021 and Izgin 2022
   were added under full-title filenames, because their short archive names
   hold Al Jahdali 2022 and Belardo 2026. **Still to do by you:** delete the
   Li 2022 file
   (`2022_Crossref_Mathematics_of_Computation_Li_Implicit-explicit_relaxation_Runge-Kutta_methods_constructio.pdf`,
   a journal front matter); Li et al. 2022 is dropped. All of these enter in
   chunk 6 (18 sources).
5. **Bundle-fit candidates for a D17 copy** (none made):
   - hanveiga-2021 (ADER, DeC) and gottlieb-2022, fekete-2022 (SSP time
     stepping): `high-order-capturing-schemes`, which compiles ADER and SSP
     stepping as ingredients of shock-capturing schemes;
   - hedayatinasab-2021 (fully multi-dimensional von Neumann analysis of
     flux reconstruction): `fourier-analysis-of-schemes`;
   - jin-2022 (asymptotic-preserving schemes for kinetic, semiclassical and
     particle problems): `hyperbolic-pde-theory` for its relaxation and
     diffusion limits; most of the review beyond §5 is kinetic theory.
6. **Registry choices you may want to veto:** $h$ for the step (sources'
   $\Delta t$); $q$ stage order and $q_{\mathrm w}$ weak stage order
   (Biswas et al. write $\tilde q$ and $q$); $\phi_k$ with the $1/(k-1)!$
   factor (Chinomona & Reynolds omit it); multirate ratio $m$ and micro-step
   index $\ell$ from 0 (Roberts et al. write $M$ and $\lambda=1..M$).

### Identity and version problems

- 17 of 20 files are arXiv preprints, not versions of record, although
  named "Crossref"; only hedayatinasab-2021, steinebach-2023 and jin-2022
  are typeset journal versions. Every Source page has a
  `# Version read` section; claims and numbering are those of the version
  read.
- fekete-2022: the file is arXiv 1806.08693v1 with a different title
  ("Embedded error estimation and adaptive step-size control for optimal
  explicit SSP Runge–Kutta methods") and author order (Conde, Fekete,
  Shadid) from the JCAM paper (Fekete, Conde, Shadid). Slug follows the
  published first author.
- steinebach-2023 does not print the Rodas5P coefficients (they live in
  OrdinaryDiffEq.jl); fekete-2022 defers its pairs' SSP coefficients to a
  GitHub draft.
- ketcheson-2023, reynolds-2023, gardner-2022, blanes-2024: placeholder
  DOIs or volume numbers in the preprint template.

### Printed slips (recorded on the Source pages; none affects a concept page)

- sun-2021 Prop. 2.2: the $\beta_{k^*}$ formulas are off by a factor $\mp2$
  against the paper's own Table 6.1 (checked symbolically by the reader).
- sun-2022 Ex. 4.3: $D=\mathrm{diag}\{1,1/4\}$ should be $1/16$; the
  Kraaijevanger–Spijker tableau quoted has $b^\top c=2$ (first order only).
- biswas-2024 Remark 3.3 ($p=s+1-\sigma$ should be $s-\sigma$) and Cor. 4.5
  (DIRK bound $s-p-1+\sigma$ should be $s-p+1-\sigma$; Biswas et al. 2023
  Thm 4.2 confirms).
- ketcheson-2023 Eq. (38): the closed form contradicts the series (37); the
  consistent function is $\frac2z\arctan\frac z2$.
- blanes-2024: (7.10) $\sqrt3/2$ should be $\sqrt3/6$; (7.8), (7.6), (5.24),
  (5.52) index or factor slips; Appendix A and Table 8.1 recommend different
  methods; WHT96 "(16,2)" vs "(17,2)".
- farrell-2021: Lobatto IIIC(3) given stage order 3 (standard: 2); Eq. (10)
  sign, Eq. (15) missing $h$; "Gauss–Lobatto" for Gauss–Legendre.
- gottlieb-2022: transposed indices in the fourth-order Butcher list; the
  "type A" label holds only in an extended sense.
- chinomona-2021: sign of the KPR forcing in the splitting (p. 21);
  sector angles swapped (p. 16); $\varphi_k$ without $1/(k-1)!$.
- reynolds-2023 Eq. (22): Brusselator diffusion printed as $d\,u_{xx}$ in all
  three equations; three references printed twice.
- hanveiga-2021: sign of $F$ flips between sections; Eq. (42) index; the
  stated collocation order $M+1$ is a lower bound for Gauss nodes; the
  stability study is called "A-stability".
- southworth-2022: NACA time step $5\times10^{-2}$ vs $2\times10^{-2}$;
  "explicit 6th-order SDIRK"; claim of "symplectic DIRK ≤ 4th order"
  (composition of implicit midpoint gives any even order; compiler check
  recorded on [symplecticity](wiki/properties/symplecticity.md)).
- jin-2022: 25 slips listed in the notes, among them Eq. (5.1) "stiff,
  explicit" for the implicit BGK term, the sign of $\mathcal L$ (pp. 455/457),
  and $\partial_t$ for $\Delta t$ in (5.61).
- hedayatinasab-2021: concave/convex hull; the exact solution lacks a minus
  sign; wrong section/equation cross-references.

### Contradictions opened

| Name | Page | Status |
|---|---|---|
| Reduced order of Gauss methods on stiff PDEs: $q$ or $q+1$ | definitions/order-reduction | Open |

Qualifications recorded (not contradictions): Fekete vs Ranocha on SSP
embeddings under adaptive control; controller rankings differ across
Fekete, Reynolds and Ranocha (different test sets); Hedayati Nasab's 1.97×
over RK4 vs Ranocha's "no consistent gain" (different baselines); PID as
ARKODE's default although PI/Gustafsson win on its own Brusselator test;
Jin's "an AP scheme converges uniformly" overstates the definition.
