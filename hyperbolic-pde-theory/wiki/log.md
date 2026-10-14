# Directory Update Log

## 2026-10-14

* **Ingestion of [arfken-2013](/sources/arfken-2013.md)** (second source,
  D21; scoped read: preface, Ch. 7 *Ordinary Differential Equations*,
  pp. 329–380, and Ch. 9 *Partial Differential Equations*, pp. 401–446;
  exercises skimmed; printed pages cited, PDF offset +9 in Ch. 7 and +8 in
  Ch. 9). Merge path.
  * Created 2 pages: [Helmholtz equation](/definitions/helmholtz-equation.md)
    (≥2 sources) and [series solutions of linear ODEs (Frobenius'
    method)](/methods/frobenius-series-solutions.md) (substantive named
    method; the only new ODE page, kept to what the PDE pages use).
  * Updated 20 concept pages with Arfken citations next to Riley's:
    definitions (9: classification, characteristics, boundary-condition
    types, homogeneous problems, Wronskian, wave, diffusion, Laplace/Poisson,
    fundamental solution), methods (7: first-order PDE
    characteristics, constant-coefficient second order, separation of
    variables, integral transforms, PDE Green's functions, variation of
    parameters, first-order ODE methods), results (4: d'Alembert, boundary
    data, uniqueness for Poisson, linear ODE structure). Green's functions
    for linear ODEs untouched (Arfken's Ch. 10 not read). Audit lines added
    to [riley-2006](/sources/riley-2006.md).
  * Contradictions: 1 opened, on the [Helmholtz equation](/definitions/helmholtz-equation.md):
    Arfken p. 413 (Dirichlet solutions of $\nabla^2u \pm k^2u = 0$ only for
    certain $k$) against Riley Ex. 20.25, pp. 711–712 (uniqueness for the
    minus sign).
  * Qualifications recorded: classification invariance (Arfken eq. 9.21,
    p. 411, one transformation, vs Riley Ex. 20.24, p. 710, general);
    classification in more variables (Arfken p. 411, usage only); data
    along a characteristic (Riley p. 700 underdetermined, Arfken p. 406
    inconsistent unless redundant); homogeneous ODE definitions (Riley
    p. 685 scaling, Arfken p. 330 equal powers); converse of the Wronskian
    test (Riley p. 491, Arfken p. 360 with footnote conditions);
    Table 9.1 vs Table 20.1 (stability, "in one direction", Helmholtz).
  * Compiler's checks: Arfken eq. 9.126 (p. 443) is not a solution of the
    planar radial diffusion equation (symbolic check; Riley's eq. 20.37
    is); Arfken's no-interior-extremum argument (p. 433) does not cover
    degenerate stationary points. The ODE along a first-order
    characteristic, a compiler's derivation at founding, is now stated by
    Arfken for constant coefficients (eqs. 9.8–9.9). The Wronskian gap is
    narrowed (Abel's formula), not closed.
  * Registry extensions: $x_0$; $b_3$, $\mathbf b$; $c(u)$; $\hat\xi$,
    $\hat\eta$; $\nu$ (Frobenius exponent); $k_x$, $k_y$, $k_z$; $j_\ell$,
    $y_\ell$; $L_z$; $\chi_0$, $\chi_1$, $\chi_2$.
  * Bibliography: 27 entries (was 4). Added arfken-2013 and 22 works it
    cites: the 12 + 7 Additional Readings of Chs. 7 and 9 (Cohen 1992 and
    Margenau–Murphy 1956 in both; Morse–Feshbach 1953 merged into the
    existing entry, citedby now 2), 5 footnote citations, and the book's
    2nd edition cited in the text (arfken-1970, year unverified). 23
    references merged in all.

## 2026-10-13

* **Scaffolding and ingestion of [riley-2006](/sources/riley-2006.md)**
  (founding source, scoped read: front matter, Chs. 14–15, 20–21,
  pp. 468–530 and 675–774; exercises skimmed).
  * Seeded the [notation registry](/notation.md). Principal coefficients
    are $a_{ij}$ (to free $A$ for the flux Jacobian), the right-hand side
    is $\psi$, and the Laplace variable is $p$ (to free $s$ for a shock
    speed). A reserved section covers hyperbolic systems: $m$, $f(u)$,
    $A(u)$, $\lambda^{(p)}$, $r^{(p)}$, $\ell^{(p)}$, $w^{(p)}$, $u_L$, $u_R$.
  * Created 21 concept pages. Definitions (9): second-order classification,
    characteristic curves, boundary-condition types, homogeneous problems,
    Wronskian, fundamental solution, wave, diffusion, Laplace/Poisson
    equations. Methods (8): first-order linear PDE characteristics,
    constant-coefficient second-order general solution, separation of
    variables, integral transforms, PDE Green's functions, ODE Green's
    functions, variation of parameters, first-order ODE methods. Results
    (4): d'Alembert's formula, boundary data by equation type, uniqueness
    for Poisson, structure of linear ODE solutions. Indexes written.
  * Compiler's derivations flagged on the pages: the ODE for $u$ along a
    first-order characteristic; the p. 690 statement on elliptic arguments
    holds only without a mixed term; the eigenfunction form of $G$ needs
    $\lambda_n \ne 0$; the Wronskian converse used on p. 509 is not proved
    in the chapters read.
  * Bibliography: 4 entries (riley-2006 plus the 3 works its footnotes cite:
    morse-1953, piaggio-1954, schiff-1955).
