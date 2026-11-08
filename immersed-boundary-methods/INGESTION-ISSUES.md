# Ingestion issues — immersed-boundary-methods

Reviewer's digest, one section per chunk, newest first: contradictions
opened (the normative record is the `## Contradictions` section of the
named page), printed inconsistencies, identity and metadata problems,
bundle-fit suggestions, and questions left to the human. Not part of the
OKF wiki; maintained by the compiler at every chunk.

## Chunk 3 — 2014–2022: FSI reviews, shifted boundary, state redistribution, moving EB (2026-11-08)

Sources (10): sotiropoulos-2014, main-2018, griffith-2020, berger-2021,
atallah-2022, giuliani-2022-b, nair-2022, natarajan-2022, ni-2022, ou-2022.
30 of 57 ingested, 27 concept pages plus the registry, 1186 bibliography
entries.

### Decisions for the human

1. **Versions read.** Four sources were read from arXiv preprints of the
   published papers (berger-2021 arXiv:2005.05734v1, giuliani-2022-b
   arXiv:2112.12360v2, nair-2022 arXiv:2103.06415v1, natarajan-2022
   arXiv:2108.00126v1) and two from accepted manuscripts (main-2018,
   atallah-2022); metadata are the published identities.
2. **Timestamp correction (whole night).** Chunk-2 pages and the step-01
   registry first carried invented future timestamps; step 02 was re-snapped
   with real-clock times. Step 01's tree still holds notation.md with
   21:30Z, corrected by step 02.

### Contradictions

None opened. Recorded as a qualified difference: griffith-2020 states that
immersed formulations "do not appear to suffer" added-mass instabilities even
with explicit coupling, while uhlmann-2005 measures a density-ratio limit for
explicit coupling of rigid particles and sotiropoulos-2014 reviews the
added-mass problem of loose coupling (methods/fluid-structure-coupling).

### Identity and metadata

- giuliani-2022-b is the JCP paper of September 2022; the SISC paper of
  February 2022 (chunk 4) is giuliani-2022 by publication order.

### Bibliography decisions taken

- 30 same-key, different-work aliases, among them liu-1998-c (insect
  flight), kang-2009-b, burman-2010-b (ghost penalty), xu-2006 pair printed
  in swapped order by griffith-2020, berger-1989 pair swapped in
  natarajan-2022, berger-1984-b (Berger–Oliger), liu-2003-b, wang-2020-b/-c,
  yang-2012-c (deposited twice by ni-2022).
- 7 same-work merges, e.g. berger-2015 → berger-2016 (year variant noted),
  hansbo-2002, nitsche-1971, arnold-2002, AMReX zhang-2021.
- noh-1963 (CEL report year in natarajan-2022) kept apart from noh-1964
  (book chapter in pember-1995); a merge is the human's call.

### Bundle fit

All ten fit. ni-2022 (material point method) and ou-2022 (reacting low-Mach
flow) are application-driven but contribute named coupling and ghost-cell
variants.

## Chunk 2 — 2003–2015: ghost cells, embedded boundaries, projection, ILW, CutFEM (2026-11-08)

Sources (10): tseng-2003, mittal-2005, uhlmann-2005, colella-2006,
ghias-2007, taira-2007, mittal-2008, tan-2010, chaudhuri-2011, burman-2015.
20 of 57 ingested, 24 concept pages plus the registry, 609 bibliography
entries.

### Decisions for the human

1. **Versions read that are not the version of record.** uhlmann-2005 was
   read from arXiv:1809.08170v1 (a 2018 posting of the published paper);
   colella-2006 from an author preprint with the published title and
   abstract. Metadata are the published identities.
2. **Reconstructed formula.** The hybrid update and redistribution of
   colella-2006 are written in registry form from the paper's prose because
   the text layer of the version read garbles the equations
   (methods/redistribution); a visual check of the printed equations would
   confirm the sign convention of $\delta\mathbf M$.
3. **Reading depth** as in chunk 1: methods in full, results for set-up,
   tables and conclusions.

### Contradictions

None opened. Points of view recorded as such, not as contradictions:
tseng-2003 calls spreading and local reconstruction "equivalent", while
mittal-2005 and ghias-2007 distinguish diffuse from sharp forcing; ghias-2007
calls colella-2006 "locally first-order", consistent with colella-2006's own
$O(h)$ truncation error and $O(h)$ $L^\infty$ error at the boundary.

### Identity and metadata

- mittal-2008: Crossref gives the fourth author as "Najjar F."; page 1 prints
  F.M. Najjar.
- burman-2015: published online 29 Dec 2014, issue 2015 (slug uses 2015).
- chaudhuri-2011: the abstract describes the image-point interpolation as "a
  local quadratic scheme" while §2.2 uses inverse-distance weighting; the
  pages record both.

### Bibliography decisions taken

- Same key, different works (aliased): verzicco-2000-b (LES with boundary
  body forces), verzicco-1996-b (cylindrical finite-difference scheme),
  liu-1998-b (preconditioned multigrid), quirk-1994-b (Computers & Fluids),
  beyer-1992-b (Beyer–LeVeque SINUM), lee-2003-b (Lee–LeVeque IIM),
  mittal-1999-b (spectral collocation for spheres), mittal-2002-c (sphere
  wake symmetry), fedkiw-2002-b (book chapter), iaccarino-2003-b (CTR brief),
  peskin-1972-b (thesis, also via chaudhuri-2011), and the Mittal 1997 pair
  printed in swapped suffix order by ghias-2007.
- fauci-1994 kept under the year printed by peskin-2002 although Bull. Math.
  Biol. 57 is the 1995 volume (note on the entry); a re-key to fauci-1995
  is the human's call.
- khadra-2000 (published) and khadra-1999 (submitted form cited by
  angot-1999) kept distinct.
- Software entries GetFEM++ and LifeV keyed getfem-2014 and lifev-2014.
- patankar-2001: first page printed 185 by uhlmann-2005 and 197 in the
  mittal-2005 deposit; merged as one work with a note.

### Bundle fit

All ten fit. burman-2015 (finite elements) and tan-2010 (high-order finite
differences) extend the bundle beyond Cartesian finite volumes, as the
archive intends.

## Chunk 1 — the founding papers, 1972–2002 (2026-11-08)

Sources (10): peskin-1972, goldstein-1993, leveque-1994, pember-1995,
fedkiw-1999, ye-1999, angot-1999, fadlun-2000, kim-2001, peskin-2002.
10 of 57 ingested, 18 concept pages plus the registry, 312 bibliography
entries.

### Decisions for the human

1. **Bundle name** `immersed-boundary-methods` (D32), chosen on the owner's
   behalf — confirm or rename before committing.
2. **Reading depth.** Compiled inline without subagents. Method sections and
   theory were read in full; long result sections of fedkiw-1999, ye-1999,
   fadlun-2000, kim-2001 and pember-1995 were read for set-up, tables and
   conclusions. Each Source page states its version read.
3. **OCR sources.** goldstein-1993 and pember-1995 are image-only scans read
   through tesseract OCR; their display equations are not legible, so no
   equation from them is quoted beyond what their prose states (Pember's
   preliminary update and redistribution formulas are described in words).
   A visual page-by-page reading would recover the formulas.
4. **Slug order for Giuliani 2022.** By publication order the SISC paper
   (Feb 2022) is giuliani-2022 and the JCP paper (Sep 2022) giuliani-2022-b.
   The bundle `high-order-capturing-schemes` uses giuliani-2022 for the JCP
   paper. Bundles are independent (D12), so this is legal, but a reader
   moving between bundles may be confused.

### Contradictions

None opened.

### Identity and metadata

- pember-1995: Crossref spells the fourth author "Curtchfield"; page 1 prints
  Crutchfield (used).
- peskin-1972: the text layer prints the author as "PISKIN" on page 1.
- burman-2015 (chunk 2) is filed as 2014 (online year); the issue is 2015.
- Seven archive papers are also Sources elsewhere (peskin-2002, mittal-2008,
  berger-2021, giuliani-2022-b, natarajan-2022, liu-2025 in
  `high-order-capturing-schemes`; jones-2026 in `div-free-amr`).

### Printed slips (reference lists)

- pember-1995 ref. 18 prints 1969 for Math. Comput. 22:745 (1968), aliased to
  chorin-1968; ref. 45 prints 1944 for an AIAA paper of 1994; ref. 58 prints
  "J. Comput. Phys. 23(1):125" for Computers & Fluids 23:125, aliased by
  ye-1999's Crossref record; ref. 65 prints 1993 for the 1983 AIAA conference.
- goldstein-1993 ref. 2 is "Deleted in proof"; ref. 1's author reads
  "Bae-Lev" in the OCR, entered as Bar-Lev.

### Bibliography decisions taken

- Undated citations (in press, submitted, in preparation, "200x") are keyed
  by the citing paper's year with a note: chu-1993, colella-1995,
  khadra-1999, jiang-1999, liu-1999, mayo-1994, lim-2002, schmid-2002,
  zhang-2002, peskin-1993-b, tu-1993. peskin-1993-b has the title of
  peskin-1992 and tu-1993 is probably tu-1992; both kept distinct as
  pre-publication citations (standing ruling on preprints).
- fedkiw-1999-b (the isobaric-fix paper, JCP 148) is suffixed although it
  appeared before the ingested fedkiw-1999, whose slug is fixed.
- peskin-1972-b is Peskin's 1972 PhD thesis, distinct from the paper.

### Bundle fit

All ten papers fit this bundle. fedkiw-1999 (multimaterial ghost fluid) and
leveque-1994 (elliptic interface problems) are interface methods rather than
solid-body methods; they are central to the archive's sharp-interface line.
