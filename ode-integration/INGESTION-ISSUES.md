# Ingestion issues — ode-integration

Reviewer's digest, one section per chunk, newest first: contradictions
opened (the normative record is the `## Contradictions` section of the
named page), printed inconsistencies, identity and metadata problems,
bundle-fit suggestions, and questions left to the human. Not part of the
OKF wiki; maintained by the compiler at every chunk.

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
