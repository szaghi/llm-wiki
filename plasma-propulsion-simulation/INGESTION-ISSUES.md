# Ingestion issues — plasma-propulsion-simulation

Reviewer's digest, one section per chunk, newest first: contradictions
opened (the normative record is the `## Contradictions` section of the
named page), printed inconsistencies, identity and metadata problems,
scope decisions, and questions left to the human. Not part of the OKF
wiki; maintained by the compiler at every chunk.

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
