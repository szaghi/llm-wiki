# Ingestion issues — turbulence-modelling

Reviewer's digest, one section per chunk, newest first: contradictions
opened (the normative record is the `## Contradictions` section of the
named page), printed inconsistencies, identity and metadata problems,
bundle-fit suggestions, and questions left to the human. Not part of the
OKF wiki; maintained by the compiler at every chunk.

## Chunk 11 — 2022–2024 papers: one-equation SGS models, subgrid velocity enrichment, pseudo-DNS, compressible and real-gas SGS tests, RSM-IDDES buffet, SATES on 30P30N, actuator lines, TBL and ML-combustion reviews (2026-10-27)

Sources (20): stanly-2022, cao-2022-c, chambers-2022, hausmann-2022,
huang-2022-c, li-2022-k, wang-2022-j, zhang-2022-f, zhang-2022-g,
zhang-2022-h, zhang-2022-i, devenport-2022, ihme-2022, cheng-2023-b,
fureby-2023, wu-2023-b, shan-2023, mani-2023, idelsohn-2024, coulon-2023.
220 of 307 ingested, 165 concept pages plus the registry, 10358
bibliography entries. Deep lint A1–A8 over the chunk-11 content done.
Compiled overnight under the temporary night protocol (no review between
chunks; staged and committed by the human afterwards).

### Decisions for the human

1. **Bibliography calls left by the resolver:**
   - The master key `wang-2022-c` was renamed `wang-2022-j` by hand: it is
     the same work as the ingested Source (Phys. Fluids 34:095108).
   - zhang-2022-f/-h's "G. Page 2009" print folded into `grinstein-2007`,
     while the master keeps a separate `grinstein-2010`.
   - huang-2022-c's "CTR ARB 2017" print folded into `yang-2016-c` on
     authors and title (Crossref cannot check CTR briefs).
   - zhang-2022-g's "M. D. Renzo" refs: ref. 23 folded into `direnzo-2020`,
     ref. 20 kept as printed (`renzo-2021`); the bundle key rule would make
     it `direnzo-2021-*` (same question as chunk 10's Crossref-surname keys).
   - zhang-2022-f's "S. Gs" refs (Sidharth) kept as printed `gs-*`; the
     "B. Halpern" editor (zhang-2022-f, -h) recorded as printed.
   - The master key `patano-2003` (absorbing ihme-2022's Pantano 2003) is a
     misspelt key; rename?
2. **Candidate pages that now qualify** (two or more sources):
   modelled-stress depletion / grid-induced separation (mani-2023,
   wu-2023-b, the DES page); a partially-stirred-reactor page would need a
   second source; Devenport & Lowe's equilibrium boundary layers,
   roughness, internal and 3-D boundary layers (single source); plus the
   chunk-10 list (converging–diverging channel, discrete adjoint,
   k-corrective-frozen, BVD reconstruction, SUPG/PSPG, heat-flux models,
   Rosenbrock time integration).
3. **Yoshizawa's $C_I$:** Hausmann et al. call 0.0826 the "originally
   proposed value" of $k_{\mathrm{sgs}}=C_I\Delta^2|S|^2$ (Yoshizawa 1986);
   Volpiani prints 0.0066 for the same form without calling it original.
   Recorded side by side on the one-equation page; promote to a
   contradiction?
4. **Notation changes in committed content:** the roughness length on
   lesgo, smagorinsky-model and zhang-2022-i is $y_{0,\mathrm r}$ (was
   $y_0$); the Mason–Thomson constant is $C_{\mathrm{MT}}$ (was $C_0$); the
   ROUND symbols on numerical-dissipation follow the WENO page.
5. **Still open from earlier chunks:** the chunk-10 calls
   (`ghaffarimotlagh-2013`/`teneikelder-2018` keys, `garnier-2013`,
   duplicated slip-wall subsection, SST constant names) and the chunk-9
   and earlier lists.

### Contradictions

Two opened, verified in both PDFs, *Open.*:
- **Hammerhead Model 11 Reynolds number:** $4.2\times10^6$ (wang-2021-l
  §3.3) against $4.0\times10^6$ (li-2022-k §III C), same diameter and
  Mach number (hammerhead page; the DES page points to it).
- **30P30N span:** $C/9$ "as recommended by the BANC-III workshop"
  (wu-2023-b) against a minimum of $0.74C$ citing the BANC-III summary
  (wang-2024).
cao-2022-c added to the open gas-kinetic dissipation entry ("dissipation
adequate" side). Seven open in all. Side by side, not conflicts: DIAD
ranking (valencia-2026 vs zhang-2022-f/-h); Ihme §4.1.4 vs §5.4 on ref.
[570]; fureby-2023 vs tang-2022 flame index; huang-2022-c vs
vicentecruz-2023 on SVV implicit LES; zhang-2022-g ">90%" vs dang-2022
"up to 90%"; the 30P30N lift results (wu-2023-b vs wang-2024).

### Printed slips (recorded on the Source pages)

- chambers-2022: $S_T$ 386 ± 11 (text) vs 385 (Table I); ±11 not from
  ±3, ±4.9; PIV uncertainty implies $S_{\mathrm{CJ}}\approx192$ against
  292.4 m/s; CJ-speed formula printed three ways.
- cao-2022-c: "approximately 20 times" (ratios 22–68), "two times", "except
  at $t=15$".
- hausmann-2022: Eq. 11 sign gives $\nu'_t\le0$; Eq. 40 units; Eq. 39 and
  Eq. 54 factors; Table I length scales against the text.
- huang-2022-c: Reichardt intercept 7.63 against $B=5.2$; Table I
  $Re_\delta$ against Eq. 19; spacings match element size over $N_p-1$.
- li-2022-k: Eq. 3 ω-production sign; $M_{ij}$ used twice.
- wang-2022-j: ANNSGM-7-19 coefficients ∓1.6×10⁻² (Table I) vs ∓0.0016
  (Table II).
- zhang-2022-f: "two orders of magnitude" (ratio 18); $M_t$ 0.79/0.80.
- zhang-2022-g: abstract grid "5×10⁶" vs 5.51×10⁹; φ defined in the
  x–y plane; forcing described two ways.
- zhang-2022-h: Eq. 10 dimensions; $\Pi$ sign against Eq. 33.
- zhang-2022-i: Fig. 8 legend vs text turbine positions.
- devenport-2022: Eqs. 2.33, 3.30 factors; §5.3 angles 1.7°/0.17° vs
  3.4°/0.34°; four printed duplicate references.
- ihme-2022: Eq. 36 argmax; §3.4.3 $T^*_{\min}$ vs Table 1b; §4.1.4 vs §5.4.
- cheng-2023-b: undefined β₂; weights of Eqs. 2.11 and 2.13 differ; Eq.
  3.3 empty interval; refs [7] = [25].
- fureby-2023: Table 1 rows C/D repeat A/B; "harmonic mean" for a
  geometric mean; swapped figure and case labels.
- wu-2023-b: Eq. 2 destruction $\beta\rho\omega^3$; Eq. 15 right state at
  $j-\tfrac12$; group labels.
- shan-2023: Eq. 8 negative mixing length; scaling range; 0.996/0.995;
  "over 57%" vs "over 60%".
- mani-2023: reference-list slips ("Balaras UPE", AIAA numbers).
- idelsohn-2024: $l_R$ text vs Table 2; $\tau_p$ units; "0.04 cm … ≈ 500
  μm"; $k^c$ without ½.
- coulon-2023: $Le_f$, $Re$ printed without division; Δt in μm; $Re_t$
  "the same" vs 355/313/271.
- stanly-2022: 15 M vs 13,002,444 points; refinement ratio; TSR 5.35 vs
  5.41; mean chord.

### Bibliography

8894 → 10358 entries, `FLAGS: 0`, 388 aliases, 73 verified silences;
printed duplicates folded (krogstad-1992, rotta-1979, degraaff-2000,
bradshaw-1965, godunov-1959, kleusberg-2017). Same key, different work,
re-keyed: `heinz-2020-b`, `li-2021-k`, `li-2021-l`, `li-2022-l`,
`gao-2022-b`, `wang-2013-j`, `wang-2013-k`, `wang-2023-i`, `liu-2022-k`,
`prakash-2022-c`. Preprints kept apart: `dang-2022-c` (of dang-2022),
`cao-2022-d`, `prakash-2021`.

### Bundle fit (D17 candidates, no copy made)

chambers-2022 (experimental DDT), coulon-2023 (premixed-flame DNS),
fureby-2023 (scramjet combustion) and ihme-2022 (ML in combustion) are
combustion papers with marginal turbulence-modelling content;
cheng-2023-b and the WCNS material of wu-2023-b fit
`high-order-capturing-schemes` or `weno-teno` as well; stanly-2022 and
zhang-2022-i are wind-energy LES. Here they sit only on the pages they
bear on.

## Chunk 10 — 2022 papers: variational multiscale LES, learned EARSMs and CFD-driven training, discrete-adjoint field inversion, output-based adaptation, Rosenbrock DG, temporal LES, BVD and compact schemes, hypersonic WMLES, pressure dilatation; second whole-bundle deep lint (2026-10-27)

Sources (20): mardani-2022, chen-2022-g, fidkowski-2022, hamedi-2022,
ma-2022, ghidoni-2022, cherroud-2022, devanna-2022, he-2022-b,
sandberg-2022-b, brenner-2022, deng-2022, kang-2022, simonis-2022,
svard-2022, vannoordt-2022, qi-2022-b, tonicello-2022, yu-2022-e,
zhang-2022-b. 200 of 307 ingested, 158 concept pages plus the registry,
8894 bibliography entries. Deep lint A1–A12 over the whole bundle done
(the second; the next is due by 250 ingestions or with the chunk that
completes the archive).

### Decisions for the human

1. **Keys taken from Crossref surnames:** chen-2022-g prints "G. Motlagh"
   and "M.F.P.T. Eikelder"; the resolver keyed them `ghaffarimotlagh-2013`
   and `teneikelder-2018`/`-b` (full surnames, particles joined, as the
   bundle law asks). Keep, or key by the printed forms?
2. **Possible reprint:** qi-2022-b's Garnier et al. (Springer, 2013) is
   kept apart from `garnier-2009` as a possible reprint or edition.
3. **Candidate pages that now qualify** (three or more sources each):
   converging–diverging channel benchmark (cherroud-2022, cato-2023,
   oulghelou-2025); discrete-adjoint method (brenner-2022,
   fidkowski-2022, fanizza-2025, yan-2022); k-corrective-frozen procedure
   (cherroud-2022, oulghelou-2025, sandberg-2022-b); boundary-variation-
   diminishing reconstruction (deng-2022, takagi-2022, huang-2025,
   li-2024-c); SUPG/PSPG stabilized finite elements (chen-2022-g,
   prietosaavedra-2024, prakash-2022); turbulent heat-flux models
   GDH/GGDH/HoGGDH (sandberg-2022-b, sandberg-2022). Two sources:
   Rosenbrock/peer linearly implicit time integration (ghidoni-2022,
   liu-2022-g); weighted compact nonlinear schemes (ma-2022, with
   wu-2024-b in chunk 14). Plus the chunk-8 and chunk-9 lists.
4. **Duplicated subsection:** the dynamic-slip-wall subsection of
   wall-modelled LES nearly repeats the new slip-wall-model page; cut it
   to a pointer?
5. **Constant names on the SST page:** the page quotes Menter's table
   ($\alpha$, $\beta$, as the registry allows); cherroud-2022 maps the same
   constant to $\gamma_\omega$, oulghelou-2025 to $\alpha$. Both are
   permitted; unify on $\gamma_\omega$ if preferred.
6. **Still open from earlier chunks:** the chunk-9 calls (han-2022-c
   `cai-2012`; `pitsch-1988`→`pitsch-2000`; in-press `park-2017-d`,
   `lozanoduran-2017-b`; `lozanoduran-2020-e`; the zhao-2021-c /
   zhao-2023 shared tables); the chunk-8 calls (`wilcox-2004`,
   `schubauer-1955`, `berger-2017`, `tamaki-2022-b`); `xiao-2015` and
   `ming-2019` renames; the `fusion-mhd-simulation` tab in
   `tearing-mode.md`; `ge-2015`; `jameson-1988`; `suder-1996`; the old
   preprint versions (cao-2024, reddy-2026, chunk 7).

### Contradictions

None opened. The five open entries were re-verified in the whole-bundle
audit, all genuine, attributed on both sides and Open:
sparse-regression coefficients (tensor-basis neural network; Cherroud et
al. 2022 now on both sides: invariant-dependent coefficients at
$\lambda=10^2$, Eq. A.1, but constant coefficients in every selected
model), gas-kinetic dissipation, Cai & Sagaut wall-law constants, Ahmed
slant topology, Langtry–Menter $F_3$ exponent. Recorded side by side, not
as conflicts: Duraisamy et al. (2019) and Sandberg & Zhao (2022) on the
same gene-expression-programming step-to-hill transfer (two second-hand
accounts); Hopkins & Inouye as quoted by Huang et al. (1.16) and Zhang et
al. (≈1.1); Svärd against Aiello and Brillon on entropy-conservative
fluxes (different flows and measures); Brenner against Wang (2023c) on
ensemble Kalman methods in high dimension (different baselines); Mardani
& Nazari's trend against Parente and Romero-Anton (the authors' own
statement); tandem-cylinder $Re$ 1.66×10⁵ (Ghidoni) and 1.6×10⁵ (Wang).

### Printed slips (recorded on the Source pages)

- chen-2022-g: Eq. 21 $\gamma=\tfrac12+\alpha_m+\alpha_f$ gives first
  order (second with $-\alpha_f$); Eq. 14 $\tau_{\mathrm C}$ units; Eq. 30
  $\Delta y^+=0.879$ only over one half-height *(compiler checks)*.
- mardani-2022: Eq. 20 bound 0.7568 (root 0.75488); Table 3 $C_\tau$
  0.6369 (0.6396 from Eq. 24); Eq. 25 exponent ½ (Table 3 follows ¼);
  two definitions of $Re_T$; "$C_{D1}=2.137$".
- ma-2022: the boundary row of $B$ sums to zero; Eq. 3 "pvu"; a missing
  $B$ row.
- ghidoni-2022: ROS3PL "three stages" (four in Table 1); Table 2 order
  5.00 (3.05 from its errors); Eq. 62 missing $q_r$; Tables 13–14
  percentages; text against Table 9 (1.19/1.13, 0.225/0.23); wrong
  cross-references.
- deng-2022: Eq. 15 coefficient 11/501 (sum 84179/84168; 11/504 sums to
  1); [20] = [50].
- simonis-2022: Eq. 25 $2\pi\nu\mathcal Z$ (the paper's Eqs. 22–23 give
  $\nu\mathcal Z$); Eq. 14 against Eq. 15; Table 1 $\Delta t$; "Table 1"
  for Table 2; "$\Theta=10$".
- svard-2022: the Taylor–Green initial pressure fits a $\cos z$ velocity,
  not the printed $\sin z$; dissipation peak "close to 0.0013" (Table 5,
  0.0115 in the text); the abstract announces a Rayleigh–Taylor test that
  is not run.
- vannoordt-2022: Table 5 spacings imply $Re_\tau\approx5400$; Eq. 9
  sensor exceeds 1 as printed; "50% larger" domain.
- tonicello-2022: 54M printed degrees of freedom (58.8M from elements and
  points).
- qi-2022-b: Eq. 3.9 gives $C_0=1/6$ for the box filter, not the stated
  1/12; $Pr$ definition; heat-flux sign.
- yu-2022-e: Eq. 3.16 a factor 2 against Eqs. 6.2–6.4.
- brenner-2022: Eq. 6 omits $\partial_j(\beta\nu_t)\,\partial_i\langle u_j\rangle$
  (derivation only, no verdict on "momentum conserved"); Fig. 13 caption
  threshold reversed.
- cherroud-2022: Eq. 11 production sign; Eq. 26 missing inverse.
- he-2022-b: "traceless" $S^*_{ij}$ is not; 87.5% against 87.2%; two
  inconsistent maps of the $f_w$ regions.
- sandberg-2022-b: Eq. 1 trace sign; GGDH/HoGGDH dimensions.
- zhang-2022-b: §6.1 $\partial p/\partial y$ against Table 4
  $\partial/\partial x$; "modified strong" against "generalized" Reynolds
  analogy; typos.
- rickard-2026 (on the slip-wall page): validity bound 50 and 100; caption
  10% against 22%.

### Bibliography

8241 → 8894 entries, `FLAGS: 0`, 251 aliases, 57 verified silences, 3
printed duplicates folded (henrick-2005, mcquaid-2021, gatski-1993).
Same key, different work, re-keyed: `wang-2013-g` (fidkowski),
`wang-2013-h` (sandberg-2022-b, visual tracking), `wang-2013-i` (deng),
`li-2021-j`, `liu-2022-j`, `zangeneh-2021-d` (SciTech 2021),
`lee-2015-c`, `ihme-2012-b`, `li-2017-d`, `zhou-2019-f`, `yu-2016-c`,
`bernardini-2011-c`, `tang-2020-b`; `devanna-2022-b`, `kang-2022-b` for
the authors' other 2022 papers. The cited Sandberg & Michelassi "2021" is
the ingested `sandberg-2022`; Hopkins & Inouye (1971) volume 9 confirmed
on Crossref (the master said 6); poinsot-1992 keeps the master DOI (the
printed one resolves to another JCP record); the master author of
tonicello-2022 is now "Tonicello". Preprints and conference versions kept
apart (eivazi-2021-b, cai-2021-d, navah-2018-b, milani-2021,
pichler-2015-b, alhawwary-2018-c).

### Bundle fit (D17 candidates, no copy made)

deng-2022 (BVD shock capturing), ma-2022 (weighted compact nonlinear
schemes), svard-2022 (entropy-stable weak solutions) and ghidoni-2022
(time integration for high-order DG) are numerics papers that fit
`high-order-capturing-schemes` or `weno-teno` as well; here they sit only
on the numerics pages they bear on and on their benchmarks.

### Whole-bundle deep lint (A1–A12)

About 650 "as recalled" phrasings rewritten as "X (§…) cites Y"; about
120 compiler judgements removed or attributed; checks resting on
unprinted data removed (Hamedi's $\eta_{\max}=3N$ from figure axes;
Zhang's $T_w/T_e$; a remembered sound speed; Wang's machine-precision
reading of $\alpha_f=36$; a remembered leaky-ReLU form; a remembered
Student-$t$ property); Tonicello's Eq. 5.5 restored to the printed
$\tfrac23$ (drafters had $\tfrac32$); Simonis's relaxation-time check
redone on the right row of Table 1; symbols aligned bundle-wide (see the
log); 18 tag synonyms merged.

## Chunk 9 — 2013–2022 papers: High-Order CFD Workshop, wall-modelled LES and hybrid RANS/LES reviews, turbomachinery data-driven review, KEEP schemes, GEP and random-forest closures, wall-model-integrated LES, gas-kinetic LES, thickened flames and flamelet ignition (2026-10-27)

Sources (20): maltsev-2022, ruggeri-2022, wang-2013, bose-2018, kuya-2018,
heinz-2020, agostinelli-2021, monfaredi-2021, sugaya-2021, li-2021,
lv-2021, zangeneh-2021, zhao-2021-c, kumar-2022-b, sandberg-2022,
liu-2022-g, han-2022-c, berger-2022, bottler-2022, cuenot-2022. 180 of 307
ingested, 153 concept pages plus the registry, 8241 bibliography entries.
Deep lint A1–A10 over the chunk-9 content done.

### Decisions for the human

1. **Bibliography calls left by the resolver:**
   - han-2022-c's `cai-2012` prints the authors and title of Cai et al.
     2016 (J. Sci. Comput. 68) with the volume and page of Zhang & Shu
     2012; kept as printed with a note. Which work is it?
   - cuenot-2022's "Pitsch 1988" is folded into `pitsch-2000` (its
     authors and vol:page are those of Pitsch, Riesmeier & Peters 2000,
     checked on Crossref); bottler-2022's own Pitsch 2000 paper becomes
     `pitsch-2000-b`.
   - bose-2018 prints Park (2017) and Lozano-Durán et al. (2017) as "In
     press": kept as `park-2017-d` and `lozanoduran-2017-b`, following
     the earlier in-press ruling.
   - zangeneh-2021's twice-printed Lozano-Durán & Bae reference is folded
     into `lozanoduran-2020-e` (the CTR brief), not the arXiv preprint
     `lozanoduran-2020-b`.
2. **Possible duplicate run:** zhao-2021-c and zhao-2023 (same four
   authors) print the same channel grid tables with the same slips
   ($\mu=2.83\times10^{-4}$, $\Delta z^+=8.33$) and the same implicit-LES
   value at $Re_\tau=395$ on $96^3$ (360.35). The pages state the shared
   values only; whether it is one run reported twice is not settled by
   the papers.
3. **Notation change in committed content:** the Duan–Martín
   temperature–velocity constant, written $C_T$ on four concept pages and
   chen-2024 since chunks 4–6, is renamed $C_{\mathrm{DM}}$: $C_T$ is the
   TENO cut-off in registry §11 since chunk 8.
4. **Candidate pages that now qualify** (two or more sources):
   composition-space model (bottler-2022, bottler-2023); counterflow
   diffusion flame (cuenot-2022, berger-2022, bottler-2022); kinetic
   relaxation-time eddy-viscosity coupling (zhao-2021-c, heinz-2020, the
   gas-kinetic and LES pages); integral wall model (lv-2021, bose-2018);
   plus the chunk-8 list (three-element high-lift airfoil, explicit wall
   models, log-ω formulation, THINC, deconvolution SGS models).
5. **Older wording outside this chunk's audit depth:** many "as recalled"
   phrasings from chunks 1–8 remain (immersed-boundary method about 25,
   hybrid RANS/LES about 13, DNS, isotropic turbulence, Taylor–Green,
   Morkovin, CES, FW-H, LBM, OpenFOAM). The whole-bundle deep lint due
   with chunk 10 rewrites them.
6. **Tags:** near-duplicates reported again (`k-omega`/`k-omega-sst`,
   `wall-function`/`wall-model`, `isotropic-turbulence`/
   `decaying-turbulence`, `supersonic-flow`/`compressible`,
   `cylinder-wake`/`bluff-body`, `moving-grids`/`cartesian-grid`) and the
   merged `machine-learning` tag reintroduced on one page (re-merged into
   `data-driven`). The whole-bundle lint of chunk 10 sweeps them.
7. **Still open from earlier chunks:** the chunk-8 calls (`wilcox-2004`,
   `schubauer-1955`, journal versions absorbed by `berger-2017` and
   `tamaki-2022-b`); `xiao-2015` and `ming-2019` key renames; the
   `fusion-mhd-simulation` tab in `tearing-mode.md`; `ge-2015`;
   `jameson-1988`; `suder-1996`; cao-2024 and reddy-2026 read from old
   preprints; the chunk-7 preprint versions.

### Contradictions

None opened. Extended: the gas-kinetic dissipation entry
([high-order gas-kinetic scheme](wiki/methods/high-order-gas-kinetic-scheme.md))
gains Zhao et al. (2021) on the side of Cao et al. (2022). Five open in
all.

Moved to Qualifications by the compiler: the measured reattachment point of
the [NASA wall-mounted hump](wiki/benchmarks/nasa-wall-mounted-hump.md),
1.15 chords in Oulghelou et al. (2025, Table 11, citing the Naughton,
Viken & Greenblatt skin-friction report) against 1.10 in Heinz (2020,
Table 3, citing Greenblatt et al. Part 1): each source cites a different
report of the experiment.

Kept as attributed qualifications: DES as a zonal method (Sandberg &
Michelassi) against a single model (Haering et al., Bose & Park); KEEP's
entropy property (Kuya, "nominally satisfies") against Aiello et al.'s
"approximately EC"; the Choi–Moin prefactor (Bose & Park against Goc et
al.); the Caradonna–Tung thrust (Sugaya & Imamura against Han et al.);
Lozano-Durán & Bae (2023) listing zangeneh-2021 among models needing
inaccessible inputs.

### Printed slips (recorded on the Source pages)

- maltsev-2022: Eqs. 27, 48/61, 69, 86/88, 98, 140; Table II labels;
  "80% saving" (35.6–45.3% in Table II). ruggeri-2022: Eq. D1 sign, HLL
  branch, headline claims against Tables III–IX, network widths.
- wang-2013: Ringleb $q_0$, tandem $\delta_1$/$\delta_2$, domain signs,
  "P∞ = 105", DRP credited to Bogey & Bailly but cited to Kim & Lee.
  bose-2018: Eq. 9 units, the inline sign before Eq. 7, Fig. 5 legend,
  author names. kuya-2018: Fig. 9 Mach number, $k_0$ for $\kappa_0$,
  derivative subscripts (corrigendum appended in the file).
- heinz-2020: $C_+$ 0.876 (0.867), Table 5 5.3% (5.2%), duplicated
  reference. agostinelli-2021: Eq. A.4 units, duplicated reference.
  monfaredi-2021: receiver position, 3.7 against 3.6 dB, "third
  harmonic". sugaya-2021: "Posa et al. [14]", missing §4.4, Eq. 22.
- li-2021: Table II column label, stride 17 (16), Eq. 24 $Q$, Eq. 25
  $\sqrt6$, Eq. 22 against Table IV coefficients. lv-2021: Eq. 3 against
  Eq. 8, Table II Hill-Equil spacing, Fig. 15 Hill-C, section pointer.
  zangeneh-2021: Eqs. 4, 6, 12, "shear stress tensor", reference numbers,
  Re 617 000 against 617 300.
- zhao-2021-c: $\mu$, $\Delta z^+$, $N$ product for quotient, Eq. 16
  $-\tfrac12$, WALE Eq. 18 trace sign, DNS attribution. kumar-2022-b: Eq.
  50 weights sum 25/35, channel Mach and $Re_\tau$, "WENP4P".
  sandberg-2022: Eq. 2 sign convention, citation years and authors.
- liu-2022-g: "Cd is 0.159", Eqs. 31, 33, 34, $P_f$ units. han-2022-c:
  stencil indices, Eq. 6 MUSCL not third order, Table 2 cell count,
  Table 5 timing. berger-2022: "TurbStable" twice, Eq. 7 for 9, Ka against
  Table 1. bottler-2022: conclusions not in the body, Eq. 9 $\notin$.
  cuenot-2022: Eq. 15, $\varepsilon_{\mathrm{num}}$ exponent, +65%
  (+60.5%), Eq. 6 $C_{\mathrm{st}}^2$, reference mesh.

### Bibliography

8241 entries (+1009 from 1662 printed references); 62 verified silences,
4 printed duplicates folded (sugaya [4]/[41], agostinelli [3]/[27], heinz
[87]/[222], zangeneh 1/32), `FLAGS: 0`. Re-keyed: `agostinelli-2021-b`,
`monfaredi-2021-b`, `lv-2021-b`, `heinz-2020-c`, `zangeneh-2021-b`/`-c`,
`sugaya-2021-b`, `li-2021-i`; spelling variants folded (`lemetayer-2004`,
`degraaff-2000`, `ffowcswilliams-1969`, `bhatnagar-1954`,
`brouillette-2002`). The eleven Sources that were already cited works
(maltsev-2022, wang-2013, bose-2018, kuya-2018, heinz-2020, li-2021,
lv-2021, zangeneh-2021, zhao-2021-c, sandberg-2022, bottler-2022) keep
their keys, completed from page 1.

### Bundle fit (D17 candidates, no copy made)

- maltsev-2022 (compressible multiphase numerics review), ruggeri-2022
  (neural Riemann solver for real fluids and explosives), liu-2022-g
  (laminar fluid–structure interaction): no turbulence content;
  kumar-2022-b and han-2022-c (WENO variants) carry little. `weno-teno`
  and `high-order-capturing-schemes` share their subjects.
- bottler-2022 (laminar flamelet ignition), agostinelli-2021 (conjugate
  heat transfer and thermoacoustics), monfaredi-2021 (aeroacoustic
  adjoint optimization): applications of off-the-shelf closures.

### Candidate pages (kept inline until a second source)

High-Order CFD Workshop; SD7003 airfoil; spectral gap; bypass transition;
realizability; Bachalo–Johnson transonic bump; dynamic slip-wall and
virtual-wall models; inner–outer predictive model; optimal-estimator
analysis; thermodiffusive instability; random-forest closures; overset
grids; rod–airfoil configuration; shock train; neural Riemann solvers.

## Chunk 8 — 2022–2026 papers: high-order RANS and transition solvers, k-τ in Nek5000, ZDES in a lattice-Boltzmann solver, scale-adaptive simulation, dynamic stall, explicit wall-model fits, deconvolution SGS models, relaxation filtering, TENO shock capturing (2026-10-27)

Sources (20): vandenhoeck-2022, batther-2022, gao-2022, huang-2022-d,
lodares-2022, takagi-2022, ahn-2023, pan-2023, adhikari-2023, jiang-2025,
huang-2024, liang-2024, volpiani-2024, husson-2024, li-2024-c,
tomboulides-2025, huang-2025, nuca-2025, ghidoni-2026-b, valencia-2026.
160 of 307 ingested, 148 concept pages plus the registry, 7232
bibliography entries. Deep lint A1–A8 over the chunk-8 content done.

### Decisions for the human

1. **The archive grew to 307 files.** The 147 files added since
   2026-10-26 were identified from the page-1 DOI and Crossref, with the
   page-1 title checked: all distinct works, no byte copies, none a second
   version of one of the 160 planned works. 26 of them are already cited
   in the bibliography and keep their keys (Bose 2018, Kuya 2018, Heinz
   2020, Mani 2023, …); two title matches were rejected as different works
   (`kiris-2023` is the J. Aircraft paper, not the AIAA conference paper
   `kiris-2022-b`; `wang-2022-j` is Phys. Fluids 34:095108, not
   `wang-2021-g`). They are planned as chunks 9–15 (20 each) and 16 (7),
   in archive order. Consequences: the whole-bundle deep lint falls due
   by 190 ingestions (chunk 10); the closing bibliography sweeps
   (`--dupes`, fuzzy titles) move to the chunk that completes the archive.
2. **Slug renamed: `mihaescu-2023` → `ahn-2023`.** Page 1 prints four
   authors (Ahn, Mihaescu, Karnam, Gutmark); Crossref omits the first.
   The key follows page 1.
3. **Bibliography calls left by the resolver:**
   - `wilcox-2004` ("Turbulent Modeling for CFD", Birmingham Press,
     printed by huang-2022-d) is kept apart from `wilcox-1998` and
     `wilcox-2006` only by its year; probably a reprint. Fold?
   - `schubauer-1955` (NACA TN 3489) kept apart from `schubauer-1956`
     (NACA report form). Same work?
   - `berger-2017` and `tamaki-2022-b` absorb the journal versions of
     conference papers, as in earlier chunks, though they carry
     conference DOIs.
   - `rusanov-1961` (Russian original) folded into `rusanov-1962` (English
     translation), following the earlier translation fold.
4. **Candidate pages that now qualify** (two or more sources):
   three-element high-lift airfoil (30P-30N in huang-2022-d, LEISA2 in
   husson-2024); explicit wall-model approximations (Cai & Sagaut,
   Mozaffari, nuca-2025); log-ω formulation (vandenhoeck-2022,
   elzaabalawy-2023, ghidoni-2026, ghidoni-2026-b); THINC / boundary
   variation diminishing reconstruction (takagi-2022, huang-2025,
   li-2024-c; kept inline on the WENO page by bundle fit); deconvolution
   SGS models (about 100 lines on the scale-similarity page, four models
   from valencia-2026 plus caban-2026 and cao-2024). The chunk-6 "Ducros
   sensor" candidate is now covered by the new shock-sensor page.
5. **Tags:** near-duplicates reported again by the auditors and left as
   they are: `k-omega`/`k-omega-sst`, `wall-function`/`wall-model`,
   `isotropic-turbulence`/`decaying-turbulence`, `supersonic-flow`/
   `compressible`, `airfoil`/`high-lift`, `cylinder-wake`/`bluff-body`,
   and single-use tags.
6. **Process failure, repaired:** drafters wrote timestamps later than the
   real clock on 12 pages (up to 07:35Z at about 06:10Z); the auditors
   reset them, and a bundle-wide scan finds no future timestamp. Gendered
   pronouns written by drafters on four pages were removed.
7. **Still open from earlier chunks:** `xiao-2015` and `ming-2019` key
   renames; the `fusion-mhd-simulation` tab in `tearing-mode.md` line
   247; `ge-2015`; `jameson-1988`; `suder-1996` thesis vs report;
   cao-2024 and reddy-2026 read from old preprints; the four chunk-7
   preprint versions.

### Contradictions

Opened (1): exponent of the Langtry–Menter $F_3$
([k-ω SST model](wiki/methods/k-omega-sst-model.md)): menter-2022 Eq. 7
prints $\exp[-(R_y/120)^2]$, vandenhoeck-2022 Eq. 38 prints
$\exp[-(R_y/120)^8]$; both checked on the page images. Langtry & Menter
(2009), which would decide it, is not ingested.

Extended: the Cai & Sagaut constants of the
[law of the wall](wiki/definitions/law-of-the-wall.md) gain nuca-2025's
third functional form with re-fitted constants. Five open in all.

Kept as attributed qualifications: the Driver–Seegmiller step Reynolds
number (36,000 in ghidoni-2026, 37,425 in tomboulides-2025); the
Wieghardt plate $Re_L$ (1.03e7 in vandenhoeck-2022, 11.1e6 in
ghidoni-2026, no shared $L$); the span effect on SWBLI size (Helm &
Martín against Gao et al.'s hedged reading); Pan & Zhang's attribution to
Pope of a modelled-energy fraction up to 80% beside Jakhar et al.'s
resolved-energy rule; the "Feiereisen" naming of split forms; two printed
forms of the TENO troubled-cell indicator (huang-2024 Eq. 32,
huang-2025 Eq. 11).

### Not reproduced (compiler checks on the pages)

- nuca-2025 Tables V–VI: the fixed-parameter wall-model fits give
  0.47–1.9% error from the printed coefficients, against the printed
  ≤0.05%; with the minus sign restored in Eq. 10 the global models of
  Table IV do reproduce (0.63–0.82%). Cause unresolved.
- adhikari-2023: observed cross-helicity at 1 au printed −0.38, equal to
  the model boundary value, while the observed Table 1 means give about
  −0.43; the paper defines neither quantity, so no check is made.

### Printed slips (recorded on the Source pages)

- vandenhoeck-2022: Eqs. 82–83 superscript, $F^D$ for $F^I$, $Tu$ units,
  references. batther-2022: DDES time step "one order larger" against
  "8%", cost 1500 CPU hours against about 37,000 core-hours, stage label.
- gao-2022: "35% less" (25.9%), Table 3 $Re_\theta$ and $L_{\mathrm{sc}}$,
  $k_{Se}$, Strouhal resolution. huang-2022-d: ordering constraint
  reversed, LU-SGS cited to Reichardt, lift error 5.74% (5.83%), mesh 4
  "smaller", $u_\tau$ forms.
- lodares-2022: FUN3D in Table 2 for the CFL3D values, Eq. 93 superscript,
  "entropy stable"/"entropy conserving". takagi-2022: DMR end time 0.2
  against 2.0, Shu–Osher domain, Eq. 15.
- ahn-2023: "Tam's model⁵⁷" (ref. 16), Eq. 7 incomplete, Eqs. 2 and 6,
  reflection location sign. pan-2023: abstract against body on DES/DDES,
  validation claim, spanwise cell count, Pedersen/Pederson.
- adhikari-2023: $\eta_1$ 1.8e-4 against 1.8e-5, β symbol, turnover
  distances. jiang-2025: $C_u$ for $C_\mu$, $P$ for $P_k$, $C_{d1}$ value
  missing.
- huang-2024: Eq. 38 sign, Table 2 exponent, Eq. 56 basis range.
  liang-2024: reference duplicated, "K=0", cost percentages truncated.
- volpiani-2024: grid "1288", Eq. 38 trace, Eq. 24/25 pointer, caption,
  citation labels. husson-2024: Eqs. 10, 13, 17, 43, 37 (arctangent
  argument order), node count 2.6e9 against 2700e6.
- li-2024-c: Eq. 42 range, time step "smaller", Courant number.
  tomboulides-2025: $Re_\tau$ 1000 against 1142, Eq. 29, $p=9$ against
  $p=7$, drag "slight overprediction".
- huang-2025: "conversion laws", references. nuca-2025: Eq. 10 sign,
  caption, κ range, coefficient count.
- ghidoni-2026-b: Eq. 27 operator, Table I constants, T3A $Tu$ 3.3%
  against 2.3%, Table VII rows, Blair B7/B13, Schubauer–Klebanoff and B1
  onset errors, reference 57. valencia-2026: Table II sign, Eqs. 8, 39,
  50, text against Tables VI–VII.

### Bibliography

7232 entries (+711 from 1315 printed references); 95 verified silences,
1 printed duplicate folded (von Neumann & Richtmyer, liang-2024 [8]/[10]),
`FLAGS: 0`. Cited planned sources take their planned slugs; keys printed
with a Source or planned slug for a different work re-keyed (`wang-2013-e`,
`wang-2013-f`, `li-2021-h`, `li-2022-c`, `li-2024-g`, `chen-2024-d`,
`gao-2023-b`, `liang-2024-b`, `maeyama-2022-c`, `huang-2025-b`,
`liu-2022-h`, `wang-2022-k`); preprints kept distinct (`mateogabin-2021`,
`motheau-2020-b`).

### Bundle fit (D17 candidates, no copy made)

- takagi-2022 (TENO-THINC), huang-2024 and huang-2025 (TENO limiters for
  RKDG), li-2024-c (multiphase TENO-THINC): shock-capturing numerics with
  inviscid tests only; liang-2024 (TENO-S) adds Taylor–Green and isotropic
  decay. `weno-teno` and `high-order-capturing-schemes` share their
  subjects.
- adhikari-2023: heliospheric turbulence transport (`fusion-mhd-simulation`
  and `astrophysical-simulation-codes` neighbours); ahn-2023: jet
  aeroacoustics.

### Candidate pages (kept inline until a second source)

Amplification-factor transport model; OVERFLOW; exponential decay
procedure and variational reconstruction; turbulent pipe flow;
T-junction mixing; Schubauer–Skramstad plate; Aérospatiale A airfoil;
nearly incompressible MHD; spectral proper orthogonal decomposition;
explicitly filtered LES; aliasing error; BASIC; libWallModelledLES.

## Chunk 7 — 2021–2026 papers: k-ω and wall functions in high-order RANS, CES and PITM, modal filtering and induced filters, multi-filter neural closures, volume-filtered immersed boundaries, entropy-conservative schemes; first whole-bundle deep lint (2026-10-26)

Sources (20): brillon-2026, caban-2026, dayer-2026, schotte-2026,
aiello-2026, lederer-2026, xu-2026, rickard-2026, wu-2026, jakhar-2026,
ranjbar-2026, ghidoni-2026, wang-2023, elzaabalawy-2023, wang-2021-l,
heinz-2022, luo-2021-b, tang-2022, yang-2022-b, zheng-2022. 140 of 160
ingested, 143 concept pages plus the registry, 6521 bibliography entries.
Deep lint A1–A10 over the whole bundle done.

### Decisions for the human

1. **Damage in committed content, repaired here.** The chunk-6 commit
   (58aad80) lost two sections of `wiki/methods/inflow-turbulence-generation.md`
   ("Triggering transition instead", "Choosing no inflow turbulence"),
   deleted by a compiler edit that removed one section by slicing to the
   next heading. They are restored verbatim from fdc020d. A scan of every
   chunk commit for lost headings and lines found no other loss.
2. **Overdue whole-bundle deep lint.** D26 requires one every 50
   ingestions; none ran before this chunk (120 ingested). It ran now, over
   all 284 pages. The next one is due by 190 ingestions, or with the chunk
   that completes the archive.
3. **The archive grew to 160 files.** The 26 new files fill chunk 7 to 20
   and make chunk 8 (20); the plan and the bundle law record it.
4. **Bibliography calls left by the resolver:**
   - `xiao-2015` is a 2006 J. Aircraft paper (43:1377, DOI
     10.2514/1.20127); its key and year come from zhao-2023-b's misprint.
     Rename the key?
   - `ming-2019`: the first author's surname is Yu (Yu, Xu & Pirozzoli),
     not "Ming". Rename the key?
   - `cockburn-1990` carried the DOI of Cockburn & Shu (1998); replaced by
     the Math. Comp. 54:545 DOI printed by dayer-2026 (Crossref-verified).
5. **Versions read.** Eight files are preprints or manuscripts
   (brillon-2026 and lederer-2026 are 2024 arXiv versions of 2026 papers;
   dayer-2026 is the submitted manuscript, four authors printed against
   three on Crossref; jakhar-2026's Supplemental Material is not in the
   file, and four of its claims rest on it). Replace with versions of
   record if you want the published claims.
6. **Candidate pages that now qualify:** approximate deconvolution model
   (caban-2026, cao-2024, the scale-similarity page); partially integrated
   transport model, PITM (heinz-2022, haering-2022, prietosaavedra-2024);
   Comte-Bellot–Corrsin grid turbulence (five sources); mass-conserving
   mixed-stress method (lederer-2023, lederer-2026); plus the chunk-6 list
   (discrete-adjoint method, wall-stress boundary condition, Ducros sensor,
   cutoff pile-up, curved backward-facing step, volume penalization) and
   the earlier ones.
7. **Tags:** synonyms merged bundle-wide (log entry). Left as they are:
   `k-omega`/`k-omega-sst` (different models), `wall-function`/`wall-model`
   (RANS against LES), `isotropic-turbulence`/`decaying-turbulence` (forced
   against decaying), and about 45 single-use tags.
8. **Still open from earlier chunks:** the `fusion-mhd-simulation` tab in
   `tearing-mode.md` line 247; `ge-2015`; `jameson-1988`; `suder-1996`
   thesis vs report; cao-2024 and reddy-2026 read from old preprints.

### Contradictions

Four open, all re-verified by the whole-bundle audit and kept:
sparse-regression coefficients
([tensor-basis neural network](wiki/methods/tensor-basis-neural-network.md));
gas-kinetic dissipation
([high-order gas-kinetic scheme](wiki/methods/high-order-gas-kinetic-scheme.md));
Cai & Sagaut wall-law constants ([law of the wall](wiki/definitions/law-of-the-wall.md));
Ahmed slant topology ([Ahmed body](wiki/benchmarks/ahmed-body.md)). No
chunk-7 source bears on them, and none was opened in chunk 7.

Kept as attributed qualifications: Wu & Lele (2026) against Kurz et al.,
Beck & Kurz and Sirignano & MacArt on discretization-consistent training
(no source runs both on one flow); Aiello et al. against Brillon &
Nadarajah on the weight of entropy conservation (Mach 3–5 thermally
perfect gas against Mach 0.1); Ghidoni et al. against Constant et al. on
wall functions for the NACA 0012 (body-fitted DG against immersed
boundary); Elzaabalawy et al. against Ghidoni et al. on the $k$–$\ln\omega$
form (method choices); the CRM-HL Reynolds numbers (5.49e6 on the mean
chord, 5.6e6 on the root chord); lederer-2023 against lederer-2026 HOPU
settings (two versions of the method); Rickard & Kasbaoui's no-slip forcing
against the wall-law immersed boundaries of Cai, Constant and Mozaffari
(different quantities).

### Printed slips (recorded on the Source pages)

- brillon-2026: $\kappa_c$ 122 for 112, $\kappa_{\mathrm{grid}}$ 4 for 2,
  Eq. 54 sign, clipping bound stated twice. caban-2026: Eqs. 16, 23, 32,
  42, 43; table pointers.
- dayer-2026: Eq. 14 order, $L_x^+$ 1009 for 1109, figure pointers,
  heat-flux sign, Eqs. 23, 25. schotte-2026: $\mathbf S$ without ½, Eq. 20,
  domain, residual thresholds, RAE2822 drag claim.
- aiello-2026: $\Delta t_s$ units, table pointers, garbled references.
  lederer-2026: Eqs. 5, 12, convective time, a DOI printed twice.
- xu-2026: least-squares rates, the "flux Jacobian", Eq. 33, duplicate
  references. rickard-2026: Eq. 2.25, the Fig. 6 ratio, the
  $\Delta_f^+\ge50$ against $\ge100$ threshold.
- wu-2026: network names across tables, Table 2 subset, reversed
  conclusion. jakhar-2026: Case 4 coarse-graining, caption symbols.
- ranjbar-2026: Eq. 7 $Ma_c$ for $Ma_c^2$, "internal energy", $Q_S$
  sign. ghidoni-2026: text against Table 1, inverted mesh range, Eq. 8.
- wang-2023: Ringleb credited to a book, figure caption, "≈2/3".
  elzaabalawy-2023: $\beta_1=0.75$, Table 3 percentages, $\varepsilon$
  printed "1⁻¹²", references [40]/[41] titles.
- wang-2021-l: Favre "hat", 1.8 % against 1.89 %, $C_{DES,k-\varpi}$.
  heinz-2022: one typo. luo-2021-b: Eq. 12, weight indices.
- tang-2022: Eqs. 3, 12–13, 17; Yoshizawa cited as [20].
  yang-2022-b: convection against viscous dominance, Lumley vertex, cell
  count. zheng-2022: CFL in Table 5, Appendix C, Eq. 23.

### Bibliography

6521 entries (+639 from 1089 printed references); 175 aliases, 24
verified silences, 5 printed duplicates folded, `FLAGS: 0`. Re-keyed away
from Source slugs: `aiello-2026-b`, `li-2024-d`, `li-2024-e`,
`wang-2024-g`, `liu-2024-c`, `kim-2024-c`, `wu-2025-b`, `lee-2013-c`,
`yang-2022-c`, `wu-2018-f`; `maejima-2024` (printed "Maejimam") kept
distinct from the Source `maejima-2025`; xu-2026's `bernades-2023`/`-b`
swapped to their identities; `chaouat-2021` and `jakhar-2025` separated
from Source keys they had matched by title.

### Bundle fit (D17 candidates, no copy made)

- wang-2023 (DG error transport, inviscid Euler), luo-2021-b (WENO-Z+M),
  xu-2026 (real-gas shock capturing), zheng-2022 (semi-Lagrangian WENO for
  Vlasov and 2-D Euler): no turbulence content; `weno-teno` and
  `high-order-capturing-schemes` share their subjects.
- schotte-2026 (mesh adaptation, RANS only), yang-2022-b (tip-leakage
  vortex), tang-2022 (supersonic combustion): applications of
  off-the-shelf closures.

### Candidate pages (kept inline until a second source)

Error transport equations; hybridizable DG; multi-filter training
augmentation; forced two-dimensional turbulence; Leith model; tandem
cylinders; tip-leakage vortex; minimal-span channel; JAGUAR; volume-filtered
immersed boundaries and slip-wall models; thermally perfect gas and EC-TP
flux; CDHD flux; nonlinearly stable flux reconstruction; subgrid scalar
variance closure.

## Chunk 6 — 2024–2026 papers: transitional DDES and cascade buffet, conditioned field inversion and model blending, neural-operator and super-resolution LES, shock capturing on the supersonic Taylor–Green vortex, GALÆXI, spectral-element WMLES, exascale DNS, bulk viscosity (2026-10-26)

Sources (20): moller-2024, cao-2024, cernetic-2024, chapelier-2024,
li-2024, llorente-2024, wu-2025, fanizza-2025, kurz-2025, oulghelou-2025,
zhao-2025, lohrer-2025, maejima-2025, rismondo-2025, yeung-2025,
klose-2025, beattie-2025, baldan-2025, mukha-2025, reddy-2026. 120 of 134
ingested, 134 concept pages plus the registry, 5882 bibliography entries.
Deep lint A1–A8 over the chunk-6 content done.

### Decisions for the human

1. **New contradiction** (below, Ahmed body): close by fiat, or keep open
   until a source that reports the Lienhart et al. PIV on the slant is
   ingested.
2. **Versions read.** Fifteen of the 20 files are preprints, author
   manuscripts or accepted manuscripts. Two differ materially from the
   published paper: cao-2024 is the arXiv v1 of July 2021 (five authors,
   Crossref lists four) and reddy-2026 is a preprint of 4 March 2021,
   five years before the CiCP version; mukha-2025's preprint has two
   authors, Crossref three. The pages carry the published metadata and
   the claims of the version read. Replace these files with the versions
   of record if you want the published claims.
3. **Bibliography calls left by the resolver:**
   - `suder-1996-b` (Suder's PhD thesis) is kept separate from `suder-1996`
     (the NASA report of the same title and year); chunk 5 folded
     Bardina's thesis and report into one entry. Fold or keep?
   - `mayle-1991` carried the DOI of Walker's 1993 discussion; replaced by
     Mayle's own DOI (Crossref-verified).
   - `kingma-2014`: maejima-2025 prints Gulrajani's arXiv number for Adam;
     the correct number is kept with a note.
4. **Candidate pages that now qualify** (≥2 sources): discrete-adjoint
   method (Fanizza, Wu, Cato, Yan); sigma model (Mukha,
   Moratilla-Vega); wall-stress boundary condition (Bae, Gillyns, Mukha);
   Ducros sensor (four or more sources); cutoff pile-up and
   thermalization in under-resolved LES (Vicente Cruz, Prakash, Kurz 2023,
   Flad, Chapelier); curved backward-facing step (Wu, Oulghelou);
   volume penalization (Ferrer, Llorente); plus the earlier lists
   (turbulent Prandtl number, modal/entropy filters, S809, Kelvin–Helmholtz,
   Hall MHD, interior-penalty DG, linear forcing, anisotropy-invariant map,
   optimal eddy viscosity, PVD cascade).
5. **Tag synonyms** reported by every auditor: `wall-modelled-les` (1) /
   `wmles` (42); `isotropic-turbulence` / `decaying-turbulence`;
   `machine-learning` / `data-driven` / `neural-network`; `high-order` /
   `dg`; single-use benchmark tags (`ahmed-body`, `periodic-hill`,
   `taylor-green-vortex`, `channel-flow`, `cylinder-wake`, `k-omega-sst`).
   A bundle-wide tag merge is proposed for the whole-bundle deep lint
   with chunk 7.
6. **Still open from chunk 5:** the `fusion-mhd-simulation` tab character
   in `tearing-mode.md` line 247, `ge-2015`, `jameson-1988`.

### Contradictions

- **Topology of the mean slant flow of the 25° Ahmed body.** Wu et al.
  (2025, §4.4) state that the experiment (Lienhart et al. PIV) "remains
  attached all along the slant"; Cai et al. (2022) describe the 25° shear
  layer as separating and reattaching on the slant, and Delassaux et al.
  (2023, §5) find the hybrids that separate and reattach closest to their
  own experiment. *Open* on [Ahmed body](wiki/benchmarks/ahmed-body.md).
- Reclassified: Gillyns et al. (2022) against Mukha et al. (2025) on
  time-averaging the wall-model input in Nek5000 — Mukha et al. tie the
  divergence to the filter settings and each paper reports on its own
  set-up; now a qualification on
  [equilibrium wall model](wiki/methods/equilibrium-wall-model.md),
  Nek5000, spectral-element method and turbulent channel flow.
- Updated: the open sparse-regression entry on
  [tensor-basis neural network](wiki/methods/tensor-basis-neural-network.md)
  now cites Oulghelou et al. (2025) on both sides. Four contradictions
  are open in the bundle: sparse-regression coefficients, gas-kinetic
  dissipation, the Cai & Sagaut wall-law constants and the Ahmed slant.

Kept as attributed qualifications: Fanizza et al. against Cato et al. on
corrections constrained to the Boussinesq form; Wu et al. against Yan et
al. on correcting the attached boundary layer; Möller et al.'s
$C_{\mathrm{DES}}=0.65$ against Carlsson et al. and Delassaux et al.;
Kim et al. (2022) against Maejima & Kawai on backscatter in channel flow;
Wang et al. (2023b) against Yeung et al. on single-precision DNS; Beattie
et al. ("shear-viscous compressible DNS is an implicit LES of the
compressible modes") against Seta & Federrath (2022), who state no bulk
viscosity; Lewis et al. (2023) against Rismondo et al. on FW-H quadrupole
terms; the NASA Rotor 37 design data (TP 1338, pressure ratio 1.82, cited
by Alauzet et al.; TP 1659, 2.05, cited by Kurz et al.; tip Mach 1.48
against 1.4939).

### Printed slips (recorded on the Source pages)

- moller-2024: reference [12] year; $\kappa$ for two quantities;
  "$l_{\mathrm{ratio}}<0$ not possible" (compiler check: the bound is
  $\ge1$). cao-2024: Eq. 11 metric terms, $(x_\eta)$ for $(x_\zeta)$,
  $C_f$, $C_p$ without ½, $Re_\tau$ from $\Delta x^+$ (compiler checks).
- cernetic-2024: Eq. 35 coefficient 351 printed as 315, Eq. 13 factor ½,
  "triple" for ×8, Eq. 8 index, swapped Fig. 2 panels (compiler checks).
  chapelier-2024: Eq. 5 without $\rho$, $Re$ without $L$, two descriptions
  of the SD3D artificial diffusion.
- li-2024: Eq. 9 against Eqs. 10–11 (factor −2), Eq. 23, "three times
  slower" (CPU only). llorente-2024: non-symmetric closure, heat-flux
  sign, missing time integral, "negative semi-definite".
- wu-2025: table and figure cross-references, Eq. 21 dimensions,
  misattributed author names. fanizza-2025: text against Tables 1–4,
  Fig. 3 against Eq. 40 (compiler check).
- kurz-2025: Eq. 15 indices, swapped captions, the 4×4×2 → 256³ mesh
  path. oulghelou-2025: $Re$ 13600/12600, OpenFOAM version labels,
  feature bounds. zhao-2025: Eq. 5, "∇τ" for the divergence, Algorithm 1
  pressure term, §5.4 directions.
- lohrer-2025: $T_f^{-1}$, Eq. A2 inverted ratio, $(0.0058U)^2$,
  stiffness factor, 66 against 288 hull iterations (compiler checks).
  maejima-2025: §6.2.2 signs, $k_z^+$ for $\lambda_z^+$, Kingma & Ba
  arXiv number.
- rismondo-2025: blockage 0.005% (compiler check 0.51%), tip Mach,
  "deviatoric" for antisymmetric, the $\ell_{ij}$/$T_{ij}$ viscous-stress
  sign. yeung-2025: Eq. 4.1 parenthesis, Fig. 5 intercept $\ln a$, cost
  (compiler checks).
- klose-2025: malformed inequalities, "Bassy-Rebay", overloaded $t$ and
  $N$. beattie-2025: Eq. 47 factor 3, E1 $\nu/3$, signs of Eqs. 56–57,
  $\gamma=1-R/c_V$, $k_0=\ell_0/(2\pi)$, e-fold time (compiler checks).
- baldan-2025: $\omega$ "18.67 Hz" (rad/s), Table 1 quad count, a running
  header from another paper. mukha-2025: $B=5.2$/5.5, mesh labels, node
  counts. reddy-2026: $S_{ij}$ without ½, filter width $/N$ against
  $/(N+1)$, Euler under a Navier–Stokes title.

### Bibliography

5882 entries (+895 from 1439 printed references); 229 aliases, 87
verified silences, 5 printed duplicates folded (reddy-2026 Favre and
Deardorff; oulghelou-2025 t-SNE; cao-2024 [26]/[55]; beattie-2025
Schekochihin 2002b/c, one work on Crossref), `FLAGS: 0`. Citations under
a Source's own slug: `yeung-2025-b`, `lohrer-2025-b`, `beattie-2025-b`
(and the 2025b preprint `beattie-2025-c`). Re-keyed away from Source
slugs: `kim-2024-b`, `morsbach-2024-b`, `huang-2022-c`, `liu-2024-b`,
`liu-2022-f`, `blind-2023-b` (FLEXI exascale preprint, cited by two
sources), `cao-2020-b`, `cao-2021-b`, `li-2022-h`/`-i`, `dang-2022-b`,
`zhao-2023-c`, `wang-2024-c`…`-f`, `chen-2024-b`. Preprints distinct:
`chapelier-2024-b` (cited as submitted), `cao-2021` (the preprint of
cao-2024). Identified on Crossref: `smith-2020` (printed "Marilyn J."),
`bin-2024` (AIAA J. 62:1434).

### Bundle fit (D17 candidates, no copy made)

- lohrer-2025 (aquatic canopy fluid–structure interaction) and
  rismondo-2025 (wind-turbine aeroacoustics): peripheral; turbulence
  modelling is a tool.
- cernetic-2024, beattie-2025 (astrophysical compressible turbulence):
  `astrophysical-simulation-codes` shares the subject.
- chapelier-2024, kurz-2025, cao-2024 (high-order numerics): `weno-teno`
  and `high-order-capturing-schemes` share their subjects.

### Candidate pages (kept inline until a second source)

Dynamic stall (Baldan); bypass transition (Möller); transitional DDES;
spectral proper orthogonal decomposition and the TCTA cascade (Klose);
Helmholtz decomposition and sonic scale (Beattie, Cernetic); small-scale
intermittency and dissipative anomaly (Yeung); LES activity parameter and
submerged canopy flow (Löhrer); wind-turbine wake (Rismondo); DAFoam;
converging–diverging channel; Straka density current; primitive-variable
projection; spectral difference method.

## Chunk 5 — 2023–2025 papers: autonomous and recalibrated SGS models, Bayesian and ensemble calibration, RL wall models, RSM and LKE transition, immersed-boundary and LBM wall treatments, flux reconstruction, tabulated chemistry (2026-10-26)

Sources (20): vadrot-2023, wang-2023-c, bottler-2023, steinhausen-2023,
ruan-2023, duan-2024, wang-2024, bouhafid-2024, liu-2024, petrocchi-2024,
prietosaavedra-2024, wang-2024-b, pacciani-2025, agrawal-2024,
constant-2024, mozaffari-2024, vangastelen-2024, chen-2024,
domaradzki-2024, kim-2024. 100 of 134 ingested, 115 concept pages plus the
registry, 4987 bibliography entries. Deep lint A1–A7 over the chunk-5
content done.

### Decisions for the human

1. **New contradiction** (below): ingest Cai & Sagaut (2021), close by
   fiat, or keep open.
2. **Bibliography calls left by the resolver:** `ge-2015` carries the DOI
   of Ge's dissertation (printed by an earlier source) while pacciani-2025
   cites the FTC 93:37 article (DOI 10.1007/s10494-014-9533-9): replace or
   split? `jameson-1988` records pages 3:377–401, which Crossref assigns to
   the 1989 Lecture Notes chapter of the same title (the 1988 paper is
   3:233–260): note added, pages unchanged.
3. **Escape-sequence damage in committed content.** The chunk-4 commit
   carried one bell character (a mangled `\approx`) in
   `benchmarks/periodic-hill.md`; repaired here. Outside this bundle,
   `fusion-mhd-simulation/wiki/definitions/tearing-mode.md` line 247 has a
   tab where `\to` belongs (`$3/1\to2/1$`); not touched (other bundle) —
   say whether to fix it in a separate commit.
4. **Versions read.** Nine of the 20 files are preprints or manuscripts
   (seven arXiv, two HAL).
5. **Candidate pages that now qualify:** turbulent Prandtl number (Chen et
   al. 2024, Huang et al. 2022, Helm & Martín 2022); modal and entropy
   filters for DG (Wang 2024, Dzanic & Witherden cited); S809 airfoil
   (Menter et al. 2022, Pacciani et al. 2025); Kelvin–Helmholtz instability
   (Ruan et al. 2023, Kou et al. 2023); plus the earlier list (Hall MHD,
   interior-penalty DG, linear forcing, anisotropy-invariant map, optimal
   eddy viscosity).
6. **Bundle fit:** bottler-2023 (laminar premixed hydrogen flames, no
   turbulence) is the weakest fit of the archive so far; it is ingested
   with a minimal footprint (its Source page and the tabulated-chemistry
   page).

### Contradictions

- **Constants of the Cai & Sagaut (2021) explicit inverse wall law.**
  Cai et al. (2022) print the blend scale 180.8, exponent 0.789 and
  $E=11.27$; Mozaffari et al. (2024) print 86.58, 0.7894 and $E\approx7.9$
  for the same form attributed to the same work; neither calls its set a
  recalibration. *Open* on [law of the wall](wiki/definitions/law-of-the-wall.md).

Kept as attributed qualifications after checking the PDFs: the T3
Schubauer–Klebanoff inlet turbulence intensity (0.03% in Menter et al.
2022, 0.3% in Pacciani et al. 2025, each an inlet setting tuned to the
measured decay); model-form error called "aleatoric" (Agrawal &
Koutsourelakis) and "epistemic" (Duraisamy et al. 2019) under different
definitions; the Parnaudeau et al. reference data called experiment and
LES (one experimental and numerical study); Domaradzki against Vela-Martín
on negative eddy viscosity; Wang et al. (2024) against Goc et al. on
numerical dissipation; Duan & Wang against Saini et al. on the
Taylor–Green dissipation shares; Vadrot et al. (2023a) against Bae &
Koumoutsakos on the reward bonus and the log-layer mismatch; Cai et al.
against Mozaffari et al. on the Ahmed slant.

### Printed slips (recorded on the Source pages)

- vadrot-2023: Eq. 12 against Eq. 2 (compiler check); Eq. 6 index.
  wang-2023-c: integration limits of Eq. 24; duraisamy-2019 page printed
  537.
- steinhausen-2023: $\delta_L$ definition; "vertical" for vortical.
  ruan-2023: $E_k$/$E_{tur}$; Eqs. 7–8 without ½ and $1/(8\pi)$.
- duan-2024: $Re_\tau$ definition, P2/P3 legend, model constants not
  printed. wang-2024: undefined ξ and γ after Eq. 11; Eq. 2 indices; swapped
  diffusion labels.
- bouhafid-2024: Eq. 4.3 without the square; abstract against §4.3.1 on
  the vortex lifespan; $t_b$ (compiler check).
- liu-2024: Table 1 row assignment; dissipation multiplied by max(γ, 0.1).
  petrocchi-2024: duplicated run IDs; Eq. 8 and Table 3 (compiler checks).
- prietosaavedra-2024: Table 5 caption; flow-through counts; Appendix A
  units (compiler checks). wang-2024-b: Table 2a, "[-5.5:4]", Eq. 7, the
  TGV Mach number (compiler check), entropy filter credited to the wrong
  reference.
- pacciani-2025: $f_{\mu,\ell}$ exponent without the minus sign (compiler
  check); figure references. agrawal-2024: Reynolds-stress sign, $T^{(7)}$
  antisymmetric as printed (compiler check), Table 2 viscosities.
- constant-2024: "$y^+=0$" for the first-cell height; normal/tangential
  swap; Table 3 and 9 errors. mozaffari-2024: production index in Eqs.
  16–17; "Exp." column from a DES paper.
- vangastelen-2024: duplicate [29]/[32]; [29] cited as PINN work;
  "machine precision" against "up to a time discretization error".
  chen-2024: Eq. 3.14 step; $y/\delta_{99}$ labels. domaradzki-2024: Table 1
  and 2 $\lambda$; Table 2 caption units. kim-2024: grid sizes in App. D;
  "LES390ccc".

### Bibliography

4987 entries (+746); 198 aliases, 67 verified silences, 2 printed
duplicates folded (agrawal-2024 [53]/[64]; vangastelen-2024 [29]/[32]),
`FLAGS: 0`, `--dupes` clean. Re-keyed away from Source slugs: `li-2022-g`,
`cao-2022-b`, `liu-2022-c`/`-d`/`-e`, `wang-2023-e`/`-f`,
`dzanic-2022-b`, `kang-2023-b`, `petrocchi-2022` (conference paper with the
same title). Preprints distinct: `vadrot-2022`, `kurz-2022-d`,
`prakash-2022-b`. Surname normalizations: `rai-1991`, `martin-2000`,
`vanalbada-1982`, `dileoni-2021`. DOIs corrected from Crossref:
`spalart-2007`, `cai-2021-b`, `ahmed-1984`.

### Bundle fit (D17 candidates, no copy made)

- bottler-2023, steinhausen-2023 (combustion chemistry), ruan-2023 (solar
  flare MHD: `astrophysical-simulation-codes`), bouhafid-2024 (aircraft
  wake vortices): peripheral to closure modelling.
- wang-2024, wang-2024-b, duan-2024 (high-order numerics): `weno-teno` and
  `high-order-capturing-schemes` share their subjects.

### Candidate pages (kept inline until a second source)

OAT15A transonic buffet; PVD compressor cascade (Liu et al. 2024, Li &
Liu 2022 — qualifies); continuous eddy simulation; TKE budget; Lethe;
energy-conserving neural closure; fusion SGS network; stochastic
variational inference; states–action map of RL wall models; aircraft
wake vortex; flame–wall interaction.

## Chunk 4 — 2023–2024 papers: learned SGS models, symbolic regression, anisotropic SGS stress, hybrid RANS/LES of cars and turbomachinery, stabilized high-order methods, lattice Boltzmann, Hall MHD (2026-10-26)

Sources (20): delassaux-2023, zhao-2023, zhao-2023-b, moratillavega-2024,
morsbach-2024, saini-2023, slaughter-2023, kurz-2023, bernades-2023,
cheylan-2023, kou-2023, lederer-2023, wang-2023-b, kang-2023,
lozanoduran-2023, sirignano-2023, foldes-2023, lewis-2023, inagaki-2023,
tang-2023. 80 of 134 ingested, 103 concept pages plus the registry, 4241
bibliography entries. Deep lint A1–A7 over the chunk-4 content done.

### Decisions for the human

1. **Two contradictions opened** (see below): both rest partly on works
   outside the archive or on judgements of adequacy; close by fiat, or keep
   them open until a source settles them.
2. **Bibliography calls left by the resolver:** `bardina-1983` merges a
   PhD thesis (kang-2023) and a Stanford report (inagaki-2023) printed with
   the same title, authors and year; `lewis-2021` (online-first form) now
   also holds the 2022 AIAA J. 60 issue printed by lewis-2023; `yuan-2020`
   and `yuan-2020-b` stay separate (arXiv paper and Phys. Fluids
   32:115106, relation not confirmed). Split or keep on your word.
3. **Versions read.** Ten of the 20 files are preprints or manuscripts
   (seven arXiv, one Research Square, two HAL); delassaux-2023's HAL title
   ("Computational analysis …") differs from the published one ("Numerical
   analysis …").
4. **Candidate pages that now qualify** (two or more sources): Hall MHD
   (Ferrand et al. 2022, Foldes et al. 2023); interior-penalty DG (Kou et
   al., Zhao et al. 2023b, Ferrer et al.); a differential Reynolds-stress
   model (Morsbach et al., Mozaffari et al.); linear forcing of isotropic
   turbulence (Kurz et al., Kang et al.); the anisotropy-invariant map
   (Tang et al., Kang et al., Morsbach et al., Helm & Martín); the optimal
   eddy viscosity (chunk 3). Inline for now; say which you want as pages.

### Contradictions

- **Sparse-regression closures: constant or invariant-dependent
  coefficients?** Tang et al. (2023, §III B) say such closures "only contain
  constant coefficients that keep unchanged for the whole computational
  domain"; Duraisamy (2021, §III.A) describes the sparse regression of
  Schmelzer et al. as acting on "candidate functions which are written as
  tensor polynomials of the aforementioned invariants". Both recall
  Schmelzer et al. (2020), not ingested. *Open* on
  [tensor-basis neural network](wiki/methods/tensor-basis-neural-network.md).
- **Is the fifth-order gas-kinetic scheme's dissipation right for implicit
  LES?** Cao et al. (2022, §3.1): on the Taylor–Green vortex the coarse-mesh
  filtering "correctly mimics" the unresolved dissipation from $128^3$ up;
  Zhao et al. (2023a, §5.1): the same scheme at $256^3$ "is still
  over-dissipative". *Open* on
  [high-order gas-kinetic schemes](wiki/methods/high-order-gas-kinetic-scheme.md).

Kept as attributed qualifications: Kurz et al. against Beck & Kurz on the
dynamic model (they agree where their cases overlap); Lederer et al.
against Abe on explicit models in implicit LES; wall-resolved LES cost
exponents $Re^{2.7}$ and $Re^{2.5}$ (recalled from different works); SST
limiter with rotation (Dzanic et al.) or strain (Zhao et al. 2023b);
Carreño Ruiz & D'Ambrosio against Morsbach et al. on separation bubbles;
Ferrand et al. against Foldes et al. below the ion scale (different
quantities); ACAT1 data of François et al. against Lewis et al.; Ahmed
body width 0.389 m against 380 mm.

### Printed slips (recorded on the Source pages)

- delassaux-2023: 185M against 180M cells; Table 3 sign of ΔCd; 8 against
  9 refinement boxes; core-hour ratio (compiler check).
- zhao-2023: $N=(5-3\gamma)(\gamma-1)$; viscosity and $\Delta z^+$ against
  their own formulas (compiler check). zhao-2023-b: Eqs. 2-2/2-5, the
  $\omega$ wall condition against $C_w$, ref. [30] title.
- moratillavega-2024: CFL bound, $St_{\max}$, element counts (compiler
  checks); probe distance 20 against 15. morsbach-2024: coarse-mesh DOF;
  Afshar et al. (2022) cited but not listed.
- saini-2023: percentage ranges across sections; ε for two quantities.
  slaughter-2023: $C_p$ printed as the dynamic pressure; unsquared TKE;
  $St=30$ against 10–20.
- kurz-2023: reward form of Table 1 against Eq. 21. bernades-2023: Eq. 33
  velocity difference, $N_f$ of the F4 filter, $G^E$ factor.
- cheylan-2023: Eqs. 12, 37, 40; Table 7 Strouhal error (compiler check).
  kou-2023: Eq. 27, 4096 against 4095 DOF, two against three test cases.
  lederer-2023: Eq. 9 upwind term without the absolute value; Table 3
  gDOF equal to Table 1's; quadrature order (compiler check).
- wang-2023-b: Table 3 speed-ups, Table 8 ratio definition, G1 GPU count.
  kang-2023: Leaky ReLU printed as $\max[-0.02x,x]$; Eq. (3.4) partly
  illegible (gap recorded). lozanoduran-2023: duplicated "2019a" labels,
  $\Pi$ wording, training ranges against validation cases.
- sirignano-2023: §4.2 "all statistics" against §7. foldes-2023: D3Q27
  edge weight 8/27 against 1/54; Eqs. 3.27 and B1 (compiler checks).
  lewis-2023: Table 9 total, Table 10 error, mesh averages against the
  quoted WMLES ranges. inagaki-2023: Eqs. 7, 12, 14, factor ½ after Eq. 10.
  tang-2023: barycentric station 1.5 against 0.5; figure captions swapped;
  Eqs. 16 and 19.

### Bibliography

4241 entries (+668 from 1113 printed references); 132 aliases, 29
verified silences, 2 printed duplicates folded (lewis-2023: Ffowcs
Williams & Hawkings 1969; Meyer et al. 2019), `FLAGS: 0`. Printed keys
equal to a Source slug for a different work re-keyed: `sirignano-2023-c`,
`bernades-2023-b`, `menter-2022-b`, `huang-2022-b`, `li-2022-f`,
`wang-2023-d`, `yan-2022-b`, `lozanoduran-2022-b` (Lozano-Durán & Arranz);
`kurz-2022-c` (ETNA, distinct from its preprint `kurz-2020`);
`polacsek-2022-b` (published form of the submitted `polacsek-2022`).
Wrong earlier merges split: the BR1 paper to `gassner-2018`,
`balakumar-2015`. `ducros-1999` volume 152 (printed 1252) confirmed on
Crossref.

### Bundle fit (D17 candidates, no copy made)

- moratillavega-2024, lewis-2023 (aeroacoustics), cheylan-2023
  (fluid–structure interaction), wang-2023-b (GPU and floating-point
  precision): peripheral to closure modelling.
- foldes-2023 (Hall-MHD lattice Boltzmann): `astrophysical-simulation-codes`.
- bernades-2023, kou-2023, lederer-2023, zhao-2023 (numerics):
  `weno-teno` and `high-order-capturing-schemes` share their subjects.

### Candidate pages (kept inline until a second source)

NASA CRM-HL; turbulent Poiseuille–Couette flow; MTU T161 cascade; DrivAer
car; Settles cavity–ramp; NACA 0012; σ model; variational multiscale
method; reduced-precision simulation; Orszag–Tang vortex; Burgers
turbulence; RHEA, TRACE, AVBP, NGSolve; explicit algebraic Reynolds-stress
model; grid-induced separation; subdomain energy-budget dissipation
analysis.

## Chunk 3 — 2022–2023 papers: learned SGS and RANS closures, immersed boundaries, GPU codes, shock–boundary-layer interaction, plasma and wave turbulence (2026-10-26)

Sources (20): maeyama-2022, coelho-2022, fischer-2022, davidovits-2022,
kochurin-2022, helm-2022, cai-2022, dang-2022, eivazi-2022, kim-2022,
mcconkey-2022, seyedi-2022, dahlin-2022, ferrand-2022, gan-2022,
placco-2023, ferrer-2023, blind-2023, carlsson-2023, cato-2023. 60 of 134
ingested, 84 concept pages plus the registry, 3573 bibliography entries.
Deep lint A1–A7 over the chunk-3 content done.

### Decisions for the human

1. **Two new archive files.** Wang & Roy (2023), J. Comput. Phys.
   474:111760 (error transport for DG), and Elzaabalawy et al. (2023),
   J. Comput. Phys. 483:112059, appeared after founding; both are planned
   in chunk 7 (now 14 sources) as `wang-2023` and `elzaabalawy-2023`. To keep
   suffixes in publication order, the planned GPU gas-kinetic paper
   (J. Comput. Phys. 476:111899, chunk 4) becomes `wang-2023-b` and the
   EnKF SGS paper (Phys. Fluids 35:085107, chunk 5) `wang-2023-c`.
2. **Bibliography calls left by the resolver:** ferrer-2023's Reed & Hill
   Los Alamos report was folded into `reed-1973` (the conference entry), as
   in chunk 2; `pope-2006` (a reprint printed by helm-2022) was folded into
   `pope-2000`, while `pope-2010` and `karniadakis-2005`/`karniadakis-2013`
   remain separate entries; ferrand-2022's Kolmogorov (1941) citation
   (Russian edition, page 16 against 19) was folded into
   `kolmogorov-1941` without a Crossref check. Split or keep on your word.
3. **carlsson-2023 ref. [28]** prints the title and authors of its ref.
   [35] with a different DOI; the DOI resolves to Probst, Löwe, Reuß, Knopp
   & Kessler, AIAA J. 54:2972, which matches the text's "Löwe [28]". The
   entry (`probst-2016`) now follows the DOI's record.
4. **Versions read.** Sixteen of the 20 files are preprints or author
   manuscripts (13 arXiv, 2 HAL, 1 author manuscript); the Source pages say which
   and cite their locators. blind-2023's arXiv title ("Grid-adaptation for
   wall-modeled large eddy simulation using unstructured high-order
   methods") differs from the published one; ferrer-2023's arXiv version
   prints 13 authors where Crossref lists 14 (Marbona H. added).
5. **Optimal eddy viscosity page?** McConkey et al. (Eqs. 6–7), Cato et
   al. (Eq. 18), Abe (2021) and Vela-Martín (2022) use the same projection
   of a reference stress on the strain rate (compiler check). It is now
   inline on the Boussinesq page; a page of its own qualifies.

### Contradictions

None open. Considered and kept as attributed qualifications:
**modelled-energy threshold of LES** — Haering et al. recall the 10% of
Jiménez & Moser but run well past it; Seyedi & Zayernouri use 10% as the
line between LES and very-large-eddy simulation; Helm & Martín say 25–30%
"may be possible"; Blind et al. cite Toosi & Larsson's finding that the
ratio correlates poorly with length scales; the four define the fraction
differently ([large-eddy simulation](wiki/definitions/large-eddy-simulation.md)).
Also: Kim et al. (eddy-viscosity form limiting for a learned SGS model)
against Cato et al. (stress misalignment immaterial to the reconstructed
mean flow); best-fit eddy viscosity of the stress (McConkey) against that
of the mean velocity (Cato); Gan et al.'s Alfvén anisotropy exponent
against Schekochihin's local-field argument; Kochurin et al.'s weak
turbulence of a non-conducting ferrofluid against Schekochihin's critique
of weak MHD turbulence; Seyedi & Zayernouri against Kim et al. on
backscatter; Ferrer et al. against Flad & Gassner on DG for implicit LES;
Cogo et al. against Placco et al. on the schemes of STREAmS; the Trettel–
Larsson transformation printed with the square root over the whole
integrand (Carlsson et al., Eq. 26) and without it (Cogo et al., Huang et
al.). The FLEXI mortar types of Krais et al. (2:1, 4:1) and Blind et al.
(2-to-1) were found to describe the same halving.

One chunk-2 error corrected: the channel page called the PANS fraction
$\beta_k$ "resolved"; it is the unresolved fraction. Cato et al. print
$c_{w1}=c_{b1}/\kappa^2+\dots$ with Alauzet et al.'s constants, which
confirms the chunk-2 compiler check on Alauzet et al.'s $c_{b1}/\kappa$.

### Printed slips (recorded on the Source pages)

- helm-2022: separation-length increase 32% (abstract) against 30%
  (§§IV F, V); 25% and 18% for the same wall value; 12% (§V) against 14%
  (§III B); Table III wide-domain row duplicates the narrow one; rescaling
  lengths 29δ/7δ attached to the wrong simulation types; index slips.
- dang-2022: 24 567 against 24 576 GPUs; Table 6 total ($10^{12}$ against
  the rows' $10^{11}$, compiler check); weak- and strong-scaling
  efficiencies against the printed times; WENO-SYMBO operation count 216
  against 262; Eqs. 12, 13, 15–16, 19, 27, 38; companion Part 2 cited but
  not listed.
- blind-2023: test-level factor 1.59 (1.31 from the printed degrees,
  compiler check); Table 4 captioned $Re_\tau=550$; 512 DOF per element
  against degree 5; Table 2 row $l=2$.
- fischer-2022: Table 1 header $n$, Table 2 38-node time, $E=6840$ against
  6480, 248× against 234×, operation count of §2.3.
- seyedi-2022: order "$2\alpha\in(1,2]$" against $\alpha\in(0,1]$;
  swapped labels in Eq. 24; inconsistent symbols in Eqs. 7, 10, 19, 21.
- placco-2023: $C_P$ without the square on the Mach number; "order of
  magnitude" reduction against Table 3 (factor 2.2–4.6, compiler check).
- cato-2023: Eqs. 2b, 9, A16; ref. [9] cited as "Duraisamy et al." (first
  author Singh); threshold 0.86 against 0.8.
- carlsson-2023: LD2 credited to "Löwe et al. [28]"; $C_{dw}$/$C_w$; figure
  and equation cross-references.
- maeyama-2022: $\Omega_i$ for $\Omega_e$; phase velocities 42.7, 45.1
  against 47.3, 42.6 from the printed values (compiler check).
- ferrand-2022: $d_i=0.05/L_0$; missing $\sqrt{\mu_0}$ in Eqs. 17, 23
  (compiler check); $F_{F21}$ for $F_{A18}$.
- dahlin-2022: "just over 15×" against 18 (compiler check); kochurin-2022:
  $\omega\sim k^{-3/2}$ for $k^{+3/2}$ (Fig. 4); gan-2022: run C wave
  fraction 0.271 against "less than ∼25%", run A fast fraction; davidovits-
  2022: Fig. 6 Mach numbers against Table I; cai-2022: Eqs. 16, 18
  consistent only for $\Delta=1$; kim-2022: run length; mcconkey-2022:
  Table II duplicates, invariant count; ferrer-2023: Eq. 2, Fortran
  2003/2008, scaling "up to 1000 processors"; eivazi-2022, coelho-2022:
  minor.

### Bibliography

3573 entries (+805); 87 aliases, about 55 verified silences, 2 printed
duplicates folded (ferrer-2023 refs [16]/[40]; gan-2022 Meyrand 2016),
`FLAGS: 0`, `--dupes` clean. Printed keys equal to a Source slug for a
different work re-keyed: `li-2022-c` (Li, Chen & Ren, JCP 448, cited by
dang-2022), `li-2022-d` (Li, He & Liu, PoF 34, cato-2023), `li-2022-e`
(Tianwen-1, Astrodynamics, placco-2023), `cai-2022-c`, `kim-2022-b`;
self-citations kept as `@misc` entries `maeyama-2022-b` (code and data)
and `kochurin-2022-b` (supplemental material). Preprints kept distinct:
`mateogabin-2021`, `duraisamy-2020`. Corrected from Crossref:
`ohyabu-1994` (printed 1984), `paruta-2018` (volume 25), `priest-1996`
(Phil. Trans. A), `lumley-1978` (pages 123–176), `probst-2016`.

### Bundle fit (D17 candidates, no copy made)

- maeyama-2022 (gyrokinetic cross-scale turbulence) and coelho-2022
  (stellarator edge turbulence with GBS): `fusion-mhd-simulation`.
- dahlin-2022 (coronal helicity condensation; its "subgrid-scale model" is
  a parametrized source term, not an LES closure), ferrand-2022 and gan-2022
  (space-plasma and compressible MHD turbulence): `astrophysical-simulation-codes`.
- kochurin-2022 (magneto-capillary wave turbulence), davidovits-2022
  (laboratory shock-generated turbulence), placco-2023 (planetary entry),
  fischer-2022 and ferrer-2023 (software papers): peripheral to closure
  modelling.

### Candidate pages (kept inline until a second source)

Optimal eddy viscosity (qualifies, see decision 5); constrained LES;
lattice Boltzmann method and ProLB; Ahmed body; continuous spectral
element method; Ducros and Jameson shock sensors; Reynolds-stress
anisotropy invariants; Reynolds-force vector; Richtmyer–Meshkov
instability; very-large-eddy simulation; v2-f model; WALE model;
gyrokinetics and GKV; drift-reduced Braginskii model and GBS; MHD
wave-mode decomposition; proper orthogonal decomposition.

## Chunk 2 — 2021–2023 papers: SGS clipping, PANS, mesh adaptation, DES, transition, wall laws, gas-kinetic DNS, RL wall models, dynamos (2026-10-25)

Sources (20): abe-2021, pereira-2021, prakash-2022, mozaffari-2022,
hoy-2022, basile-2023, carrenoruiz-2022, gillyns-2022, knopp-2022,
yan-2022, alauzet-2022, cao-2022, mateogabin-2022, cogo-2022, huang-2022,
francois-2022, liu-2022, martinalvarez-2022, seta-2022, bae-2022. 40 of 132
ingested, 68 concept pages plus the registry, 2768 bibliography entries.
Deep lint A1–A7 over the chunk-2 content done.

### Decisions for the human

1. **New archive file.** Ghidoni et al. (2026), J. Comput. Phys.
   550:114637 (explicit wall function for high-order DG RANS), appeared in
   the archive after founding; identity checked on Crossref and page 1,
   planned as `ghidoni-2026` in chunk 7 (now 12 sources).
2. **Bibliography calls left by the resolver:** the chunk-1 key
   `langtry-2004` holds Langtry et al. Part II, J. Turbomach. 128:423, whose
   print issue is 2006 (the year-of-issue rule would make it
   `langtry-2006`); `duan-2011-b` (Part 3, JFM 672) precedes `duan-2011`
   (Part 4, 684), so the suffixes are not in publication order; Reed & Hill,
   printed "1977, p. 23" with no venue by mateogabin-2022, was folded into
   `reed-1973` on authors and title alone. Rename or split on your word.
3. **Version read of bae-2022** is the Research Square preprint v1 (June
   2021); the Nature Communications version may differ in numbers and
   wording, and the pages cite the preprint.

### Contradictions

None open. One opened at drafting and reclassified: **log-layer mismatch
of the Bae & Koumoutsakos RL wall model** — Bae & Koumoutsakos (2022,
preprint) report a friction-velocity error below 5% from $Re_\tau=5200$
to $10^6$; Vadrot et al. (2023b, Table III) measure log-layer mismatches of
$+1$ to $+2$ and $-0.9$ to $-3.2$ in their re-implementation. Different
quantities, solvers and matching heights ($h^+_{\mathrm{wm}}$ about 4.7
times lower in Vadrot et al., compiler check), and Vadrot et al. attribute
the difference to grid resolution: now a qualification on
[machine-learning wall models](wiki/methods/machine-learning-wall-model.md),
cross-referenced from the RL-closure, log-layer-mismatch and benchmark
pages. Near-conflicts kept as attributed qualifications: Yan et al.'s
strain-based baseline SA against Li & Liu; two printed forms of the DDES
shielding function (François et al., Yan et al.); unsteady RANS judged
incorrect (Mozaffari et al.) and needed (Carreño Ruiz & D'Ambrosio) in
different regimes; Abe (2021) and Cao et al. (2022) on implicit LES in
different settings.

### Printed slips (recorded on the Source pages)

- alauzet-2022: $c_{w1}$ printed with $c_{b1}/\kappa$ (the log-layer
  balance gives $c_{b1}/\kappa^2$, 3.24 against 2.76, compiler check);
  destruction-term sign in Eq. 13; inverted anisotropic-ratio formula;
  Table 2 mass-flow ratios of the elsA rows.
- pereira-2021: production-sign slip between Eqs. 5 and 17; the "half-width"
  growth rate of Eq. A9 is that of the full height.
- yan-2022: SA destruction term without the square; training hill shapes
  (text 0.5/0.8, captions 0.8/1.2); Table 4 against Table 3.
- cao-2022: Eq. 11 sign; $k_{\max}$ formula against Table 8.
- cogo-2022: Table 2 shape factor of case M6L (10.9 printed, 13.4 from the
  row); Eqs. 5.9–5.10 exponent. huang-2022: Table 3 ratios; $H_{12}$
  against the Hopkins correlation.
- basile-2023: `max` in Eq. 18 against the marking rules.
- bae-2022: reward sign (Eq. 9) and $\beta$ update (Eq. 8).
- seta-2022: compression-term sign reading; Table 3 parts against the
  Table 2 total; Lorentz force labelled "dyne".
- martinalvarez-2022: §3.2 exponent pairing; liu-2022: $q=10^3$ caption,
  Eq. 13 primes, units of $E_{\mathrm{mag}}$.
- knopp-2022: constant 1.78 kept in §7.4 after the revision to 1.68;
  prakash-2022: correlation-coefficient normalization (Eq. 19);
  mateogabin-2022, mozaffari-2022, francois-2022, carrenoruiz-2022,
  gillyns-2022, hoy-2022, abe-2021: minor slips.

### Bibliography

2768 entries (+953 from 1248 printed references); 105 aliases, 38 verified
silences, 3 printed duplicates folded (liu-2022 Kretschmer 2019/2020 and
Schmidt 2011a/b; martinalvarez-2022 Attia 2021), `FLAGS: 0`. Keys corrected
from Crossref: `pudritz-1989` (printed 2002), `vazza-2018`,
`steinwandel-2020`, `kretschmer-2020`, `beck-2016-b`; cao-2022's
`jeffrey-2014` aliased to `slotnick-2014`, carrenoruiz-2022's
`menter-1994` to `menter-1994-b`.

### Bundle fit (D17 candidates, no copy made)

- liu-2022, martinalvarez-2022, seta-2022 (dynamos in galaxy and
  interstellar-medium simulations): `astrophysical-simulation-codes`.
- mateogabin-2022 (entropy-stable SVV and shock capturing for DG) and
  cao-2022 (gas-kinetic schemes): `weno-teno`.
- alauzet-2022 (adjoint-based anisotropic mesh adaptation for steady RANS)
  and hoy-2022 (fluid–structure interaction under shock/boundary-layer
  interaction): peripheral to closure modelling.

### Candidate pages (kept inline until a second source)

Stabilized mixed model; approximate deconvolution; anisotropic
minimum-dissipation model; laminar separation bubble; SD7003 airfoil;
nonequilibrium turbulence; discrete adjoint (Yan, Alauzet); strong
Reynolds analogy; uniform momentum zones; inflow turbulence generation
(Bae, Cogo, Huang); shock/boundary-layer interaction; dilatational
dissipation; wall-model input filtering; spectral elements and Nek5000;
quasi-Eulerian refinement; mean-field dynamo; solenoidal and compressive
forcing.

## Chunk 1 — reviews and vocabulary papers (2026-10-25)

Sources (20): duraisamy-2019, duraisamy-2021, schekochihin-2022,
vadrot-2023-b, goc-2021, domingo-2023, vicentecruz-2023, velamartin-2022,
menter-2022, haering-2022, dzanic-2022, flad-2017, krais-2021, fowler-2022,
griffin-2023, lozanoduran-2022, agrawal-2022, beck-2023, li-2022,
agdestein-2025. 55 concept pages plus the registry, 1815 bibliography
entries. Deep lint A1–A7 over all 75 pages done.

### Decisions for the human

1. **Bundle name and scope.** The bundle is `turbulence-modelling` (the
   archive's spelling) and takes the whole archive, including turbulent
   combustion, MHD and plasma turbulence, and DG/FR numerics (D30). Rename
   or narrow it now if you want: the slug sets every path.
2. **Periodic-hill period: $9h$ or $9.5h$?** Haering et al. (2022, §V B)
   print the domain of the ERCOFTAC case UFR 3-30 as "$9.5h\times3.035h\times
   4.5h$"; Dzanic et al. (2022, §3.1) give $9h$ crest to crest for the
   Fröhlich et al. configuration. Opened as a contradiction at drafting,
   moved to Qualifications on
   [periodic hill](wiki/benchmarks/periodic-hill.md) by the deep lint (the
   papers make no claim about each other's domain). The auditor found that
   the ERCOFTAC knowledge-base page of UFR 3-30 gives $9h$; that web page
   is not an ingested source and is not used as evidence in the wiki. If
   you rule the $9.5h$ a printed slip, the qualification can say so.
3. **WMLES cost exponent, $Re^{4/3}$ against $Re^{1.1}$.** Opened as a
   contradiction at drafting on
   [grid-point requirements](wiki/results/les-grid-point-requirements.md),
   moved to Qualifications by the deep lint: Goc et al. (2021, §4) assume
   their own time-step scaling for an aircraft at chord Reynolds number,
   Griffin et al. (2023) and Vadrot et al. (2023b) quote Yang & Griffin
   (2021) for a flat plate. Ingesting Yang & Griffin (2021) would settle
   the exponent; it is on the bibliography frontier.
4. **Three MHD pages carry `status: hypothesis`**
   ([dynamic alignment](wiki/properties/dynamic-alignment.md),
   [tearing-mediated turbulence](wiki/results/tearing-mediated-mhd-turbulence.md),
   [small-scale dynamo](wiki/results/small-scale-dynamo.md)), because
   Schekochihin (2022) calls these theories "hotly debated … still subject
   to verification" (§8.2) and the dynamo evidence "tentative" (§13).

### Contradictions

None open. Two opened at drafting and moved to Qualifications (items 2 and
3 above). Near-conflicts recorded as qualifications with both sides
attributed: Beck & Kurz (2023) against Agdestein & Sanderse (2025) on
whether a closure must be trained inside the solver (different
discretizations); Duraisamy et al. (2019) "enforces" against Duraisamy
(2021) "promotes" model consistency; Haering et al. (2022) against
Dzanic et al. (2022) on numerical dissipation and PANS; Vela-Martín (2022,
isotropic turbulence) against Li & Liu (2022, rotating RANS flow) on
backscatter.

### Printed slips (recorded on the Source pages)

- schekochihin-2022: Eq. (7.17) prints $\varepsilon^{-3/4}$ (dimensionally
  $\varepsilon^{-1/4}$); §12.5.2 decay exponent $t^{-1/2}$ against $t^{-2/3}$
  from the printed exponents; p. 111 (§13.3.4) and footnote 79 print
  positive $Rm$ exponents for $\lambda_R$ against Eq. (13.9).
- flad-2017: filter width printed as a volume; $C_S$ squared in App. A–B,
  unsquared in C–D; dynamic procedure (D.2/D.4) sign and unsquared width
  ratio; Eq. C.3 drops the plateau term.
- dzanic-2022: Eq. 11 destruction term dimensionally short of $\omega_u$;
  Eq. 23 not the log transform of Eq. 11; DNS spanwise resolution ratio.
- krais-2021: Eq. 31 weight ratio inverted; Eq. 46 interpolation matrices
  swapped; Eq. 64 flux arguments; Fig. 20 legend off by one power of two.
- vicentecruz-2023: Eq. 23 sign, Eq. 38 missing $4\pi k^2$, Eq. 39 missing
  $\nu$.
- beck-2023: Eq. 18 reward exponent sign (always $\ge1$ as printed).
- fowler-2022: Eq. 3.6 leading minus.
- griffin-2023: Eq. 1.2 damping exponent sign; $\kappa$ printed "4.1";
  "4Δ" against 3.6Δ.
- goc-2021: viscous stress without the factor 2; "<4 h" and "7.5 days"
  against Table 1.
- haering-2022: Eq. 1 short of $\nu^2$; the $9.5h$ period (item 2).
- lozanoduran-2022: twelve number and label slips ($m\approx-1/7$, $+5/6$,
  $\alpha_q$ for $\alpha_p$, Re values, figure captions).
- menter-2022, velamartin-2022, agdestein-2025, agrawal-2022,
  duraisamy-2019, duraisamy-2021, domingo-2023, vadrot-2023-b, li-2022:
  minor slips (labels, cross-references, reference-list defects).

### Identity and metadata

- No archive defects: 131 distinct works, no byte copies, no misfiled
  papers. Twelve files carried preprint DOIs (Research Square, SSRN,
  conference); their published identities were taken from Crossref and
  checked against page 1.
- Versions read in chunk 1: eight arXiv preprints (duraisamy-2019,
  schekochihin-2022, dzanic-2022, flad-2017, krais-2021, lozanoduran-2022,
  beck-2023, agdestein-2025), four CHORUS accepted manuscripts
  (duraisamy-2021, vadrot-2023-b, haering-2022, agrawal-2022), two HAL
  author manuscripts (domingo-2023, vicentecruz-2023), six versions of
  record. Locators are those of the version read.

### Bibliography

1815 entries from 2083 printed references; 119 aliases, 42 verified
silences, 6 printed duplicates folded (haering Girimaji [22]/[34],
duraisamy-2021 Mishra [32]/[79], four pairs in domingo-2023), `FLAGS: 0`,
`--dupes` clean. Keys printed with a Source slug for a different work were
re-keyed (`cai-2022-b`, `li-2022-b`, `liu-2022-b`, `schekochihin-2022-b`,
`bae-2022-b`, `sirignano-2023-b`, `goc-2021-b`, `goc-2021-c`). Calls left to
the human:

1. vicentecruz-2023 prints Lilly's NCAR 1966 title with the 1967 IBM
   symposium venue and year; folded by title into `lilly-1966` (it could be
   `lilly-1967`).
2. `wu-2018-e` (duraisamy-2021, "in preparation") is probably the study of
   the arXiv preprint `wu-2018-d`; kept distinct (preprint rule).
3. A "Pope 2001, IOP" citation was folded into the book `pope-2000`.
4. menter-2022's printed DOIs for Ge 2015 (resolves to a dissertation) and
   Suluksna 2009 (resolves to Int. J. Heat Fluid Flow) disagree with the
   printed venues; kept as printed, with notes.
5. beck-2023 cites its own published version (ref. [84]); the entry is kept
   without a self-`citedby`, as the linter requires.

### Bundle fit (D17 candidates, no copy made)

- krais-2021 (FLEXI) and flad-2017 (kinetic-energy-preserving DG): also in
  the subject of `weno-teno`, which has a FLEXI page of its own.
- schekochihin-2022 (MHD turbulence theory): `fusion-mhd-simulation` or
  `astrophysical-simulation-codes`.
- domingo-2023 (DNS of turbulent combustion): peripheral to closure
  modelling.

### Candidate pages (kept inline until a second source)

Kolmogorov flow; equipartition spectrum; split forms and summation by
parts; polynomial de-aliasing; flux reconstruction and PyFR; quasi-DNS;
commutation error and computational subgrid stress; approximate
deconvolution; Lagrangian dynamic and anisotropic minimum-dissipation
models; variational multiscale LES; detached-eddy simulation; resolution
tensor and modelled-stress depletion; quadratic constitutive relation;
transition hysteresis; circular cylinder at $Re_D=3900$; Gaussian bump;
dynamic slip and integral wall models; extrapolation theorem; reconnection
and plasmoids; Saffman-type invariants; weak and imbalanced MHD turbulence.
