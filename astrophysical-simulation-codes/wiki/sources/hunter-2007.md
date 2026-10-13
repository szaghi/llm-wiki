---
type: Source
title: "Hunter (2007) — Matplotlib: A 2D Graphics Environment"
description: "Short software article introducing matplotlib, a Python 2D plotting library with a Matlab-like interface (PyLab), GUI-embeddable and with publication-quality raster and vector output, built on three layers (canvas, renderer, artist); cited by the bundle's code papers as the tool that drew their figures."
resource: "doi:10.1109/MCSE.2007.55"
source_kind: paper
authors: [Hunter J.D.]
year: 2007
venue: "Comput. Sci. Eng. 9:90–95"
local_file: "/home/stefano/papers/mosaic/astrophysical-simulation-codes/2007-CiSE-Hunter-101109MCSE200755.pdf"
tags: [software, analysis]
timestamp: 2026-10-13T00:00:00Z
---

# Summary

A first-person software article in the "Scientific Programming"
department of Computing in Science & Engineering. Hunter wrote
matplotlib, a Python 2D plotting library, to replace Matlab's 2D graphics
in an application for viewing electrocorticography data (pbrain, part of
nipy), because no Python graphics package met his requirements (p. 90–91).
The user interface deliberately reverse-engineers Matlab's (the PyLab
wrapper). The article demonstrates line and fill plots with TeX labels,
images with interpolation, colour maps, contours and colour bars,
GUI-independent event handling and picking, and the basemap
map-projection toolkit, and describes the three-layer architecture
(canvas, renderer, artist) with the Agg raster back end as the worked
example (p. 94–95). It has no numerical method, no benchmark and no
reference list. The bundle's code papers cite it as the tool that drew
their figures; it bears on no solver, mesh or verification claim.

# Key claims

1. **Requirements** (p. 90–91). No existing Python package was
   "embeddable in a GUI for application development, support different
   platforms, offer extremely high-quality raster and vector (primarily
   PostScript) hardcopy output for publication, provide support for
   mathematical expressions, and work interactively from the shell". The
   basic Matlab interface was "reverse-engineered".
2. **Capabilities in 2007** (p. 91). Binaries for OS X, Windows and the
   major Linux distributions; embeddable in GTK, WX, Tk, Qt and FLTK;
   PostScript, SVG and PDF output; TeX for text and mathematics; xy, bar,
   pie and scatter plots, images, contours, animation, picking, event
   handling, annotations; a permissive licence based on the PSF licence.
   No matplotlib version number is printed.
3. **PyLab** (p. 91). A Matlab-emulation wrapper of the matplotlib API,
   justified as a teaching aid; IPython's `-pylab` mode handles GUI
   main-loop threading.
4. **Images and events** (p. 91–93). Nearest, bilinear, bicubic and "14
   other" interpolation methods, the classic Matlab colour maps, several
   colour maps and colour bars per axes; GUI events abstracted across "the
   five major GUIs", and a `pick` method on every artist.
5. **Architecture** (p. 94–95). Three base classes: FigureCanvasBase,
   RendererBase and Artist. The Figure is the top-level artist; its draw
   call recurses through the axes to primitives (lines, polygons, text),
   which call low-level renderer methods. Back ends are kept "reasonably
   simple and dumb", knowing nothing of coordinates or the figure
   hierarchy, so new output formats are quick to add at the cost of
   format-specific features; changing the output format means changing
   the canvas.
6. **Scope** (p. 95). Stated goals: real-time plotting performance,
   arbitrary axis scales, user coordinate systems and basic 3D; for
   sophisticated 3D the project defers to VTK and MayaVi2 and keeps its
   "core competency—high-quality interactive scientific 2D graphs".

# Tests

None. Figs. 1–4 are demonstrations: the pbrain viewer embedded in GTK,
LaTeX-rendered text, a bivariate-Gaussian difference image with contours
and two colour bars, and a basemap orthographic projection.

# Notation map

Not applicable: the article has no mathematics (the only expression is a
TeX string in a code example, p. 91).

# Pages created or updated

* Created this Source page.
* No concept page attributes anything to this paper beyond its citation;
  no Software page for matplotlib: it is an analysis and plotting
  dependency, outside the bundle's scope (simulation codes and their
  physics modules), and no source treats it as part of a code's design.
  Its uses in the bundle: the software statement of
  [Kim & Ostriker (2017)](/sources/kim-2017.md) and the reference lists of
  the citing sources.

# Citations

1. Hunter J.D. (2007), "Matplotlib: A 2D Graphics Environment",
   Comput. Sci. Eng. 9(3):90–95, doi:10.1109/MCSE.2007.55. Local file:
   `/home/stefano/papers/mosaic/astrophysical-simulation-codes/2007-CiSE-Hunter-101109MCSE200755.pdf`.
   * **Version read.** The typeset publisher PDF (6 pages, May/June 2007,
     "1521-9615/07/\$25.00 © 2007 IEEE"); the last page of the file also
     carries the issue's advertiser index, which is not part of the
     article. Not a preprint.
   * **Identity.** Checked on Crossref: title, single author, vol. 9,
     issue 3, pp. 90–95, print 2007.
   * **How it was read.** Text extraction (non-layout, because the layout
     mode interleaves the two columns); fully legible.
   * **Recorded as printed.** Nothing beyond typographic quotes in the code
     examples.
   * **Reference list:** none printed (Crossref also lists none). The
     in-text pointers are URLs and two cross-references to other articles
     of the same issue, not reference entries. The slug therefore appears
     in no `citedby` field and stays on the `--pending` list by design.
     The `hunter-2007` entry (cited by 10 sources, among them
     [Turk et al. (2011)](/sources/turk-2011-c.md)) carries the page-1
     title. Bibliography: 2522 entries.
