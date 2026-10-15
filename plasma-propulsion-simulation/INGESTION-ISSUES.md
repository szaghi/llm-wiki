# Ingestion issues — plasma-propulsion-simulation

Reviewer's digest, one section per chunk, newest first: contradictions
opened (the normative record is the `## Contradictions` section of the
named page), printed inconsistencies, identity and metadata problems,
scope decisions, and questions left to the human. Not part of the OKF
wiki; maintained by the compiler at every chunk.

## Human rulings (2026-10-15)

1. **`voland-2005` → `voland-2006`**, in this bundle and in the two bundles
   that share the key (Crossref doi:10.1016/j.actaastro.2006.02.021, print
   July 2006).
2. **Preprints are kept** as distinct bibliography entries, not folded into
   the published version ("they are what I studied"). This undoes the
   chunk-4 and chunk-5 folds: `hippke-2017-f`, `learned-2008` and
   `lubin-2016-b` are separate entries. It is the rule for future
   ingestions.
3. **The GPU-priority contradiction is closed by fiat** against Gallo et
   al.'s claim (hypothesis-grade closure). Two contradictions stay Open.
4. **Orphan warnings: option B** (D24). The lint no longer warns for
   Source pages tagged `context`, which cuts this bundle's orphan
   warnings from 85 to the 3 full ingestions that wait for a second
   source. The bundle-law amendment was trimmed to match.

## Chunk 6 — the last 7 Source-only pages, closing sweeps, deep lint #2 (2026-10-15)

Sources: yamaguchi-2018, yang-2018-b, yu-2018, yuan-2018, zhang-2018-b,
zhang-2018-c, zhao-2018-b. They cover Hayabusa2 operations, structures and
reflector accuracy, tether deployment, magnetically suspended actuators and
pyroshock, all outside this bundle's domain (D23).

**The archive is complete: 108 of 108 files are ingested** (`tools/worklist.sh`:
pending 0). The audit found no errors and 5 minor items, all fixed.

### Notes

* **yamaguchi-2018** reports Hayabusa2's ion engines: four 10 mN engines,
  about 3900 h and about 580 m/s by March 2018. These figures are mission
  context in a planning paper, with no thruster model, so the page is
  Source-only. The paper gives its 7000 h figure with two different scopes,
  recorded as printed.
* Page 1 matched the filename's title for all 7 files. Every file is the
  publisher's version, and every issue year is 2018.

### Bibliography (3899 → 4084 entries, FLAGS 0)

* **Ingested-slug and self-key traps:**
  * yang-2018-b's and yuan-2018's citations printed as `yang-2018` are not
    the ingested tether paper. They are now `yang-2018-d` and `-f`.
  * yang-2018-b's ref. [31] carried its own slug and is now `yang-2018-e`.
  * zhang-2018-c's "li-2018" is now `li-2018-g`.
* **Year re-keys from Crossref:** coleman 2011→2012, greschik 2015→2001,
  wang 2012→2014.
* **Venue slips corrected with notes:** six entries. One is `kanzawa-2016`,
  which came in with chunk 4: its page 949 → 952, per Crossref.
* yu-2018's ref. [16] title is kept exactly as printed ("are-entry
  capsule"), with the correction in the note.
* **Closing sweeps (mandatory after the final chunk):**
  * `--dupes`: 0 groups.
  * Cross-year fuzzy-title sweep: 51 candidate pairs, all distinct works.
  * Placeholder titles grouped by venue: 0.
  * Shared DOIs across keys: 0.
  * Same-key vol:page check over the whole bibliography: 38 differences, all
    intended variants with notes.

  No corpus-wide merge was needed.

### Deep lint #2 (all concept pages, registry, root index)

Findings: 1 error, 3 law items, 24 minor items, 11 tag merges. All are
applied except two optional items, listed below as decisions. The error:
the mobility page misstated Reza et al.'s Hall parameter, which is
$\omega_{ce}/\nu_{\mathrm{ano}}$, not $\Omega_e$. Unregistered symbols are
gone from concept pages, and `$\mathrm{Re}_m$` is now registered. The three
Open contradictions were re-verified. Details are in `wiki/log.md`.

### Decisions for you

1. **Issue-year rule:** `wang-2014-g` follows the Crossref issue year, while
   `deng-2014` keeps its printed year because its article number marks it as
   2014. If the rule is "issue year, always", deng-2014 becomes deng-2015.
2. **Mangled keys:** `s-2002` and `m-1992` keep keys built from mangled
   author strings. Corporate keys (`dod-2002`, `asm-1992`) would be cleaner;
   re-key them?
3. **`performance` tag:** it is used only for computational performance, so
   it collides in meaning with thruster performance (registry §6). Rename it
   to `computational-performance`? Not applied.
4. **GPU-priority contradiction:** it has been Open since chunk 1 and is
   recommended for your fiat closure.
5. **Still open from chunks 3–5:**
   * the `voland-2005` re-key across three bundles;
   * dropping `first-1973`;
   * the orphan-warning amendment and the lint exemption for `context` pages;
   * the preprint folds (hippke-2018-b, learned-2012, lubin-2016);
   * the unverified years and `neuhauster-2018`.

## Chunk 5 — 20 Source-only pages (2026-10-15)

Sources: meng-2018-b, miller-2018, mu-2018, nies-2018, pallone-2018,
perez-2018, pestrenin-2018, sabatini-2018, semyonov-2018, unknown-2018,
verspieren-2018, volpe-2018, wang-2018, wang-2018-b, wang-2018-e, wang-2018-f,
wu-2018, wu-2018-b, wu-2018-c, xu-2018. They cover space robotics, GNC,
structures, radiation dosimetry, operations, relativistic flight, history and
the issue's front matter, all outside this bundle's domain (D23). No concept
page changed. Each paper's slips are on its Source page under "Recorded as
printed". The read-only audit found no errors and 4 minor items, all fixed.

### Identity and metadata

* Page 1 matched the filename's title for all 20 files. Every file is the
  publisher's version, and every issue year is 2018.
* **`unknown-2018` is the front matter:** the inside front cover with the
  publication information, the IAA committee and the editorial board. Crossref
  lists it as doi:10.1016/S0094-5765(18)31642-4. It is recorded as a `report`
  and has no reference list, so `bib_to_md.py --pending` will list it
  permanently. Two files in other bundles already have the same status.
* semyonov-2018 discusses ion acceleration for an antimatter-powered rocket
  only at feasibility level, with no thruster or plasma model, so it is
  Source-only. Its Summary says so.

### Bibliography (3360 → 3899 entries, FLAGS 0, `--dupes` clean)

* **Pre-step:** the cited-work entry `wu-2018` (Wu & Sun, Acta Astronaut.
  149:11, an ablative pulsed plasma thruster paper) was re-keyed to
  `wu-2018-d` before the merge, freeing the slug of a chunk-5 paper.
* **Self-key and reserved-slug traps:**
  * verspieren-2018's ref. [12], a private interview, is now
    `verspieren-2018-e`.
  * Two citations printed as `wang-2018`, from wang-2018-f and wu-2018-b, are
    now `wang-2018-g` and `-h`.
  * wu-2018-b's "liu-2018" is a different work from the ingested paper and is
    now `liu-2018-f`.
* **Key collisions:** semyonov-2018's NASA 2017 press release is a different
  work from the existing handbook entry, so it is now `nasa-2017-b`.
  verspieren-2018's ref. [19] also collided with an existing key and is now
  `verspieren-2017-d`.
* **Internal duplicates:** wang-2018-f prints [2]=[41] and [27]=[48]; each
  pair is now one entry.
* **Year re-keys from Crossref:** yu 2012→2016, christian 2016→2017,
  belvin 2015→1989, foix 2017→2011, lefebvre 2010→2008. Two of volpe-2018's
  citations resolve to existing entries: sabatini 2017→2015, and
  Clohessy–Wiltshire to the existing `clohessy-1960`.
* **Kept as distinct works:** thomson-1999 vs thomson-2000; nies-2016, the
  conference version of the ingested nies-2018; johnson-2012 vs 2013; eight
  Philippine bills that the heuristic resolver wanted to merge.

### Decisions for you

1. **`sirohi-2000`:** Crossref has two versions with this exact title, a 2000
   journal article and a 1999 SPIE paper. It is keyed by the journal version,
   and no DOI is recorded.
2. **Years not verified on Crossref:** campbell-1985 (printed 1984 and 1985),
   verspieren-2017-c (IAC-17), nies-2016 (IAC 2016), and two entries dated by
   their URLs.
3. **`neuhauster-2018`** keeps the surname as printed; the author is probably
   Neuhauser, which I did not verify.
4. **semyonov-2018 cites Lubin in JBIS.** Its citation is merged onto the
   existing `lubin-2016` entry, which keeps its arXiv form with a note. This
   is one more preprint-vs-published case, alongside chunk 4's.
5. Chunks 3 and 4's open decisions still stand: the `voland-2005` re-key,
   `first-1973`, the orphan-warning amendment, and the preprint folds.

## Chunk 4 — 20 Source-only pages (2026-10-15)

Sources: ghassabian-2018, haley-2018, helman-2018, hippke-2018, hippke-2018-b,
hou-2018, huang-2018, huang-2018-b, huang-2018-c, joffre-2018, ke-2018,
kim-2018, kumar-2018, lemay-2018, li-2018-b, li-2018-c, liu-2018, liu-2018-b,
loureiro-2018, mcdowell-2018. These cover spacecraft GNC, structures and
impact shielding, missions, communications, SETI, astrobiology and policy,
all outside this bundle's domain (D23). No concept page changed, and the
scope rule rules out any contradiction. Each paper's slips are on its Source
page under "Recorded as printed". The read-only audit found no errors and 7
minor items, all fixed.

### Identity and metadata

* **Two re-slugs:**
  * **`ghassabian-2018`**, filed under "Hady". Page 1 prints all six names
    surname-first: "Ghassabian G. Hady", "Calzada Diaz Abigail", and so on.
    The e-mail is hady.ghassabian@…, and Crossref swaps given and family
    names for all six authors. Only the running head reads "Hady" as the
    surname.
  * **`lemay-2018`**, filed under "Le". Crossref gives the family name
    "Le May".
* Page 1 matched the filename's title for all 20 files. Every file is the
  publisher's typeset version, and every issue year is 2018.

### Bibliography (2738 → 3360 entries, FLAGS 0, `--dupes` clean)

* **Pre-step:** the cited-work entries `kim-2018` (New J. Phys. 20:063033) and
  `liu-2018` (Rev. Sci. Instrum. 89:043502) were re-keyed to `kim-2018-b` and
  `liu-2018-e` before the merge. Their slugs belong to chunk-4 papers. No wiki
  page cited the old keys.
* **Reserved-slug and self-key traps:**
  * hippke-2018's ref. [10] (Interstellar Communication VIII, arXiv) is now
    `hippke-2018-c`.
  * huang-2018-c's refs. [2] and [6] are now `huang-2018-e` and `-f`.
  * li-2018-c's ref. [19] is now `huang-2018-g`.
  * huang-2018-b's "sun-2018" is a different work from the ingested core paper
    and is now `sun-2018-b`.
  * `ke-2018-b` and `mcdowell-2018-b` were checked and are free.
* **Year re-keys from Crossref:** subbarao 2012→2008, singla 2012→2006,
  bhat 2006→2000, gazi 2006→2005, greschik 2015→2007.
* **Undated references:**
  * DOI years: zhang-2017-k, kirsch-2005, guo-2014, gomez-2001.
  * Years from a URL or conference: lewis-1992, munoz-2017,
    nasaspaceflight-2012.
  * 6 web entries take the citing year.
* **Name swaps fixed from Crossref:** 7 entries. One author has two
  spellings, Virgili and Bastida Virgili, now one stem.
* **Venue and identifier slips:** 7 entries, each corrected with a note
  (e.g. zhang-2016-g, cole-2011, kurokawa-1994, matney-2010).
* A `$` in a cited title is escaped, because it broke the lint.

### Decisions for you

1. **Preprints merged into published versions.** This is the first case in
   this bundle:
   * hippke-2018 cites the arXiv preprint of the ingested hippke-2018-b, and
     that citation now counts toward hippke-2018-b;
   * it also cites both the preprint and the journal form of Learned et al.,
     and both now point to `learned-2012`.

   Each entry records the fold in a note. The handoff says to keep
   conference, report and reprint forms separate. Preprints were not listed,
   and another bundle merges them. Confirm, or ask for separate entries.
2. **Years not verified on Crossref:** lewis-1992, munoz-2017 and
   nasaspaceflight-2012 take their years from a URL or a conference date.
3. Chunk 3's open decisions still stand: the `voland-2005` re-key,
   `first-1973`, and the orphan-warning amendment.

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
