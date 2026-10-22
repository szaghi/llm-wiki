# Ingestion issues — weno-teno

Reviewer's digest, one section per chunk, newest first: contradictions
opened (the normative record is the `## Contradictions` section of the
named page), printed inconsistencies, identity and metadata problems,
bundle-fit suggestions, and questions left to the human. Not part of the
OKF wiki; maintained by the compiler at every chunk.

## Chunk 1 — founding chunk: reviews and vocabulary (2026-10-21)

Sources (20): fu-2023, wu-2023-b, deng-2023, huang-2026, balsara-2024,
wang-2022-b, ye-2022, fu-2021, luo-2021-b, li-2022-b, ranocha-2023,
chertock-2023, wang-2023-b, takagi-2022, peng-2024, abgrall-2023,
coppola-2023, ruedaramirez-2022, cui-2024, kuzmin-2023. 82 concept pages,
the registry, 20 Source pages, 860 bibliography entries.

### Decisions for the human

1. **Archive defects (page-1 and checksum check of all 207 files).** Two
   files are byte copies of other files and one holds another paper than
   its name says:
   - `2023_..._Computers_amp_Fluids_Wang_Fifth_order_AWENO_...pdf` is a byte
     copy of Li et al. 2022 (WENO-ZN, C&F 244:105547);
   - `2024_..._Journal_of_Computational_Physics_Li_A_family_of_TENOA-THINC-MOOD_...pdf`
     is a byte copy of Liang et al. 2022 (TENO, JCP 467:111465);
   - `2026_..._Physics_of_Fluids_Feng_Improvements_of_weighted_...pdf`
     holds Wang, Don & Wang 2023 (C&F 251:105743), which will be ingested
     from it as `wang-2023` in chunk 11.

   Missing works, listed with DOIs in `~/papers/mosaic/weno-teno-redownload.csv`:
   Feng et al. 2026 (Phys. Fluids 38:011302, `10.1063/5.0303368`) and Li et
   al. 2024 (JCP 519:113375, `10.1016/j.jcp.2024.113375`). Proposal, as for
   ode-integration: you re-download both into `~/papers/re-download`, and
   authorize the compiler to overwrite the three files so that every
   filename names its content (Li 2024 into the TENOA-THINC-MOOD file;
   the Wang 2023 paper into the AWENO-named file; Feng 2026 into the
   Feng-named file). Until then the two byte-copy filenames stay on the
   worklist as pending.
2. **Contradiction "accuracy condition on $\tau_K$"** ([TENO](wiki/methods/targeted-eno.md)).
   Fu (2023, §3.1, Eq. 17) states that $\tau_K/(\beta_k+\epsilon)=O(\Delta x^s)$
   for any $s>0$ gives the design order; Ye et al. (2022, §3.5, Eqs. 36–38)
   state that $O(\Delta x^{K-2})$, i.e. $\tau_K=O(\Delta x^K)$, "need[s] to be
   satisfied". Three auditors read both papers as incompatible claims about
   the same property and kept the entry *Open*; a fourth reads Ye et al.'s
   "need" as a stronger sufficient condition (their own Eq. 39 uses a
   sixth-order $\tau$ for every $K$) and would move it to Qualifications.
   It stays open; you may close it by fiat.
3. **Bibliography calls to confirm:**
   - `ranocha-2018-c`: Ranocha's 2018 thesis (cited by ranocha-2023) and its
     Cuvillier book edition (cited by ruedaramirez-2022) merged as one work.
   - `liu-2021-b` (no venue printed) kept apart from `liu-2022` (SISC
     44:A230), of which it is probably the preprint; it was not printed as
     a preprint.
   - `toro-2009` and `toro-2013` kept distinct as printed.
   - `sonntag-2014`: ruedaramirez-2022 ref [4] printed without a year, keyed
     by its venue (FVCA VII, 2014).
   - `harten-1997` and `shu-1989-b` treated as reprints in the Springer
     collection "Upwind and High-Resolution Schemes", silenced against the
     originals.
   - `demichele-2023-c`: the "submitted" form of `demichele-2023`, its own
     entry by the preprint rule.
4. **Bundle fit (no D17 copy made).** ranocha-2023 is mainly a
   software/HPC paper on DG kernels (fits a codes bundle as well);
   kuzmin-2023 is a continuous-finite-element paper; balsara-2024's test
   systems are multiphase models. All are in scope here. None of the 20
   chunk-1 works is a Source page of another bundle.

### Identity and metadata

- Version read differs from the version of record for 13 sources:
  arXiv preprints wu-2023-b (v1, 28 pp.; the SIAM Review paper has 43, so
  numbering may differ), ranocha-2023 (v2), chertock-2023 (v2), fu-2021
  (v1), peng-2024 (v1), kuzmin-2023 (v1), coppola-2023 (v1),
  ruedaramirez-2022 (v2), cui-2024 (v1); author or accepted manuscripts
  deng-2023, balsara-2024, abgrall-2023. Each Source page records the
  version and cites its numbering.
- peng-2024: Crossref has no volume or pages yet (online 30 July 2024);
  the venue is "Math. Comp." only.
- coppola-2023: page 1 prints the second author as A. E. P. Veldman
  (Crossref: A. E.); the page-1 form is used.
- Filenames name a given name in place of the surname for Balsara
  ("Dinshaw", a chunk-4 source) and Sousa ("C", chunk 3).

### Printed slips (the Source pages list them in full)

- li-2022-b Table 2, $r=5$, $k=4$: 77/20 for 77/60 (row sum 214/60).
- ye-2022 Tables 1, 3, 5: signs and order of several interpolation
  coefficients (re-derived exactly).
- abgrall-2023 Eqs. (51)–(52): quadrature weights that do not sum to 1;
  Eqs. (55)–(56) swapped; Eq. (111) claims one order too many.
- wu-2023-b Eq. (6.21): exponent $+1/2$ of $\rho$ where $-1/2$ holds (arXiv v1;
  whether the version of record fixes it is unknown).
- cui-2024 Example 3: Rankine–Hugoniot pressure ratio with $M^2+1$ for $M^2-1$.
- balsara-2024 §VIII.b: anti-diffusion "switched off" together with
  $\psi=1$ (full anti-diffusion); §III "we don't consider well-balancing"
  against well-balanced results in §VIII.
- fu-2023 and takagi-2022: double Mach reflection captioned at $t=2.0$
  (Takagi et al.'s text gives $t=0.2$; the review's figure carries the same caption); fu-2023's hierarchical voting count
  (14 cases by Eq. 20 as printed, not 9).
- chertock-2023: the Titarev–Toro-type state is a Mach 1.3 shock, not 1.1,
  and its density drops a digit against Luo & Wu and Fu 2021.
- deng-2023 Eq. 6.6: the new WENO weight stays $O(1)$ away from the linear
  weight at the accuracy point, so the scheme is formally second order,
  not uniformly third (compiler check).
- ranocha-2023 §4.2: the text's speed-up ranges disagree with its own
  Table 2.
- coppola-2023 Eq. (6): a missing minus sign.
- Double Mach reflection post-shock pressure: 116.8333 (fu-2021,
  takagi-2022, ye-2022, huang-2026) against the Rankine–Hugoniot value
  116.5 (peng-2024, wang-2023-b): a setup difference, not a contradiction.

### Candidates for later pages

Kept inline until a second source or a named contribution arrives: the
Hu–Adams–Shu positivity flux limiter (fu-2021, takagi-2022, wang-2022-b
use it), bar states and invariant domains, OFDG, the logarithmic mean,
entropy projection, TENO-N, hybrid and unstructured TENO, multi-resolution
WENO as its own page, WENO-P/P+, the convection boundedness criterion, the
Titarev–Toro problem, the Leblanc shock tube, two-dimensional explosion and
implosion problems.
