---
type: Method
title: "Kennedy–Carpenter additive Runge–Kutta methods (ARK3, ARK4, ARK5)"
description: "The three IMEX additive Runge–Kutta pairs of Kennedy and Carpenter: an explicit method coupled to an L-stable, stiffly accurate, stage-order-2 ESDIRK with shared weights and abscissae, orders 3, 4, 5 with embedded orders 2, 3, 4; design conditions, printed coefficients, stability data, stiffness leakage and order-reduction tests."
status: established
aliases: ["ARK3(2)4L[2]SA", "ARK4(3)6L[2]SA", "ARK5(4)8L[2]SA", "Kennedy–Carpenter ARK"]
tags: [imex, runge-kutta, stiff, implicit, explicit, step-size-control]
timestamp: 2026-10-29T18:13:00Z
---

# Kennedy–Carpenter additive Runge–Kutta methods (ARK3, ARK4, ARK5)

[Kennedy & Carpenter (2003)](/sources/kennedy-2003.md) construct three
[IMEX additive Runge–Kutta](/methods/imex-runge-kutta.md) pairs for
$y'=f^{\mathrm E}(y)+f^{\mathrm I}(y)$, written for method-of-lines
convection–diffusion–reaction systems with convection and diffusion in the nonstiff
$f^{\mathrm E}$ and the chemistry in the stiff $f^{\mathrm I}$ (§1, §3). Each pair couples an
explicit Runge–Kutta method (ERK) with an
[ESDIRK](/methods/diagonally-implicit-runge-kutta.md), a diagonally implicit method with an
explicit first stage and constant diagonal $\gamma=a^{\mathrm I}_{ii}$, $i\ge2$. The two
tableaux share weights, embedded weights and abscissae:
$b^{\mathrm E}=b^{\mathrm I}=b$, $\hat b^{\mathrm E}=\hat b^{\mathrm I}=\hat b$,
$c^{\mathrm E}=c^{\mathrm I}=c$. The implicit part is L-stable,
[stiffly accurate](/properties/stiff-accuracy.md) and has
[stage order](/definitions/stage-order.md) 2, and the pairs couple without coupling error
up to their full order 3, 4 and 5 (§4–6, App. B). Every pair carries an
[embedded method](/methods/embedded-runge-kutta-pair.md) one order lower and a
[dense output](/methods/dense-output.md). The version read is the NASA Technical Memorandum
NASA/TM-2001-211038; section, equation, table and appendix numbers below are those of the TM.
The three pairs are the IMEX defaults of [ARKODE](/software/arkode.md)
([Reynolds et al. 2023](/sources/reynolds-2023.md), §2.2).

## Structure and naming

With step $h$ and stage values $Y_i$, the scheme is the additive Runge–Kutta step of
[IMEX Runge–Kutta](/methods/imex-runge-kutta.md) with shared $b$ and $c$ (Kennedy & Carpenter
2003, Eqs. (3)–(4), (24)). The two tableaux have the form (§3, p. 12)

$$\begin{array}{c|ccccc}
0&0&&&&\\
2\gamma&2\gamma&0&&&\\
c_3&a^{\mathrm E}_{31}&a^{\mathrm E}_{32}&0&&\\
\vdots&\vdots&&&\ddots&\\
1&a^{\mathrm E}_{s1}&\cdots&&a^{\mathrm E}_{s,s-1}&0\\\hline
&b_1&\cdots&&b_{s-1}&b_s
\end{array}\qquad
\begin{array}{c|ccccc}
0&0&&&&\\
2\gamma&\gamma&\gamma&&&\\
c_3&a^{\mathrm I}_{31}&a^{\mathrm I}_{32}&\gamma&&\\
\vdots&\vdots&&&\ddots&\\
1&b_1&\cdots&&b_{s-1}&\gamma\\\hline
&b_1&\cdots&&b_{s-1}&\gamma
\end{array}$$

so the first stage is $Y_1=y_n$, every later stage needs one solve with the matrix
$I-h\gamma J^{\mathrm I}$ ($J^{\mathrm I}$ the Jacobian of $f^{\mathrm I}$, page-local), and the
last implicit row equals $b$ (stiff accuracy). Counting coefficients, the ERK has $s(s+1)/2$
and the ESDIRK $(s^2+s+2)/2$; sharing $b$ and $c$ removes $2s-1$, and stiff accuracy leaves
$s^2-2s+2$ free parameters (§3).

The name **ARK$p(\hat p)s$S[$q$]X** follows the Dormand–Prince convention: main order $p$,
embedded order $\hat p$, $s$ stages, stability label S ("L": the additive method is
L-stable), stage order $q$ of the implicit part in brackets, and other properties X ("SA":
stiffly accurate) (§3; the paper writes $q$ for the main and $p$ for the embedded order).

## Design conditions

- **Coupling.** With $b^{\mathrm E}=b^{\mathrm I}$ and $c^{\mathrm E}=c^{\mathrm I}$, a
  2-additive method has 0, 0, 0, 2, 13, 63, 272 coupling conditions at orders 1–7
  (Table 4); without either simplification the coupling is error-free only to first order
  (§2.1.2). The two coupling conditions at order 4 are those listed on
  [IMEX Runge–Kutta](/methods/imex-runge-kutta.md).
- **Simplifying assumptions.** Imposing the column assumption $D(1)$ on both tableaux
  forces $b_s\gamma=b_s(1-c_s)$ and $0=b_s(1-c_s)$ at $j=s$, so $D(1)$ can hold for one
  method only, and with stiff accuracy ($c_s=1$) only for the ERK (Eq. (25)). Stage order 3
  is impossible for the ESDIRK: the second stage leaves the residual
  $\sum_ja^{\mathrm I}_{2j}c_j^2-c_2^3/3=\tfrac43\gamma^3\neq0$ (§3.1.1).
- **L-stability of the pair.** On $y'=\lambda_{\mathrm E}y+\lambda_{\mathrm I}y$ with
  $z_{\mathrm E}=h\lambda_{\mathrm E}$, $z_{\mathrm I}=h\lambda_{\mathrm I}$ (page-local) the
  step multiplies $y_n$ by
  $$R(z_{\mathrm E},z_{\mathrm I})=\frac{\det\bigl(I-z_{\mathrm E}A^{\mathrm E}-z_{\mathrm I}A^{\mathrm I}+(z_{\mathrm E}+z_{\mathrm I})\mathbf 1b^\top\bigr)}{\det\bigl(I-z_{\mathrm I}A^{\mathrm I}\bigr)},\qquad \det\bigl(I-z_{\mathrm I}A^{\mathrm I}\bigr)=(1-\gamma z_{\mathrm I})^{s-1}$$
  (Eqs. (26)–(28)). Write $\mathsf p_{ij}$ (page-local) for the coefficient of
  $z_{\mathrm I}^{\,i}z_{\mathrm E}^{\,j}$ in the numerator. The limit
  $z_{\mathrm I}\to-\infty$ vanishes for every $z_{\mathrm E}$ only if
  $\mathsf p_{s,0}=\mathsf p_{s-1,0}=\mathsf p_{s-1,1}=0$ (Eq. (31)). Stiff accuracy gives
  $\mathsf p_{s,0}=0$, the explicit first stage gives $\mathsf p_{s-1,0}=0$, and
  $\mathsf p_{s-1,1}=0$ is an extra coupling condition. Kennedy & Carpenter state that
  "several of the methods given by Ascher et al. and Griepentrog do not account for this"
  (§3.1.2); see the stability comparison below.
- **I-stability** of the ESDIRK is checked with the E-polynomial
  $E(y)=Q(iy)Q(-iy)-P(iy)P(-iy)\ge0$, $R=P/Q$ its stability function (Eq. (29)).
- **Free parameters** are spent on the principal error norm $\mathcal A^{(p+1)}$, the 2-norm of
  the order-$(p+1)$ truncation-error coefficients over all bicoloured trees (Eq. (10)), on
  the embedded-quality ratios $B$, $C$, $E$ and the largest coefficient $D$ ("usually kept
  less than 20") (§2.1.3), and on the explicit stability limits $\lambda_{\mathrm{inv}}$
  (imaginary axis) and $\lambda_{\mathrm{visc}}$ (negative real axis), which set the convective
  step $h\approx\lambda_{\mathrm{inv}}\Delta x/(u+a)$ and the diffusive step
  $h\approx\lambda_{\mathrm{visc}}\Delta x^2/\mu$ (§3.2.3, Eq. (45)); $\lambda_{\mathrm{inv}}$,
  $\lambda_{\mathrm{visc}}$, flow speed $u$, sound speed $a$ and viscosity $\mu$ are page-local
  (the paper writes $\lambda$, $\lambda_v$ and $\nu$, which the registry reserves for the
  eigenvalue and the Courant number).

## The three pairs

**ARK3(2)4L[2]SA** (§4, Eqs. (47)–(49); App. D). Four stages; $\gamma$ is the root
$\approx0.43586652150845899941601$ of $6\gamma^3-18\gamma^2+9\gamma-1=0$, the only one that
gives an I-stable ESDIRK; $c_3=\frac35$ and the fourth-order ERK elementary weight of the
chain tree are the optimization parameters. The same cubic and root fix the diagonal of the
implicit part of ARS(3,4,3) in [Ascher et al. (1997)](/sources/ascher-1997.md) (§2.7),
who call it the middle root. Coefficients as printed:

- $c=\bigl(0,\ \frac{1767732205903}{2027836641118},\ \frac35,\ 1\bigr)$, $\gamma=\frac{1767732205903}{4055673282236}$;
- $A^{\mathrm E}$: $a_{21}=\frac{1767732205903}{2027836641118}$;
  $a_{31}=\frac{5535828885825}{10492691773637}$, $a_{32}=\frac{788022342437}{10882634858940}$;
  $a_{41}=\frac{6485989280629}{16251701735622}$, $a_{42}=-\frac{4246266847089}{9704473918619}$,
  $a_{43}=\frac{10755448449292}{10357097424841}$;
- $A^{\mathrm I}$: row 2 $(\gamma,\gamma)$; row 3
  $\bigl(\frac{2746238789719}{10658868560708},\ -\frac{640167445237}{6845629431997},\ \gamma\bigr)$;
  row 4 $=b$;
- $b=\bigl(\frac{1471266399579}{7840856788654},\ -\frac{4482444167858}{7529755066697},\ \frac{11266239266428}{11593286722821},\ \gamma\bigr)$;
- $\hat b=\bigl(\frac{2756255671327}{12835298489170},\ -\frac{10771552573575}{22201958757719},\ \frac{9247589265047}{10645013368117},\ \frac{2193209047091}{5459859503100}\bigr)$.

**ARK4(3)6L[2]SA** (§5, Eqs. (52)–(55); App. D). Six stages, $\gamma=\frac14$,
$c=\bigl(0,\frac12,\frac{83}{250},\frac{31}{50},\frac{17}{20},1\bigr)$, $b_2=\hat b_2=0$:

- $A^{\mathrm E}$: $a_{21}=\frac12$; $a_{31}=\frac{13861}{62500}$, $a_{32}=\frac{6889}{62500}$;
  $a_{41}=-\frac{116923316275}{2393684061468}$, $a_{42}=-\frac{2731218467317}{15368042101831}$,
  $a_{43}=\frac{9408046702089}{11113171139209}$;
  $a_{51}=-\frac{451086348788}{2902428689909}$, $a_{52}=-\frac{2682348792572}{7519795681897}$,
  $a_{53}=\frac{12662868775082}{11960479115383}$, $a_{54}=\frac{3355817975965}{11060851509271}$;
  $a_{61}=\frac{647845179188}{3216320057751}$, $a_{62}=\frac{73281519250}{8382639484533}$,
  $a_{63}=\frac{552539513391}{3454668386233}$, $a_{64}=\frac{3354512671639}{8306763924573}$,
  $a_{65}=\frac{4040}{17871}$;
- $A^{\mathrm I}$ (diagonal $\frac14$ from row 2): row 2 $(\frac14,\frac14)$; row 3
  $(\frac{8611}{62500},-\frac{1743}{31250},\frac14)$; row 4
  $(\frac{5012029}{34652500},-\frac{654441}{2922500},\frac{174375}{388108},\frac14)$; row 5
  $(\frac{15267082809}{155376265600},-\frac{71443401}{120774400},\frac{730878875}{902184768},\frac{2285395}{8070912},\frac14)$;
  row 6 $=b$;
- $b=\bigl(\frac{82889}{524892},\ 0,\ \frac{15625}{83664},\ \frac{69875}{102672},\ -\frac{2260}{8211},\ \frac14\bigr)$;
- $\hat b=\bigl(\frac{4586570599}{29645900160},\ 0,\ \frac{178811875}{945068544},\ \frac{814220225}{1159782912},\ -\frac{3700637}{11593932},\ \frac{61727}{225920}\bigr)$.

Before it, Kennedy & Carpenter show that a five-stage, stage-order-2, stiffly accurate,
L-stable ESDIRK of order 4 needs $24\gamma^4-96\gamma^3+72\gamma^2-16\gamma+1=0$, whose only
L-stable root gives $c_2=2\gamma\approx1.1456$ and a minimum principal error
$\mathcal A^{(5)}=0.03855$, "approximately 15 times greater than SDIRK4"; a five-stage 4(2)
pair built anyway has $\mathcal A^{(5)}=0.07664$. For six stages, I-stability requires
$0.24799\le\gamma\le0.67604$ (§5, Eqs. (50)–(51)).

**ARK5(4)8L[2]SA** (§6, Eqs. (58)–(59); App. D). Eight stages, $\gamma=\frac{41}{200}$, with
$C(3)$ on the ESDIRK from stage 3 on, $C(2)$ on both tableaux, $D(1)$ on the ERK, zero
second-column entries below row 3 in both tableaux, and $b_2=b_3=\hat b_2=\hat b_3=0$:

- $c=\bigl(0,\ \frac{41}{100},\ \frac{2935347310677}{11292855782101},\ \frac{1426016391358}{7196633302097},\ \frac{92}{100},\ \frac{24}{100},\ \frac35,\ 1\bigr)$;
- $A^{\mathrm E}$: $a_{21}=\frac{41}{100}$;
  $a_{31}=\frac{367902744464}{2072280473677}$, $a_{32}=\frac{677623207551}{8224143866563}$;
  $a_{41}=\frac{1268023523408}{10340822734521}$, $a_{43}=\frac{1029933939417}{13636558850479}$;
  $a_{51}=\frac{14463281900351}{6315353703477}$, $a_{53}=\frac{66114435211212}{5879490589093}$,
  $a_{54}=-\frac{54053170152839}{4284798021562}$;
  $a_{61}=\frac{14090043504691}{34967701212078}$, $a_{63}=\frac{15191511035443}{11219624916014}$,
  $a_{64}=-\frac{18461159152457}{12425892160975}$, $a_{65}=-\frac{281667163811}{9011619295870}$;
  $a_{71}=\frac{19230459214898}{13134317526959}$, $a_{73}=\frac{21275331358303}{2942455364971}$,
  $a_{74}=-\frac{38145345988419}{4862620318723}$, $a_{75}=a_{76}=-\frac18$;
  $a_{81}=-\frac{19977161125411}{11928030595625}$, $a_{83}=-\frac{40795976796054}{6384907823539}$,
  $a_{84}=\frac{177454434618887}{12078138498510}$, $a_{85}=\frac{782672205425}{8267701900261}$,
  $a_{86}=-\frac{69563011059811}{9646580694205}$, $a_{87}=\frac{7356628210526}{4942186776405}$;
  $a_{i2}=0$ for $i\ge4$;
- $A^{\mathrm I}$ (diagonal $\frac{41}{200}$ from row 2, $a^{\mathrm I}_{i2}=0$ for $i\ge4$):
  row 2 $(\frac{41}{200},\frac{41}{200})$;
  row 3 $(\frac{41}{400},-\frac{567603406766}{11931857230679},\frac{41}{200})$;
  row 4 $(\frac{683785636431}{9252920307686},0,-\frac{110385047103}{1367015193373},\frac{41}{200})$;
  row 5 $(\frac{3016520224154}{10081342136671},0,\frac{30586259806659}{12414158314087},-\frac{22760509404356}{11113319521817},\frac{41}{200})$;
  row 6 $(\frac{218866479029}{1489978393911},0,\frac{638256894668}{5436446318841},-\frac{1179710474555}{5321154724896},-\frac{60928119172}{8023461067671},\frac{41}{200})$;
  row 7 $(\frac{1020004230633}{5715676835656},0,\frac{25762820946817}{25263940353407},-\frac{2161375909145}{9755907335909},-\frac{211217309593}{5846859502534},-\frac{4269925059573}{7827059040749},\frac{41}{200})$;
  row 8 $=b$;
- $b=\bigl(-\frac{872700587467}{9133579230613},\ 0,\ 0,\ \frac{22348218063261}{9555858737531},\ -\frac{1143369518992}{8141816002931},\ -\frac{39379526789629}{19018526304540},\ \frac{32727382324388}{42900044865799},\ \frac{41}{200}\bigr)$;
- $\hat b=\bigl(-\frac{975461918565}{9796059967033},\ 0,\ 0,\ \frac{78070527104295}{32432590147079},\ -\frac{548382580838}{3424219808633},\ -\frac{33438840321285}{15594753105479},\ \frac{3629800801594}{4656183773603},\ \frac{4035322873751}{18575991585200}\bigr)$.

A seven-stage fifth-order pair needs $0.18391\le\gamma\le0.33414$ for L-stability, and the
authors "have been unable to find any promising solutions" (§6, Eqs. (56)–(57)); "better
5(4) pairs probably require nine-stages" (§6). The printed rationals of all three pairs
satisfy the row sums $A^{\mathrm E}\mathbf 1=A^{\mathrm I}\mathbf 1=c$ and the bicoloured order
conditions to the stated orders *(compiler check, not in the sources: exact rational
arithmetic on the App. D entries)*.

Dense output: second order for ARK3(2)4L[2]SA, second and third order for ARK4(3)6L[2]SA,
third order for ARK5(4)8L[2]SA; a fourth-order dense output for the last is not possible
(§5–6, App. D). The second-order output is chosen for extrapolation (stability of the
extrapolant), the third-order one for interpolation (§5, Tables 5–7).

## Properties

From Kennedy & Carpenter (2003, App. B–C; Table 14, $s_I$ the number of implicit stages):

| pair | $(s,s_I)$ | $\mathcal A^{(p+1)}$ | $(\lambda_{\mathrm{inv}},\lambda_{\mathrm{visc}})$ | $\mathrm{CFL}/s_I$ inviscid / viscous | $D$ | embedded $\hat R(z_{\mathrm E},-\infty)$ |
|---|---|---|---|---|---|---|
| ARK3(2)4L[2]SA | (4,3) | 0.07217 | (1.24, 0.92) | 0.413 / 0.307 | 1.038 | $-0.075-0.087z_{\mathrm E}$ |
| ARK4(3)6L[2]SA | (6,5) | 0.01224 | (2.01, 1.06) | 0.402 / 0.212 | 1.059 | $-0.150-0.040z_{\mathrm E}$ |
| ARK5(4)8L[2]SA | (8,7) | 0.006988 | (0.43, 0.67) | 0.061 / 0.096 | 14.69 | $+0.200+0.286z_{\mathrm E}$ |

All three main methods are A-stable with $R(z_{\mathrm E},-\infty)=0$ and stiffly accurate;
the embedded methods are A-stable but not stiffly accurate (App. C). The §6 text gives
$(0.43,0.96)$ for ARK5(4)8L[2]SA; see Qualifications. For comparison, App. B lists
Ascher (2,3,3) with $\mathcal A^{(4)}=0.2064$ and $R(z_{\mathrm E},-\infty)=-0.732(1+z_{\mathrm E})$,
Ascher (3,4,3) with $R(z_{\mathrm E},-\infty)=0.106z_{\mathrm E}$, and Calvo's LIRK4 with
$\mathcal A^{(5)}=0.03919$ and $D=14.17$. [Ascher et al. (1997)](/sources/ascher-1997.md)
(§2.5–2.8) call the implicit parts of their (2,3,2), (2,2,2), (3,4,3) and (4,4,3) pairs
L-stable and rate the pairs on an advection–diffusion test equation
([IMEX Runge–Kutta](/methods/imex-runge-kutta.md)).

**Quadratic invariants.** An additive method conserves linear invariants only with
$b^{\mathrm E}=b^{\mathrm I}$, and certain quadratic ones only if in addition
$\mathcal M_{ij}=b_ia^{\mathrm I}_{ij}+b_ja^{\mathrm E}_{ji}-b_ib_j=0$
(page-local matrix; the paper writes $M^{[E,I]}$, and the registry reserves $M$ for the mass matrix) (§2.1.6, §3.1.3, Eqs. (20), (32)). None of the
three pairs makes it vanish; its printed norm is 1.203, 0.6684, 13.443 (App. B).

**Internal stability.** The ESDIRK stage values have
$R^{(i)}_{\mathrm{int}}(-\infty)=+1,-1,-0.806$ (stages 1–3 of ARK3(2)4L[2]SA),
$+1,-1,-0.774,-0.083,-0.157$ (ARK4(3)6L[2]SA) and
$+1,-1,-0.732,-0.649,+0.856,-0.967,-0.353$ (ARK5(4)8L[2]SA), all of modulus at most 1,
against $-2.464$ and $-4.909$ at the last internal stage of Griepentrog's three- and
four-stage methods (Tables 10, 12); see [internal stability](/definitions/internal-stability.md).

## Tests

Kennedy & Carpenter test on Kaps' problem, the [Van der Pol oscillator](/benchmarks/van-der-pol-oscillator.md),
Pareschi and Russo's problem and a one-dimensional Mach-5 hydrogen–oxygen reacting shock
(§7), comparing 37 existing and new IMEX additive pairs and the IMEX-BDF schemes SBDF2–4 (§8).

- **Stiffness leakage.** Kennedy & Carpenter define it as stiffness that "would leak out of
  the stiff terms and stiffen the nonstiff terms", seen as a maximum stable Courant number
  that falls as the reaction stiffness $\varepsilon^{-1}$ grows; it is "catastrophic" when the
  step falls in direct proportion to the stiffness (§8.1). With equilibrium initial data the
  new pairs show little leakage, while Zhong's ASIRK-3A, Yoh's SIRK-3A, LSSIRK-3A and
  LSSIRK-4A and Shen's ASIRK-3A fall from 0.36–0.57 to 0.0 as the stiffness grows by $10^6$
  (Table 8, whose columns are headed $\varepsilon=10^0,10^2,10^4,10^6$, while Tables 9, 11 and 13
  head theirs $\varepsilon=10^0$ and negative powers of ten). With nonequilibrium initial data and exothermic chemistry
  all additive pairs leak at fixed step (ARK3(2)4L[2]SA 0.57 at $\varepsilon=1$ to 0.001 at
  $10^{-7}$; ARK4(3)6L[2]SA 0.67 to 0.001), while SBDF2/3/4 show insignificant leakage
  (Tables 11, 13); with step-size control the three new pairs pass the transient (§8.1).
- **Accuracy and efficiency.** On the reacting-shock problem ARK3(2)4L[2]SA and Ascher et
  al.'s (2,3,3) are the most efficient third-order pairs (Fig. 2), and "ARK4(3)6L[2]SA would
  appear to be the most efficient high-order IMEX additive Runge-Kutta method of which we are
  aware for this problem" (§8.2, Fig. 3). The fifth-order result is called "disappointing"
  (§9). SBDF3 and SBDF4 are slightly more efficient but have no error estimate or step-size
  control (§8.2, §9); see [IMEX linear multistep methods](/methods/imex-linear-multistep-methods.md).
- **Order reduction.** On Kaps', Van der Pol and Pareschi–Russo problems every additive
  pair of classical order above 2 loses order at intermediate stiffness $\varepsilon\approx h$,
  while the SBDF schemes do not (§8.3a, Figs. 8–12). Empirical error forms for
  $\varepsilon\le\mathrm{const}\cdot h$ (Table 15):

  | pair | ESDIRK alone, differential / algebraic | IMEX, differential / algebraic |
  |---|---|---|
  | ARK3(2)4L[2]SA | $h^3+\varepsilon h^3$ / $h^3+\varepsilon h^2$ | $h^3+\varepsilon h^2$ / $h^2+\varepsilon h$ |
  | ARK4(3)6L[2]SA | $h^4+\varepsilon h^3$ / $h^4+\varepsilon h^2$ | $h^4+\varepsilon h^2$ / $h^3+\varepsilon h$ |
  | ARK5(4)8L[2]SA | $h^4+\varepsilon h^3$ / $h^4+\varepsilon h^2$ | $h^4+\varepsilon h^2$ / $h^3+\varepsilon h$ |

  Stage order 2 "does not translate into higher order-of-accuracy for the differential
  variables for any of the IMEX schemes"; ARK5(4)8L[2]SA behaves like a fourth-order scheme
  under stiffness, which the authors leave unexplained, and "no attempt is made to
  theoretically predict the form of the global error of IMEX ARK$_2$ methods" (§8.3a). See
  [order reduction](/definitions/order-reduction.md).
- **Step-size control.** Among I, PI, PID and predictive (PC) controllers, PC is ineffective,
  I marginal, and PI and PID guide the integration through the Van der Pol boundary layers
  and the chemical equilibration, PID best (§8.4). The chosen gains $k_I=0.25$, $k_P=0.14$,
  $k_D=0.10$ give exponents $0.49/\hat p$, $0.34/\hat p$, $0.10/\hat p$ on the three most recent
  error estimates (§3.2.3, Eqs. (41)–(43)); see [step-size control](/methods/step-size-control.md).
- **Stage predictors.** Extrapolating the previous step's dense output to the new stage
  times as Newton starting values gives a uniform speedup for $\varepsilon=1$ to $10^{-6}$
  (§3.2.2, §8.5, Table 16); see [implicit stage solvers](/methods/implicit-stage-solvers.md).

## Later use in the sources

ARKODE ships the three pairs and a later ARK4(3)7L[2]SA1 of Kennedy & Carpenter, which is not
in the 2003 paper; the ESDIRK of ARK5(4)8L[2]SA is ARKODE's default fifth-order DIRK
(Reynolds et al. 2023, §2.2). The third-order pair is the IMEX scheme of
[Orlando & Bonaventura (2025)](/sources/orlando-2025.md) (Table 1) and
[Orlando et al. (2025b)](/sources/orlando-2025-b.md) (Table 21), both attributing it to
Kennedy and Carpenter. Their diagonal $\gamma=\frac{1767732205903}{4055673282236}$ and
abscissae $c=(0,2\gamma,\frac35,1)$ are those of App. D; for the sign of $a^{\mathrm I}_{32}$,
printed without the minus in Orlando & Bonaventura's Table 1, see
[IMEX Runge–Kutta](/methods/imex-runge-kutta.md) (Qualifications): with the App. D entries
and a plus sign row 3 sums to $0.25765+0.09351+0.43587=0.78703$, the sum recorded for that
table *(compiler check, not in the sources)*.
[Biswas & Ketcheson (2023)](/sources/biswas-2023-b.md) (§6) relax ARK3(2)4L[2]SA and
ARK4(3)6L[2]SA for the energy of KdV, and
[Kang & Constantinescu (2022)](/sources/kang-2022.md) relax Kennedy–Carpenter ARK methods
on Burgers ([relaxation Runge–Kutta](/methods/relaxation-runge-kutta.md)).
[Roberts et al. (2021)](/sources/roberts-2021.md) (§6.2) use ARK4(3)6L[2]SA as an IMEX
baseline for [multirate GARK](/methods/multirate-gark.md) methods, and
[González-Tabernero et al. (2024)](/sources/gonzaleztabernero-2024.md) as a fourth-order
integrator in boundary-treatment tests
([Runge–Kutta stage boundary treatment](/methods/runge-kutta-stage-boundary-treatment.md)).

## Qualifications

- **Printed stability limits of ARK5(4)8L[2]SA.** The §6 text prints
  $(\lambda,\lambda_v)=(0.43,0.96)$, App. B $(0.43,0.67)$; Table 14 gives a viscous
  $\mathrm{CFL}/s_I=0.096$ with $s_I=7$, and $0.67/7=0.096$ while $0.96/7=0.137$ *(compiler
  check, not in the sources)*. The paper's $(\lambda,\lambda_v)$ are
  $(\lambda_{\mathrm{inv}},\lambda_{\mathrm{visc}})$ here. The table above uses the App. B value.
- **Normalization of the controller exponents.** The I controller is written with exponent
  $1/(\hat p+1)$, the PI, PID and PC controllers with $1/\hat p$, $\hat p$ the embedded order
  (Eqs. (39)–(42)). Comparisons of gain triples across sources depend on this choice.
- **Scope of the tests.** The leakage and efficiency rankings come from one reacting-shock
  problem at fixed Courant number and three small singular-perturbation problems (§7–8), and
  the controller ranking from two problems (§8.4).
- An ESDIRK with stage order 2 cannot be algebraically stable, which the paper states citing
  Spijker without proof (§3).

# Citations

- [Kennedy & Carpenter (2003)](/sources/kennedy-2003.md) — NASA/TM-2001-211038: §2.1.2 (Tables 1–4), §2.1.3 (Eqs. (7)–(11)), §2.1.6 (Eq. (20)), §3 (Eqs. (24)–(25)), §3.1.2 (Eqs. (26)–(31)), §3.1.3 (Eqs. (32)–(33)), §3.2.2–3.2.3 (Eqs. (37)–(45)), §4 (Eqs. (47)–(49)), §5 (Eqs. (50)–(55)), §6 (Eqs. (56)–(59)), §7, §8.1–8.5 (Tables 8–16, Figs. 2–13), §9, App. B–D.
- [Ascher et al. (1997)](/sources/ascher-1997.md) — §2.7 (the cubic $6x^3-18x^2+9x-1=0$ for the ARS(3,4,3) diagonal).
- [Reynolds et al. (2023)](/sources/reynolds-2023.md) — §2.2 (ARKODE default tables).
- [Orlando & Bonaventura (2025)](/sources/orlando-2025.md) — Table 1.
- [Orlando et al. (2025b)](/sources/orlando-2025-b.md) — Table 21.
- [Biswas & Ketcheson (2023)](/sources/biswas-2023-b.md) — §6.
- [Kang & Constantinescu (2022)](/sources/kang-2022.md) — §3.2.
- [Roberts et al. (2021)](/sources/roberts-2021.md) — §6.2.
- [González-Tabernero et al. (2024)](/sources/gonzaleztabernero-2024.md) — 1D convective heat test with ARK4(3)6L[2]SA.
