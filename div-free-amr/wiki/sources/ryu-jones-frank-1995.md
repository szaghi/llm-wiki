---
type: Source
title: "Ryu, Jones & Frank (1995) — Numerical Magnetohydrodynamics in Astrophysics: Algorithm and Tests for Multi-Dimensional Flow"
description: "Strang-split multidimensional extension of the Ryu–Jones Harten-TVD MHD code with an FFT Poisson projection of the collocated field after every step (wide 2Δx Laplacian, central divergence source; ≲5% of CPU periodic, ≲30% with a doubled box); no divergence value reported."
resource: "doi:10.1086/176347"
source_kind: paper
authors: [Ryu D., Jones T.W., Frank A.]
year: 1995
venue: "Astrophys. J. 452:785"
local_file: "/home/stefano/papers/mosaic/div-free-amr/1995-ApJ-Ryu-101086176347.pdf"
tags: [projection, poisson, fft, tvd, godunov, operator-splitting, mhd, astrophysics]
timestamp: 2026-10-13T00:00:00Z
---

# Summary

The paper takes the authors' 1D second-order Harten-TVD ideal-MHD code
([Ryu & Jones (1995)](/sources/ryu-jones-1995.md)) to two and three
dimensions by Strang-type directional splitting (§2.3, eq. 2.22). During
each sweep the field component parallel to the sweep is held fixed. The
solenoidal constraint is restored after every time step by an explicit
Poisson **projection**, which the authors call "a correction via a gauge
transformation" and credit to Brackbill & Barnes (1980) (§1, §2.4, eqs.
2.23–2.24).

The discrete Poisson operator is the wide $2\Delta x$ stencil with the
cell-centred central divergence as source. It is solved by FFT, on a box
doubled with a chosen symmetry when the boundaries are not periodic. The
cost is ≲5% of CPU time with periodic boundaries and ≲30% with the
extended box.

Tests: two diagonal MHD shock tubes at $256^2$; linear-wave decay as a
measure of numerical viscosity and resistivity; the MHD Kelvin–Helmholtz
instability; a compressible
[Orszag–Tang vortex](/benchmarks/orszag-tang-vortex.md). **No divergence
value is reported anywhere in the paper.** This is the "explicit Poisson
divergence-cleaning step" that [Ryu et al. (1998)](/sources/ryu-1998.md)
later replaced with constrained transport.

# Key claims

1. **Base scheme** (§2.2, eqs. 2.9–2.21). The seven-wave Harten-TVD scheme
   of Ryu & Jones (1995), with arithmetic interface averages instead of a
   Roe average. The renormalized eigenvectors are **not printed**: the
   reader is sent to Brio & Wu (1988) and Ryu & Jones (1995). The
   entropy-fix parameters are "optimized for the multi-dimensional code":
   $\varepsilon = 0.3$ (fast), 0.1 (Alfvén), 0.45 (slow), 0.0 (entropy)
   (eqs. 2.20–2.21). Courant number typically 0.6, "up to 0.9" sufficient
   for most runs. Harten's contact and rotational steepeners are dropped:
   they produced "spurious numerical oscillations" (p. 6).
2. **Strang splitting** (§2.3, eq. 2.22). $q^{n+1} = L_zL_yL_xq^n$, with
   the sweep order permuted over six steps "to maintain second-order
   accuracy"; $\Delta t$ is fixed over each six-step sequence. In each
   sweep "the parallel … component of magnetic field is kept constant and
   only the perpendicular component is updated".
3. **Origin of the divergence error** (§2.4, p. 7). The scheme conserves
   the face fluxes of each directional pass, but "nothing maintains a
   constant magnetic flux in the Gauss's Law sense across the entire
   surface of each cell". The error "usually grows exponentially during
   the computations, causing an artificial force parallel to the magnetic
   field" ("see e.g., Schmidt-Voigt 1987"). The growth is asserted, not
   shown.
4. **Why not the Brackbill–Barnes form** (§2.4, p. 7). Zachary, Malagoli &
   Colella (1994) used the "modified form of the MHD equations originally
   suggested in Brackbill & Barnes (1980)", found "no discernible
   differences with and without the correction", and "abandoned the
   correction". The authors reject the modified form: it "is not suitable
   for our code and it does not remove $\nabla\cdot B$ completely anyway".
5. **The projection** (§2.4, eqs. 2.23–2.24). Solve
   $\nabla^2\phi + \nabla\cdot B = 0$ (2.23) and set $B^c = B + \nabla\phi$,
   $B$ the field after the split update. In 2D Cartesian form
   $$\frac{\phi_{i+2,j} - 2\phi_{i,j} + \phi_{i-2,j}}{4(\Delta x)^2} + \frac{\phi_{i,j+2} - 2\phi_{i,j} + \phi_{i,j-2}}{4(\Delta y)^2} = -\left(\frac{B_{x,i+1,j} - B_{x,i-1,j}}{2\Delta x} + \frac{B_{y,i,j+1} - B_{y,i,j-1}}{2\Delta y}\right)\quad(2.24).$$
   * The Laplacian is the wide stencil, the composition of two central
     first differences; the source is the central divergence of the
     collocated field.
   * The difference form of the gradient in $B^c = B + \nabla\phi$ is
     **not printed**. Exactness of the corrected central divergence needs
     the central $2\Delta x$ gradient, since the Laplacian then factors as
     central divergence of central gradient. This is implied by eq. 2.24,
     not stated.
   * **Solver.** FFT, which "can provide an exact solution to
     $\phi_{i,j}$ … if the field structure is periodic" (Bracewell 1986).
     For non-periodic boundaries the box is doubled "for this step only"
     with "an appropriate symmetry"; the symmetries are not specified.
   * **Cost.** "≲5% of the total CPU time" with periodic boundaries,
     "≲30%" with reflecting or continuous boundaries.
   * **Placement.** Applied "in each time step" (abstract, §1); whether
     after each sweep or after each multi-directional step is not stated.
   * The constraint is called "enforced exactly"; no residual divergence is
     measured.
6. **Performance** (§2.4, §4). About 400 MFlops on one Cray C90 processor:
   about $2\times10^5$ cells/s in 1D, $10^5$ in 2D.
7. **Numerical dissipation** (§3.2, Figs. 3–5). Decay rates of 2D linear
   Alfvén, fast and slow waves scale as $n_{\rm cells}^{-2}$, "confirming
   that our code has second-order accuracy". At $\beta = 2$ the numerical
   Reynolds number is "roughly 20–30 times smaller" than for the
   hydrodynamic TVD code (Ryu & Goodman 1994), and the MHD decay rate
   stays "significantly larger" as $\beta\to\infty$, because the 7-field
   code does not reduce exactly to the 5-field hydro code. §4: turbulent
   structures must exceed "~50 cells" to be inertial-range.
8. **Shock capture** (§3.1, §4). Strong fast shocks in 2–3 cells; the 2D
   diagonal results are "virtually the same as with the one-dimensional
   code".

# Tests

All with $\gamma = 5/3$ and Courant number 0.6 (§3). Figures are absent
from the file; findings come from text and captions.

1. **Diagonal shock tube, planar field** (§3.1, Fig. 1). $[0,1]^2$,
   $256^2$, along the diagonal, against the exact solver of Ryu & Jones.
   Left $(1, 10, 0, 0, 5/\sqrt{4\pi}, 0, 20)$, right
   $(1, -10, 0, 0, 5/\sqrt{4\pi}, 0, 1)$ in $(\rho, v_\parallel, v_\perp,
   v_z, B_\perp, B_z, E)$, $B_\parallel = 5/\sqrt{4\pi}$, $t = 0.08\sqrt2$:
   Ryu & Jones Fig. 1a. Fast shocks, a slow rarefaction, a contact and a
   slow shock. Three anomalous $v_\perp$ points come from cancellation in
   $v_\perp = (-v_x + v_y)/\sqrt2$.
2. **Diagonal shock tube, "2+1/2-D"** (§3.1, Fig. 2). Left
   $(1.08, 1.2, 0.01, 0.5, 3.6/\sqrt{4\pi}, 2/\sqrt{4\pi}, 0.95)$, right
   $(1, 0, 0, 0, 4/\sqrt{4\pi}, 2/\sqrt{4\pi}, 1)$,
   $B_\parallel = 2/\sqrt{4\pi}$, $256^2$, $t = 0.2\sqrt2$: Ryu & Jones
   Fig. 2a, seven structures. Other Ryu–Jones tubes were run and called
   "comparable" (not shown). **No $B_\parallel$ or divergence diagnostic**
   for either tube
   ([rotated shock tube](/benchmarks/rotated-shock-tube.md)).
3. **Linear-wave decay** (§3.2, eqs. 3.6–3.16, Figs. 3–5). Standing waves
   along the diagonal of a periodic unit box; $\rho_o = 1$, $p_o = 1$,
   $B_o = 1$ along $x$ ($\beta = 2$); amplitudes 0.1 (Alfvén) and $10^{-4}$
   (fast, slow); grids $8^2$ to $256^2$. A $\beta$-scan of the fast wave on
   $128^2$ ($\beta = 2\times10^{-2}$ to $2\times10^6$, plus the hydro code)
   peaks "around $\beta = 1$".
4. **MHD Kelvin–Helmholtz** (§3.3, eqs. 3.17–3.19). Periodic in $x$,
   reflecting in $y$, $\tanh$ shear layer of width $L/(8\pi)$, field 0.4
   along the flow, sonic Mach 1, Alfvén Mach 2.5; Miura–Pritchett
   eigenmode with predicted growth rate $0.68V_o/L$. At $128^2$, $256^2$,
   $512^2$ the runs grow at the predicted rate after a transient; the
   $512^2$ images are "very similar" to Miura (1984).
5. **Compressible Orszag–Tang** (§3.4, eqs. 3.20–3.23, Fig. 8 caption).
   $v = v_o[-\sin(2\pi y)\hat x + \sin(2\pi x)\hat y]$,
   $B = B_o[-\sin(2\pi y)\hat x + \sin(4\pi x)\hat y]$, $v_o = 1$,
   $B_o = 1/\sqrt{4\pi}$, $M^2 = 1$, $\beta = 10/3$, $\gamma = 5/3$;
   periodic $[0,1]^2$, $256^2$, shown at $t = 0.48$. Shocks in 2–3 cells;
   structure "match[es] closely" Dahlburg & Picone (1989) and Zachary et
   al. (1994), with different initial conditions and epochs. Qualitative
   only ([Orszag–Tang vortex](/benchmarks/orszag-tang-vortex.md)).

**Divergence measurements: none.** No test reports $\nabla\cdot B$, a
$B_\parallel$ error, or a with/without-projection comparison.

# Notation map

| Ryu, Jones & Frank | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $B$ (after the split update) | $B_h^*$ | provisional field |
| $B^c$ | $B_h$ | corrected field, collocated, cell-centred |
| $\phi$ (eq. 2.23) | $\phi_h$ | **sign flip**: $B^c = B + \nabla\phi$, so $\phi_h = -\phi$ in the convention $B_h = B_h^* - G_h\phi_h$ |
| right side of eq. 2.24 | $D_h^{\mathrm c} B_h^*$ | central divergence |
| $\nabla$ in $B^c = B + \nabla\phi$ | $G_h$, central $2\Delta x$ | stencil not printed; inferred from the factored Laplacian |
| left side of eq. 2.24 | $D_h^{\mathrm c} G_h$ | the wide-stencil variant of [projection](/methods/projection-method.md) |
| $\Delta x$, $\Delta y$ | $h$ | uniform grids |
| $\Delta t^n$, superscript $n$ | $\Delta t$, $n$ | |
| $L_x, L_y, L_z$ (sweep operators); $L_k$, $R_k$ (eigenvectors) | words | **collision**: $R$ is restriction; $L$ also the box size in §3 |
| $q$ (state vector) | words | **collision**: $q$ is the ghost-fill accuracy order |
| $\Gamma$ (decay or growth rate) | words | **collision**: $\Gamma$ is the ghost-fill operator |
| $R$ (numerical Reynolds number) | words | **collision** with restriction |
| $\beta$ (plasma beta) vs $\beta_k$ (TVD coefficient) | words | in-paper double use |
| $\varepsilon$ (entropy fix) | words | distinct from $\epsilon_{\mathrm W}$ |

# Pages created or updated

* Updated [Orszag–Tang vortex](/benchmarks/orszag-tang-vortex.md): the $[0,1]^2$ compressible set-up this paper states.
* Updated [Projection method](/methods/projection-method.md): an early MHD projection with stated discrete operators, an FFT direct solve, its cost, and the round-off qualification of "solver tolerance".
* Updated [Eight-wave formulation](/methods/eight-wave.md): why the authors rejected the Brackbill–Barnes nonconservative form.
* Updated [Rotated shock tube](/benchmarks/rotated-shock-tube.md): the 45° diagonal tubes of the Ryu codes.
* Updated [Exact discrete divergence](/properties/exact-discrete-divergence.md) (the earlier statement of the exponential-growth claim, §2.4).

# Citations

1. `~/papers/mosaic/div-free-amr/1995-ApJ-Ryu-101086176347.pdf`.
   * **Version read.** The arXiv preprint astro-ph/9505073 (stamped 17 May
     1995; report CNU-AST-95-1; "Submitted to the Astrophysical Journal"),
     20 pages, figures absent (captions only, pp. 19–20). Page numbers,
     figure numbers and refereed changes of the ApJ version are unknown.
   * **Identity.** doi:10.1086/176347, checked on Crossref: title (printed
     there "Multidimensional", without the hyphen of page 1), authors Ryu,
     Jones, Frank; Astrophys. J. 452, first page 785, issued October 1995.
   * **How it was read.** Text extraction of all pages; pp. 5–12, 14, 15
     and 20 were rendered at 110 dpi to check eqs. 2.9–2.24, 3.1–3.16,
     3.20–3.23, the test states and the captions. The limiter eqs.
     2.17–2.19 are a best reading of small rendered accents.
   * **Recorded as printed.**
     * Eq. 3.22 prints $M^2 \equiv v_o/(\gamma p_o/\rho_o)$, without the
       square on $v_o$; [Ryu et al. (1998)](/sources/ryu-1998.md) inherits
       it.
     * The Fig. 8 caption prints "25/36π" and "5/12π" (reader's reading:
       $25/(36\pi)$ and $5/(12\pi)$, consistent with $M = 1$,
       $\beta = 10/3$).
     * The text figure numbers in §§3.3–3.4 lag the captions by one; the
       text also uses "Fig. 5" for the $\beta$-scan.
     * Fig. 1 is at $t = 0.08\sqrt2$ in both text and caption, which
       supports the text of Ryu et al. (1998) against its Fig. 2a caption.
   * **Reference list.** 38 entries, all merged; ApJ style without titles,
     so article entries carry the placeholder title. Strang is printed
     with first page 505 (Crossref: 5:506). The "1994b preprint" of Dai &
     Woodward was merged into `dai-woodward-1994-b` by context, unverified.
     The bibliography key `ryu-1995` was renamed `ryu-jones-frank-1995` to
     match this page. The bibliography holds 3711 entries after this
     batch.
