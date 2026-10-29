# Ingestion issues — ode-integration

Reviewer's digest, one section per chunk, newest first: contradictions
opened (the normative record is the `## Contradictions` section of the
named page), printed inconsistencies, identity and metadata problems,
bundle-fit suggestions, and questions left to the human. Not part of the
OKF wiki; maintained by the compiler at every chunk.

## Chunk 7 — founding papers: stiffness, A-stability, implicit RK, Dormand–Prince, TVD/SSP, IMEX, exponential integrators, relaxation (2026-10-29)

Sources (10): curtiss-1952, dahlquist-1963, butcher-1964, dormand-1980,
shu-1988, ascher-1997, gottlieb-2001, kennedy-2003, hochbruck-2010,
ketcheson-2019. Added by the human after the archive was complete; 128 of
128 sources, 144 concept pages, 3999 bibliography entries. Every key
already existed in the bibliography as a cited work; metadata verified on
Crossref.

### Versions read (not the version of record)

- `shu-1988`: ICASE Report 87-33 / NASA CR-178304 (May 1987, "Submitted to
  J. Comput. Phys."), 74 pages. Equation numbers on the pages are the
  report's.
- `kennedy-2003`: NASA/TM-2001-211038 (July 2001), 54 pages.
- `ketcheson-2019`: arXiv:1905.09847v1 (23 May 2019).
- The other seven are scans or typeset versions of record. The old scans
  (1952–1980) were transcribed from page images; OCR text was not used for
  equations or coefficients.

### Contradictions

None opened. Recorded side by side, attributed (no verdict):
- Scope of the barrier for implicit SSP methods: Gottlieb et al. (2001,
  Props. 6.2–6.3, forms without explicit terms) next to later recollections
  ("at most first order", "only $L^2$ stable") and Ketcheson's unconditionally
  SSP order-2 methods as recalled by Gottlieb et al. (2022)
  (strong-stability-preserving-runge-kutta, strong-stability).
- Strong stability of linear Runge–Kutta methods: Gottlieb et al. (2001)
  prove RK4 (Prop. 3.3) and state $C_s=2$ as an aim; Sun & Shu's broader
  statement kept beside it.
- Origin of relaxation: the page's "introduced by Ketcheson (2019)" (as
  recalled by later sources) next to Ketcheson's own credit to Dekker &
  Verwer (1984) and later work.
- Lawson2a order: Caliari et al. (2024) order 2; Hochbruck & Ostermann
  (2010, Ex. 2.32) "first-order accurate by Theorem 2.17" (stiff order;
  the tableau does not meet that theorem's assumptions, compiler check).
- ARS(3,4,3) digits: 0.5529291479 (Ascher et al.) vs 0.5529291480…
  (Chinomona & Reynolds).
- DIRK tableau names (Alexander, Nørsett) vs Ascher et al.'s citations of
  the Hairer–Wanner books; Butcher's 3-stage method credited by Butcher to
  Clippinger and Dimsdale, "Lobatto" not used.
- Kennedy & Carpenter: some Ascher pairs violate the extra condition for an
  L-stable pair; Ascher et al. call only the implicit parts L-stable.
- PID gains (0.49, −0.34, 0.10): Kennedy & Carpenter divide by the embedded
  order, Ranocha et al. by that order plus one.
- Gottlieb et al. (2001, §5) cite Dahlquist (1963) for the odd-$k$ order
  bound; Dahlquist (p. 28) recalls $p\le k+2$ from Henrici.

### Printed slips (on the Source pages)

- **Shu & Osher (1988), scheme (2.23)** — needs a ruling. As printed in the
  ICASE report (transcription confirmed against the page image), its Butcher
  form gives $b^\top Ac=8/45\ne1/6$ (compiler check), so the coefficients
  do not satisfy the third-order conditions, while the printed CFL $7/30$ is
  reproduced exactly. The paper calls it a fifth-order method from Lambert's
  book, p. 143. The JCP version was not read. Options: leave as a recorded
  slip (current state), or add the JCP version to the archive so the
  compiler can compare. Also (2.21): last term $\Delta tL(u^{(3)})$ where the
  scheme with $u^{(2)}$ is classical RK4 with bound $137/200$ (compiler check).
- Curtiss & Hirschfelder (1952): Eq. (16) sign, Eq. (19) sign and factor
  2/3, Eq. (23) index, argument order in Eq. (9); footnote 2 not printed.
- Dahlquist (1963): two equations numbered (1.5); $\mathfrak S_\lambda$ for
  $\mathfrak S_\delta$ (p. 38); cross-reference and limit-variable slips.
- Dormand & Prince (1980): reference numbers [12]/[13], [3]/[4]; "(3.3)"
  used twice.
- Gottlieb et al. (2001): missing super/subscripts (p. 102), $c$ used for
  two quantities, name spellings.
- Kennedy & Carpenter (2003): ARK5 explicit stability limits (0.43, 0.96)
  in §6 vs (0.43, 0.67) in App. B; Table 8 column heading; Eq. (59) $1/k!$
  vs $1/k$; App. C value repeated.
- Hochbruck & Ostermann (2010): six small slips (theorem number, boundary
  condition, recursion start, $\mathbb C^d$ vs $\mathbb C^m$, missing $h$,
  equation reference).
- Ketcheson (2019): index slips (pp. 3, 8), the stage-derivative series on
  p. 8, the order of the residual in the proof of Thm. 3 (order-$p$
  conclusion unaffected, compiler check).
- Ascher et al. (1997): two bounds printed "≤" that hold with equality;
  Table 1 "per step" vs "per stage"; name spellings in the references.

### Identity and bibliography

1. **`lambert-1972`**: Dormand & Prince and Shu & Osher print Lambert's
   book as 1973 (Wiley imprint); folded into the existing `lambert-1972`.
   Re-key to 1973?
2. **`robertson-1963`** (cited by Dahlquist): no year printed; the key
   takes the citing paper's year (bundle rule). Verify the year of the
   *Information Processing* (UNESCO) proceedings and re-key if you want.
3. **`budd-1999` / `iserles-1999`**: Hochbruck & Ostermann print Iserles &
   Nørsett's title for Budd & Iserles (Phil. Trans. A 357); kept as printed
   with a note, so a future `--dupes` run flags this pair (expected).
4. **`hundsdorfer-2007-c`** (corrected 2nd printing) kept apart by printed
   year, as in the chunk-6 printings policy (pending decision 2 of chunk 6).
5. `curtiss-1952` prints no reference list: it stays on `--pending` by
   construction (as `runge-1895` in another bundle).

### Bundle fit

- `shu-1988`: §II is time integration; §III–IV (flux-based ENO) are spatial
  discretization and shock capturing, ingested only as the generator of
  the semi-discrete system.

### Candidates for new pages (kept inline)

Trapezoidal rule (Dahlquist 1963 and many pages); SSP multistep methods
and the unconditional-SSP barrier (Gottlieb et al. §5–6, now sections);
the downwind operator; Magnus integrators (Blanes et al. 2024 + Hochbruck
& Ostermann 2010: two sources); trigonometric (Gautschi-type) integrators
and exponential Rosenbrock methods (long sections of exponential-integrators,
now about 900 lines); stiffness leakage, Kaps' problem and the
Pareschi–Russo problem (Kennedy & Carpenter only); DETEST (Dormand &
Prince only); Butcher's principal error function.

### Other follow-ups

- The title of `definitions/internal-stability.md` still says "explicit
  Runge–Kutta methods" while the page now covers DIRK stages: widen it?
- Verdict wording and non-standard labels ("compiler remark", "not a
  contradiction", "slip", "correct") older than chunk 7 remain on several
  pages (SSP, symplecticity, Patankar, low-storage, fully implicit,
  embedded, step-size control, B-series, stability function): a bundle-wide
  sweep like the one done for turbulence-modelling is suggested.
- Tag synonyms reported: imex/additive/gark; embedded-pair/error-estimation;
  convection-diffusion/advection-diffusion-reaction;
  dispersion-analysis/dispersion-relation-preserving/von-neumann-analysis.
  Not merged.
- Kaps' problem: the differential/algebraic labelling on the DAE page was
  not checked against the PDF.

## Chunk 6 — final chunk: invariant domains, Patankar stability, FIMEX, mRKC, splitting, learned integrators (2026-10-20)

Sources (18): pan-2022, quezadadeluna-2022, ern-2022, zhu-2024, muller-2023,
ern-2023, kirby-2025, akrivis-2025, sayyari-2026, nath-2026, spiteri-2026,
abdulle-2022, wei-2026, goswami-2023, maurya-2021, buvoli-2023,
vermeire-2021, izgin-2022. The archive is complete: 118 of 118 sources,
139 concept pages (257 with the Source pages, plus the registry), 3771
bibliography entries. Closing sweeps and the whole-bundle deep lint done
(log, 2026-10-20).

### Decisions for the human

1. **Pending rulings from chunk 5** (still open): `shtilman-1958` vs
   `shtilman-1991`; moving `veiga-2020`/`veiga-2021` to the `hanveiga-`
   spelling. (`kennedy-2021` is now folded into `kennedy-2016`.)
2. **Same-DOI book printings kept apart by printed year** (existing hairer
   policy): axelsson, hairer, hundsdorfer, toro, karniadakis,
   leveque-2002/2004. Merge them instead?
3. **Two preprint forms of one unpublished paper:** `schutz-2021-b` (arXiv)
   and `schutz-2021-c` (Hasselt report) kept distinct. Fold?
4. **Merger's call to confirm:** izgin-2022 ref [29] (Nüßlein et al. 2021,
   printed without venue) is keyed as the published CAMCoS paper
   (`nusslein-2021`), because the printed year 2021 is the publication
   year (the arXiv preprint is 2020); the reader had taken it as the
   preprint.
5. **`sexton-2018`** (arXiv:1808.03718) also absorbs a citation printed
   with year 2019 and the later arXiv title: same arXiv id, so the same
   preprint; confirm.
6. **Bundle-fit candidates for a D17 copy** (none made): muller-2023 and
   nath-2026 (learned surrogates; time integration peripheral),
   quezadadeluna-2022, ern-2022, ern-2023, zhu-2024, sayyari-2026, wei-2026
   (spatial bound-preserving and entropy-stable discretizations) for
   `high-order-capturing-schemes`; maurya-2021 (dispersion-relation
   preserving schemes) for `fourier-analysis-of-schemes`.
7. **Tag synonyms reported, not renamed:** `ssp`/`strong-stability`,
   `dispersion-analysis`/`dispersion-relation-preserving`/`von-neumann-analysis`,
   `wave-equation`/`wave-propagation`, `diagonally-implicit`/`fully-implicit`
   vs `implicit`, `implicit-stage-solvers`/`linear-algebra`/`preconditioning`,
   `bdf`/`linear-multistep`, single-use `lawson`, `leja`, `paradiag`,
   `parareal`, `infinitesimal`, `locally-stiff`.
8. **Unverified items left on the pages, labelled:** four Bencomo & Chan
   slips (appendix transpose, "IDT" wording, Fig. 4(b) legend, the "block
   matrix" part of the ξ slip) and Gaburro et al.'s Eq. (36) "missing
   $\gamma_nh$"; whether Buvoli & Southworth integrate $\delta u_{xxx}$ or
   $\delta^2u_{xxx}$ in KdV (the paper prints δ = 0.022 and calls the run
   identical to two cited experiments); Ern & Guermond's Burgers initial
   square (printed $|x-\tfrac12|\le1$; their Fig. 3 plateau sits near
   $[0.5,1.5]^2$, matching neither reading).

### Identity and version problems

- Re-downloaded files confirmed on page 1 against Crossref: abdulle-2022
  (arXiv v6), wei-2026 (author manuscript; Math. Comp. prints no volume or
  pages yet — the Source page says they must be added), goswami-2023 and
  maurya-2021 (versions of record), buvoli-2023 (arXiv v2 main paper plus
  the SIAM supplement as a second file), vermeire-2021 and izgin-2022 (the
  full-title files; the short-named files hold aljahdali-2022 and
  belardo-2026).
- Versions of record: pan-2022, kirby-2025, spiteri-2026, goswami-2023,
  maurya-2021, vermeire-2021. Preprints or manuscripts: the rest (ern-2022
  and ern-2023 as HAL drafts, the latter pre-review).
- The Crossref row prepared for ern-2022 carried Part II's title; the Source
  page uses Part I (SIAM J. Sci. Comput. 44:A3366-A3392).
- Display names follow the author count: Quezada de Luna & Ketcheson
  (2022), Spiteri & Wei (2026), Sayyari & Yamaleev (2026).
- The Li 2022 front-matter file is still in the archive; the user deletes
  it (Li 2022 dropped from the corpus).

### Printed slips (recorded on the Source pages)

- ern-2023: three literature efficiency values (0.24, 0.26, 0.08) equal
  $\Delta c_{\max}/s$ instead of the paper's own $1/(s\Delta c_{\max})$
  (0.471, 0.423, 1/3; compiler check); Eq. (62) interval; ern-2022: Eq.
  (12) definition of $l'(l)$; table labels.
- izzo-2025 (chunk 5) reprints Zhu, Huang & Yang's $k=3$ scheme with
  $\beta=(0,\tfrac32,0)$; Zhu et al. print $\tfrac32hf(y_n)$ (checked in
  both PDFs): the slip is Izzo et al.'s.
- spiteri-2026: OS22μ coefficient $1/(2\mu-2)$ for $1/(2-2\mu)$; Remark 3.6
  minimiser sign ($\mu=1-1/\sqrt2\approx0.293$; the printed −0.293 is
  worse than Strang; compiler check from exact BCH coefficients); Remark
  3.1 index swap; Lemma 3.1 product order.
- maurya-2021: Eq. (10) as printed makes the velocity update forward Euler;
  Table 4 rows for weight 1.01; the method is sequential and explicit
  (OPIRK1 with weight 1 is the forward–backward scheme; compiler
  identification).
- pan-2022: Table 1 ratios inconsistent with their own columns.
- goswami-2023: Eq. (35) column entry ($\tilde k+2$ for $\tilde k+3$);
  algorithms omit the step factor.
- kirby-2025: Eq. (2.8) step factor; (A.5) coefficient; mesh size in Fig. 5.
- izgin-2022: Remark 3.2 sign, Eq. (47), Lemma 3.10 limit.
- wei-2026: relaxation RK miscited as [4]; Lemma 2 proof point (corrected
  point reproduces the printed constant; compiler check).
- akrivis-2025: Eq. (118) index and sign; Theorem 7 reference.
- abdulle-2022: App. A $z_2$ missing square; Thm 2.4 proof; Robertson
  initial data non-standard.
- buvoli-2023: arXiv Fig. 4 labels (corrected in the SIAM supplement);
  $B\{2\}$ for $B\{1\}$; Eq. (5.17).
- quezadadeluna-2022: initial datum $\sin^4(2\pi x)$ for $\sin^4x$;
  measured rates about 4 with fifth-order space and time unexplained.
- sayyari-2026: index slips in Theorem 1's proof; the BDF2 pseudo-step bound
  beats forward Euler only if $4\rho_n>\rho_{n-1}$ (compiler check).
- zhu-2024: Example 2 rates, Example 5 state; positivity proof omitted;
  "large time steps" not supported by reported steps.
- muller-2023, nath-2026: notation and table-label slips; Nath et al.'s
  inverse simplex map (App. B) right-hand side.

### Contradictions opened

None. Qualifications recorded: Ern & Guermond's "implicit SSP methods are
at most first order" (holds for unconditional SSP; finite-coefficient
implicit SSP methods exist up to order 6 per Kuzmin et al., Ciallella et
al., Quezada de Luna & Ketcheson); their efficiency ratio is not the SSP
effective coefficient; Izgin et al.'s "unconditionally stable" is Lyapunov
stability of steady states, consistent with Torlo et al. (2022); Zhu et
al.'s MP multistep methods precede Izzo et al.'s analysis; Wei & Shu's RK3
family includes Kutta's method and excludes SSP-RK3; Sayyari & Yamaleev
prove positivity per pseudotime iterate, not for the converged BDF
solution; Müller's conservation is exact for the learned equations, not
for the RK4 steps; Nath et al. report no inference timings; Irksome's
boundary default change (Farrell et al. 2021 → Kirby & MacLachlan 2025)
is a documented change of default by the software's authors.

## Chunk 5 — Patankar and positivity, parallel-in-time, deferred correction and ADER (2026-10-20)

Sources (20): nusslein-2021, torlo-2022, ciallella-2022, babbar-2022,
zeifang-2022, chouchoulis-2022, kuzmin-2022, carrel-2023, micalizzi-2024,
buvoli-2024, popov-2024, saupe-2025, gander-2024, babbar-2025,
permyakova-2025, izzo-2025, caklovic-2025, jin-2025, muralikrishnan-2025,
nurkhametova-2026. 18 new concept pages (131 in all, 232 with the Source
pages and the registry), 37 extended, 3374 bibliography entries. Deep lint
(D26) over the chunk's pages before staging.

### Decisions for the human

1. **Bibliography calls to confirm:** `shtilman-1958` keeps the year
   printed by permyakova-2025 although Crossref dates the paper 1991
   (Physica D 52:477) — re-key to `shtilman-1991`? `veiga-2020` and
   `veiga-2021` are works of M. Han Veiga, whose ingested paper is
   `hanveiga-2021` — move both to the `hanveiga-` spelling? `kennedy-2021`
   (pre-existing) duplicates `kennedy-2016`, the NASA DIRK review, with a
   placeholder year — fold it?
2. **"Reader's check" attributions on older pages.** The chunk-5 deep lint
   replaced every "reader's check" on the chunk's pages by a verified
   *(compiler check)* or removed it. 17 pages from chunks 1–4 still carry
   the phrase (e.g. stability-function, step-size-control,
   imex-linear-multistep-methods, tase-operators, quinpi, ketcheson-2023).
   Planned for the whole-bundle deep lint of chunk 6.
3. **Bundle-fit candidates for a D17 copy** (none made): ciallella-2022
   (WENO and well-balancing for shallow water), babbar-2022 and babbar-2025
   (flux reconstruction, AMR on curvilinear meshes), kuzmin-2022 (flux
   limiting) for `high-order-capturing-schemes`; muralikrishnan-2025
   (particle-in-Fourier, Vlasov–Poisson) for `fusion-mhd-simulation` or
   `plasma-propulsion-simulation`.
4. **Tag synonyms reported by the auditors:** `ssp`/`strong-stability`,
   `embedded-pair`/`error-estimation`, `cfd`/`hyperbolic-conservation-laws`,
   `parallel-stages`/`parallel`, `bdf`/`linear-multistep`; single-use
   `paradiag`, `parareal`, `high-order-methods`. For the chunk-6 sweep.
5. **Unverified or unresolved items:**
   - Chouchoulis et al.'s Table 7 entry $c_2^3/6$: $c_3^3/6$ reproduces their
     own Fig. 1 (compiler check), not checked against the original
     Ökten Turacı & Öziş tableau.
   - Saupe et al.'s $\varepsilon_{\mathrm{TOL}}^{5/4}$ scaling fits four
     nodes; their runs point to three (5/3); the paper never states the
     node count.
   - Nurkhametova et al.'s stratospheric problem differs from Nüßlein et
     al.'s ($r_{11}$ and the factor $\mathcal M$ absent, $k_4$ printed
     differently): deliberate change or transcription slip, neither paper
     says.
   - Jin et al.'s four optimized coarse propagators agree to about two
     digits whichever fine propagator they were optimized for (compiler
     check of Appendix B); recorded neutrally.
6. **Docs build (chunk-4 item 1) resolved** by the split build (D28,
   566339f): peak 4.1 GB, CI green.

### Identity and version problems

- No file is a version of record: 19 are arXiv versions, nurkhametova-2026
  is the Virginia Tech report CSL-TR-26-1 (accepted text). Archive
  filenames say "Crossref_<journal>" for all of them.
- buvoli-2024: the file has 33 pages, the footers count 34; the text and
  the 79 references run complete.
- muralikrishnan-2025: Crossref records no volume and the arXiv file prints
  none; the venue is written without one (not guessed).
- zeifang-2022: the arXiv title lacks the published leading "Implicit".
- micalizzi-2024 and saupe-2025 take the issue year (online one year
  earlier); jin-2025 (Bangti Jin et al.) is unrelated to jin-2022.
- The bibliography key `izgin-2022` is reserved for the chunk-6 Source
  (ESAIM: M2AN); other works printed under it were re-keyed.

### Printed slips (recorded on the Source pages)

- nurkhametova-2026: SDIRK32 embedded weights sum to 0.3788; the positivity
  proof assumes $b\ge0$ (and $a_{ij}\ge0$), which SDIRK32 and SDIRK43
  violate (compiler check, pp. 28–29); MAPK null-vector claim; Eq. (27).
- izzo-2025: the $k=3$ scheme of Zhu, Huang & Yang printed with
  $\beta=(0,3/2,0)$ (first order; $(3/2,0,0)$ is second order); Table 4
  last row; Test 5 data.
- torlo-2022: Eq. (6) vs Fig. 1 initial data; "MPRK(3,4,2,0.5)" for
  MPRK(4,3,2,0.5); η3 printed twice; Eq. (69) Robertson rate $k_2y_2$ for
  $k_2y_2^2$.
- nusslein-2021: Eq. (2.13) drops the step factor (interval [1/45, 2/9] for
  [1/15, 2/3]); Eq. (3.3) weights; sign in (2.14d).
- ciallella-2022: Eq. (44) $(x-0.5)^2$ for $(y-0.5)^2$; overhead 18% vs 10%.
- kuzmin-2022: (B.7b) missing $d_i$; (B.9) $(1+\gamma)$ in the numerator;
  Algorithm 1 loop start.
- gander-2024: τ dropped in Eq. (2.2) and the shifted Arnoldi relation;
  Algorithm 3.1 lines 12–13; GMRES preconditioner sign; Theorem 3.1's proof
  has gaps.
- buvoli-2024: Eq. 9 φ without the factorial factor; Eq. 32 error matrix;
  Eq. 17 $|u|u$; Remark 1 growth claim; Table 4a f/g swapped; "8096 cores".
- carrel-2023: Eq. (34) indices; "Algorithm 3.1" for Definition 3.1; Thm 3.5
  for $n\le k$.
- jin-2025: Appendix B θ-scheme forcing weight; Eq. (3.8) sign; Corollary
  3.6 bound vs value.
- muralikrishnan-2025: Thm 5.3 proof $\Delta T t_g^p$; Eq. (5.3) omits
  $E_{\mathrm{ext}}$.
- caklovic-2025: Table 1 caption; Theorem 2.8 and 2.12 proofs; §3.2
  A-stability definition; the conclusion over-claims against §4.2–§4.3.
- saupe-2025: Algorithm 2 max for min; Eq. 31; Eq. (13) $Q_\Delta$ first
  column; "up to order 2M" for all node families (Gauss only).
- micalizzi-2024: Theorem 2.1 needs $\alpha_1>0$; speed-up ratio inverted
  in §9.1.1; supplement root formula.
- zeifang-2022: Eq. (9) missing $+I_l$; Taylor–Green initial velocity cos for
  sin and the dissipation-rate sign; Algorithm 1 range.
- popov-2024: Eq. (15) missing factor $z$; Eqs. (26)–(27), (31)–(32); the
  "(N+1)²" evaluation count is off by a factor $N+1$ (compiler check of
  Eq. (11)).
- chouchoulis-2022: Table 7 (above); tests at σ=0.5 above their own linear
  limits for two schemes.
- babbar-2022: §5.2 Taylor term; figure captions; Lax problem 100 vs 200
  cells; babbar-2025: §5.2 inverted acceptance rule; smoothness threshold
  exponent; Couette velocity; Mach 2000 jet boundary states.
- permyakova-2025: Eq. (7) $t^n$ for $t^{n-1}$; Eq. (A.2); Eq. (16c); Fig. 6
  caption arithmetic; refs [14], [62].

### Contradictions opened

None. Qualifications recorded: Izzo et al.'s order-6 unconditionally
positive MP linear multistep methods are nonlinear, so the order barrier
for unconditionally positive linear methods does not apply; Nurkhametova
et al. prove order $\min(p,q+1)$ while observing the nominal orders;
Popov's A- and L-stability rest on plots and rank checks, not proof;
Permyakova & Goldobin claim classical order 4 for ETD4RK without a
stiff-order statement (compiler check: Luan's conditions guarantee stiff
order 2); the SSP status of deferred correction beyond the explicit order
barrier is not decided by any ingested source; Babbar & Chandrashekar's
"first error-based stepping for a single-stage method" stays their claim.

## Chunk 4 — local time stepping, multirate, exponential integrators, EIN (2026-10-20)

Sources (20): luan-2021, unfer-2021, grote-2021, sreejith-2022, tan-2022,
wolf-2022, luan-2022, deka-2022, liu-2023, fish-2023, puppo-2024, fish-2024,
doehring-2024-b, caliari-2024, loffeld-2024, dallerit-2025, tan-2025,
buvoli-2025, pulicani-2026, buvoli-2026. 16 new concept pages (113 in all,
194 with the Source pages and the registry), 32 extended, 2766
bibliography entries. Deep lint (D26) over the chunk's pages before staging.

### Decisions for the human

1. **Docs build at the limit (decide before chunk 5).** With chunk 4 the
   full site build peaks at 14.2 GB RSS locally (13.5 GB with chunk 3),
   against the 14 GB heap cap and the 16 GB runner. Chunk 4 may still pass
   in CI; chunk 5 will not. Options, in order of effort:
   (a) serve each bundle's `bibliography.md` as static HTML outside the
   Vue build (the seven bibliography pages are the largest page modules);
   (b) build each bundle as its own VitePress site under `dist/bundles/`,
   with the landing site and the bundle map built separately (memory
   then scales with the largest bundle, not the sum);
   (c) a larger paid runner. (b) is the durable fix.
2. **Reclassification applied by the deep lint (veto possible):** "maximum
   order of multirate infinitesimal methods". Loffeld et al. (2024, §2.1)
   write that the coupling strategy "currently limits MRI approaches to
   at-best fourth order", meaning the MIS, MRI-GARK and IMEX-MRI-GARK
   methods they use; Luan et al. (2022) build sixth-order multirate
   exponential Rosenbrock methods. Recorded as a qualification on
   [multirate infinitesimal methods](wiki/methods/multirate-infinitesimal-methods.md).
3. **Bibliography calls to confirm:** `jameson-2024` carries the citing
   paper's year as a placeholder although the work is Jameson & Turkel (AIAA
   J., 1981) — re-key to `jameson-1981`? Roe 1981 cited with the volume and
   pages of its 1997 JCP reprint was folded onto `roe-1981` with a note
   rather than a separate reprint entry. Luan et al. (2022) ref [7], printed
   "D. E. K. et al.", is keyed `keyes-2013`.
4. **Bundle-fit candidates for a D17 copy** (none made): wolf-2022 (ADER-DG
   seismic waves), puppo-2024 (implicit CWENO finite volumes),
   doehring-2024-b (P-ERK on AMR) for `high-order-capturing-schemes`;
   deka-2022 (exponential integrators for resistive MHD) for
   `astrophysical-simulation-codes` or `fusion-mhd-simulation`.
5. **Unverified items:** sreejith-2022 printed slips 6–7 (theoretical
   speedups in Tables 4 and 7) are the reader's recomputations; fish-2023's
   Fig. 5 vs Fig. 7 cost discrepancy is unexplained in the paper.

### Identity and version problems

- 13 of 20 files are preprints (arXiv; HAL for pulicani-2026; an AASTeX
  author draft for deka-2022; the loffeld-2024 preprint prints a placeholder
  DOI). Versions of record: dallerit-2025, sreejith-2022, tan-2022, tan-2025,
  unfer-2021 and, as posted after publication, wolf-2022 (arXiv v3).
- sreejith-2022: Crossref records the family name "N.A."; the bundle keys
  the source `sreejith`, the name printed in the paper's own references.
- unfer-2021 uses "ARK" for asynchronous Runge–Kutta, not additive.

### Printed slips (recorded on the Source pages)

- luan-2021: expRK4s5 "5d5" for 4; a factor 2 missing on the $\phi_3$
  vector of expRK4s6; sign of $\beta_5$ in expRK5s10; expRK5s8 prefactors.
- luan-2022: exprb42 weight $\frac{16}9\phi_3$ for $\frac{32}9\phi_3$;
  $b_3$ of the fifth-order base scheme; sign of $F_s$; "36" conditions for 37
  trees up to order 6.
- dallerit-2025: $w_j([[\bullet],\bullet])=c_j/2$ for $c_j^3/2$; product
  indices in Eqs. 19, 33, 36.
- fish-2024: Brusselator $(w-1)u$ for $(w+1)u$; KPR $u^2$ for $v^2$ and the
  partition's sign; fish-2023: Brusselator slow part sign.
- buvoli-2025: (2.4) $Y_j$ for $W_j$; Algorithm 6.1 line 17; §3 step limit
  inverted; buvoli-2026: final time 5 vs 6, the $\gamma$ formula sign.
- unfer-2021: $S_R$ with min for max; an ARK3 error exponent; Eq. (105).
- deka-2022: the nonlinear remainder $F(u)=f(u)-J(u)$; the φ recursion
  start; reference venue/DOI mismatch (Einkemmer et al. 2017).
- liu-2023: the penalty condition in Appendix A; Lemma 4 needs
  irreducibility.
- grote-2021: the eigenvalue interval of §4.2; wolf-2022: Eq. (5) Taylor
  sum start; puppo-2024: Eq. (26) and figure equation numbers;
  pulicani-2026: Eq. 52, Eq. 4, Eq. 21, ref [59] attribution; doehring-2024-b:
  Eqs. (3.4), (4.4), (4.6); tan-2022/tan-2025: domain and index slips;
  caliari-2024: a figure legend; loffeld-2024: two convergence rates in
  Table 1; sreejith-2022: Table 4 node counts copied from Case 1.

### Contradictions opened

None. Qualifications recorded: the MRI maximum-order statement (above);
Wolf et al.'s "splitting is not high order" (true of the splitting they
cite); Caliari et al. vs Tan et al. on whether the smallest stable EIN
ratio is best; Fish et al. (2024) vs Chinomona & Reynolds on Brusselator
convergence rates of IMEX-MRI-GARK3a (different fast steps); Tan et al.'s
0.54 threshold is the coupled-stiff-limit threshold of ARS(4,4,3) (compiler
computation, 0.5361).

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
