---
type: Method
title: "Parareal"
description: "Parareal iterates a cheap serial coarse propagator and an accurate fine propagator run in parallel on all time slices; it converges to the serial fine solution, exactly after N iterations. The page gathers its convergence bounds and the variants with low-rank, optimized rational and exponential propagators."
status: established
aliases: [parareal algorithm, Lions–Maday–Turinici algorithm, low-rank Parareal, exponential Parareal, ERK Parareal, optimized coarse propagator, OCP, multi-block parareal, windowed parareal]
tags: [parallel, stiff, exponential, stability, verification]
timestamp: 2026-10-20T16:00:00Z
---

# Parareal

**Parareal** (Lions, Maday and Turinici, 2001, as recalled by all five sources
below) is the main method of [parallel-in-time integration](/methods/parallel-in-time-integration.md)
*across the steps*. The interval $[t_0,T_N]$ is cut into $N$ time slices
$T_0<T_1<\dots<T_N$ of length $\Delta T$, usually one per process. A **fine
propagator** $\mathcal F$ is an accurate one-slice solution map, typically $N_f$
steps of size $h=\Delta T/N_f$ of a one-step method ($N_f$ page-local). A **coarse
propagator** $\mathcal G$ is a cheap one-slice map. Starting from a serial coarse
sweep $U^{(0)}_{j+1}=\mathcal G(U^{(0)}_j)$, the iteration is

$$U^{(k+1)}_0=y_0,\qquad U^{(k+1)}_{j+1}=\mathcal G\big(U^{(k+1)}_j\big)+\mathcal F\big(U^{(k)}_j\big)-\mathcal G\big(U^{(k)}_j\big),\qquad j=0,\dots,N-1.$$

The $N$ fine solves $\mathcal F(U^{(k)}_j)$ of one iteration are independent and run in
parallel; only the coarse correction is serial
([Carrel et al. (2023)](/sources/carrel-2023.md), Def. 2.1;
[Jin et al. (2025)](/sources/jin-2025.md), Alg. 2.1;
[Buvoli & Minion (2024)](/sources/buvoli-2024.md), Eq. (4), Table 1;
[Muralikrishnan & Speck (2025)](/sources/muralikrishnan-2025.md), Eqs. (4.1)–(4.2)).
The fixed point is the serial fine solution $U_{j+1}=\mathcal F(U_j)$, not the exact
solution: every convergence statement below measures the distance to it, unless a
source says otherwise. Carrel et al. call the iteration "Newton-like"; Muralikrishnan
& Speck observe that errors in late slices decrease about as fast as in early ones,
consistent with Parareal as an approximate Newton method (App. A.3, as recalled).

## Cost and speedup

**Finite termination.** After $k$ iterations the first $k$ slices hold the fine
solution exactly, so Parareal reproduces the serial fine solution after $N$ iterations
(Carrel et al. 2023, §2.1; Buvoli & Minion 2024, §5.4: the error-propagation matrix
is nilpotent). Jin et al. (2025, §4.2, Fig. 4.2) see the error drop to zero after 5
iterations with $N=5$. Speedup therefore needs convergence in $K\ll N$ iterations.

**Model speedup.** With costs $c_{\mathcal G}$, $c_{\mathcal F}$ of one coarse and one
fine slice solve (page-local) and communication neglected, Buvoli & Minion (2024,
Eq. (5), recalled from Aubanel) write

$$S=\frac{N}{N\,c_{\mathcal G}/c_{\mathcal F}+K\,(1+c_{\mathcal G}/c_{\mathcal F})},$$

from serial cost $Nc_{\mathcal F}$ and parallel cost $Nc_{\mathcal G}+K(c_{\mathcal G}+c_{\mathcal F})$.
Muralikrishnan & Speck (2025, §4) state the same two conditions in words: coarse plus
communication cost much below the fine cost, and far fewer iterations than slices.
Jin et al. (2025, §4) define efficiency as speedup divided by $N$, after Maday–Mula.
Muralikrishnan & Speck (App. A.4) move processes to the time direction only once the
spatial parallel efficiency drops below 50 %, because Parareal would need convergence in
two iterations to reach 50 % efficiency itself.

**How the reported numbers were obtained.** The sources measure different things:

| source | runs in parallel? | what the number is |
|---|---|---|
| Buvoli & Minion (2024), NLS | yes, 2048 cores (Cori Haswell) | model speedup 38.5 from the formula (iteration count not printed); measured 10.4 against serial ERK4, communication-bound (§4) |
| Buvoli & Minion (2024), KP equation | partly | convergence curves computed serially on one node; speedups 9.09–11.71 at $K=28$ iterations, extrapolated from a shortened run $t\in[0,1]$ on 64 nodes (§6.1–6.2) |
| Buvoli & Minion (2024), Vlasov–Poisson | yes, $N=2048$ on 2048 cores | measured 24× reduction of time to solution against serial ERK4 at $K=8$ iterations; model and measured speedup agree closely (§6.3) |
| Muralikrishnan & Speck (2025) | yes, up to 1536 A100 GPUs (32 space × 48 time) | measured Parareal times (run to a tolerance) over a space-only reference extrapolated from one 768-step Penning-trap run scaled by 8: 4.2, 4.7, 2.4 (5.8, 5.6, 4.4 with an order-7 B-spline fine shape function) (§6.3) |
| Jin et al. (2025) | no | simulated: sequential coarse time plus the maximum fine time per iteration, communication ignored; 3–11 iterations to the target accuracy (§4, Tables 4.2–4.3) |
| Carrel et al. (2023) | no | none; good speedup is "reasonable to expect" from the cost gap between ranks (§5) |

## Convergence theory

**Bounds as recalled.** Carrel et al. (2023, §2.1) recall from Gander & Vandewalle
(2007) that Parareal converges well on parabolic problems and worse on hyperbolic ones.
Muralikrishnan & Speck (2025, Eq. (5.7)) recall the Gander–Hairer superlinear bound:
if $\alpha$ bounds the difference $\mathcal F-\mathcal G$ over one slice and $\beta$ is
a Lipschitz constant of $\mathcal G$ (both page-local),

$$e^{(k)}_{j+1}\le\bar\beta^{\,j-k}\,\frac{\alpha^k}{k!}\prod_{i=1}^{k}(j+1-i)\;\delta,\qquad\bar\beta=\max(1,\beta),$$

with $e^{(k)}_j$ the error at $T_j$ and $\delta$ the largest initial error over the
slices. The product vanishes for $k>j$, which is finite termination again.

**Linear parabolic problems: the convergence factor.** Jin et al. (2025) take
$y'=Ly+g(t)$ with $-L$ self-adjoint, positive definite and with compact inverse, and a
fine and a coarse one-step method with rational stability functions
$R_{\mathrm f}$, $R_{\mathcal G}$ (page-local; the fine slice map has
$R_{\mathrm f}(z/N_f)^{N_f}$). In each eigencomponent, with $z=\Delta T\lambda$, the error
obeys $e^{(k+1)}_{j+1}=R_{\mathcal G}(z)\,e^{(k+1)}_j+\big(R_{\mathrm f}(z/N_f)^{N_f}-R_{\mathcal G}(z)\big)e^{(k)}_j$
(§3.1, Eq. (3.1)). Summing the geometric series gives the **convergence factor**

$$\kappa_c=\sup_{z}\frac{\big|R_{\mathrm f}(z/N_f)^{N_f}-R_{\mathcal G}(z)\big|}{1-\lvert R_{\mathcal G}(z)\rvert},$$

the supremum over the scaled spectrum (Eq. (3.2); Jin et al. write it with $s=-z>0$).
**Theorem 3.2:** if both methods satisfy $\lvert R(z)\rvert<1$ for $z<0$, are accurate of
some order $p\ge1$ and are strongly stable, $\lvert R(-\infty)\rvert<1$, then
$\max_j\lVert U^{(k)}_j-U_j\rVert\le c\,\kappa_c^k$, also for non-smooth initial data.
This is a linear bound; it ignores the finite-termination effect. A fine method with
$\lvert R(-\infty)\rvert=1$ (Crank–Nicolson, Gauss) needs a bounded spectrum and large $N_f$,
which is why the authors call such fine propagators seldom used (§2.1, Remark 3.1).

The backward-Euler coarse propagator gives the barrier that this analysis targets:
Yang–Yuan–Zhou proved a mesh- and $N_f$-robust contraction factor $\approx0.3$, observed to
be sharp, and Friedhoff–Southworth report $\approx0.26$ for SDIRK-22 and $\approx0.15$ for
SDIRK-33 as both coarse and fine method (Jin et al. 2025, §2.2, as recalled). Jin et al.
evaluate $\kappa_c$ to $0.264$–$0.299$ for backward Euler and $0.261$–$0.269$ for
SDIRK-22 over $N_f\in\{2,\dots,128\}$ and four L-stable fine methods (Table 4.1).

**Non-diffusive problems: partitioned Dahlquist analysis.** Buvoli & Minion (2024, §5)
apply Parareal to $y'=\lambda_1y+\lambda_2y$ with $\lambda_1,\lambda_2$ imaginary, the
first exponentiated and the second treated explicitly. Both propagators reduce to scalar
slice factors $R_{\mathcal G}$, $R_{\mathcal F}$; the iterates obey
$\mathbf e^{(k)}=E\,\mathbf e^{(k-1)}$ with the nilpotent matrix
$E=I-\mathcal M_{\mathcal G}^{-1}\mathcal M_{\mathcal F}$, where $\mathcal M_{\mathcal G}$, $\mathcal M_{\mathcal F}$ are lower
bidiagonal with $1$ on the diagonal and $-R_{\mathcal G}$, $-R_{\mathcal F}$ below it
(Eqs. (30)–(34); page-local symbols, calligraphic because $M$ is the mass matrix). Because $E$ is nilpotent its spectrum says
nothing about the rate; instead $\lVert E\rVert<1$ guarantees monotone convergence, with
the closed form

$$\lVert E\rVert_\infty=\frac{1-\lvert R_{\mathcal G}\rvert^{N}}{1-\lvert R_{\mathcal G}\rvert}\,\lvert R_{\mathcal G}-R_{\mathcal F}\rvert$$

(Eq. (40), shown in their earlier IMEX-Parareal paper). The set where
$\lVert E\rVert_\infty<1$ is the **convergence region**. They also give the stability
function of a whole Parareal run with $k$ iterations, viewed as one step over all slices
(Eq. (37)); it depends on $k$. The criterion is applied mode by mode: a Fourier mode
converges monotonically only if its scaled frequency lies below the width of the
convergence region, and the other modes stay at coarse accuracy (§5.5, §5.7). The authors
conclude that Parareal reaches fine accuracy for low-frequency oscillatory modes and only
coarse accuracy for high-frequency ones, so that non-diffusive PDEs with rapid spectral
broadening, high-order dispersive terms or Fourier pseudo-spectral discretizations are the
hardest cases.

## Variants with special propagators

### Low-rank Parareal

Carrel et al. (2023) apply Parareal to matrix ODEs $X'=f(X)$, $X\in\mathbb R^{m\times m}$
(page-local), with propagators that differ in **rank** (coarse rank $r_c$, fine rank $r$, page-local) rather than step size or order.
With $\mathcal T_r$ the truncated SVD to rank $r$ and $\psi_r$ the flow of dynamical
low-rank approximation at rank $r$ over one slice (page-local), the coarse propagator is
$\psi_{r_c}\circ\mathcal T_{r_c}$ and the fine one $\psi_r\circ\mathcal T_r$, with $r_c<r$ ($r=m$
gives the exact flow) (Def. 3.1, Eqs. (7)–(9)). The cost of DLRA integrators grows like
$O(mr^2+r^3)$, so the coarse solve is cheap (§3, footnote 1). Iterates have rank at most
$r+2r_c$; a small random perturbation in the initial coarse sweep makes the rank exactly
$r+2r_c$, so that the iteration runs on the correct manifold.

For an affine autonomous field $X'=\mathcal A(X)+B$ with one-sided Lipschitz constant
$\ell<0$ and DLRA modelling error $\epsilon_r$ at rank $r$ (page-local), **Lemma 3.2** gives the
double recursion

$$\lVert e^{(k+1)}_{j+1}\rVert\le\alpha\lVert e^{(k)}_j\rVert+\beta\lVert e^{(k+1)}_j\rVert+\chi,$$

with $\alpha=e^{\ell\Delta T}C_{r,r_c}$, $\beta=e^{\ell\Delta T}C_{r_c}$ (Lipschitz constants of
$\mathcal T_r-\mathcal T_{r_c}$ and $\mathcal T_{r_c}$), and $\chi$ (page-local) collecting the best rank-$r$
approximation error and the modelling errors (Eqs. (11), (15)–(16)). If $\alpha+\beta<1$,
up to the stagnation level $\chi/(1-\alpha-\beta)$:

- **Theorem 3.3** (linear): error factor $(\alpha/(1-\beta))^k$;
- **Theorem 3.5** (superlinear): $\frac{\alpha^k}{(k-1)!}\frac{\prod_{i=2}^k(j-i)}{1-\beta}$;
- **Theorem 3.6** (linear): $\alpha^k(1+\beta)^{j-1}$.

**Lemma 3.4** solves the equality version of the recursion in closed form by generating
functions, extending Gander & Hairer (2008, Thm. 1, as recalled) by the $\chi$ term.
None of the three bounds is uniformly best; they describe different phases (§3.2,
Fig. 1). The truncation constants are bounded to first order by singular-gap ratios,
$\sigma_{r_c}/(\sigma_{r_c}-\sigma_{r_c+1})$ for $\mathcal T_{r_c}$ (**Theorem 3.8**, first part cited from
Breiding–Vannieuwenhoven and Feppon–Lermusiaux). Since $\ell<0$, a large $\Delta T$ makes
$\alpha$, $\beta$ small: convergence for large slices on dissipative problems. A
rank-adaptive variant truncates the fine propagator by a tolerance (Def. 4.4).

Numerically (no parallel runs), the convergence rate on the differential Lyapunov
equation of a 2D heat problem is independent of the coarse rank $r_c\in\{2,4,6\}$, the fine
rank and the size $n\in\{50,100,200\}$, and faster for larger $\Delta T$, as the theory
predicts; a parametric heat problem shows linear-then-superlinear convergence; a
differential Riccati equation, outside the affine theory, converges but depends more on
$r_c$ (§4, Figs. 3–8).

### Optimized coarse propagators

Jin et al. (2025, §3.2, Alg. 3.1) choose the coarse stability function to minimize the
convergence factor $\kappa_c$ for a given fine method. They parametrize
$R_{\mathcal G}$ as a rational function of numerator degree $n_R$ and denominator degree
$m_R$ (page-local), with positive denominator coefficients written as exponentials,
impose order-$p$ consistency as linear constraints on the numerator coefficients
(Eq. (3.5)), enforce $\lvert R_{\mathcal G}\rvert<1$ exactly by checking only its real
critical points and $z=-\infty$ through a log-barrier (Eq. (3.7)), and minimize over a
sampled spectrum by subgradient descent with a path-following barrier weight. The forcing
weights of the inhomogeneous term then follow from strict-accuracy conditions (Eq. (3.8)).
**Proposition 3.3:** the optimized coarse propagator (OCP) is consistent of order $p$ and
strongly stable.

With $m_R=n_R=2$, $p=1$ and $N_f=16$, the OCPs reach $\kappa_c\approx0.013$–$0.020$ over
$N_f\in\{2,\dots,128\}$ against $\approx0.3$ for backward Euler, for 2-, 3- and 4-stage
Lobatto IIIC and 3-stage Radau IIA fine methods (Table 4.1). For the 2-stage Lobatto IIIC
fine method the OCP is, in registry form ($z=\Delta T\lambda$),

$$R_{\mathcal G}(z)=\frac{1+0.20967z+0.00484z^2}{1-0.79033z+0.37931z^2},$$

translated from Appendix B, where the variable is $-z$. For an A-stable
$\vartheta$-method fine propagator with $\vartheta=0.52$ (page-local), a degree-3 OCP
gives $\approx0.10$ against $0.298$. **Theorem 3.5** bounds the change of
$\kappa_c$ for $N_f\in[16,128]$ by $112\sup\lvert h_\kappa\rvert$, with
$h_\kappa$ an explicit sensitivity function (page-local), under convexity assumptions on
the fine method; **Corollary 3.6** gives a variation of at most $0.055$ for 2-stage
Lobatto IIIC. The assumptions hold for 2- and 4-stage Lobatto IIIC and 3-stage Radau IIA,
not for 3-stage Lobatto IIIC, whose stability function changes sign (Remark 3.7).

Experiments show observed contraction $\approx0.04$ with OCPs against $\approx0.3$ with
backward Euler on the [heat equation](/benchmarks/heat-equation.md), the
[Allen–Cahn equation](/benchmarks/allen-cahn-equation.md) and the viscous
[Burgers equation](/benchmarks/burgers-equation.md). The simulated efficiencies are 2.2–2.6
times those of backward Euler on the heat equation and 1.7–3.4 times on Allen–Cahn, the
ratios of the printed Table 4.2–4.3 entries *(compiler check, not in the source)*, with
iteration counts falling from 10–11 to 4 and from 6–11 to 3–5. For nonlinear problems the coarse
method is semi-implicit, with the nonlinearity explicit, and uses the OCP from the linear
theory. For Allen–Cahn with $\varepsilon^2=0.02$ ($\varepsilon$ the interface width) or
Burgers with viscosity $0.02$ and larger $N_f$, the gain over backward Euler shrinks, and
the authors call for nonlinear modifications (§4.2, Figs. 4.5, 4.7). The approach needs no
training data, unlike neural-network coarse propagators (§1).

### Exponential Runge–Kutta propagators

Buvoli & Minion (2024) use [exponential Runge–Kutta methods](/methods/exponential-integrators.md)
(exponential Euler; Cox–Matthews ETD2RK and ETD3RK; Krogstad's fourth-order method,
ERK1–ERK4) as both coarse and fine propagator for semilinear problems $y'=Ly+N(t,y)$
whose linear part has imaginary spectrum. Exponential integrators resolve the fast linear
waves exactly even at coarse steps. Unmodified, ERK Parareal diverges on the nonlinear
Schrödinger equation. **Repartitioning**, which adds a damping operator to the
exponentiated part and subtracts it from the nonlinear part so that the eigenvalues of
the linear operator are rotated by a small angle into the left half-plane, makes it
stable and convergent (§3.2, §4, Fig. 2). Linear analysis explains why: the Parareal
iteration magnifies the very weak instability of serial ERK4 on imaginary spectra, and
repartitioning removes it (§5.3, Fig. 5). Two trade-offs follow from the analysis:

- a larger number of coarse steps per slice, or a higher coarse order, enlarges the
  convergence region at the cost of speedup; the region width grows about linearly in
  the number of coarse steps (§5.4, §5.6, Remark 1);
- without repartitioning the region extends infinitely along $\lambda_2=0$, where the
  exponential method is exact; any rotation destroys this, so the smallest angle that
  ensures stability is best (§5.6, Fig. 10).

Even with repartitioning, stability holds only when the exponentiated linear term carries
most of the stiffness (§5.3). On the [Vlasov–Poisson](/benchmarks/vlasov-poisson-equation.md)
bump-on-tail problem, three coarse steps per slice converge to fine accuracy in eight
iterations, while two fail although the linear analysis predicts (barely) convergence;
the authors suggest the nonlinear term may not be as non-stiff as assumed (§6.3). They
claim the first use of ETD Runge–Kutta methods inside Parareal (§7).

### Particle methods: coarse propagators by discretization change

Muralikrishnan & Speck (2025) apply Parareal to the full particle phase-space state of
particle-in-Fourier (PIF) discretizations of the Vlasov–Poisson system. Spatial
coarsening is undefined for particles at random positions, and dropping Fourier modes is
ineffective, so the coarse propagator is either PIF with a looser nonuniform-FFT
tolerance or the grid-based particle-in-cell (PIC) scheme, each optionally with a larger
step (§1, §4). The time integrator is the second-order velocity Verlet or Boris scheme.
Inserting bounds on $\mathcal F-\mathcal G$ into the Gander–Hairer bound gives
**Theorems 5.2–5.3**: the factor $\alpha$ becomes
$C_{\mathrm{grid}}\Delta x^{\min(m_s+1,2)}+C_{\mathrm{noise}}P_c^{-1/2}+C_{\mathrm{time}}\Delta T\,h_{\mathcal G}^{p}$
for the PIC coarse propagator (shape-function order $m_s$, $P_c$ particles per cell,
coarse step $h_{\mathcal G}$, all page-local) and $C_{\mathrm{nufft}}\epsilon_{\mathrm{nu}}+C_{\mathrm{time}}\Delta T\,h_{\mathcal G}^{p}$
for the loose-tolerance PIF coarse propagator ($\epsilon_{\mathrm{nu}}$ the nonuniform-FFT
tolerance, page-local). With $p=2$ this predicts $O(h_{\mathcal G}^{2k})$ convergence in
the coarse step (§6.2.3). Experiments confirm the predicted $P_c^{-k/2}$,
$\Delta x^{2k}$ and $\epsilon_{\mathrm{nu}}^k$ scalings and, for Landau damping with the PIF
coarse propagator, $h_{\mathcal G}^{2k}$ (Figs. 1–5). Parareal over the whole interval
converged too slowly on the Penning trap, and 16 successive blocks ("multi-block"
Parareal) raised its measured speedup from 1.1 to 1.5 (App. A.5). A converged Parareal solution
keeps the conservation properties of the fine scheme only if the Parareal tolerance is
near machine precision (Remark 5.4; see [symplecticity](/properties/symplecticity.md)).

## Qualifications

- **Penning trap: half the predicted rate.** On the Penning trap, Muralikrishnan & Speck
  (2025, §6.2.3, Fig. 3) observe convergence only like $O(h_{\mathcal G}^{k})$, not the
  predicted $O(h_{\mathcal G}^{2k})$, also with the PIF coarse propagator and a 16-times
  smaller fine step. The authors leave the reason open and link it to the dynamics (a fast
  modified cyclotron frequency) rather than to the coarse propagator. Their bound treats
  $C_{\mathrm{time}}$ as independent of $k$ and asserts, without proof, that the PIF
  operator norms are bounded independently of grid and particle number (Thm. 5.2 proof).
- **Optimized coarse propagators are nearly independent of the fine method.** The four
  $m_R=n_R=2$ OCPs printed in Jin et al. (2025, App. B) agree to about two digits (in the
  source's variable, numerators $1-0.210\lambda+0.005\lambda^2$ to within $0.002$ in the
  linear and $10^{-4}$ in the quadratic coefficient, denominators $1+0.79\lambda+0.38\lambda^2$
  to within $0.004$) *(compiler check of the printed coefficients)*. The paper presents
  the OCPs as optimized for the underlying fine method (§1). For $N_f\ge16$ every accurate
  fine method has $R_{\mathrm f}(z/N_f)^{N_f}\approx e^z$, which would explain the agreement
  *(compiler remark)*.
- **OCP order.** All reported OCPs have order $p=1$; the gain over backward Euler is in the
  damping profile, not in accuracy. The §3 introduction states a factor $\approx0.02$ for
  $N_f\in[16,128]$, where Table 4.1 gives $0.013$–$0.014$.
- **Linear analysis is not a guarantee.** Buvoli & Minion's Vlasov–Poisson run with two
  coarse steps fails although the analysis predicts convergence (§6.3). In their
  Remark 1, the final bound "$\lvert r_1\rvert+\lvert r_2\rvert<(C_2N_gN_p)^{-1}$ grows linearly in
  $N_g$" contradicts itself: the expression shrinks with $N_g$, while their Eq. (64)
  gives the condition $\lvert r_1\rvert+\lvert r_2\rvert<N_g(C_2N_p)^{-1/q}$, proportional to $N_g$ *(compiler check of Eqs. (64)–(65), not in the source; the symbols are the source's)*.
- **Low-rank Parareal scope.** The theory needs an affine field; Carrel et al. note that
  affinity enters one step of the proof only (§5). The Riccati run with $r_c=4$, called
  "slower (but still superlinear)", stagnates near $10^{-2}$ for most iterations
  (Fig. 8a). The singular-gap bound for the fine rank appears unnecessary in experiments
  (Remark 3.9).
- **Versions read.** All five sources were read as arXiv preprints; equation and section
  numbers are those of the preprints.

# Citations

- [Carrel et al. (2023)](/sources/carrel-2023.md) — arXiv v2: Def. 2.1, §2.1; Def. 3.1 (Eqs. (7)–(9)); Lemma 3.2 (Eq. (11)); Eqs. (15)–(16); Thms. 3.3, 3.5, 3.6; Lemma 3.4; Thm. 3.8; Remark 3.9; Def. 4.4; §4 (Figs. 1–9); §5.
- [Jin et al. (2025)](/sources/jin-2025.md) — arXiv v2: Alg. 2.1, §2.1–2.2; §3.1 (Eqs. (3.1)–(3.2), Thm. 3.2, Remark 3.1); §3.2 (Eqs. (3.4)–(3.8), Alg. 3.1, Prop. 3.3); §3.3 (Thm. 3.5, Cor. 3.6, Remark 3.7); §4 (Table 4.1–4.3, Figs. 4.2–4.7); App. B.
- [Buvoli & Minion (2024)](/sources/buvoli-2024.md) — arXiv v2: Eqs. (4)–(6), Table 1; §3.2 (Eqs. (13)–(15)); §4 (Figs. 2–4); §5.3–5.7 (Eqs. (30)–(50), Figs. 5–10); §6.1–6.3 (Figs. 14, 16); App. F (Remark 1); §7.
- [Muralikrishnan & Speck (2025)](/sources/muralikrishnan-2025.md) — arXiv v2: §1, §4 (Eqs. (4.1)–(4.2)); §5.2–5.5 (Lemma 5.1, Thms. 5.2–5.3, Eq. (5.7), Remark 5.4); §6.2–6.3 (Figs. 1–6); App. A.3–A.5.
- [Gander & Palitta (2024)](/sources/gander-2024.md) — arXiv v2: §1 (Parareal and its analyses cited as background to ParaDiag).
