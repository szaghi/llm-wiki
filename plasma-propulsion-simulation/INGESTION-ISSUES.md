# Ingestion issues — plasma-propulsion-simulation

Reviewer's digest, one section per chunk, newest first: contradictions
opened (the normative record is the `## Contradictions` section of the
named page), printed inconsistencies, identity and metadata problems,
scope decisions, and questions left to the human. Not part of the OKF
wiki; maintained by the compiler at every chunk.

## Chunk 3 — five papers in full, 15 Source-only pages (2026-10-15)

Sources in full: alpatov-2018, shuvalov-2018, gomezjenkins-2018,
garciagarrido-2018, yang-2018. Source-only: ahmad-2018, an-2018, antoni-2018,
bu-2018, cai-2018-b, cerf-2018, conte-2018, crusan-2018, delchambre-2018,
dhara-2018, dong-2018, gagg-2018, grieve-2018, guo-2018, gomezsanjuan-2018.
New concept pages: [ion-beam shepherd](wiki/definitions/ion-beam-shepherd.md)
(alpatov, shuvalov, takahashi-2019, cai-2018) and
[plasma drag augmentation of a magnetized body](wiki/results/magnetized-body-plasma-drag.md)
(shuvalov). Notation §7 added (plasma–body interaction).

### Contradictions opened

None. Judged qualifications:
* Alpatov's analytic far-plume force (collisionless, full momentum deposition,
  no charge exchange, no reflection) vs the EX-PWS PIC-DSMC plate force of
  cai-2018. The regimes differ (7 m in orbit vs 0.6–1.0 m in a chamber), and
  Cai's own sensitivities support the simplifications: reflection changes the
  force by 0.1–0.25 %, and CEX ions carry under 0.1 % of the momentum.
* The beam pressures Shuvalov quotes for LEOSWEEP (8.43 and 4.04 mN/m² at 7 and
  10 m) cannot be derived from Alpatov's LEOSWEEP beam in Table 2. The auditor
  gets a disc mean of about 10.6 and 5.5 mN/m², and about 34 mN/m² on axis.
  Shuvalov does not state the area or averaging, so this is recorded here only,
  not in the wiki.

### Printed inconsistencies worth your attention

* **alpatov-2018:**
  * Table 2 prints the Xe ion mass as 2.8×10⁻²⁵ kg; the correct value is
    2.18×10⁻²⁵ kg. Only 2.18 reproduces the printed 0.031 N (0.0315 N vs
    0.0405 N).
  * Table 2 gives $I_{sp}$ = 3400 s next to an ion velocity of 71580 m/s, which
    corresponds to about 7300 s. That implies a propellant utilization of about
    0.47, which the paper never states.
  * The 2×10⁻⁷ N/kg bound is an orbital-perturbation estimate, not a beam
    force. The drafts had it wrong; the audit caught it and it is fixed.
* **shuvalov-2018:**
  * The boundary field is undoubled in Eqs. 4–5 and doubled in §§4–5.
  * The printed ratio 3.72 uses the doubled field and the larger sphere: it
    recomputes to 3.69, against 3.23 for the smaller sphere.
  * The §5 value $B_W$ = 3.9×10⁻³ T is a misprint for 3.9×10⁻² T.
  * The claim that 0.6–0.8 T matches the shepherd beam pressures holds only for
    the 4.04 and 1.44 mN/m² beams, via Fig. 9. In the paper's own Fig. 8 at
    700 km, the 8.43 mN/m² case needs about 2.6 T. The drafts overstated this;
    it is fixed.
  * The magnetic moment of 1.1–7.2 A·m² does not fit 0.2 T surface fields.
  * The values the text gives for Fig. 8 are 1.3–1.5× the plotted markers.
* Every Source page records its paper's other slips under "Recorded as printed".
  Recomputations by readers are labelled "Reader's check" and kept separate.
  The pages with the most (equation-level slips) are conte-2018, cai-2018-b,
  delchambre-2018, gagg-2018, guo-2018, gomezjenkins-2018, garciagarrido-2018
  and yang-2018.

### Identity and metadata

* **Re-slug:** the file filed under "Gomez" is by Gomez Jenkins, Krejci &
  Lozano. Crossref gives the family name "Gomez Jenkins", and the paper's own
  ref. [16] prints "Gomez-Jenkins". Its slug is `gomezjenkins-2018`, following
  the bundle's convention for compound surnames (garciagarrido, gomezsanjuan).
  The bundle law and the plan were updated to match.
* Page 1 matched the filename for all 20 files. Every file is the publisher's
  typeset version, and every issue year is 2018.

### Bibliography (2130 → 2738 entries, FLAGS 0, `--dupes` clean)

* Self-key traps re-keyed: three cited works carried the citing paper's own
  slug.
  * bu-2018's ref. [1] is now `bu-2018-d`.
  * an-2018's ref. [13] is now `an-2018-b`.
  * conte-2018's ref. [9] is now `conte-2018-b`.
* cai-2018-b's ref. [13] is the authors' IAC 2017 version of the same paper. It
  stays a separate entry, `cai-2017-c`.
* Collisions with existing keys:
  * alpatov's `zhou-1996` (Zhou, Doyle & Glover) and an-2018's `wang-2000`
    (Wang & Stengel) are different works and got new suffixes.
  * shuvalov's `bombardelli-2011` is the existing entry.
* Year re-keys from Crossref: huang-2015 → huang-2016-g, fujii-2012 → 1996,
  umetani-2010 → 1989, chacko-1986 → 1987, conte-2017 → conte-2018-b.
* Undated references keyed by the year their DOI resolves to: qi-2015,
  bezrouk-2018, committee-2010, cerf-2007, scott-2007. esa-2014 takes its year
  from the reference's URL; 20 other undated entries take the citing year 2018,
  with a note.
* "de Almeida Prado" is keyed `dealmeidaprado-*`, following the repo convention
  of keeping name particles in the stem.
* Internal duplicates in garciagarrido-2018 ([9]=[29], [10]=[23]) and
  antoni-2018's folded repeat printings (45 printed → 37 works) were verified.
* grieve-2018's refs [24]/[25] are one title in two venues, kept as two
  entries.

### Decisions for you

1. **`voland-2005` has the wrong year.** Crossref
   (doi:10.1016/j.actaastro.2006.02.021) puts Acta Astronaut. 59:181 in 2006.
   an-2018 prints the year correctly. The key is shared with the
   high-speed-aerothermodynamics and chemical-airbreathing-propulsion
   bibliographies, so re-keying it to `voland-2006` means changing three
   bundles. I merged under the existing key and changed nothing. Re-key it?
2. **Year-uncertain keys.** `folkner-2018` and `europeancommission-2018` follow
   the citing-year rule; their real dates (2014; March 2017) cannot be verified
   on Crossref. `esa-2014` takes its year from a URL.
3. **`first-1973`** is antoni-2018's ref. [4], a list of the EU enlargement
   waves, not a citable work. I kept it as `misc` with an honest title, because
   the rule is to merge reference lists unfiltered. Drop it?
4. **Orphan warnings, amended bundle law.** gomezjenkins-2018,
   garciagarrido-2018 and yang-2018 are full ingestions, but none earns a
   concept page, so the lint reports each as an orphan. I amended the bundle
   law to accept that case, with the reason on each page and no `context` tag.
   The amendment is yours to veto. The open question from chunk 2 still
   stands: should the lint exempt pages tagged `context`?
5. **Scope trim, applied.** The off-domain controller and propellant detail of
   alpatov-2018 stays on its Source page. The ion-beam-shepherd page keeps only
   a three-line summary of it, per the bundle's scope rule.

## Chunk 2 — 21 Source-only pages (2026-10-14)

Sources: knight-2018, liu-2018-c, liu-2018-d, meng-2018, moradi-2018,
wang-2018-d, zhao-2018, zuo-2018, fedele-2018, cheng-2018, armbruster-2018,
bai-2018, peng-2018, zhou-2018, song-2018, wang-2018-c, yan-2018, ye-2018,
veale-2018, li-2018, greer-2018 — high-speed aerothermodynamics and chemical
propulsion, outside this bundle's domain (D23). No concept page changed, no
contradiction possible under the scope rule. Their printed inconsistencies are
recorded on each Source page and digested in the issues files of the two
bundles that compile them in full (D23; named here only because this file is
outside the wiki).

* **Bibliography:** 1437 → 2130 entries. Cited works whose natural key was a
  slug reserved for another Acta vol. 151 file were re-keyed past it
  (`zhang-2018-d`…`-i`, `li-2018-d/e/f`, `zhao-2018-c`, `yan-2018-b`,
  `huang-2018-d`, `guo-2018-b`). zhao-2018 cites "Mosavat 2018", which is the
  ingested moradi-2018 (Crossref).
* **Lint:** each Source-only page has no incoming link from a concept page, so
  the lint warns "orphan" for each (21 now, 67 when all chunks are in). The
  bundle law records them as expected. **Decision for you:** keep the
  warnings, or let `tools/lint_okf.py` exempt pages tagged `context` (a tool
  change I have not made).
* **Wording ruling applied:** the Source-only pages do not name the bundles
  that compile the papers in full (D12: no claim about other bundles in
  bundle content); the bundle law now says so.
* Version read: every paper is the publisher's typeset version; page 1
  matched the filename for all 21.

## Chunk 1 — the core (2026-10-14)

Sources: boyd-2005, mungiguerra-2018, adamovich-2017, cai-2018, sun-2018,
zhang-2018, taccogna-2019, takahashi-2019, charoy-2020, gallo-2021,
giannetti-2021, reza-2022, taccogna-2023, ahedo-2023, eckels-2024,
marks-2025, munoz-2025, miranda-2026, troyetsky-2026, saravia-2026.

### Contradictions opened (all Open)

1. **Form of the Jorns (2018) data-driven anomalous collision frequency** —
   [anomalous electron transport](wiki/definitions/anomalous-electron-transport.md).
   taccogna-2019 §2.4 prints $\nu_{\mathrm{ano}}\propto\omega_{ce}(c_s/u_{e,\theta})^2$;
   taccogna-2023 Eq. 22 prints $\omega_{ce}(u_i/u_{e,\theta})^2$; both cite Jorns,
   PSST 27:104007 (2018), not ingested. Closes on ingesting Jorns (2018).
2. **First GPU PIC simulation of a plasma thruster** —
   [GPU acceleration](wiki/methods/gpu-acceleration-of-pic.md). gallo-2021 §2.6
   claims priority (citing one review); taccogna-2023 states the CUDA code
   ECCOPIC2S-M ran the 2019 axial–azimuthal benchmark, and taccogna-2023 and
   marks-2025 cite CHAOS (MPI-CUDA PIC-DSMC, 2018). **Recommended for your fiat
   closure** against the priority claim.
3. **Cause of the ion-acoustic character of azimuthal PIC below about 1000
   particles per cell** — [electron drift instability](wiki/definitions/electron-drift-instability.md).
   taccogna-2019 §3.4: numerical noise "facilitates the transition"; charoy-2020
   pp. 17–18 (about 250 per cell): physical nonlinear smearing of the cyclotron
   resonances. Found by the audit; neither source tests the other's mechanism.

Tensions judged qualifications (prose on the pages, not entries): particles per
cell as convergence criteria (taccogna-2019 vs charoy-2020 vs marks-2025);
saravia-2026 non-identifiability of the plume Bohm coefficient vs giannetti-2021's
current-only calibration; reza-2022 (Lafleur mobility identity confirmed) vs
charoy-2020 (ion-trapping saturation rejected); cell size $\Delta x<3.4\lambda_D$
(miranda-2026) vs $\le\lambda_D$; polytropic indices; SPT-100 parameter spread;
marks-2025's insensitivity of transport to the azimuthal spectrum vs the
friction closure (compiler note).

### Identity and archive problems

* **The file `2009_..._Physics_of_Fluids_Bird_Accuracy_and_efficiency_...pdf` is
  not Bird et al. (2009).** Page 1 is Mungiguerra, Zuppardi, Spanò Cuomo &
  Savino, *Acta Astronaut.* 151:456–466 (2018). Ingested as `mungiguerra-2018`.
  **Bird, Gallis, Torczynski & Rader (2009), Phys. Fluids 21:017103,
  doi:10.1063/1.3067865 is not in the archive — download it if you want it.**
  Consequently the archive holds 16 papers outside *Acta Astronautica*, and 92
  files from Acta vol. 151 (not 91 as recorded at scaffolding; corrected in the
  bundle law).
* Versions read other than the version of record: charoy-2020 and
  taccogna-2019 (HAL accepted manuscripts), taccogna-2023 (accepted
  manuscript, different title: "Plasma propulsion simulation using
  particles"), reza-2022 (Research Square preprint; Figs. 8–12 and 14 have no
  images, results from text only; preprint prints 34 references, the journal
  36). Reference counts of the published versions differ for taccogna-2019
  (199 printed vs 239 on Crossref) and taccogna-2023 (344 vs 391); the
  bibliography carries the lists as read.
* sun-2018 is purely experimental (ablative PPT ignition); it supports only the
  PPT page.

### Printed inconsistencies (details on each Source page, "Recorded as printed")

Every source has some. The ones a concept page quotes or depends on:
* saravia-2026: $k_m$ printed $2.5\times10^{13}$ m³/s, almost certainly $10^{-13}$.
* miranda-2026: the printed $\omega_{pe}$ is $f_{pe}$; the theoretical
  wavelength does not follow from the printed $\lambda_D$.
* marks-2025: $B_{\max}$ printed $10^{-12}$ T (text: 10 mT); GPU/node counts
  differ between text and Table 3; 3.5× quoted vs 3.78× from its own timings.
* munoz-2025: water reaction count 25+20 not reproducible from Table 4;
  300 V × 1.6 A = 480 W printed 520 W; loss fractions sum to 1.06.
* boyd-2005: SPT-100 density about $10^{17}$ m⁻³ in §3.4 vs $10^{18}$–$10^{19}$ in
  Table 1; eq. 2.3 has $\partial p/\partial t$ on the right of the energy equation.
* taccogna-2019: plume potential drop "50 %" (§2.5) vs "one third" (§3.6);
  breathing period 30 µs (33 kHz) beside "about 20 kHz".
* cai-2018: shadow density drop "five orders" (§4.2) vs "three" (conclusion);
  accommodation 0.74 in text vs Table 1 values.
* gallo-2021: its "RK4" (Eqs. 3–4) is not the classical scheme; Isp 662 s
  (Fig. 10) vs 698 s (Table 3).
* zhang-2018: about 25000 K at the wall at 100 ns vs about 7300 K from its own
  fluence fit; the "atmospheric" validation with a model without ambient gas.
* eckels-2024: uncertainty bounds called "overconfident" (p. 17) and
  "overly-conservative" (p. 28) for the same reason.

### Bibliography decisions (1437 entries; resolution module and report kept in the session scratchpad)

* `taccogna-2019` (this RMPP review) vs the PSST 2019 EDI paper it cites →
  the latter is `taccogna-2019-b`; Charoy's 2020 thesis is `charoy-2020-b`;
  munoz-2025's "Maryam 2022" is `reza-2022` (by DOI).
* 16 undated web resources keyed by the earliest citing year with a note
  (e.g. `landmark-2019`, `ultranest-2026`), per bundle convention.
* Year re-keys only where Crossref proves the true year (e.g. `hockney-1988`,
  printed 1989; `gascon-2003`, printed 2023), printed forms kept in notes.
* **Decisions for you:** (a) publication forms are kept apart — conference
  paper vs its report issue (`sankovic-1993`/`sankovic-1994`), book reprints
  (`bird-1994`/`bird-1998`, `jahn-1968`/`jahn-2006`, `hockney-1988`/`hockney-2021`);
  confirm the policy. (b) `birdsall-2004`: the Taylor & Francis reprint's year
  (2004 or 2005) is not on Crossref. (c) `biagi-2021` and `biagi-2022` (LXCat
  Biagi database, two versions) kept distinct. (d) `boeuf-2019` (LANDMARK
  wixsite) kept distinct from `landmark-2019` (landmark-plasma.com).

### Scope and granularity

* mungiguerra-2018 (DSMC aerodynamics of a de-orbiting small satellite) is
  outside the plasma domain; it contributes only to the DSMC and gas–surface
  pages (scope rule).
* Merged after the audit, below the granularity bar: LANDMARK test case 3
  (into the 1D fluid model page), LPPic (into the axial–azimuthal benchmark
  page), EP2PLUS (into the hybrid-model page).

### Notation decisions

* Bohm-type coefficients are normalized to $\nu_{\mathrm{ano}}=\alpha_{\mathrm B}\omega_{ce}/16$;
  every source's native form and its conversion is on its Source page.
* Permittivity scaling $\varepsilon_0\to f_\varepsilon^2\varepsilon_0$ (Debye length
  scales by $f_\varepsilon$); calibrated parameters $\boldsymbol\vartheta$ (never
  $\theta$, the azimuthal coordinate).
