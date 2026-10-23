---
type: Definition
title: "Notation registry"
description: "Normative symbol registry — every concept page writes mathematics in this notation, never in paper-native symbols."
status: established
tags: [notation, meta]
timestamp: 2026-10-20T03:57:00Z
---

# Notation registry

Every concept page of this bundle writes mathematics in the symbols below.
A source's own symbols are translated on its Source page (`# Notation map`).
The registry was seeded on 2026-10-19 from the first chunk (Runge–Kutta
theory, B-series, splitting, IMEX and multirate methods, step-size control,
asymptotic-preserving schemes, integrator software). It follows the
Hairer–Nørsett–Wanner conventions where they exist, because most sources
do. Extend this registry, and log the extension, before writing a symbol it
lacks.

**Clashes kept on purpose.** A few letters carry two meanings in
well-separated families; the family is always clear from the page, and a
page that needs both meanings renames one locally and says so: $\gamma$
(tree density; Rosenbrock diagonal coefficient; composition weights
$\gamma_j$; relaxation parameter $\gamma_n$), $\alpha$ (Shu–Osher coefficients; Rosenbrock coefficients;
the angle of A($\alpha$)-stability), $\eta$ (the entropy or invariant
$\eta(y)$; the integer argument of the simplifying assumption $C(\eta)$), $k$ (number of steps of a multistep method; the exponent order
$\min(p,\hat p)+1$ of a PID controller; the Parareal iteration index), $\beta$ (PID exponents $\beta_1,\beta_2,\beta_3$;
multistep coefficients $\beta_j$; Shu–Osher $\beta_{ij}$). $M$ is reserved for the mass matrix,
never a node count or a multirate ratio.

## 1. Problem and time grid

| Symbol | Meaning | Note |
|---|---|---|
| $t$, $y(t)\in\mathbb R^d$ | time and the exact solution of the initial-value problem | $d$ is the dimension; vectors are not bold |
| $y'=f(t,y)$, $y(t_0)=y_0$ | the IVP | autonomous form $y'=f(y)$ when a page says so |
| $J=\partial f/\partial y$ | Jacobian of $f$ | $J_n$ evaluated at $(t_n,y_n)$ |
| $M$ | mass matrix of $My'=f(t,y)$ | singular only on DAE pages, which say so |
| $L$ | linear operator of a linear or semi-discretized problem $y'=Ly$ | spatial semi-discretization (method of lines) |
| $\lambda$ | eigenvalue, or the scalar of the Dahlquist test equation $y'=\lambda y$ | stable half-plane $\operatorname{Re}\lambda\le0$ |
| $h$ | step size | sources' $\Delta t$, $\tau$, $\delta t$ are translated to $h$ |
| $t_n$, $y_n$ | time grid $t_{n+1}=t_n+h_n$ and numerical solution $y_n\approx y(t_n)$ | $h_n$ when steps vary |
| $\varepsilon$ | small (stiffness) parameter of a singularly perturbed or multiscale problem | relaxation time, Knudsen or Mach number, stated per page |
| $\Delta x$ | mesh width of a spatial discretization | |
| $\nu$ | Courant (CFL) number | |
| $\langle\cdot,\cdot\rangle$, $\lVert\cdot\rVert$ | inner product and its norm | other norms carry subscripts |

## 2. Runge–Kutta methods

| Symbol | Meaning | Note |
|---|---|---|
| $s$ | number of stages | |
| $A=(a_{ij})$, $b=(b_i)$, $c=(c_i)$ | Butcher matrix, weights, abscissae | $b$ and $c$ are column vectors; $b^\top$ in formulas |
| $\mathbf 1$ | vector of ones | |
| $Y_i$ | stage values, $Y_i=y_n+h\sum_j a_{ij}f(t_n+c_jh,Y_j)$ | sources written with stage derivatives $k_i=f(t_n+c_ih,Y_i)$ are translated |
| $y_{n+1}=y_n+h\sum_i b_if(t_n+c_ih,Y_i)$ | the update | |
| $\hat b$, $\hat y_{n+1}$, $\hat p$ | embedded weights, embedded solution, embedded order | |
| $p$ | classical order | |
| $q$ | stage order | |
| $q_{\mathrm w}$ | weak stage order | |
| $\tau^{(k)}=Ac^{k-1}-c^k/k$ | $k$-th stage-order residual | powers of $c$ componentwise |
| $B(\xi)$, $C(\eta)$, $D(\zeta)$ | Butcher's simplifying assumptions | |
| $\mathcal K_m=\operatorname{span}\{\tau^{(k)},A\tau^{(k)},\dots\}$ | Krylov space of the stage-order residuals of weak-stage-order theory | Biswas et al. write $K_m$ |
| $\mathcal Y$ | smallest $A^\top$-invariant subspace containing $b$ | Biswas et al. write $Y$, which clashes with the stage values |
| $n_c$ | number of distinct abscissae $c_i$ | |
| $\mathcal C$ | SSP coefficient | $\mathcal C_{\mathrm{eff}}=\mathcal C/s$ effective SSP coefficient |
| $h_{\mathrm{FE}}$ | forward-Euler step bound of the strong-stability hypothesis | sources' $\Delta t_{\mathrm{FE}}$ |
| $\alpha_{ij}$, $\beta_{ij}$ | Shu–Osher form coefficients | |

## 3. Linear stability

| Symbol | Meaning | Note |
|---|---|---|
| $z=h\lambda$ | scaled eigenvalue | |
| $R(z)$ | stability function, $R(z)=1+zb^\top(I-zA)^{-1}\mathbf 1$ | rational for implicit methods |
| $P(z)$ | stability polynomial of an explicit method | $P(z)=\sum_{j=0}^s\theta_jz^j$ with $\theta_j=1/j!$ for $j\le p$ |
| $\mathcal S=\{z\in\mathbb C:\lvert R(z)\rvert\le1\}$ | region of absolute stability | |

## 4. Trees and B-series

| Symbol | Meaning | Note |
|---|---|---|
| $T$, $\tau$, $\varnothing$ | set of rooted trees, a tree, the empty tree | |
| $\lvert\tau\rvert$ | order (number of vertices) | |
| $\sigma(\tau)$, $\gamma(\tau)$ | symmetry and density | |
| $F(\tau)$ | elementary differential | |
| $\Phi(\tau)$ | elementary weight of a Runge–Kutta method | order $p$ iff $\Phi(\tau)=1/\gamma(\tau)$ for $\lvert\tau\rvert\le p$ |
| $B(a,y)=a(\varnothing)y+\sum_{\tau\in T}\frac{h^{\lvert\tau\rvert}}{\sigma(\tau)}a(\tau)F(\tau)(y)$ | B-series with coefficient map $a$ | |
| $a\cdot b$ | composition of coefficient maps (Butcher product) | $B(b,B(a,y))=B(a\cdot b,y)$ |
| $b\star a$ | substitution law | |
| $\tilde f$ | modified vector field of backward error analysis | |

## 5. Flows, splitting and composition

| Symbol | Meaning | Note |
|---|---|---|
| $\varphi_h$ | exact flow over time $h$ | $\varphi^{[i]}_h$ flow of the part $f^{[i]}$ |
| $\psi_h$ | a numerical one-step map | $\psi_h^*=\psi_{-h}^{-1}$ its adjoint |
| $f=f^{[1]}+f^{[2]}$ | split vector field of a splitting method | operator letters $A$, $B$ only when a page says so |
| $a_j$, $b_j$ | splitting coefficients, $\psi_h=\varphi^{[2]}_{b_sh}\circ\varphi^{[1]}_{a_sh}\circ\dots\circ\varphi^{[2]}_{b_1h}\circ\varphi^{[1]}_{a_1h}$ | |
| $\gamma_j$ | composition weights, $\psi_h=\chi_{\gamma_sh}\circ\dots\circ\chi_{\gamma_1h}$ with a basic method $\chi_h$ | |
| $[X,Y]$ | Lie bracket / commutator | |
| $\pi_h$ | processor of a processed method $\pi_h\circ\psi_h\circ\pi_h^{-1}$ | |

## 6. Additive, partitioned and multirate methods

| Symbol | Meaning | Note |
|---|---|---|
| $f=f^{\mathrm E}+f^{\mathrm I}$ | explicit (non-stiff) and implicit (stiff) parts | IMEX |
| $(A^{\mathrm E},b^{\mathrm E},c^{\mathrm E})$, $(A^{\mathrm I},b^{\mathrm I},c^{\mathrm I})$ | explicit and implicit tableaux of an IMEX/additive RK method | |
| $f=\sum_q f^{\{q\}}$, $A^{\{q,r\}}$, $b^{\{q\}}$ | partitions and coupling matrices of a GARK method | |
| $f^{\{\mathrm s\}}$, $f^{\{\mathrm f\}}$ | slow and fast parts of a multirate problem | |
| $H$, $h$, $m$ | macro step, micro step, multirate ratio $m=H/h$ | multirate pages only; elsewhere $h$ is the step; sources' $M$ is translated |
| $\ell$ | micro-step index, $\ell=0,\dots,m-1$ | sources' $\lambda$ clashes with the eigenvalue |
| $\Gamma^{(k)}$, $\Omega^{(k)}$ | coupling coefficient matrices of MRI-GARK and IMEX-MRI-GARK methods (implicit and explicit slow parts) | $\gamma_{ij}(\theta)=\sum_k\gamma^{(k)}_{ij}\theta^k$ |
| $F(u,v)$ | nonlinear partition of the right-hand side, $f(y)=F(y,y)$; IMEX-NPRK methods are implicit in the first argument $u$ and explicit in the second $v$ | nonlinearly partitioned Runge–Kutta (NPRK) pages |
| $\phi_k(z)$ | $\phi_0(z)=e^z$, $\phi_k(z)=\int_0^1e^{(1-\theta)z}\frac{\theta^{k-1}}{(k-1)!}\,d\theta$ | sources without the $1/(k-1)!$ factor are translated |

## 7. Other method families

| Symbol | Meaning | Note |
|---|---|---|
| $\alpha_{ij}$, $\gamma_{ij}$, $\gamma$ | Rosenbrock coefficients, $\gamma=\gamma_{ii}$ | |
| $\dot f$ | $\dot f(y)=f'(y)f(y)$, the second derivative of the solution (autonomous) | multiderivative methods; $\dot a_{ij}$, $\dot b_i$ its coefficients |
| $t_{n,m}$, $m=0,\dots,\mathsf M$ | subnodes of a deferred-correction or ADER step | sans-serif $\mathsf M$, distinct from the mass matrix |
| $K$ | number of correction (Picard) iterations | |
| $\mathrm{atol}$, $\mathrm{rtol}$ | absolute and relative tolerances | |
| $\lVert\cdot\rVert_{\mathrm{WRMS}}$ | weighted root-mean-square norm of step-size control | |
| $\mathrm{err}_n$ | scaled local error estimate of step $n$ | accept iff $\mathrm{err}_n\le1$ |
| $\beta_1,\beta_2,\beta_3$ | PID controller exponents, $h_{n+1}=h_n\,\mathrm{err}_n^{-\beta_1/k}\mathrm{err}_{n-1}^{-\beta_2/k}\mathrm{err}_{n-2}^{-\beta_3/k}$ | $k=\min(p,\hat p)+1$; sources' other parameterizations are translated |

## 8. Structure preservation

| Symbol | Meaning | Note |
|---|---|---|
| $\eta(y)$ | a convex entropy, energy or other invariant functional of the solution | $\eta'(y)$ its gradient; the page states which |
| $\gamma_n$ | relaxation parameter of step $n$ | relaxed solution $y^{\gamma}_{n+1}=y_n+\gamma_n(y_{n+1}-y_n)$ at time $t_n+\gamma_nh$ (incremental-direction technique: at $t_n+h$); distinct from the Rosenbrock $\gamma$ |
| $y_i'=\sum_{j}\bigl(p_{ij}(y)-d_{ij}(y)\bigr)$ | production–destruction system: $p_{ij}\ge0$ is the rate from constituent $j$ to $i$, $d_{ij}\ge0$ the rate from $i$ to $j$ | conservative when $p_{ij}=d_{ji}$ (then $\mathbf 1^\top y$ is invariant); $d_{ii}=p_{ii}=0$ |
| $\varpi_i$ | Patankar weight denominator: a modified Patankar scheme multiplies a production term $p_{ij}$ by $y^{n+1}_j/\varpi_j$ and a destruction term $d_{ij}$ by $y^{n+1}_i/\varpi_i$ | sources write $\sigma_i$ or $\pi_i$ (both registry symbols) |


## 9. Linear multistep methods

| Symbol | Meaning | Note |
|---|---|---|
| $k$ | number of steps of a linear multistep method | the BDF$k$ method has order $k$; distinct from the iteration count $K$ |
| $\alpha_j$, $\beta_j$ | coefficients, $\sum_{j=0}^k\alpha_jy_{n+j}=h\sum_{j=0}^k\beta_jf(t_{n+j},y_{n+j})$ | single-index family, distinct from the Shu–Osher $\alpha_{ij}$, $\beta_{ij}$ |
| $\varrho(\zeta)$, $\sigma(\zeta)$ | first and second generating polynomials, $\varrho(\zeta)=\sum_j\alpha_j\zeta^j$, $\sigma(\zeta)=\sum_j\beta_j\zeta^j$ | $\sigma(\zeta)$ takes a complex argument, distinct from the tree symmetry $\sigma(\tau)$ |
| $r_n=h_n/h_{n-1}$ | step-size ratio of a variable-step method | |
| $G$ | symmetric positive definite matrix of a G-norm, $\lVert Y\rVert_G^2=\sum_{i,j}g_{ij}\langle y_i,y_j\rangle$ | G-stability |
| $\mu_1,\dots,\mu_k$ | Nevanlinna–Odeh multipliers: the scheme is tested with $y_{n+k}-\sum_j\mu_jy_{n+k-j}$ | sources' $\eta_j$ are translated ($\eta$ is the registry entropy) |

## 10. Parallel-in-time methods and spectral deferred correction

| Symbol | Meaning | Note |
|---|---|---|
| $T_0<T_1<\dots<T_N$, $\Delta T$ | time slices of a parallel-in-time partition and the slice length | $N$ slices, usually one per process; $h$ stays the step inside a slice |
| $\mathcal F$, $\mathcal G$ | fine and coarse propagators: one-slice solution maps of an accurate and a cheap method | calligraphic, distinct from the elementary differential $F(\tau)$ and the NPRK $F(u,v)$ |
| $U_j^{(k)}$ | Parareal iterate at $T_j$ after $k$ iterations, $U^{(k+1)}_{j+1}=\mathcal G(U^{(k+1)}_j)+\mathcal F(U^{(k)}_j)-\mathcal G(U^{(k)}_j)$ | $k$ is the iteration index here; the clash with the multistep $k$ is kept on purpose |
| $Q$ | collocation (integration) matrix of a spectral deferred correction step on $\mathsf M$ nodes | the Butcher matrix $A$ of the underlying collocation method |
| $Q_\Delta$ | approximation of $Q$ that preconditions an SDC sweep (lower-triangular, or diagonal for parallel-across-the-method SDC) | sources' $Q_\Delta$ |
