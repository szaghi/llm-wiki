---
type: Benchmark
title: "Turbulent channel flow"
description: "Pressure-driven flow between two parallel walls, periodic in the wall-parallel directions: DNS at Re_τ 100 to 800 (including rough walls, thermally perfect gases and MHD), wall-resolved, implicit and very coarse LES at 180 to 2000, wall-modelled and immersed-boundary LES and a priori wall-model tests at Re_τ 544 to 10¹⁰, hybrid RANS/LES to 20,000, high-order RANS, and compressible channels."
status: established
aliases: [plane channel flow, channel flow, half-channel flow, compressible channel flow, minimal channel, rough-wall channel, MHD channel, Hartmann flow, curved-wall channel bump]
tags: [benchmark, wall-model, wmles, hybrid-rans-les, boundary-layer, dns, data-driven, compressible, immersed-boundary, rans, spectral-element, mhd, lattice-boltzmann, gpu]
timestamp: 2026-10-29T16:01:00Z
---

# Turbulent channel flow

Plane channel flow is the flow between two parallel walls a distance $2\delta$
apart, driven by a mean pressure gradient (or an equivalent body force) and
periodic in the streamwise ($x$) and spanwise ($z$) directions; $y$ is
wall-normal. It is statistically stationary and homogeneous in $x$, $z$ and
time, so the mean velocity $\langle u\rangle(y)$ and the Reynolds stresses
$R_{ij}(y)$ converge from plane and time averages, and DNS exists up to high
friction Reynolds number $Re_\tau=u_\tau\delta/\nu_w$. The **half-channel**
variant simulates $0\le y\le\delta$ with a symmetry condition at $y=\delta$.
The compressible variant adds an energy source and isothermal walls, giving
wall heat flux. In this bundle the channel is the calibration and sanity
check for wall models, the first test of hybrid RANS/LES, the wall-bounded
a posteriori test of subgrid models, the validation case of new DNS
discretizations, and a source of a priori data for subgrid and RANS
closures.

## Configurations in the sources

| Source | Purpose | $Re_\tau$ | Domain ($x\times y\times z$) | Grid |
|---|---|---|---|---|
| [Flad & Gassner (2017)](/sources/flad-2017.md), §6.2, App. E | DG LES | 590 | $2\pi\times2\times\pi$ | $8^3$ elements, $N=7$; $\Delta x^+\approx58$, $\Delta z^+\approx29$, $\Delta y^+$ from 7 to 28 |
| [Agrawal et al. (2022)](/sources/agrawal-2022.md), §V, §VII.D | a priori SGS test; WMLES | 395, 2000 (a priori); 4200 (WMLES) | $2\pi\delta\times2\delta\times\pi\delta$ | $128\times40\times64$, uniform, $\Delta^+\approx200$ |
| [Lozano-Durán et al. (2022)](/sources/lozanoduran-2022.md), §IV.B, App. B | WMLES error calibration | 4200 | not printed | isotropic Voronoi, $\Delta/\delta=1/3$ to $1/160$ |
| [Fowler et al. (2022)](/sources/fowler-2022.md), §5 | WMLES of a new wall model | $10^3$ to $5\times10^5$ | $8\pi\times2\times3\pi$ (units $\delta$) | $128\times30\times48$; $\Delta x^+=\Delta z^+=196$, $\Delta y^+=67$ at $Re_\tau=1000$ |
| [Vadrot et al. (2023b)](/sources/vadrot-2023-b.md), §II–III | half-channel WMLES of learned wall models | 180 to $10^{10}$ (eleven values) | $2\pi\delta\times\delta\times2\pi\delta$ | $24^3$, $32^3$, $48^3$, $72^3$ |
| [Haering et al. (2022)](/sources/haering-2022.md), §III B, §V A | a priori filtering; hybrid RANS/LES | 1000 (a priori); about 5200; 20,000 | $8\pi\delta\times2\delta\times3\pi\delta$ | $N_y=110$; $\Delta x^+$ from 701 to 1552 |
| [Griffin et al. (2023)](/sources/griffin-2023.md), §4 | compressible WMLES | 319 to 1842 | $\pi\delta\times2\delta\times(\pi\sqrt3/4)\delta$ | 12 points per half-height (9 to 48 in grid studies) |
| [Cao et al. (2022)](/sources/cao-2022.md), §3.3, Tables 5–7 | DNS with a gas-kinetic scheme | 180 (176.0 and 179.2 obtained) | $2\pi\delta\times2\delta\times\pi\delta$ | $96^3$ and $128^3$, tanh-stretched in $y$; $\Delta x^+=11.77$, 8.83; $\Delta z^+=5.89$, 4.42; $\Delta y^+_{\min}=0.29$, 0.21 |
| [Prakash et al. (2022)](/sources/prakash-2022.md), §III.B.3, Tables 3–4 | wall-resolved LES of structural SGS models | 590 | $2\pi\delta\times2\delta\times\pi\delta$ | trilinear finite elements, $48\times111\times48$ ($\Delta x^+=78$, $\Delta z^+=39$) and $64\times133\times64$ ($\Delta x^+=58$, $\Delta z^+=29$), first point at $\Delta y^+=1$ |
| [Gillyns et al. (2022)](/sources/gillyns-2022.md), §§5–9 | spectral-element WMLES | 1000, 5200 | $2\pi\delta\times2\delta\times\pi\delta$ | $N=7$; $22\times16$ elements in $x$, $z$ ($0.286\delta$, $0.196\delta$ per element) with 4 to 6 elements per half-height at 1000; 20 and 10 elements per half-height at 5200 |
| [Bae & Koumoutsakos (2022)](/sources/bae-2022.md), Methods, Table 1 | in-solver training and testing of RL wall models | 2000, 4200, 8000 (training); 5200 to $10^6$ (testing) | $2\pi\delta\times2\delta\times\pi\delta$ | $\Delta x=\Delta z=0.05\delta$; $\Delta y=0.05\delta$, refined to $0.025\delta$ and $0.01\delta$ in two test cases |
| [Kim et al. (2022)](/sources/kim-2022.md), Tables I–III | in-solver training of a reinforcement-learning SGS model | 180, 360 (training); 720 (testing) | $4\pi\times2\times2\pi$, $2\pi\times2\times\pi$, $\pi\times2\times0.5\pi$ (units $\delta$) | LES $32\times49\times32$ ($\Delta x^+=70.7$, $\Delta z^+=35.3$) and $24\times49\times24$ (94.2, 47.1) at 180; $32\times65\times32$ at 360; $32\times97\times32$ at 720 |
| [Blind et al. (2023)](/sources/blind-2023.md), §3, Tables 1–4 | residual-based grid adaptation of DG LES | 550, 2000 (wall-resolved); 2000 (wall-modelled) | $10\delta\times2\delta\times3\delta$ | DGSEM $N=5$, from $10\times2\times3$ elements to 16,200 elements ($3.5\times10^6$ DOF) at 550 and 142,662 elements ($3.1\times10^7$ DOF) with 2-to-1 mortars at 2000 |
| [Carlsson et al. (2023)](/sources/carlsson-2023.md), §4.3, Table 2 | SST-IDDES with low-dissipation schemes | 395, 2400, 18,000 (bulk Mach 0.15); 500, 1015, 5000 (bulk Mach 1.5) | $2\pi\delta\times2\delta\times\pi\delta$ | $64\times N_y\times64$ with $N_y$ from 75 to 132, first point at $y^+\approx0.5$, stretching 1.14; $\Delta x^+$ from 40 to 1795; one $128\times118\times128$ grid at 1015 |
| [Zhao et al. (2023a)](/sources/zhao-2023.md), §5.2, Tables 6–9 | implicit LES with a gas-kinetic scheme | 180, 395 (Mach 0.1) | $2\pi\times2\times\pi$ (units $\delta$) | $64\times96\times64$ ($\Delta x^+=17.66$, $\Delta y^+_{\min}=0.29$); $96^3$ ($\Delta x^+=25.84$, $\Delta z^+=12.92$, $\Delta y^+_{\min}=0.58$) |
| [Wang et al. (2023b)](/sources/wang-2023-b.md), §4.2, Tables 6–7 | GPU DNS, single against double precision | 395 (Mach 0.1); bulk $Re=3000$ at bulk Mach 0.8, isothermal walls | $2\pi\times2\times\pi$ (units $\delta$) | $256\times128\times128$ and $256\times256\times128$ ($\Delta x^+=\Delta z^+=9.69$); $128^3$ and $128\times256\times128$ ($\Delta x^+=8.76$, $\Delta z^+=4.38$) |
| [Lederer et al. (2023)](/sources/lederer-2023.md), §4, Table 1 | under-resolved LES with a divergence-free mixed finite-element method | 392.24 | $2\pi\times2\times\pi$ | $6^3$, $12^3$, $16^3$ hexahedra at $N=3$ and $4^3$, $6^3$, $8^3$ at $N=6$ (43.2 to 775.7 thousand DOF); first-element height per point $\Delta y^+=3.0$ to 13.6 |
| [Kang et al. (2023)](/sources/kang-2023.md), §3.5, Tables 8, 10 | a priori and a posteriori test of a neural-network SGS model | 180 (training), 395 (testing) | $4\pi\delta\times2\delta\times\tfrac43\pi\delta$ at 180; $2\pi\delta\times2\delta\times\pi\delta$ at 395 | DNS $192^3$; LES $48^3$ ($\Delta x^+=47.2$, $\Delta z^+=15.7$ at 180), $32\times48\times32$, $64^3$ |
| [Inagaki & Kobayashi (2023)](/sources/inagaki-2023.md), §III A, App. B–C | a priori budget of the anisotropic SGS stress | 400 | $2\pi h\times2h\times\pi h$ | DNS $256\times192\times256$; filters and LES at $(\Delta x^+,\Delta z^+)=(26.2,13.1)$, $(52.4,26.2)$, $(105,52.4)$ |
| [Bernades et al. (2023)](/sources/bernades-2023.md), §4.3 | DNS of a transcritical (real-gas) channel | 100 at the cold wall | $4\pi\delta\times2\delta\times\tfrac43\pi\delta$ | $128^3$; $\Delta x^+=9.8$, $\Delta z^+=3.3$, first point $y^+=0.1$ |
| [Vadrot et al. (2023a)](/sources/vadrot-2023.md), §II–IV | half-channel WMLES of a reinforcement-learning wall model (LESGO) | trained at $10^4$; tested at 180 to $10^{10}$ (eleven values) | $2\pi\delta\times\delta\times2\pi\delta$ | $48^3$, uniform |
| [Duan & Wang (2024)](/sources/duan-2024.md), §5.3–5.4 | explicit SGS models and filter widths in flux reconstruction; wall-resolved and wall-modelled | 180 (wall-resolved); 544, 5200 (wall-modelled) | $4\pi\delta\times2\delta\times\tfrac43\pi\delta$ | 180: $100\times20\times33$ elements, $N=3$ ($\Delta x^+=\Delta z^+=5.7$, $\Delta y^+=0.68$ per point); 544 and 5200: $60\times16\times40$ elements, $N=2$ to 5 (element sizes $\Delta x^+=1088$, $\Delta y^+=650$, $\Delta z^+=544$ at 5200) |
| [Wang et al. (2024)](/sources/wang-2024.md), §3.2 | WALE LES comparing central and upwind convection | 180, bulk Mach 0.2 | $6.4\delta\times2\delta\times3.2\delta$ | $128\times66\times128$; $\Delta x^+\approx9$, $\Delta z^+\approx4.5$, first point $y^+\approx0.72$ |
| [Kim et al. (2024)](/sources/kim-2024.md), App. D | a posteriori test of a fused neural-network SGS model | 178 | $2\pi\delta\times2\delta\times\pi\delta$ | DNS $96\times97\times96$; LES $16\times49\times16$ and $12\times49\times12$ |
| [Cao et al. (2024)](/sources/cao-2024.md), §3.3, Tables 4–5 | implicit LES with a gas-kinetic scheme on curvilinear meshes; compressible, isothermal walls | about 211–221 (bulk $Re=3000$, bulk Mach 1.5) | $4\pi\delta\times2\delta\times\tfrac43\pi\delta$ | $128^3$ ($\Delta x^+=21.18$, $\Delta z^+=7.06$, $\Delta y^+_{\min}=0.50$); $160^3$ called DNS |
| [Mukha et al. (2025)](/sources/mukha-2025.md), §III, Table I | spectral-element WMLES (Nek5000, $N=7$) | about 8000 | $8\delta\times2\delta\times6\delta$ | $16\times4\times12$, $32\times8\times24$, $64\times16\times48$ elements (2, 4, 8 per $\delta$) |
| [Maejima & Kawai (2025)](/sources/maejima-2025.md), §4, Tables 1–2 | very coarse LES with a super-resolution SGS model; compressible at bulk Mach 0.1 | 1000 (training and test), 2000 (test) | $6\pi\delta\times2\delta\times2\pi\delta$ | DNS $\Delta x^+=9$, $\Delta z^+=4.5$; LESx4 $(36,18)$; LESx8 $(72,36)$ |
| [Oulghelou et al. (2025)](/sources/oulghelou-2025.md), §4.2.1 | 2D RANS training case of blended SST corrections | 1000 | — | $40\times60$, wall-refined |
| [Steinhausen et al. (2023)](/sources/steinhausen-2023.md), §2.1 | inflow of a flame–wall interaction simulation | bulk $Re=U_bH/\nu\approx2770$ on the half-width $H$ (page-local) | precursor $14H\times3H\times2H$ (periodic) | 60 million cells, wall spacing 25 µm ($y^+=0.24$) |
| [Elzaabalawy et al. (2023)](/sources/elzaabalawy-2023.md), §5.2 | high-order RANS verification | bulk $Re=2\times10^6$ and $2\times10^8$ on $\delta$ ($Re_\tau$ not printed) | periodic in $x$ | hybridizable DG, $N=3$ triangles; 60 and 120 degrees of freedom across $y$; 30 to 300 elements in the grid study |
| [Wu & Lele (2026)](/sources/wu-2026.md), §6.2 | a posteriori WMLES of neural-network SGS models | 1000 | as the Johns Hopkins database | $128\times96\times32$ (as printed), filter width 16 DNS spacings |
| [D'Ayer et al. (2026)](/sources/dayer-2026.md), §3.2 | DNS over hemispherical roughness with an immersed boundary | 400 | minimal channel, $L_x^+\approx1009$, $L_z^+\approx240$ | spectral difference $N=3$; 17 to 25 million degrees of freedom |
| [Aiello et al. (2026)](/sources/aiello-2026.md), §3.3 | compressible DNS of a thermally perfect gas (CO₂) | about 470, 630, 800 (bulk Mach 3, 4, 5 on wall sound speed) | $10\delta\times2\delta\times3\delta$ | up to $816\times356\times512$; $\Delta x^+\le9.7$, $\Delta y^+_w\le0.32$, $\Delta z^+\le4.6$ |
| [Ranjbar et al. (2026)](/sources/ranjbar-2026.md), §III.C | compressible LES with explicit modal filtering | 395 (bulk $Re=7095$, Mach 0.3) | $2\pi\delta\times2\delta\times\pi\delta$ | $14\times12\times16$ elements, $N=6$, 921,984 points, 6 inside $y^+=10$ |
| [Rickard & Kasbaoui (2026)](/sources/rickard-2026.md), §3 | a priori volume filtering for immersed-boundary WMLES | 5200 (Lee & Moser DNS) | as the DNS | filter sizes $\Delta_f^+=50$ to 300 (page-local) |
| [Zhao et al. (2021)](/sources/zhao-2021-c.md), §IV, Tables I, VIII | implicit against explicit LES with a gas-kinetic scheme, Mach 0.1 | 180, 395 | $2\pi\times2\times\pi$ (units $\delta$) | $96^3$ at 180 ($\Delta x^+=11.77$, $\Delta z^+=5.89$, $\Delta y^+_{\min}=0.29$); $96^3$ (25.84, 12.92, 0.58) and $128^3$ (19.38, 9.69, 0.43) at 395 |
| [Lv et al. (2021)](/sources/lv-2021.md), §IV A, Table I | wall model integrated in the LES discretization | 180, 2000, 50,000 | $2\pi\delta\times2\delta\times2\pi\delta$ | uniform: $32^3$, $64^3$, $128^3$ at 2000 (first cell $\Delta_1^+=125$, 63, 31); $64\times128\times64$ at 180 (2.81); $64^3$ at 50,000 ($1.6\times10^3$) |
| [Kumar & Ghosh (2022)](/sources/kumar-2022-b.md), §3.2.2, Table 4 | DNS with a bandwidth-optimized WENO scheme; supersonic, isothermal walls | 240 (centreline Mach 1.49) | $4\pi\delta\times2\delta\times\tfrac43\pi\delta$ | $192\times128\times151$ ($x$, $z$, $y$), stretched in $y$ |
| [Chen et al. (2022)](/sources/chen-2022-g.md), §4, Table 1 | residual-based VMS LES against classical LES; energy budget of the stabilization terms | 180 | $2\pi\delta\times2\delta\times\tfrac43\pi\delta$ | $32\times64\times32$ trilinear hexahedra, $\Delta y^+_{\min}=0.88$; same mesh for the finite-difference LES |
| [Hamedi & Vermeire (2022)](/sources/hamedi-2022.md), §5.1, Table 2 | flux reconstruction with and without an optimized modal filter, Mach 0.3 | 395 (bulk $Re=6800$) | $2\pi\delta\times2\delta\times\pi\delta$ | $24\times18\times18$ elements at $N=3$, $20\times15\times15$ at $N=4$, $16\times12\times12$ at $N=5$ (about 0.5 million DOF, 3/8 of the DNS resolution); $\Delta x^+\approx25$, $\Delta y^+\approx0.9$, $\Delta z^+\approx17$ |
| [Qi et al. (2022)](/sources/qi-2022-b.md), §4.1, Tables 1, 6 | a priori and a posteriori test of a quasi-dynamic $k_{\mathrm{sgs}}$-equation model; compressible, isothermal walls | 220 (bulk $Re=3000$, Mach 1.5); about 450 (bulk $Re=4880$, Mach 3.0) | $4\pi\delta\times2\delta\times\tfrac43\pi\delta$ | DNS $900\times201\times300$; LES $64\times87\times64$, $48\times65\times48$, $48\times49\times48$ ($\Delta x^+=42.2$–57.5) at Mach 1.5; $86\times97\times86$ at Mach 3.0 |
| [Xu et al. (2023)](/sources/xu-2023.md), §2.1, §4, Tables 3, 5–7 | a priori training and a posteriori test of a neural-network SGS stress and heat-flux model; compressible, isothermal walls | bulk $Re=3000$ at Mach 1.5 (training; R1M15), $Re=4880$ at Mach 3.0, $Re=7000$ at Mach 1.0, $Re=3000$ at Mach 0.2 (tests) | $4\pi\times2\times\tfrac43\pi$ (R1M15) | DNS $384\times193\times128$ ($\Delta x^+=\Delta z^+=7.13$, $\Delta y^+_w=0.30$) to $768\times385\times256$; LES $64\times65\times64$ ($\Delta x^+\approx41$–43 at R1M15, 78–81 at Mach 1.0) and $100\times101\times80$ (Mach 3.0) |
| [Diez Sanhueza et al. (2023)](/sources/sanhueza-2023.md), §2.1, Table 1 | field inversion and learned correction of a low-Reynolds-number $k$-$\varepsilon$ model, 1-D RANS | 150–950 (16 low-Mach variable-property cases), 322–1876 (9 ideal-gas cases at Mach 0.7–4, wall-based), 180–4200 (5 incompressible) | fully developed, 1-D in $y$ | RANS grid not printed; DNS from the Pecnik/Patel group, Trettel & Larsson and Jiménez & Hoyas, as cited |
| [van Noordt et al. (2022)](/sources/vannoordt-2022.md), §3.1, Tables 4–5 | immersed-boundary WMLES, Mach 0.2 | 5200 (bulk $Re=125{,}000$) | $12.8\delta\times2\delta\times4.8\delta$ | Cartesian with two refinement levels; finest 1.9M cells ($\Delta^+=270\times68\times270$) and 8.9M ($173\times41\times156$) |
| [Huang et al. (2022c)](/sources/huang-2022-c.md), §III A, Table I | wall-modelled spectral-vanishing-viscosity implicit LES (Nektar++), incompressible, body-force driven | 550, 950, 2000 | $2\pi\delta\times2\delta\times\pi\delta$ | $12\times6\times10$ elements, "polynomial order $N_p=7$" as printed ($\Delta x^+\times\Delta y_1^+\times\Delta z^+=48\times20\times29$ at 550, $175\times75\times105$ at 2000); $14\times8\times12$ elements at $N_p=6$ (550) |
| [Idelsohn et al. (2024)](/sources/idelsohn-2024.md), §2.10.1, §3.2.2 | pseudo-DNS with RVE databases on very coarse meshes | bulk $Re=1.65\times10^5$ (1-D Poiseuille), $4\times10^4$ (Couette), $1.5\times10^5$ (2-D Poiseuille); particle-laden duct at $Re=57{,}000$ | 1-D and 2-D; duct $1.5\times0.5\times0.5$ m | 4 cells (Poiseuille), 3 cells (Couette); $36\times12\times12$ cells against a $300\times150\times50$ DNS (duct) |
| [Hu et al. (2024)](/sources/hu-2024.md), §5, Table 1 | grid convergence of WMLES with an algebraic equilibrium wall model (CharLES, Vreman SGS) | 1000 (constant mass flow); 934 with a sudden spanwise pressure gradient | $2\pi\delta\times2\delta\times\pi\delta$ | isotropic, six grids per matching height: $\Delta^+=400$ to 23.5 ($h_{\mathrm{wm}}=0.2\delta$) and 200 to 11.8 ($0.1\delta$), $h_{\mathrm{wm}}$ at cell centres |
| [Vermeire (2024)](/sources/vermeire-2024.md), §4.2, Table 2 | implicit LES by flux reconstruction with entropically damped artificial compressibility (incompressible) | 395 | $2\pi\delta\times2\delta\times\pi\delta$ | one quarter and one half of the DNS degrees of freedom per direction: $32\times24\times24$ to $13\times10\times10$ elements ($N=1$–4, low) and $64\times48\times48$ to $26\times20\times20$ (medium), first solution point at $y^+=1$ |
| [Wu et al. (2024)](/sources/wu-2024.md), §3.1a, Table 2 | validation of the SATES-$\sigma$ hybrid in PHengLEI, Mach 0.15, constant mass flow | 395 ($Re_b=6153$) | $2\pi\delta\times2\delta\times\pi\delta$ | $64\times96\times64$ (first $y^+=0.6$) and $128\times120\times64$ (first $y^+=0.3$) |
| [Akbarzadeh & Borazjani (2025)](/sources/akbarzadeh-2025.md), §3.2, Table 1 | compressible LES with immersed-boundary walls, dynamic Smagorinsky, hybrid central/WENO fluxes | not printed; bulk $Re=10{,}000$ on $\delta$, Mach 0.5 and 1.5 | $2\pi\delta\times2\delta\times\pi\delta$ | $48^3$ ($\Delta x^+=73.3$, $\Delta y^+_{\min}=2.8$, $\Delta z^+=36.5$) and $240\times112\times120$ (14.6, 1.96, 14.6), wall-resolved; $24^3$ (146.4, 46.6, 73.2) with a wall model |
| [Alberti et al. (2025)](/sources/alberti-2025-b.md), §3.1, Tables 2–5 | Spalart–Allmaras DDES and IDDES in incompressible modal DG, fixed pressure gradient | 400, 5200 | $2\pi\delta\times2\delta\times\pi\delta$ | $8\times8\times8$ elements, $N=6$ ($\Delta x^+=44.9$, $\Delta z^+=22.4$, first $\Delta y^+=4.1$, scaled by $N+1$) at 400; $8\times12\times4$, $N=6$ (583.4, 583.4, 6.3) at 5200; equal-DOF meshes at $N=2$ to 6 |
| [De Cosmo et al. (2025)](/sources/decosmo-2025.md), §3.3, Tables 3–4 | implicit LES with a low-dissipation Roe scheme, unstructured second-order finite volume, isothermal walls, body force | 200 ($Re_b=3173$ on $\delta$, Mach 0.143) | $12\delta\times2\delta\times4\delta$ | about $1.2\times10^6$ cells; centreline $\Delta x^+=15$, $\Delta y^+=7.5$, $\Delta z^+=10$, first cell $y^+=0.5$ |
| [Fang et al. (2025)](/sources/fang-2025.md), §3.4, Table 6 | DNS of an MHD channel with a wall-normal field (Xcompact3d, quasi-static solver) | 150 ($Re_b=2305$); Hartmann numbers 0, 4, 6, 8 | $4\pi\delta\times2\delta\times2\pi\delta$ | $256\times129\times192$, stretched in $y$; $\Delta x^+=7.4$, first $\Delta y^+=0.83$, centre $\Delta y^+=6.6$, $\Delta z^+=4.9$ |
| [Wang et al. (2024d)](/sources/wang-2024-k.md), §III A, App. C | sharp-interface immersed-boundary WMLES in a lattice Boltzmann solver, Smagorinsky $C_s=0.16$ | 1000, 2000, 5200 | $2\pi\delta\times2\delta\times2\pi\delta$ | uniform $\Delta x=\delta/20$ ($y^+\approx50$ at 1000); $\delta/40$ and $\delta/80$ at 2000 |
| [Xiao et al. (2025)](/sources/xiao-2025.md), §4.2–4.3, Tables 3–4 | GPU LES (CaLES): wall-resolved, and WMLES grid convergence | about 544 ($Re_b=2u_b\delta/\nu=20{,}000$); about 5200 ($Re_b=250{,}000$) | $12.8\delta\times2\delta\times4.8\delta$ | WRLES $192\times128\times128$ ($\Delta x^+=36.2$, $\Delta z^+=20.4$, first $\Delta y^+=0.59$) to $576\times384\times384$ (12.1, 6.8, 0.19); WMLES 13 grids per aspect ratio $\Delta x/\Delta z=1$ and 2, from $128\times32\times48$ to $6144\times1536\times2304$ |
| [Alberti et al. (2025b)](/sources/alberti-2025-c.md), §III, Tables I–II, IV–V | implicit LES with entropy-conserving or entropy-stable modal DG and an entropy-stable wall condition | 180, 395, 590 ($M_b=0.18$); 222, 500, 1000 ($M_b=1.5$) and 450 ($M_b=3$), isothermal walls | $4\pi\times2\pi\times2$ or $2\pi\times\pi\times2$ (half-heights) | moderate: $16\times16\times8$ to $32\times32\times16$ elements, $N=8$ or 9, first $\Delta y^+$ 2–5.2; severe: $6^3$ to $12^3$ elements, $N=6$ or 8, up to 2100 times fewer degrees of freedom than the DNS |
| [Gao et al. (2025)](/sources/gao-2025.md), §III A, Tables II–III | slip-wall WMLES in a finite-difference aeroacoustics solver, wall-pressure spectra | about 2000 ($M=0.3$); 576, 1050, 2100, 5100 | $2\pi h\times2h\times\pi h$ | uniform, $63\times21\times49$ to $255\times81\times190$; sample point at $y^+=58$ to 513 |
| [Gao et al. (2025b)](/sources/gao-2025-b.md), §III A | WMLES in flux reconstruction, wall-model input at the first solution point | 2000, 5200, 10,000 | $2\pi h\times2h\times\pi h$ | $48\times24\times24$ elements, $N=2$, 3, 4; first solution point at $y^+\approx120$ at 10,000 |
| [Kokkinakis & Drikakis (2025b)](/sources/kokkinakis-2025-b.md), §VI–VII, Table II | low-Mach corrections of WENO9 implicit LES in [CNS3D](/software/cns3d.md) | about 395, bulk Mach 0.2 | $6\pi\delta\times2\delta\times\pi\delta$ (text) | $64^3$ (first cell centre at $y^+=1.5$) and $128^3$ |
| [Monteiro et al. (2026)](/sources/monteiro-2026.md), §4.3 | validation of the GPU DNS solver RHEA-X | 590 | $2\pi\delta\times2\delta\times\pi\delta$ | $384\times257\times384$; $\Delta x^+\approx9.8$, $\Delta z^+\approx5.0$ (as printed), $\Delta y^+\lesssim1$ at the wall and about 5.8 at the centre |
| [Okano & Haga (2026)](/sources/okano-2026.md), §5, Apps. A–C | cold-wall WMLES in flux reconstruction (implicit LES) with a near-wall artificial viscosity; compressible, isothermal walls, constant mass flow | DNS 1692 ($Re_b=3.4\times10^4$, $M_b=0.8$); runs at wall-to-recovery temperature ratios 0.81 to 0.1 and $Re_b$ up to $1.4\times10^5$; 451 (wall ratio 0.18, bulk velocity three times the wall sound speed) | not printed in the text (sized by the Lozano-Durán–Jiménez criterion, as cited) | $40\times30\times20$ hexahedra at $N=3$ ($1.5\times10^6$ degrees of freedom), effective spacings (cell size over solution points per direction) $0.039\delta$ in $x$ and $z$, $0.008\delta$–$0.029\delta$ in $y$; fine grid $60\times46\times30$; $h_{\mathrm{wm}}=0.1\delta$ (0.2δ at 451) |
| [Germano et al. (1991)](/sources/germano-1991.md), §III | a priori and a posteriori test of the first dynamic SGS model; transition to turbulence | not printed: $Re=U_c\delta/\nu=3300$ and 7900 (a priori DNS), 8000 (transitional), 6100 (LES after transition), $U_c$ the centreline velocity | $2\pi\delta\times2\delta\times\tfrac43\pi\delta$ (LES) | Fourier–Chebyshev, $8\times49\times8$ refined progressively to $48\times65\times64$ |

Reference DNS named by the sources: Kim, Moin & Moser at $Re_\tau=180$
(Cao et al.); Moser, Kim & Mansour at $Re_\tau=590$ (Flad & Gassner;
Prakash et al.); Lozano-Durán & Jiménez at 2000 and 4200 (Agrawal et al.;
Lozano-Durán et al.); Lee & Moser at 1000 and 5200 (Haering et al.; Fowler
et al.; Vadrot et al.; Gillyns et al.); the Johns Hopkins database at 1000
(Fowler et al.; Vadrot et al.); Trettel & Larsson for the compressible
channels (Griffin et al.). The flow is driven at constant mass flow
(Cao et al.; Prakash et al., at bulk Reynolds number
$Re_b=\langle u\rangle_b\delta/\nu=10{,}975$; Gillyns et al.; Carlsson et al.)
or at constant pressure gradient (Bae & Koumoutsakos), said per source.
Further references: Lee & Moser for the grid-adaptation runs (Blind et al.);
Moser, Kim & Mansour at 395 and Modesti & Pirozzoli for the supersonic
channels at 500 and 1015 (Carlsson et al.); the authors' own DNS at 180, 360
and 720, filtered in the homogeneous directions with a cut-off filter
(Kim et al.). Kim, Moin & Moser is also the reference at 180 of
[Chen et al. (2022)](/sources/chen-2022-g.md) and at 395 of
[Hamedi & Vermeire (2022)](/sources/hamedi-2022.md); Coleman, Kim & Moser
for the compressible channels of [Qi et al. (2022)](/sources/qi-2022-b.md)
with their own DNS; Lee & Moser at 5200 for
[van Noordt et al. (2022)](/sources/vannoordt-2022.md); and the channel of
Hoyas & Jiménez at 550 validates the incompressible-limit pressure
decomposition of the boundary layers of
[Zhang et al. (2022)](/sources/zhang-2022-b.md) (§6.2, Fig. 18a; see
[turbulent boundary layers](/benchmarks/turbulent-boundary-layer.md)).

## What the case tests

**Mean-velocity error of wall-modelled LES.** All the
[wall-modelled LES](/methods/wall-modelled-les.md) studies use the channel as
the case where the [law of the wall](/definitions/law-of-the-wall.md) holds
and any error is attributable to the LES or the wall model.
[Lozano-Durán et al. (2022)](/sources/lozanoduran-2022.md), §IV.B, Fig. 7b,
calibrate the mean-velocity error of WMLES with the
[equilibrium wall model](/methods/equilibrium-wall-model.md) and dynamic
Smagorinsky at $Re_\tau=4200$ as $e_u\approx0.08\,\Delta/\delta$ (registry
$e_q$; their $\varepsilon_u$),
with $\Delta$ the isotropic cell size of their Voronoi grids (linear convergence, the same trend for a staggered finite-difference
solver), and bound it by about 15%, the difference between DNS and an
inviscid solution. Their App. B, Figs. 23–24, documents non-monotonic
convergence for $\Delta/\delta\approx0.03$–$0.05$, which they relate to the
grid's ability to support near-wall streaks; they "still lack a satisfactory
explanation". [Agrawal et al. (2022)](/sources/agrawal-2022.md), §VII.D,
Figs. 8–10, match the wall model at the second off-wall point at
$Re_\tau=4200$ and find that their tensor-coefficient model reduces the error
of the apparent von Kármán constant against the DNS value $\kappa=0.38$ from
7% (dynamic Smagorinsky) to 5%, lowers near-wall intensities, and needs no
clipping where dynamic Smagorinsky does.
[Fowler et al. (2022)](/sources/fowler-2022.md), §5.1, find their
[LaRTE wall model](/methods/lagrangian-relaxation-towards-equilibrium-wall-model.md)
"nearly indistinguishable" from the equilibrium model in mean statistics
from $Re_\tau=10^3$ to $5\times10^5$ on one fixed grid, with a slight
log-layer undershoot at $10^3$; they attribute WMLES-to-DNS differences in
the near-wall stresses to grid and SGS model, because two wall models agree.
[Vadrot et al. (2023b)](/sources/vadrot-2023-b.md) use eleven Reynolds
numbers to test whether [machine-learning wall models](/methods/machine-learning-wall-model.md)
extrapolate: one reproduces the mean at all $Re_\tau$, one fits a log law
with $\kappa=0.32$, and a reinforcement-learning model gives a
[log-layer mismatch](/definitions/log-layer-mismatch.md) of $+2.2$ to
$-3.2$ in wall units across the range (Table III). They advocate the
channel as a sanity check every learned closure should pass (§V).

**Wall models in a high-order spectral-element code.**
[Gillyns et al. (2022)](/sources/gillyns-2022.md) implement an algebraic
equilibrium wall model (Reichardt's law with $\kappa=0.38$ and intercept
4.1, inverted for $u_\tau$) in a continuous spectral-element code with
polynomial degree $N=7$ and an approximate-deconvolution SGS model. The model
samples the velocity at the top node of the wall-adjacent element and
time-filters it; without filtering the run diverges (§5). At
$Re_\tau=1000$, moving the top of the first element from $y^+=63$ to 153
changes the normalized RMS error of the mean velocity from 0.52% to 1.09%
and that of the wall-stress ratio $u_\tau/\langle u\rangle_b$ from 0.37% to
0.87% (Table 1). The mean velocity matches DNS inside the under-resolved
first element down to $y^+\approx10$, which the authors attribute to the
spectral-element discretization without a same-mesh comparison (§7). With
the first element at $0.15\delta$, 5 elements per half-height are judged
acceptable and 4 under-resolved, because the element-interface (Gibbs)
spikes in the velocity fluctuations grow (§8, Table 2). At $Re_\tau=5200$
with 20 and 10 elements per half-height (first element top at $y^+=260$ and
520), the mean-velocity error stays below 1% and the fluctuation errors reach
9% (§9, Table 3).

[Mukha et al. (2025)](/sources/mukha-2025.md) (read in arXiv v1) run
algebraic wall-stress modelling (Spalding's law, $\kappa=0.387$,
$B=4.2$, $h_{\mathrm{wm}}=0.2\delta$) in the
[spectral-element](/methods/spectral-element-method.md) code
[Nek5000](/software/nek5000.md) at $N=7$ and $Re_\tau\approx8000$ (DNS of
Yamamoto & Tsuji), with the [Vreman model](/methods/vreman-model.md):

- With the traditional, weakly enforced Neumann condition the mean
  velocity is within 1% of DNS for $y>0.1\delta$ on all three meshes;
  second-order statistics need about 4 elements per $\delta$ in every
  direction (§III.B.1, Figs. 1–2).
- Three wall stresses differ. The modelled stress errs by 0.71%, 0.76% and
  $-0.54\%$ on the three meshes, the stress from the driving pressure
  gradient by 1.95%, 0.96% and $-3.84\%$, and the stress from the mean
  velocity gradient at the wall by 12.58%, 10.86% and 8.07% (Table II).
  Because the Neumann condition is weak, the last equals the modelled one
  only asymptotically and "should essentially be disregarded"; the authors
  call this "unique to the finite element method" (§II.C.3, §III.B.2).
- No [log-layer mismatch](/definitions/log-layer-mismatch.md) appears on
  any mesh, even where the subgrid shear stress exceeds the resolved one
  at the first off-wall node; the authors read this as contradicting the
  criterion of Brasseur & Wei, with the caveat that they checked one of
  its three conditions (§III.B.2, §III.C).
- Time-averaging the wall-model input lowers the stress error a priori
  (most of the gain by 50 time steps, $0.01\delta/u_\tau$) but gives "no
  systematic accuracy gain" a posteriori; the authors conclude that
  $h_{\mathrm{wm}}$ matters more than the averaging window, "at odds with"
  Yang et al. (§III.B.3, Figs. 4–5). They did not meet the divergence
  without time filtering that Gillyns et al. report in the same code (§II.C.1).
- Derivative jumps across element faces become spikes of the subgrid
  viscosity; the Sigma model, with its cubic near-wall decay, gives
  stronger wiggles than Vreman, and the high-pass relaxation filter alone
  "does not introduce enough damping" (§III.C, Figs. 6–8). Ensuring
  continuity of derivatives is "a missing component" of the method.
- Imposing the stress instead through a wall value of the subgrid viscosity
  with no-slip (the "viscosity-based" condition) makes the modelled and
  wall-gradient stresses equal by construction, but the stress from the
  pressure gradient errs by 38.05%, 25.73% and 15.65%, the mean velocity
  and Reynolds stresses degrade strongly, and the authors judge the attempt
  "largely unsuccessful", attributing it to the global momentum imbalance
  of the continuous-Galerkin discretization (§III.D, Table IV).

The two Nek5000 studies differ in subgrid treatment (approximate
deconvolution and time-filtered input in Gillyns et al.; Vreman, Sigma or
a stronger relaxation filter in Mukha et al.), so their statements on time
filtering are not on the same set-up.

**Reinforcement-learning wall models trained inside the solver.**
[Bae & Koumoutsakos (2022)](/sources/bae-2022.md) train
[reinforcement-learning](/methods/reinforcement-learning-closure.md) wall
models inside WMLES of the channel at $Re_\tau\approx2000$, 4200 and 8000
(matching height drawn between $0.075\delta$ and $0.15\delta$; episodes of
$2\delta/u_\tau$ started from "a previously obtained WMLES flow field" plus
noise; the reward uses the true mean wall stress), with the anisotropic
minimum-dissipation SGS model. In the a posteriori tests from $Re_\tau=5200$
to $10^6$ (runs of $300\delta/u_\tau$), the velocity-based model works only
while the matching height stays in the trained range
$150<h_{\mathrm{wm}}^+<1200$ and recovers when the wall-normal grid is
refined; the log-law-based model keeps a friction error below 5% and mean
profiles aligned with the log law ($\kappa=0.41$, $B=5.2$) at every
$h_{\mathrm{wm}}^+$ (Table 1, Figs. 3–4). The equilibrium wall model gives a
wall stress perfectly correlated with the matched velocity, the log-law-based
model a maximum correlation of about 0.3, the value the authors quote from
DNS (Figs. 6–7). See [machine-learning wall models](/methods/machine-learning-wall-model.md).

**A reinforcement-learning wall model that extrapolates in Reynolds number.**
[Vadrot et al. (2023a)](/sources/vadrot-2023.md) (read in arXiv v3)
retrain the log-law-based model of
[Bae & Koumoutsakos (2022)](/sources/bae-2022.md) in the pseudo-spectral
code [LESGO](/software/lesgo.md) at $Re_\tau=10^4$ and find that it keeps a
log-layer mismatch at large Reynolds numbers, while the low-Reynolds-number
mismatch disappears; they attribute the differences from the original to
the training Reynolds number, the reinforcement-learning settings and
possibly the solver (§II.B.2, Fig. 2). They trace the high-Reynolds-number
mismatch to the rotation, with $Re_\tau$, of the line of zero velocity
error in the plane of the two states (local inverse log-law slope and
intercept), and replace the slope state by one scaled with
$\ln h_{\mathrm{wm}}^+$, which makes that line independent of $Re_\tau$
(§II.B.3, Eq. 10, Fig. 3). Trained once at $Re_\tau=10^4$ with a reward
built on the known mean wall stress of the channel, the new model recovers
the log law up to $Re_\tau=10^{10}$ on the $48^3$ half-channel whenever the
matching height lies in the log layer; at $Re_\tau=180$ it lies above the
DNS (§III.A, Fig. 6). The agents' action range and action interval change
the mean velocity little (except for intervals above ten time steps) but
control the wall-stress fluctuations, through their ratio (§III.B, §IV,
Figs. 9–12); neither model resolves the inner or outer peak of the
streamwise velocity variance on this grid (Fig. 7). See
[reinforcement-learning closures](/methods/reinforcement-learning-closure.md)
and [log-layer mismatch](/definitions/log-layer-mismatch.md). The SGS model
of these runs is not stated.

**Explicit SGS models and filter widths in high-order wall-modelled LES.**
[Duan & Wang (2024)](/sources/duan-2024.md) add the
[Smagorinsky](/methods/smagorinsky-model.md), [WALE](/methods/wale-model.md)
and [Vreman](/methods/vreman-model.md) models to
[flux reconstruction](/methods/flux-reconstruction.md) with three filter
widths built on the cube root $h$ of the element volume: $h$,
$h/\sqrt{N+1}$ and $h/(N+1)$.

- Wall-resolved at $Re_\tau=180$ ($N=3$): no-model implicit LES agrees
  very well with DNS; Smagorinsky performs very poorly with every width,
  because of its large near-wall eddy viscosity; WALE and Vreman match the
  viscous sublayer, perform poorly in the buffer and log regions with $h$,
  and agree well over the whole layer with the two smaller widths, WALE
  slightly better (§5.3, Figs. 9–10). "The smaller the eddy viscosity is,
  the better the agreement" on this fine mesh.
- Wall-modelled at $Re_\tau=5200$ on $60\times16\times40$ elements (equilibrium
  wall model fed from the second element off the wall), the no-model run is
  unstable. With Vreman, $h$ is too dissipative and $h/(N+1)$ too little at
  every $N$ from 2 to 5, and $h/\sqrt{N+1}$ is best; WALE is best with $h$
  at $N=2$ to 4 and with $h/\sqrt{N+1}$ at $N=5$, where the trend with width
  reverses, which the authors call unexpected. The same holds at
  $Re_\tau=544$ with $N=3$ (§5.4, Figs. 11–15). The authors recommend Vreman
  with $h/\sqrt{N+1}$ for high-order wall-modelled LES (§6).
- They motivate the explicit models by the dependence of high-order
  wall-modelled LES with solution limiting on the amount of limiting, which
  they cite from earlier work at $Re_\tau=5200$: too little damping
  over-predicts the wall friction and too much under-predicts it (§1,
  Fig. 2).

See [wall-modelled LES](/methods/wall-modelled-les.md) and
[large-eddy simulation](/definitions/large-eddy-simulation.md).

**Wall-resolved LES of subgrid models.**
[Prakash et al. (2022)](/sources/prakash-2022.md), §III.B.3, Table 4, use
the channel at $Re_\tau=590$ as the wall-bounded test of the
[gradient model](/methods/gradient-model.md) with and without clipping of
its backscatter. Skin friction against DNS 0.0058 (coarse/medium mesh):
dynamic Smagorinsky 0.0047/0.0049; gradient model unclipped 0.0063/0.0063,
standard clipping 0.0047/0.0050, optimal clipping 0.0051/0.0053, dynamic
mixed 0.0053/0.0055. Optimal clipping also gives a much better mean velocity
and Reynolds shear stress than standard clipping, approaching the dynamic
mixed model, which is slightly better but needs test filtering and
homogeneous averaging. Because the a priori dissipation of the two clipping
methods is identical, the authors hypothesize that the gain comes from the
higher a priori correlation of the optimally clipped stress with the exact
one (see [scale-similarity and mixed models](/methods/scale-similarity-model.md),
[energy backscatter](/definitions/energy-backscatter.md)). The TKE peak of
the unclipped gradient model is significantly overpredicted on both meshes.

**Subgrid models trained on mean statistics.**
[Kim et al. (2022)](/sources/kim-2022.md) train a pointwise neural-network
SGS model by [reinforcement learning](/methods/reinforcement-learning-closure.md)
inside channel LES, rewarding only agreement with the filtered-DNS profiles
of the mean viscous stress and the mean resolved Reynolds shear stress. At
$Re_\tau=180$ on the $\Delta x^+=70.7$, $\Delta z^+=35.3$ grid the
tensor-output models reproduce the filtered-DNS mean velocity and Reynolds
shear stress almost exactly and improve the rms velocities, the mean SGS
shear stress and the spectra over the static [Vreman model](/methods/vreman-model.md)
($C_s=0.08$ in their notation), dynamic Smagorinsky and no-model LES; an
eddy-viscosity-output variant over-predicts the mean velocity in the buffer
and log layers, like dynamic Smagorinsky (§III C, Fig. 7). Training also
succeeds on the coarser grid and at $Re_\tau=360$. At untrained Reynolds
numbers (360 and 720 for the model trained at 180) the Reynolds shear stress
stays close to the filtered DNS while the buffer-layer slope of the mean
velocity is under-estimated; on an untrained coarser grid the model fails
(§III D, Figs. 12–13). A variant with backscatter clipped performs almost
the same (see [energy backscatter](/definitions/energy-backscatter.md)).

**Grid adaptation for DG LES.** [Blind et al. (2023)](/sources/blind-2023.md),
§3, use the channel to transfer a residual-based
[mesh-adaptation](/methods/mesh-adaptation.md) method to the DG
spectral-element code [FLEXI](/software/flexi.md) with the Vreman model. At
$Re_\tau=550$ (wall-resolved) the sequence of grids resembles the
finite-difference results of Toosi & Larsson and converges after four
iterations to a spacing of about $\Delta x^+\approx18$, $\Delta y^+\approx1$,
$\Delta z^+\approx8$ per degree of freedom at the wall, where the computed
$Re_\tau$ is 556.57; the mean velocity matches the Lee & Moser DNS on the
last grid and the Reynolds stresses one grid earlier (Table 1, Figs. 1–3).
The suggested wall-parallel spacings are larger in the viscous sublayer than
in the buffer layer, which the authors call correct. At $Re_\tau=2000$ with
2-to-1 mortar interfaces the procedure converges after five iterations
($Re_\tau=1967.37$), and the mortars save about 50% of the elements against a
structured mesh of the same near-wall spacing; the time step is unchanged,
so the saving is in processors (§3.2, Tables 2–3). In wall-modelled LES at
$Re_\tau=2000$ (Spalding's law, matching at $0.1\delta$, $h_{\mathrm{wm}}^+=200$,
Vreman constant raised to 0.11) the target spacing below
$h_{\mathrm{wm}}$ is clamped to its value at $h_{\mathrm{wm}}$; the mean
velocity agrees with DNS above $h_{\mathrm{wm}}$ after three iterations and
the stresses after four, with $\langle u'u'\rangle$ not exactly converged,
which the authors attribute to WMLES (§3.3, Figs. 10–11).

**Element-based LES.** [Flad & Gassner (2017)](/sources/flad-2017.md),
§6.2, Fig. 11, compare split-form DG LES with the dynamic Smagorinsky model
against no-model, de-aliased DG at $Re_\tau=590$; the split-form LES gives
better Reynolds-stress profiles, and both are called "acceptable".

**Validation of DNS discretizations.** [Cao et al. (2022)](/sources/cao-2022.md),
§3.3, run the first channel DNS with their
[high-order gas-kinetic scheme](/methods/high-order-gas-kinetic-scheme.md),
a finite-volume scheme, at $Re_\tau=180$ and Mach 0.1 on $96^3$ and $128^3$
stretched grids. The flow transitions from a perturbed laminar profile in
over $500\,\delta/U_c$ ($U_c$ the centreline velocity) and is averaged over
$350\,\delta/U_c$, after which the total-stress residual is below 2.6% and
1.2%. The skin friction is $7.58\times10^{-3}$ and $7.82\times10^{-3}$ on
the two grids, against $8.39\times10^{-3}$ from Dean's correlation (Table 6).
The mean velocity agrees reasonably with spectral DNS and with lattice
Boltzmann and discrete unified gas-kinetic results; the Reynolds shear
stress is closer to DNS than both near the wall, whereas the other two
methods are better for some rms profiles (Figs. 10–12). The authors still
judge their scheme better overall, and note it uses a coarser, stretched
grid where the lattice Boltzmann run needs $\Delta x^+\approx0.3$ everywhere
(§3.3). See [direct numerical simulation](/definitions/direct-numerical-simulation.md).

**A compressible channel on a curvilinear gas-kinetic grid.**
[Cao et al. (2024)](/sources/cao-2024.md) (read in arXiv v1), §3.3, run
the isothermal-wall channel at bulk Mach 1.5 and bulk $Re=3000$
($\mu\propto T^{0.7}$) with the curvilinear version of their
[high-order gas-kinetic scheme](/methods/high-order-gas-kinetic-scheme.md)
as an [implicit LES](/definitions/implicit-les.md), against the spectral
DNS of Coleman et al. and the B-spline DNS of Morinishi et al., averaged
over 800 characteristic times. Wall statistics (Table 5):

| Run | grid | $Pr$ | $Re_\tau$ | $\rho_w$ | $B_q$ |
|---|---|---|---|---|---|
| DNS, Coleman et al. | $144\times90\times60$ | 0.70 | 222 | 1.355 | $-0.049$ |
| DNS, Morinishi et al. | $120\times180\times120$ | 0.72 | 218 | — | $-0.048$ |
| constrained LES, Jiang et al. | $64\times65\times64$ | 0.70 | 218 | 1.354 | $-0.048$ |
| G1, implicit LES | $128^3$ | 0.70 | 211 | 1.355 | $-0.047$ |
| G2, G1 with half the streamwise box | $128^3$ | 0.70 | 212 | 1.363 | $-0.047$ |
| G3, unit Prandtl number | $128^3$ | 1.0 | 221 | 1.476 | $-0.045$ |
| G4, "DNS" | $160^3$ | 0.70 | 213 | 1.356 | $-0.048$ |

($B_q$ the non-dimensional wall heat flux, page-local.) G1 agrees with G4
and the reference DNS in wall quantities, mean and rms profiles and the
van Driest-transformed velocity. Halving the streamwise box barely changes
wall statistics but visibly shifts the rms density and temperature, and
the unit Prandtl number of the plain BGK model changes the mean density,
temperature and Mach profiles strongly, so the authors call both the long
box and the corrected $Pr$ "essential" (Figs. 7–9). The peak turbulent
Mach number stays below 0.25, without strong shocklets.

**Reconstruction order of an implicit-LES scheme.**
[Zhao et al. (2023a)](/sources/zhao-2023.md) (read in arXiv v1), §5.2,
run the channel with their
[high-order gas-kinetic scheme](/methods/high-order-gas-kinetic-scheme.md)
as [implicit LES](/definitions/implicit-les.md), at constant mass flux
from a perturbed Poiseuille profile (transition about $400\,\delta/U_c$,
averaging $200\,\delta/U_c$). The realized $Re_\tau$ measures the scheme's
dissipation (Tables 8–9):

| Reconstruction | $Re_\tau$ at nominal 180 | $Re_\tau$ at nominal 395 |
|---|---|---|
| DNS (Moser et al.) | 178.12 | 392.24 |
| 5th order, non-compact | 171.33 | 360.35 |
| 7th order normal, 5th tangential | 177.04 | 378.97 |
| 7th order in all directions | 178.44 | 380.45 |
| 5th order, compact | 176.27 | 377.05 |

The higher-order and compact reconstructions also bring the mean velocity,
rms profiles and Reynolds stress closer to DNS and keep more energy at high
wavenumbers in the spectra at $y^+=30$ and 180, all runs showing a
levelling-off near the cutoff that the authors attribute to the mesh
(§5.2.1–5.2.3, Figs. 8–15). The compact fifth-order scheme nearly matches
the seventh-order one at the cost of the fifth-order non-compact one (0.618
against 0.595 and 0.961 s per step, Table 7).

**Single against double precision on GPUs.**
[Wang et al. (2023b)](/sources/wang-2023-b.md) (read in arXiv v1), §4.2,
run the same family of gas-kinetic schemes on GPUs as DNS of the channel at
$Re_\tau=395$, Mach 0.1, against Moser, Kim & Mansour, and of a compressible
channel at bulk Reynolds number 3000 and bulk Mach 0.8 against the DNS of Fu
et al. Single precision halves the memory and runs 2.7 times faster on a
TITAN RTX and 1.7 times on a V100 (Table 8). Statistics averaged over
$200\,\delta/U_c$ agree between precisions, with a visible deviation of
the streamwise rms, while instantaneous rms profiles at $t=20$ and $200\,\delta/U_c$ after a common restart differ;
the authors attribute the difference to round-off of the same order as the
discretization error and conclude that single precision "may not be safe"
for DNS of time-evolving turbulence but may serve LES and RANS (Figs.
10–14).

**Exactly divergence-free high-order LES.**
[Lederer et al. (2023)](/sources/lederer-2023.md) (read in arXiv v1), §4,
compare no-model LES with upwind jump dissipation, a variational-multiscale
[WALE](/methods/wale-model.md) model and their adaptive
[high-order projection-based upwinding](/methods/high-order-projection-based-upwind-method.md)
at $Re_\tau=392.24$. The mixed method transmits the wall stress exactly, so
a constant body force drives the flow without a controller (§4). All
methods converge to DNS under refinement; the WALE model is close to no
model on the finer meshes and slightly worse on the coarsest ones. Relative
errors of the bulk Reynolds number at $N=3$ on $6^3$, $12^3$, $16^3$
elements are 13.4%, 3.1%, 1.1% without model, 16.3%, 4.7%, 2.7% with WALE
and 0.7%, 1.0%, 0.6% with the adaptive upwinding, which resolves the buffer
layer on the coarsest mesh; at $N=6$ the upwinding changes little (Table
2, Figs. 1, 4–6). The authors interpret the adaptive upwinding as "a wall
model approach for standard DG ILES" (§6).

**A neural-network mixed model in the channel.**
[Kang et al. (2023)](/sources/kang-2023.md), §3.5–3.7, train their
[neural-network SGS model](/methods/neural-network-sgs-model.md) on filtered
DNS of the channel at $Re_\tau=180$, normalizing the output by the
volume-averaged norm of the resolved stress $L_{ij}$, because the gradient
model used for isotropic turbulence has the wrong near-wall scaling. On the
trained $48^3$ grid the skin friction is 0.0092 against 0.0085 for the
filtered DNS, 0.0072 for dynamic Smagorinsky and 0.0103 without model
(Table 11); the mean velocity, rms fluctuations and Reynolds shear stress
improve over dynamic Smagorinsky, which over-predicts the mean velocity, and
the model stays better on untrained grids ($32\times48\times32$, $64^3$) and
at $Re_\tau=395$ (Figs. 25–27). A model trained only on isotropic
turbulence runs stably but under-predicts the mean velocity, which the
authors attribute to the vanishing mean off-diagonal SGS stress of the
isotropic training data; plane-wise normalization partly fixes it (§3.5–3.6).
They name the resolved-stress input as the main factor of generalization to
the channel (§3.7).

**The anisotropic part of the subgrid stress on coarse grids.**
[Inagaki & Kobayashi (2023)](/sources/inagaki-2023.md) (read in arXiv v3)
filter their DNS at $Re_\tau=400$ with a sharp cut-off in $x$ and $z$ only
and split the exact SGS stress into an eddy-viscosity part that carries the
whole local energy transfer and an anisotropic remainder that carries none.
At the medium resolution $(\Delta x^+,\Delta z^+)=(52.4,26.2)$ the remainder
is negligible in the resolved energy budget; at the coarse resolution
$(105,52.4)$ its mean shear stress is comparable to the eddy-viscosity part,
it redistributes energy productively into the spanwise resolved stress near
the wall, comparably to the pressure–strain term below $y^+=100$, with a
spectral peak at $\lambda_z^+\approx130$ that the authors relate to the
streak spacing $\lambda_z^+\sim100$ (§III–IV). An a posteriori dynamic
Smagorinsky LES at the same resolutions predicts the DNS mean velocity on the
fine and medium grids and over-predicts it on the coarse one (App. C,
Table I). See [scale-similarity models](/methods/scale-similarity-model.md),
[gradient model](/methods/gradient-model.md) and
[energy backscatter](/definitions/energy-backscatter.md).

**Very coarse LES with a super-resolution subgrid model.**
[Maejima & Kawai (2025)](/sources/maejima-2025.md) target grids so
coarse that the near-wall streaks are not resolved: LESx8,
$(\Delta x^+,\Delta z^+)\approx(72,36)$, two to three points per streak
spacing, against LESx4 at $(36,18)$, with a second-order
kinetic-energy- and entropy-preserving central scheme at bulk Mach 0.1. On
such grids the resolved field differs from filtered DNS, so a model
trained on filtered-DNS input fails. Their
[super-resolution SGS model](/methods/super-resolution-sgs-model.md) maps
the coarse field to a filtered-DNS-like field with an unpaired CycleGAN,
super-resolves it with a conditional GAN trained on filtered and full DNS
planes, and takes the subgrid stress from the sub-cell fluctuations, with a
clipping that admits backscatter down to about $-2$ times the wall
viscosity.

- With the selective mixed-scale model, LESx4 reproduces DNS well while
  LESx8 overpredicts the mean velocity (§4.1, Fig. 5); at constant body
  force LESx8 overpredicts the mass flow rate by 23%, the super-resolution
  model by 10% (§6.1).
- A posteriori the super-resolution model gives the DNS mean velocity and
  the near-wall rise of total shear stress, with the subgrid shear stress
  exceeding the resolved one for $3\lesssim y^+\lesssim10$ as in filtered
  DNS; it overpredicts the near-wall wall-normal and spanwise normal
  stresses (Figs. 22–23).
- The budgets give the mechanism: subgrid backscatter into the spanwise
  stress near the wall, redistributed by pressure–strain into the
  wall-normal one at resolved wavelengths $130\lesssim\lambda_z^+\lesssim210$,
  raises the near-wall shear stress (§6.2, Figs. 25–27). This agrees with
  the a priori finding of
  [Inagaki & Kobayashi (2023)](/sources/inagaki-2023.md) above, which the
  authors cite: productive redistribution into the spanwise resolved
  stress at coarse resolution with a peak near $\lambda_z^+\approx130$.
  Less clipping (more backscatter) brings the mean velocity closer to DNS;
  a bound of $-3$ times the wall viscosity is unstable (App. C); see
  [energy backscatter](/definitions/energy-backscatter.md).
- Trained only at $Re_\tau\approx1000$, the model works a posteriori at
  $Re_\tau\approx2000$ on a grid with the same wall-unit spacings, where
  the conventional model deviates (§7, Figs. 28–29); the authors note that
  the convolutional networks need similar wall-unit resolution in training
  and use.

**A real-gas channel as a scheme test.**
[Bernades et al. (2023)](/sources/bernades-2023.md), §4.3, Figs. 8–10, run a
DNS of nitrogen at twice the critical pressure between isothermal walls at
$0.75$ and $1.5$ times the critical temperature ($Re_\tau=100$ at the cold
wall) with their pressure-equilibrium-preserving split scheme and with the
kinetic-energy-preserving scheme that conserves total energy: the two agree
to plotting accuracy in first- and second-order statistics, and the authors
state that in the channel physical viscosity mitigates the pressure
oscillations. See [pressure-equilibrium preservation](/properties/pressure-equilibrium-preservation.md)
and [kinetic-energy preservation](/properties/kinetic-energy-preservation.md).

**Wall-modelled implicit LES on one spectral/hp mesh.**
[Huang et al. (2022c)](/sources/huang-2022-c.md) (§III, Figs. 3–9) couple an
algebraic log-law wall model, imposed as a Neumann condition, to a
[spectral-vanishing-viscosity](/methods/spectral-vanishing-viscosity.md)
[implicit LES](/definitions/implicit-les.md) in [Nektar++](/software/nektar-plus-plus.md)
and run $Re_\tau=550$, 950 and 2000 on the same $12\times6\times10$-element
mesh, with the matching height at the top of the first element ($0.224\delta$)
and the grid spacings $\Delta x\simeq0.087\delta$, $\Delta y_1\simeq0.037\delta$,
$\Delta z\simeq0.052\delta$ taken from the WMLES review of Larsson et al.
(2016), as cited. The flow is driven by a constant body force from the
balance $f_1\delta/U^2=(Re_\tau/Re_\delta)^2$ with the correlation
$Re_\delta/Re_\tau=2.5\ln Re_\tau+5$ (Eqs. 18–19; $Re_\delta$ on the
centreline velocity and $U$ the velocity scale of Eq. 18, page-local; $f_1$ the streamwise body force), run for at least
250 flow-through times before averaging over more than 45. Against the DNS
of del Álamo & Jiménez and Hoyas & Jiménez, as cited, the mean velocity is
"almost not distinguishable" at 550 and over-predicted by at most 2 % at 950
and 5.4 % at 2000; rms fluctuations and the Reynolds shear stress agree
away from the interface but show a "parabolic" error near it (Figs. 4–6).
At similar resolution the mesh with fewer, higher-order elements
($12\times6\times10$ at $N_p=7$) gives better fluctuations and shear stress
than $14\times8\times12$ at $N_p=6$ (§III E, Fig. 9), and the wall-modelled
run is "as high as seven times" cheaper than wall-resolved SVV implicit LES
at 550, with no timing data (§III A). Details on
[wall-modelled LES](/methods/wall-modelled-les.md).

**Channels resolved by a few cells: pseudo-DNS.**
[Idelsohn et al. (2024)](/sources/idelsohn-2024.md) (§2.10.1, Table 1,
Figs. 6–7) solve 1-D Poiseuille flow at $Re=1.65\times10^5$ on 4 cells and
Couette flow at $Re=4\times10^4$ on 3 cells with internal and wall DNS
databases as the only closure; the mean velocity "closely matches the DNS
solution". In 2-D Poiseuille flow at $Re=1.5\times10^5$ the predicted
friction factor is 0.014 against 0.016 from the Moody diagram. In the
particle-laden part of the paper a duct at $Re=57\,000$ on $36\times12\times12$
cells reproduces the DNS change of mean velocity and kinetic energy between
laden and unladen flow, which a static-Smagorinsky LES on the same mesh
misses (§3.2.2, Fig. 28). See
[pseudo-direct numerical simulation](/methods/pseudo-direct-numerical-simulation.md).

**The suddenly skewed channel as a three-dimensional test.** The
boundary-layer review of [Devenport & Lowe (2022)](/sources/devenport-2022.md)
(§5.4, Figs. 37–42) uses DNS of channels to which a spanwise pressure
gradient is suddenly applied as the canonical non-equilibrium
three-dimensional case: Moin et al. at $Re_\tau\approx200$ with a spanwise
to streamwise pressure-gradient ratio of 100, and Lozano-Durán et al. (2020)
at $Re_\tau\approx500$ with ratio 60, run to $t^+=432$, as cited. The
spanwise flow first grows as a laminar Stokes layer; the direction of the
shear stress then lags the direction of the mean velocity gradient by
about $60t^+$, and the shear stress magnitude drops through a deficit of
the pressure–strain source of $R_{22}$, peaking near the wall at
$t^+\approx125$ and in the outer layer at $tu_\tau/\delta\approx0.6$. In the
channel $\partial P^+/\partial x^+=1/Re_\tau$ (footnote 6; $P^+=\langle p\rangle/(\rho u_\tau^2)$ page-local), and Lozano-Durán
et al. found a shear-stress reduction of at least 5 % once the ratio
exceeds $0.03Re_\tau$, as the review cites them; the review proposes the
inner-scaled spanwise gradient instead as the parameter for boundary layers
(see [turbulent boundary layers](/benchmarks/turbulent-boundary-layer.md)).
The same kind of forcing is the test of Lozano-Durán & Bae (2023) below.
[Hu et al. (2024)](/sources/hu-2024.md) (§5, §6) use the Lozano-Durán et
al. channel at $Re_\tau=934$ with a spanwise-to-streamwise pressure-gradient
ratio of 10, run to $tu_\tau/\delta=1$, as a test of WMLES grid convergence:
on the grids of their $Re_\tau=1000$ channel, the time-integrated wall
stress converges at about $\Delta=0.08\delta$ for $h_{\mathrm{wm}}=0.2\delta$
while the $0.1\delta$ error still decreases there, the flow direction
converges from about $\Delta=0.03\delta$ and $0.015\delta$ respectively, and
both collapse better against $\Delta/h_{\mathrm{wm}}$; the streamwise r.m.s.
velocity is still converging on the two finest grids and collapses better
against $\Delta/\delta$ (Figs. 5, 11–12; errors averaged over five DNS
instants up to $tu_\tau/\delta=1.02$).

**Matching height and grid convergence of WMLES.** In the canonical
channel at $Re_\tau=1000$ (JHTDB reference) the same authors find the
wall-stress error of an algebraic [equilibrium wall model](/methods/equilibrium-wall-model.md)
plateauing from $\Delta/\delta=0.08$ for $h_{\mathrm{wm}}=0.2\delta$, with
onset near $\Delta/h_{\mathrm{wm}}\approx0.4$ for both matching heights, and
the mean velocity above $h_{\mathrm{wm}}$ converging first; the streamwise
r.m.s. error is an order of magnitude larger and not controlled by
$h_{\mathrm{wm}}$, and a spectral split shows the attached-eddy energy
grid-converged and the small-scale energy not, about 80 % of it needing
$\Delta^+\approx50$ (§6, Figs. 3, 6–8, 13–14; see
[wall-modelled LES](/methods/wall-modelled-les.md)).

**Wall models beyond the canonical channel.**
[Lozano-Durán & Bae (2023)](/sources/lozanoduran-2023.md) build their
[building-block-flow wall model](/methods/building-block-flow-wall-model.md)
on channel-type flows: laminar and turbulent channels, Poiseuille–Couette
flows under favourable and adverse pressure gradient up to separation, and
a channel at $Re_\tau=700$ to which a sudden spanwise pressure gradient 80
times the streamwise one is applied (§2.3). In the latter the learned model
keeps its own wall-stress error below 1% and predicts the drop of the
streamwise wall stress and the rotation of the wall stress, which the
equilibrium model misses by construction; in the adverse-gradient
Poiseuille–Couette flows the equilibrium model has the smaller total error
"for the wrong reasons", by error cancellation (§4.5–4.6, Figs. 11–13). A
pipe at $Re_\tau\approx40{,}000$, beyond the training range, gives total
errors of 4–12% for both models with non-monotonic grid convergence (§4.4,
Fig. 10).

**An a priori test of explicit wall models.**
[Nuca et al. (2025)](/sources/nuca-2025.md), §VI, feed the velocity
signal of a wall-resolved OpenFOAM LES at $Re_\tau\approx1000$ (the
dataset of Mukha, Rezaeiravesh & Liefvendahl as cited), averaged over a
cube of side $\delta/30$ centred at $h_{\mathrm{wm}}=0.05\delta$, to the
iterative Spalding, Reichardt and equilibrium-ODE
[wall models](/methods/equilibrium-wall-model.md) and to their explicit
closed-form approximations, with $\kappa=0.387$, $B=4.21$. The explicit
models reproduce the iterated wall stress within 0.07% (fixed-parameter
fits) and 0.7% (global fits). Used as initial guesses at relative
tolerance $10^{-4}$, they cut the mean/maximum iteration counts (Table VII):

| Model | previous-step guess | fixed-parameter explicit guess | global explicit guess |
|---|---|---|---|
| Reichardt (Newton) | 1.95 / 3 | 1.79 / 2 | 1.91 / 2 |
| Spalding (Newton) | 1.95 / 3 | 1.52 / 2 | 1.95 / 2 |
| equilibrium ODE (fixed point) | 3.27 / 6 | 1.03 / 2 | 3.9 / 4 |

The authors note that robustness is not an issue in the channel or the
zero-pressure-gradient layer, where the equilibrium models match the
physics, so tests limited to such flows probe accuracy but not robustness
(§II); their robustness test is a near-stall airfoil (see
[wall-modelled LES](/methods/wall-modelled-les.md)).

**Grid convergence of the classical compressible wall model.**
[Griffin et al. (2023)](/sources/griffin-2023.md), §4, run nine compressible
channels at bulk Mach 0.7 to 4 and dimensionless wall heat flux $-B_q$ from
0.010 to 0.19 (Table 1) with 12 points per half-height and matching at
$0.3\delta$. Their [inverse-velocity-transformation wall model](/methods/inverse-velocity-transformation-wall-model.md)
keeps wall-stress and heat-flux errors small at all heat fluxes, while the
classical model's errors grow with $-B_q$. With fixed matching height and
9, 18, 36 points per half-height ($2.0\times10^4$ to $1.3\times10^6$ control
volumes against $6.4\times10^8$ for the DNS), the classical model's
log-intercept error persists under refinement (§4.1, Fig. 13). See
[compressible velocity transformations](/definitions/compressible-velocity-transformation.md).
[Huang et al. (2022)](/sources/huang-2022.md), §4.1, and
[Cogo et al. (2022)](/sources/cogo-2022.md), §4, cite results in which the
Trettel–Larsson transformation collapses isothermal cooled-wall channels
(and pipes), while both papers find a log-intercept scatter for it in
cooled supersonic and hypersonic boundary layers (see
[turbulent boundary layers](/benchmarks/turbulent-boundary-layer.md)).

**Numerical dissipation in hybrid RANS/LES.**
[Carlsson et al. (2023)](/sources/carlsson-2023.md), §4.3, Figs. 4–6, run
SST-based improved delayed DES on wall-modelled-LES grids in an unstructured
second-order finite-volume code. With the artificial dissipation of RANS
practice, the mean velocity is correct in the RANS region but shows a
significant [log-layer mismatch](/definitions/log-layer-mismatch.md) at all
Reynolds numbers as soon as the model switches to LES; with the
[low-dissipation low-dispersion scheme](/methods/low-dissipation-low-dispersion-scheme.md)
the mean velocity and total stresses agree with DNS at $Re_\tau=395$ and
only a small mismatch remains at the RANS–LES interface ($y^+\approx200$ at
2400, $\approx2000$ at 18,000). In the supersonic channels (bulk Mach 1.5,
isothermal walls) the Trettel–Larsson-transformed profiles agree with DNS
at 500 and 1015 and with Reichardt's law, the dissipative reference scheme
over-estimates the velocity in the LES region, and the streamwise
normal-stress peak is under-predicted, improved on the grid refined in $x$
and $z$ (see [compressible velocity transformations](/definitions/compressible-velocity-transformation.md)).
The shock-capturing term of the scheme switches off by itself in the
low-speed channel.

**Hybrid RANS/LES and transition from RANS.**
[Haering et al. (2022)](/sources/haering-2022.md), §V A, run the
[active model split](/methods/active-model-split.md) method at
$Re_\tau\approx5200$ on four grids from $\Delta x^+\approx701$ to 1552
(84K to 408K times fewer cells than the DNS). The mean is nearly
grid-independent with no log-layer mismatch, and the computable unresolved fraction
$\beta_k=1-k_{\mathrm{res}}/k_{\mathrm{tot}}$ (registry §11) falls to 0.4 at
the centreline on the fine grid. Started from
RANS, the hybrid state develops in time with a transient overshoot that heals
by eight flow-throughs, and in space (a $16\pi$-long channel with a RANS
inlet) without overshoot but slowly. At $Re_\tau=20{,}000$ the mean
departs from the log law for $y^+=200$–$2000$, which the authors attribute
to the RANS base model.

**The founding tests of the dynamic procedure, through transition.**
[Germano et al. (1991)](/sources/germano-1991.md) (§III) test their
[dynamic model](/methods/dynamic-procedure.md) in channel flow, with
Reynolds numbers built on the centreline velocity $U_c$ and the
half-width $\delta$, sharp-cutoff grid and test filters in $x$ and $z$
and no test filter in $y$.

- *A priori.* They use the DNS of Kim, Moin & Moser (cited) at $Re=3300$
  and 7900 (the latter on $256\times193\times192$ points, as noted in the
  paper's reference list). The test-to-grid width ratio 2 agrees best,
  and the coefficient times the squared width follows $y^{+3}$ near the
  wall without damping functions (Figs. 1–2).
- *Transitional channel.* The DNS of Zang, Gilbert & Kleiser (cited) at
  $Re=8000$ is the reference. The LES starts from a parabolic profile
  with a two-dimensional Tollmien–Schlichting mode of 2% amplitude and a
  three-dimensional one of 0.02%, solved by a Fourier–Chebyshev
  pseudospectral method on $8\times49\times8$ points at first, refined to
  $48\times65\times64$. The peak wall stress lies within 3% of the DNS,
  closer than the Smagorinsky LES of Piomelli & Zang (cited) with van
  Driest damping and an intermittency function; a coarse DNS that resolves
  the early stages (up to $t\simeq170$) "cannot predict the drag crisis …
  and the breakdown process", as cited (Fig. 4). The rms velocities and
  the Reynolds shear stress at $t=176$, 200 and 220 agree fairly with the
  filtered DNS, with late-stage differences put down to a slightly
  different onset of transition (Figs. 5–6).
- *Fully developed flow* at $Re=6100$. The wall layer is under-resolved,
  which shows as a low wall stress and a high log-law intercept (Fig. 7b).
  The streamwise intensity peaks near $y^+=12$ and is more accurate than
  with the Smagorinsky LES above (Fig. 8). Skewness and flatness compare
  fairly with the unfiltered DNS (Fig. 9). The mean streak spacing,
  $\lambda^+=140$ ($\lambda^+$ page-local), is "somewhat larger than the
  established value of 100, which is also expected of large-eddy
  simulations".

The insensitivity of these results to the width ratio is on the
[a priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)
page.

**A priori data for closures.** [Agrawal et al. (2022)](/sources/agrawal-2022.md),
§V, Figs. 1–2, filter channel DNS at $Re_\tau=395$ and 2000 (filter width
three grid spacings) and find higher stress-tensor correlations for their
tensor-coefficient model than for dynamic Smagorinsky, mostly near the wall,
and identical dissipation correlations. [Haering et al. (2022)](/sources/haering-2022.md),
§III B, Fig. 1, box-filter DNS at $Re_\tau=1000$ (excluding $y^+<300$) to
fit $\alpha_k=\beta_k^{1.7}$ between the modelled-energy fraction
$\alpha_k=k_{\mathrm{sgs}}/k_{\mathrm{tot}}$ (registry §11) and $\beta_k$. [Fowler et al. (2022)](/sources/fowler-2022.md),
§2.3, Fig. 2, time-filter Johns Hopkins DNS at $Re_\tau=1000$ to show that
filtering at their relaxation time collapses near-wall profiles onto the law
of the wall.

**RANS calibration and identifiability.**
[Duraisamy et al. (2019)](/sources/duraisamy-2019.md), §5.1, cite channel DNS
as the first data set used to assign Bayesian posterior distributions to
RANS model parameters (Oliver & Moser 2011; Cheung et al. 2011), and a
stochastic discrepancy model for the Reynolds stress tested in channel
flow at several Reynolds numbers. [Duraisamy (2021)](/sources/duraisamy-2021.md),
§VII, Fig. 4, shows a channel case in which a model-consistent perturbation
of the anisotropy, inferred from mean-velocity data, reproduces the mean
velocity and shear stress but not the anisotropy (non-identifiability; no
Reynolds number given). See
[model-form uncertainty](/definitions/model-form-uncertainty.md) and
[field inversion and machine learning](/methods/field-inversion-machine-learning.md).

**Central against upwind convection for the kinetic-energy budget.**
[Wang et al. (2024)](/sources/wang-2024.md), §3.2, Figs. 3–4, run WALE LES
at $Re_\tau=180$ with the second-order kinetic-energy-preserving split form
KGP2 and the sixth-order optimized upwind scheme OPT6. The mean velocity is
"not significantly different" between the two; OPT6 is closer to the DNS
of Kim et al. around the Reynolds-shear-stress peak and agrees better with
the turbulent-kinetic-energy budget of Moser et al., "especially for the
dissipation term". See [kinetic-energy preservation](/properties/kinetic-energy-preservation.md)
and [numerical dissipation](/properties/numerical-dissipation.md).

**Grid generalization of a fused neural-network SGS model.**
[Kim et al. (2024)](/sources/kim-2024.md), App. D, Fig. 19, check on the
channel at $Re_\tau=178$ the fusion architecture they built for the
[circular-cylinder wake](/benchmarks/circular-cylinder-wake.md): with
grid- and test-filtered strain rates in wall units, the fused network
beats the grid-filtered network and dynamic Smagorinsky on the untrained
coarser grid ($12\times49\times12$), and matches a grid-filtered network
trained on two filtered-DNS datasets as in Park & Choi; see
[neural-network SGS models](/methods/neural-network-sgs-model.md).

**RANS training data for blended corrections.**
[Oulghelou et al. (2025)](/sources/oulghelou-2025.md), §4.2.1, include
the channel at $Re_\tau=1000$ among the training flows of their
[blend of expert corrections](/methods/turbulence-model-aggregation.md) of
$k$-$\omega$ SST, compared with the DNS of Lee & Moser. The mean absolute
error of $u^+$ is 0.44 for SST, 2.41 for the separated-flow expert (which
raises the eddy viscosity and departs from the log layer) and 8.97 for the
jet expert (which lowers it); the blend gives SST a weight "very close to
one throughout the channel height" and the SST error, 0.44 (Table 3,
Fig. 4).

**A smooth-wall reference for a canopy.** [Löhrer & Fröhlich (2025)](/sources/lohrer-2025.md),
§5.3, measure the drag of an open channel over a flexible aquatic canopy
against a smooth channel at the same bulk Reynolds number, using
$C_{f0}\approx0.0549\,Re_H^{-0.24}$, which they cite from Pope ($C_{f0}\approx0.0051$
at $Re_H=20{,}000$), and compare their profiles with the Lee & Moser DNS at
$Re_\tau=5186$; the canopy raises drag 12.4-fold.

**The channel as an inflow generator.**
[Steinhausen et al. (2023)](/sources/steinhausen-2023.md) (read in arXiv
v1), §2.1, drive a reacting V-flame that quenches at the side wall with
inflow planes from a periodic non-reacting channel ($U_b=4.4$ m/s, bulk
Reynolds number about 2770 on the half-width) and resolve the near-wall
region of the reacting domain with a 12 µm wall spacing ($y^+=0.14$) on 200 million cells; see
[inflow turbulence generation](/methods/inflow-turbulence-generation.md)
and [flamelet-based tabulated chemistry](/methods/flamelet-tabulated-chemistry.md).

**High-order RANS of the $k$-$\omega$ family.**
[Elzaabalawy et al. (2023)](/sources/elzaabalawy-2023.md), §5.2, solve the
RANS channel with the Wilcox (1998) [$k$-$\omega$ model](/methods/k-omega-model.md)
on a hybridizable DG discretization of degree $N=3$. At equal degrees of
freedom and equal first-point $y^+$ it predicts the near-wall velocity,
$k$ and $\omega$ better than a second-order finite-volume solution, and at
$Re=2\times10^6$ the whole velocity profile (Figs. 7–12). Refining from 30
to 300 elements across $y$, the convergence rates are close to $N+1$ up to
150 elements and then degrade, which the authors attribute to the wall
singularity of $\omega$, making the global rate "first-order accurate at
most"; with an algebraic mixing-length model the mean velocity converges
at the optimal rate $N+1$ (Table 2, Figs. 13–16). The wall shear computed
from the HDG auxiliary strain variable converges one order faster than
from the velocity gradient: errors fall from 1.0% to 0.025% against 6.4% to
0.13% (§5.2.1, Fig. 15).

**The $k$-$\tau$ model in spectral elements.**
[Tomboulides et al. (2025)](/sources/tomboulides-2025.md), §3.1, run the
half channel at $Re_b=125{,}000$ (bulk velocity, half-height),
$Re_\tau\approx5200$, with seven wall-normal spectral elements of growth
ratio $1/0.35$ in [Nek5000](/software/nek5000.md), at polynomial degree $N=3$, 5, 7 and 9 (their $p$)
(first-point $y^+=1.7$, 0.73, 0.39, 0.25). With the wall condition
$\tau_t=0$ of their [$k$-$\tau$ model](/methods/k-tau-model.md)
($\tau_t=1/\omega$, page-local: the turbulent time scale), velocity,
$k^+$ and $\tau_t^+$ are insensitive to the near-wall resolution and
indistinguishable under $p$-refinement except at $N=3$ (Figs. 1–2), and the
profiles match the authors' regularized $k$-$\omega$, "expected since the
$\tau$ and $\omega$ transport equations are equivalent" (Fig. 3).
Friction velocity against the DNS of Lee & Moser (Table 1):

| Model | $u_\tau$ |
|---|---|
| $k$-$\tau$ | 0.0412 |
| regularized $k$-$\omega$ | 0.0413 |
| low-Reynolds $k$-$\tau$ | 0.0414 |
| low-Reynolds regularized $k$-$\omega$ | 0.0415 |
| $k$-$\omega$ SST, OpenFOAM (104 cells across) | 0.0409 |
| DNS | 0.0415 |

The same models run a pipe at $Re_b=44{,}000$, $Re_\tau=1142$ ($N=7$,
average $y^+\approx0.8$): $u_\tau=0.0523$ ($k$-$\tau$) and 0.0528
(low-Reynolds variant) against 0.0519 in the DNS of Wu & Moin, errors below
1% and 2%; the low-Reynolds variant captures the near-wall peak of $k$,
slightly offset from the DNS (§3.2, Table 2, Figs. 5–6).

**A wall model inside the LES discretization.**
[Lv et al. (2021)](/sources/lv-2021.md), §II, §IV B 1, Figs. 5–12, drop the
separate wall-model solver of [wall-modelled LES](/methods/wall-modelled-les.md):
in the wall-adjacent cell the solution is reconstructed in a basis in which
one monomial is replaced by the log law, $\kappa^{-1}\ln((y+y_0)/y_0)$ with
$\kappa=0.41$ ($y_0$ page-local: a viscous or roughness length, whose
value is not stated), so that the LES itself computes the coefficients and
the wall stress follows from them as $\tau_w/\rho=a_w^2+\nu a_1$ ($a_w$,
$a_1$ page-local: the coefficients of the log and linear terms; $a_w$ is
identified with $u_\tau$). They run it in the DG/finite-volume solver
SUPES (third-order, P3, DG treatment of the wall cells, the
[Vreman model](/methods/vreman-model.md)) on uniform grids with no
near-wall refinement, driven by a constant body force:

- at $Re_\tau=2000$ the mean velocity "follows the DNS data closely,
  irrespective of the grid resolution" ($32^3$ to $128^3$), and the rms
  velocities and Reynolds shear stress approach the DNS of Hoyas &
  Jiménez as the grid is refined (Figs. 5–6);
- the log-term coefficient correlates with the instantaneous streamwise
  velocity at the first off-wall point, and the linear coefficient with the
  sum of the convective and pressure-gradient terms there, a
  nonequilibrium measure; the correlation persists on all three grids
  (Figs. 7–10);
- when the grid resolves the wall layer ($Re_\tau=180$, $\Delta_1^+=2.81$)
  the linear term takes over and the run follows the DNS of Kim, Moin &
  Moser into the viscous sublayer and the buffer layer, with the Reynolds
  stresses slightly off in the buffer layer (Figs. 11–12);
- the log law is captured at $Re_\tau=180$, 2000 and 50,000 (Fig. 11,
  against $\kappa=0.41$, $B=5.2$).

They claim the integrated model has "exactly 0" cost over an LES without
wall model, against 30%–40% for an ODE equilibrium model and 100%–150% for
a nonequilibrium one as reported by others (§II B 4), a structural claim
without timings. See [nonequilibrium wall model](/methods/nonequilibrium-wall-model.md)
and [law of the wall](/definitions/law-of-the-wall.md); the periodic-hill
runs of the same paper are on [periodic hill](/benchmarks/periodic-hill.md).

**Implicit against explicit LES with a gas-kinetic scheme.**
[Zhao et al. (2021)](/sources/zhao-2021-c.md) run the
[high-order gas-kinetic scheme](/methods/high-order-gas-kinetic-scheme.md)
(fifth-order WENO reconstruction with linear weights normal to the face,
two-stage fourth-order time stepping) as wall-resolved LES at $Re_\tau=180$
and 395, Mach 0.1, against the DNS of Kim, Moin & Moser and of Moser, Kim
& Mansour, with no model ([implicit LES](/definitions/implicit-les.md)) or
with four eddy-viscosity models entering the kinetic solver through an
enlarged relaxation time: the [Vreman model](/methods/vreman-model.md)
(constant 0.01 at 180, the best of a scan from 0.01 to 0.1, and 0.07 at
395), [dynamic Smagorinsky](/methods/dynamic-procedure.md) with clipping,
[WALE](/methods/wale-model.md) ($C_w=0.5$, at 180 only) and a dynamic
Clark ([gradient](/methods/gradient-model.md)) model converted to an
eddy viscosity by matching dissipation. A smooth-flow interface flux is
used at 180 and a modified flux with an upwind kinetic part at 395 (§III–IV).
The realized $Re_\tau$ (Tables V–VII):

| Run | nominal 180, $96^3$ | nominal 395, $96^3$ | nominal 395, $128^3$ |
|---|---|---|---|
| DNS | 178.12 | 392.24 | 392.24 |
| implicit LES | 177.89 | 360.35 | 376.33 |
| Vreman | 174.99 | 351.36 | 370.13 |
| dynamic Smagorinsky | 175.47 | 359.54 | 375.22 |
| WALE | 172.57 | — | — |
| dynamic Clark | 172.06 | 351.35 | 369.57 |

Implicit LES gives the highest resolved $Re_\tau$ everywhere and dynamic
Smagorinsky is the best explicit model; implicit LES is best for the
$U^+$ profile and the peaks of the rms velocities, while for the Reynolds
shear stress at 180 "the results for D-model match better with DNS,
followed by iLES" and at 395 implicit LES is best (§V.A–B, Figs. 2–13);
the spectra show no visible differences, all levelling off near the cutoff
(Figs. 14–15). Per time step on $64\times96\times64$ cells and 16 cores,
implicit LES costs 0.520 s, Vreman 0.534, WALE 0.552, dynamic Smagorinsky
0.613 and dynamic Clark 0.624 with the smooth flux, and the modified flux
about twice as much (Tables III–IV). The authors explain the ranking by
the numerical dissipation of the scheme already sufficing as subgrid
dissipation, so that an explicit model lowers the near-wall velocity
gradient and $u_\tau$; no dissipation budget is shown (Abstract, §VI). At
395 on $96^3$ the resolved $Re_\tau$ is 8.1% to 10.4% below the DNS value
392.24 *(compiler check, not in the sources)*.
These runs precede the reconstruction study of
[Zhao et al. (2023a)](/sources/zhao-2023.md) above, which uses the same
domain, flow set-up and $64\times96\times64$ and $96^3$ grids.

**A supersonic channel for shock-capturing DNS.**
[Kumar & Ghosh (2022)](/sources/kumar-2022-b.md), §3.2.2, Figs. 26–29,
validate the bandwidth-optimized [WENO scheme](/methods/weno-scheme.md)
WENO3P-LIM-5 for DNS of shock–turbulence interaction on an isothermal-wall
supersonic channel driven by a homogeneous momentum source, against the
DNS of Ghosh et al.: centreline Mach 1.49 and $Re_\tau=240$ against 1.48
and 246 (Table 4). Mean density, temperature and Mach number agree well,
the rms velocities agree, and small differences in the anisotropy are
attributed to differences in mean density. A channel of the same domain
and grid feeds the shock-train DNS on
[shock–turbulent boundary layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md).

**Wall-modelled channels in a review.**
[Bose & Park (2018)](/sources/bose-2018.md) cite the following: WMLES of the channel has
reached $Re_\tau\sim10^6$–$10^8$ (§4.1); the compilation of their Fig. 4
shows the [log-layer mismatch](/definitions/log-layer-mismatch.md) of
first-point matching in channels at $Re_\tau=4000$ (Templeton et al.) and
2000 (Lee et al.), against a boundary layer matched at the third point
(§2.1); control-based (adjoint) wall models reproduce the channel up to
$Re_\tau=20{,}000$, their computed streamwise stress correlating best with
the LES fluctuations at the second wall-normal point (§2.4); and the
$Re_\tau=4200$ DNS of Lozano-Durán & Jiménez illustrates how coarse an
outer-scaled grid is against the near-wall structures (§1, Fig. 2).

**Discretization of a thermally perfect gas.**
[Aiello et al. (2026)](/sources/aiello-2026.md) run DNS of a supersonic and
hypersonic channel of CO₂ with temperature-dependent specific heats in the
GPU code [STREAmS](/software/streams.md) (sixth-order central differences,
no shock capturing after the initial transient), isothermal walls at
298.15 K, and compare convective discretizations that share the same
[kinetic-energy-preserving](/properties/kinetic-energy-preservation.md)
mass and momentum fluxes but differ in
[entropy conservation](/properties/entropy-conservation.md) for this
equation of state. Mean velocities transformed after Trettel & Larsson
collapse on the viscous sublayer for all schemes; a narrow log region
appears for $y^*\ge40$ with $\kappa=0.41$ and $B=6.0$, the large intercept
attributed to the low semi-local $Re_\tau^*$ of 160 to 190 (§4.1, Fig. 1).
With the authors' entropy-conserving scheme as the reference (Table 3):

| Scheme | $\max$ rel. diff. of transformed $u^+$ (M3 / M4 / M5) | rel. diff. of peak $R_{11}^+$ | wall-pressure r.m.s. $p'^+_w$ |
|---|---|---|---|
| entropy-conserving for the gas (reference) | — | — | 1.97 / 2.33 / 2.57 |
| Gouasmi et al. (entropy-conserving, other pressure term) | 0.57 / 0.23 / 0.78% | 1.38 / 1.21 / 5.25% | 1.97 / 2.31 / 2.55 |
| KEEP (not entropy-conserving) | 0.23 / 1.05 / 1.98% | 0.60 / 1.59 / 10.98% | 2.89 / 3.23 / 3.55 |
| Ranocha (entropy-conserving for a calorically perfect gas; M5 only) | 0.55% | 1.32% | 2.78 |

The non-entropy-conserving schemes over-predict the pressure and density
fluctuations, which drift after long times, while both entropy-conserving
schemes stay statistically stationary over a run extended by 50% (§4.2,
Fig. 3). The Reynolds shear stress does not differ between schemes. No
external DNS is used.

**Immersed-boundary roughness in a minimal channel.**
[D'Ayer et al. (2026)](/sources/dayer-2026.md) (read in the submitted
manuscript), §3.2, validate a volume-penalization
[immersed boundary method](/methods/immersed-boundary-method.md) in the
[spectral difference](/methods/spectral-difference-method.md) code JAGUAR
on the heated channel over staggered hemispheres of Wu et al. (roughness
height $\delta/20$) at $Re_\tau=400$, cropped to a minimal channel of
$8\times3$ roughness patterns, at $N=3$. Against a body-fitted run of the
same code, a finite-volume run (AVBP, the thermal reference) and the DNS of
Wu et al. (859 million degrees of freedom): the mean velocity and
temperature agree below the minimal-channel critical height
$y^+=0.4L_z^+$ (above it all minimal-channel runs over-predict the
velocity); $R_{11}^+$ and the turbulent heat fluxes differ by at most about
5%; all minimal-channel runs over-predict $R_{22}^+$ and under-predict
$R_{33}^+$, which the authors attribute to the minimal domain (Figs.
7–10, Table 3).

**Residual-based VMS as implicit LES.**
[Chen et al. (2022)](/sources/chen-2022-g.md) treat the residual-based
[variational multiscale method](/methods/variational-multiscale-method.md)
(small scales $-\tau_{\mathrm M}$ times the momentum residual and
$-\tau_{\mathrm C}$ times the continuity residual, the stabilization
parameters of registry §11) as an
[implicit LES](/definitions/implicit-les.md) and split its contribution to
the resolved kinetic-energy budget into four terms: the SUPG-type
cross-stress term, a second cross-stress term, the "Reynolds-stress" term
and the grad-div (LSIC) term (§3, Eq. 24). On the coarse mesh, against a
second-order finite-difference LES with the
[Smagorinsky model](/methods/smagorinsky-model.md) ($C_s=0.1$) and the
[dynamic procedure](/methods/dynamic-procedure.md):

- the VMS run gives better mean velocity, r.m.s. fluctuations and Reynolds
  shear stress than both; Smagorinsky strongly under-predicts the mean
  velocity below $y/\delta=0.1$ and moves the $u'_{\mathrm{rms}}$ peak away
  from $y^+\approx15$ (§4.2, Figs. 1–2), with "very high dissipation in the
  viscous sublayer" (§5, Fig. 3);
- the total VMS dissipation is much smaller than the subgrid dissipation of
  the classical models in the inner layer and larger in the outer layer,
  and its three directional components are comparable, whereas the
  classical subgrid dissipation is mostly streamwise (Fig. 3);
- the SUPG-type and grad-div terms carry most of the dissipation, the
  Reynolds-stress term dissipates two to three orders of magnitude less,
  and the second cross-stress term is positive, energy-producing, over
  most of the channel (Figs. 4–5; see
  [energy backscatter](/definitions/energy-backscatter.md)).

Reversing the sign of that term makes every stabilization term
dissipative; this modified formulation brings the outer-layer mean velocity
and the buffer-layer $u'_{\mathrm{rms}}$ closer to the DNS than VMS and
SUPG, which the authors explain by its larger numerical diffusion on a
coarse mesh (§6.2, Figs. 7–8); see
[numerical dissipation](/properties/numerical-dissipation.md). Each
comparison uses one mesh; no refinement study is shown.

**Modal filtering of flux reconstruction.**
[Hamedi & Vermeire (2022)](/sources/hamedi-2022.md), §5.1, run the channel
as an under-resolved [flux-reconstruction](/methods/flux-reconstruction.md)
LES at about 3/8 of the DNS resolution with an
[explicit modal filter](/methods/explicit-modal-filtering.md) optimized for
stability: the $N=3$ and 4 runs are stable without the filter, the $N=5$
run only with it (§5.1). The filter lowers the velocity spectra only at
the highest modes "as by design" (Figs. 20–21); mean velocity and Reynolds
stresses agree with the DNS with "no loss in accuracy" (Figs. 23–24), and
at $N=3$ the filtered run gives more accurate r.m.s. fluctuations for
$10<y^+<40$, with the streamwise peak at $y^+\approx12$ (Fig. 25a).

**Explicit modal filtering in a compressible DG channel.**
[Ranjbar et al. (2026)](/sources/ranjbar-2026.md) (read in arXiv v1),
§III.C, run the channel at $Re_\tau=395$ and Mach 0.3 in
[HORSES3D](/software/horses3d.md) against Moser et al. (1999). The
unmodelled run over-predicts all r.m.s. velocities and keeps non-zero wall
fluctuations, from the weak imposition of the wall condition; an
[explicit modal filter](/methods/explicit-modal-filtering.md) drives them
to zero, and its self-tuning form ($c_{\mathrm{st}}=0.5$, page-local) gives the closest r.m.s.
profiles; Smagorinsky is unstable for $C_s<0.15$ and inaccurate at 0.2
(no data shown); the filter costs 0.96% to 2.5% more wall time (Fig. 15,
§III.D.3).

**Multi-filter neural-network SGS models in wall-modelled LES.**
[Wu & Lele (2026)](/sources/wu-2026.md) (read in arXiv v2), §6.2, run
networks trained on filtered isotropic and channel data of the Johns
Hopkins database, without retraining, in wall-modelled LES at
$Re_\tau=1000$ with the wall model of Bou-Zeid et al. A network trained on
box-filtered data only "completely fails" with unphysical spectra and
over-predicts $R_{11}$ and $R_{33}$, and static Smagorinsky piles energy at
high wavenumbers, while the [σ model](/methods/sigma-model.md) and the
network trained on two filter types reproduce the spectra; the latter's
mean profile "lines up very well" with the filtered DNS and its stresses
are "oftentimes" the most accurate (Figs. 15–16). See
[neural-network SGS models](/methods/neural-network-sgs-model.md).

**The channel filtered for immersed-boundary wall-modelled LES.**
[Rickard & Kasbaoui (2026)](/sources/rickard-2026.md), §3–4, volume-filter
the Lee & Moser DNS at $Re_\tau=5200$ with a compact kernel truncated by
the wall and not rescaled, with filter sizes (kernel widths, page-local)
$\Delta_f^+=50$ to 300. The filtered velocity at the wall, a slip velocity
$\boldsymbol u_{\mathrm{slip}}$, has a mean of $6.93u_\tau$ at $\Delta_f^+=50$
and $13.5u_\tau$ at 300, growing logarithmically,
fluctuations of about $1.5u_\tau$, and negligible wall-normal and
spanwise means; the subfilter stress peak grows from 0.24 to 0.57 $\tau_w$
(Figs. 6–10). Away from the wall ($y\gtrsim\Delta_f$) the filtered mean
profile collapses on the DNS. From these data they fit a Van Driest slip
model and a streamwise slip length $\ell_x^+=0.0798\,\Delta_f^{+1.5385}$ for the
cosine kernel, nearly independent of the kernel (§4–5); a posteriori
tests are left to future work. See
[immersed boundary method](/methods/immersed-boundary-method.md) and
[wall-modelled LES](/methods/wall-modelled-les.md).

**A quasi-dynamic one-equation SGS model in compressible channels.**
[Qi et al. (2022)](/sources/qi-2022-b.md) solve a transport equation for
$k_{\mathrm{sgs}}$ in which a gradient-model expansion closes every term,
its coefficient fixed locally by requiring the trace of the expanded stress
to equal $2\bar\rho k_{\mathrm{sgs}}$; a Smagorinsky coefficient is then
fixed by matching the anisotropic part of the subgrid energy flux, and the
authors describe the result as a one-equation eddy-viscosity model (§3.2,
§5; see
[gradient model](/methods/gradient-model.md),
[Smagorinsky model](/methods/smagorinsky-model.md),
[dynamic procedure](/methods/dynamic-procedure.md)). No test filter is
used.

- *A priori* (Mach 1.5 DNS filtered at $6\Delta_z$): the correlation of the
  modelled subgrid energy flux and wall-normal subgrid heat flux with the
  exact ones is "almost higher than 0.95" across the channel, against
  "much lower" for the dynamic Smagorinsky model and the dynamic
  $k_{\mathrm{sgs}}$-equation model of Chai & Mahesh (§4.1, Fig. 2); the
  coefficient inferred from each expanded term agrees with the one fixed
  by $k_{\mathrm{sgs}}$ (Fig. 4).
- *A posteriori, Mach 1.5* (Tables 2–4): $Re_\tau$ against the DNS value 220
  is 220, 221 and 218 with the new model on the three grids, 213, 208 and
  201 with dynamic Smagorinsky, 215, 210 and 208 with the dynamic
  $k_{\mathrm{sgs}}$ model; as the grid coarsens the new model keeps the van
  Driest velocity and the mean temperature closest to the DNS, which the
  authors call "scale adaptivity" (Fig. 5), and on the middle grid it gives
  the best Reynolds shear stress, turbulent heat flux and r.m.s. values
  (Figs. 6–9). The a posteriori coefficient peaks near 0.08, the dynamic
  subgrid Prandtl number near 0.8 (Fig. 10).
- *Mach 3.0* (one grid, Table 7): $Re_\tau=452$, 448 and 444 for the new,
  dynamic $k_{\mathrm{sgs}}$ and dynamic Smagorinsky models, with the new
  model "obviously better" in mean and second-order statistics against the
  DNS of Coleman et al. (Figs. 12–13); no DNS row is printed in the table.
- *Cost*: $7.22\times10^{-2}$ s per step against $7.38\times10^{-2}$ s
  (dynamic $k_{\mathrm{sgs}}$) and $4.13\times10^{-2}$ s (dynamic
  Smagorinsky) on 112 CPUs (Table 5).

**A learned SGS model for compressible channels on untrained grids.**
[Xu et al. (2023)](/sources/xu-2023.md) train a
[neural-network SGS model](/methods/neural-network-sgs-model.md) (MANA,
tensor-basis coefficients of the SGS stress and heat flux, with gradients
normalized by the local grid width) on filtered DNS of one compressible
isothermal-wall channel. The channel is that of Coleman, Kim & Moser (as
cited) at bulk $Re=3000$ and Mach 1.5, with a top-hat filter of 8 and 4
DNS spacings in $x$ and $z$. A priori, eddy-viscosity models have
correlation coefficients mostly below 0.6 and relative errors near 1.0,
while MANA exceeds 0.91 with errors below 0.4 for every component (§2.2,
§3.2). A posteriori, with sixth-order central differences, the reference is
DNS filtered to the LES grid (§4, Tables 3, 5–7):

- on an untrained grid of the training channel ($n_x=6$, $n_z=2$ DNS
  spacings per LES cell) MANA's van Driest velocity in the log region is
  "fully consistent" with the filtered DNS. The Vreman, dynamic
  Smagorinsky and WALE models give a larger transformed velocity and the
  no-model LES a slightly lower one. The eddy-viscosity and no-model runs
  over-predict the rms peaks and place them farther from the wall, while
  MANA matches the velocity and temperature fluctuations and the shear
  stress and heat flux (§4.1, Figs. 13–16);
- the eddy-viscosity models give only forward SGS energy and
  temperature-variance transfer, while MANA reproduces both signs at
  $y^+=15$, as the filtered DNS does (see
  [energy backscatter](/definitions/energy-backscatter.md)); the dynamic
  model "strongly overestimates" the mean SGS kinetic-energy flux (§4.1,
  Figs. 17–20);
- in the untrained channels at Mach 3.0 ($Re=4880$), Mach 1.0 ($Re=7000$,
  an "extremely sparse grid resolution", $\Delta x^+\approx80$) and Mach 0.2,
  MANA stays the most accurate, with slightly high buffer-layer peaks of the
  wall-normal rms velocity and the shear stress (§4.2–4.3, Figs. 21–28);
- per 1000 steps MANA costs 0.79 of dynamic Smagorinsky, against 0.26–0.29
  for the no-model, Vreman and WALE runs (Table 4).

Its first two channels have the bulk Reynolds and Mach numbers and the
domain of the two channels of Qi et al. (2022) above; neither paper refers
to the other's model.

**A variable-property channel database for data-driven RANS.**
[Diez Sanhueza et al. (2023)](/sources/sanhueza-2023.md) (§2, Tables 1–3)
assemble 30 DNS of fully developed channels as truth for
[field inversion and machine learning](/methods/field-inversion-machine-learning.md)
of the Myong–Kasagi [$k$-$\varepsilon$ model](/methods/k-epsilon-model.md)
with semi-local damping. There are 16 low-Mach channels with isothermal
walls, volumetric heating and prescribed laws of density, viscosity and
conductivity in temperature (mostly $Re_{\tau,w}=395$; 150 and 950 for some
cases), the nine ideal-gas channels of Trettel & Larsson at Mach 0.7 to 4,
and five incompressible channels at $Re_\tau=180$ to 4200. The cases are
characterized by the semi-local $Re_\tau^*$ (see
[compressible velocity transformations](/definitions/compressible-velocity-transformation.md)).
The error measure is the $L_\infty$ norm of the mean-velocity difference
from the DNS. The baseline errors reach 23.4% (case JFM.CRe$^*_\tau$, a
low-Mach case with $\rho\propto T^{-1}$, $\mu\propto T^{-0.5}$) and 11.6% at
Mach 4. In ten K-fold trials with 5–6 held-out cases each the correction
lowers almost every held-out error, e.g. 23.4% to 4.0–10.2% for the hardest
case. The exception is the incompressible $Re_\tau=4200$ channel (2.3% to
14.0%), which the authors attribute to extrapolation in $Re_\tau$ (Table 3).

**Immersed-boundary WMLES at $Re_\tau=5200$.**
[van Noordt et al. (2022)](/sources/vannoordt-2022.md), §3.1, Figs. 12–14,
use the channel to tune the dissipation of a Cartesian
[immersed boundary](/methods/immersed-boundary-method.md) WMLES (blend of
a fourth-order kinetic-energy- and entropy-preserving central flux with
third-order WENO; [WALE](/methods/wale-model.md), $C_w=0.55$;
[equilibrium wall model](/methods/equilibrium-wall-model.md) exchanging at
about $0.05\delta$). An interior upwind fraction below 0.0125 generates
significant noise, larger fractions accelerate the centreline flow and
retard the near-wall flow; the interior dissipation matters much more than
that of the cells cut by the boundary. Moving the exchange point between
3 and $4\Delta x_{\min}$, or the near sampling point between 0.5 and
$1.5\Delta x_{\min}$, has no significant effect. On refinement the
log-region deviation from DNS "has almost completely vanished" (see
[log-layer mismatch](/definitions/log-layer-mismatch.md)); the Reynolds
stresses agree with a reference WMLES but poorly with the DNS in the inner
region, especially $\langle u'u'\rangle$.

**Implicit LES with artificial compressibility.** [Vermeire (2024)](/sources/vermeire-2024.md)
(§4.2, Figs. 9–18) runs wall-resolved implicit LES of the channel at
$Re_\tau=395$ with [flux reconstruction](/methods/flux-reconstruction.md)
(Rusanov interface flux, no SGS model) and the entropically damped
artificial-compressibility form of the incompressible equations, which
needs neither a pressure Poisson solve nor pseudo-time stepping, at one
quarter and one half of the DNS degrees of freedom per direction (reference
Moser, Kim & Mansour, as cited), with $N=1$–4 and incompressibility
factors $M_{\mathrm{AC}}=1/5$ to $1/40$ (page-local, not the Mach number).
After $2760t_\delta$ of start-up and $1380t_\delta$ of averaging ($t_\delta$
the paper's time unit, as printed) $Re_\tau$ is within 1 % of the target in
all cases. $N=1$ over-predicts the mean velocity, especially towards the
centreline, and degrades as $M_{\mathrm{AC}}$ is reduced to
$1/20$; $N=2$ over-predicts less and is insensitive to it; $N=3$ agrees well
at the medium resolution and $N=4$ slightly under-predicts at both. The
r.m.s. profiles are accurate for $N=3$ and 4 at all $M_{\mathrm{AC}}$,
while $N=1$ over-predicts the streamwise and spanwise components and
under-predicts the wall-normal one near the wall. The author attributes the
higher velocities of low-order runs to damped turbulent structures that
inhibit momentum transport to the walls. Most runs at $N=5$ and 6, and the
coarse $N=4$ run at $M_{\mathrm{AC}}=1/5$, were unstable, which the author
attributes to insufficient numerical dissipation for implicit LES (§4.2;
see [implicit LES](/definitions/implicit-les.md)).

**A hybrid that runs in LES mode near the centre.** [Wu et al. (2024)](/sources/wu-2024.md)
(§3.1a, Figs. 2–4) validate their [self-adaptive turbulence eddy simulation](/methods/self-adaptive-turbulence-eddy-simulation.md)
with a $\sigma$-model-based cut-off coefficient in the structured solver
[PHengLEI](/software/phenglei.md) at $Re_\tau=395$ against Moser, Kim &
Mansour: the mean velocity agrees with the DNS, a small shift on the coarser
grid disappearing on the finer; the resolution control function is 1 (URANS
mode) near the wall and decreases away from it; the ordering
$R_{11}>R_{33}>R_{22}$ is captured, with a considerable resolved shear
stress.

**Immersed-boundary walls in a compressible LES.**
[Akbarzadeh & Borazjani (2025)](/sources/akbarzadeh-2025.md), §3.2,
Figs. 3–5, represent both walls by their sharp-interface curvilinear
[immersed boundary](/methods/immersed-boundary-method.md) and run the
channel at bulk Mach 0.5 and 1.5 against the DNS of Lee & Moser (for 0.5,
which they call "quasi-incompressible" below Mach 0.6) and of Modesti &
Pirozzoli (for 1.5), without stating which DNS Reynolds number is matched.
On the two wall-resolved grids the mean velocity agrees with the DNS; the
wall-modelled $24^3$ run "cannot follow the log-law profile" because of the
low resolution; the Reynolds stresses improve with refinement. The eddy
viscosity rises sharply from the viscous sublayer to a peak near
$y=0.05\delta$ on the fine grids, the peak moving towards $0.25\delta$ on
coarser ones; the authors attribute the coarse-grid loss of agreement to
the implicit dissipation of the third-order WENO part of their scheme (see
[numerical dissipation](/properties/numerical-dissipation.md)).

**DDES and IDDES in high-order DG.** [Alberti et al. (2025)](/sources/alberti-2025-b.md),
§3.1, Figs. 2–14, run Spalart–Allmaras-based DDES and IDDES with several
subgrid lengths in an incompressible modal discontinuous Galerkin solver,
all lengths divided by a factor $s_\Delta$ (page-local) of $N+1$, $N$ or the
cube root of the degrees of freedom per element (see
[detached-eddy simulation](/methods/detached-eddy-simulation.md)):

- at $Re_\tau=400$ ($N=6$, first cell to $y^+=28.7$) the hybrids change
  the mean velocity noticeably against an implicit LES at equal
  resolution; IDDES is best, "even surpassing an ILES carried out on a much
  finer grid", which the authors attribute to its grid-based shield; the
  DDES shield is weak there because the fine grid gives little eddy
  viscosity, and sporadic unshielded patches give slight modelled-stress
  depletion; the low-Reynolds-number correction of DDES forces an
  equivalent Smagorinsky constant of 0.2, while without it the LES branch
  runs close to implicit LES (about 0.01), and the authors recommend
  dropping the correction in this framework;
- at $Re_\tau=5200$ ($8\times12\times4$ elements, $N=6$) every variant
  agrees well with the DNS of Lee & Moser except standard IDDES, which
  shows [log-layer mismatch](/definitions/log-layer-mismatch.md), traced to
  its small wall-normal-based subgrid length in the RANS–LES transition,
  whose "staircase" variation follows the faster wall-normal growth of DG
  meshes; the authors note that their discretization is "almost five times
  coarser" in true degrees of freedom than the least refined mesh of the
  UMD wall-modelled-LES resource;
- raising $N$ on a fixed mesh lowers the eddy viscosity, moves the RANS–LES
  interface towards the wall and improves the centreline velocity; at
  equal degrees of freedom the highest $N$ is best, and $s_\Delta=N+1$ is
  the most suitable normalization across degrees.

**Implicit LES with a low-dissipation Roe scheme, and a curved-wall bump.**
[De Cosmo et al. (2025)](/sources/decosmo-2025.md), §3.3–3.4, run the
channel as wall-resolved [implicit LES](/definitions/implicit-les.md) with
their low-dissipation Roe scheme, calibrated on
[isotropic decay](/benchmarks/homogeneous-isotropic-turbulence.md), in an
unstructured second-order finite-volume code, at $Re_\tau=200$ with the
mesh and domain of Banchetti, Luchini & Quadrio, against a DNS labelled
$Re_\tau=180$:

- two-point correlations at $y^+=20$ and 200 show the $12\delta\times2\delta\times4\delta$
  domain adequate (Fig. 7);
- the centreline-to-bulk velocity ratio is 1.186, against 1.168 for the
  DNS and $1.28Re_b^{-0.0116}=1.156$ printed for Dean's correlation, "3%
  higher than the reference value"; the mean velocity agrees with the DNS,
  with $u^+$ over-estimated by 2% at $y^+=100$, which the authors read,
  like a slightly high $\langle u'u'\rangle$, as a sign of slightly too
  much numerical dissipation and an under-estimated wall stress;
  Reynolds stresses and the turbulent-kinetic-energy budget agree well,
  production peaking at $y^+\approx12$, the differences ascribed to the
  $Re_\tau$ mismatch and the isothermal walls (Figs. 8–10);
- a channel whose lower wall carries an asymmetric bump of two Gaussians
  (the geometry of Banchetti et al., height $0.0837\delta$ at
  $x=4.14\delta$), fed by the periodic channel, gives the wall $C_p$ and
  $C_f$ of the DNS with a 6% over-estimate of the suction peak and a 4%
  over-estimate of the skin-friction peak, which is about three times the
  flat-wall value; the flow does not separate; the Reynolds stresses at
  $x/\delta=0$, 3 and 10, compared with an OpenFOAM LES with a one-equation
  [subgrid kinetic-energy model](/methods/subgrid-kinetic-energy-equation-model.md),
  are slightly low in $\langle v'v'\rangle$ and $\langle w'w'\rangle$,
  which the authors attribute to dissipation from mesh non-orthogonality and
  streamwise non-uniformity (Figs. 13–16).

This bump is a different flow from the Boeing
[Gaussian bump](/benchmarks/gaussian-bump.md): it sits in a fully
developed channel at low Reynolds number and does not separate.

**A magnetohydrodynamic channel: Hartmann flow and relaminarization.**
[Fang et al. (2025)](/sources/fang-2025.md), §3.3–3.4, validate the MHD
module of [Xcompact3d](/software/xcompact3d.md) on channels under a
wall-normal magnetic field, with the quasi-static (electric-potential)
solver. The laminar two-dimensional Hartmann flow at $Re_b=2800$ and
Hartmann numbers $Ha=1$, 5 and 10 ($Ha$ the Hartmann number, registry
§11, printed as $\sqrt{Re\,N_{\mathrm{St}}}$ with the Stuart number
$N_{\mathrm{St}}=\sigma B_0^2L/(\rho_0U)$, registry §11) agrees "perfectly" with the analytical profile, the
centreline velocity falling and the skin friction rising with the field at
fixed bulk velocity (Figs. 10–11). In the turbulent channel at
$Re_\tau=150$:

- without field, the mean velocity agrees with the law of the wall,
  Eckelmann's experiment and the DNS of Moser et al. (printed at
  $Re_\tau=178$), the Reynolds-stress differences from the latter vanishing
  in inner/outer scaling;
- with the field the log layer lifts, as in drag-reducing flows, and
  shrinks as $Ha$ rises, slightly higher than the THTLab data in wall units
  but in agreement in bulk scaling; the Reynolds stresses fall with $Ha$,
  agreeing with the THTLab data at $Ha=4$ and 6;
- at $Ha=8$ all Reynolds stresses vanish and the mean profile collapses on
  the laminar one: the flow relaminarizes, its streaks and hairpins
  suppressed (Figs. 12–15).

The statistics are taken between $90{,}000$ and $120{,}000\,\delta/u_b$
after a non-MHD start. See also
[direct numerical simulation](/definitions/direct-numerical-simulation.md).

**Diffused against sharp immersed interfaces in lattice Boltzmann WMLES.**
[Wang et al. (2024d)](/sources/wang-2024-k.md), §III A, Figs. 2–6,
App. C, impose an [equilibrium wall model](/methods/equilibrium-wall-model.md)
through an [immersed boundary](/methods/immersed-boundary-method.md) in a
GPU [lattice Boltzmann](/methods/lattice-boltzmann-method.md) solver
(D3Q19, Smagorinsky viscosity in the relaxation time). With the
sharp-interface version on the uniform $\delta/20$ grid the mean velocity
agrees "very well" with the DNS of Lee & Moser at $Re_\tau=1000$, 2000 and
5200, while the fluctuations are under-estimated, more at lower Reynolds
number, which the authors attribute to the lattice Boltzmann dissipation
rather than to the wall model; at $Re_\tau=2000$ the energy spectra at two
probes show a $-5/3$ range, the mean velocity is already right on the
coarsest of $\delta/20$, $\delta/40$ and $\delta/80$, and the fluctuations
converge with refinement, especially near the wall. The diffused-interface
version over-estimates the friction velocity and under-estimates the
near-wall velocity, which they attribute to the extra viscosity of the
diffused interface; the multiple-relaxation-time collision gives slightly
higher velocities above $y^+=1000$, more small structures and spurious
oscillations than the recursive regularized one. Their conclusion is that
the sharp interface suits internal flows (the external cases are on
[Ahmed body](/benchmarks/ahmed-body.md) and
[circular-cylinder wake](/benchmarks/circular-cylinder-wake.md)).

**A GPU LES solver: wall-resolved runs and non-monotonic WMLES
convergence.** [Xiao et al. (2025)](/sources/xiao-2025.md) validate
[CaLES](/software/cales.md), an incompressible second-order
staggered finite-difference solver with the static
[Smagorinsky model](/methods/smagorinsky-model.md) (van Driest damping),
the [dynamic procedure](/methods/dynamic-procedure.md) and an algebraic
log-law [equilibrium wall model](/methods/equilibrium-wall-model.md)
($\kappa=0.41$, $B=5.2$, $h_{\mathrm{wm}}=0.1\delta$, instantaneous input):

- *wall-resolved*, $Re_b=20{,}000$, against Lee & Moser at
  $Re_\tau=543.5$, $C_f=0.00591$ (§4.2, Table 3, Figs. 6–8):

  | Grid | $Re_\tau$ SM / DSM | $C_f$ error SM / DSM |
  |---|---|---|
  | $192\times128\times128$ | 568.4 / 537.3 | 9.38% / −2.25% |
  | grid 2 | 567.3 / 541.6 | 8.95% / −0.69% |
  | grid 3 | 556.8 / 539.4 | 4.95% / −1.49% |
  | $576\times384\times384$ | 544.8 / 534.7 | 0.50% / −3.22% |

  The velocity profiles depend on the grid in their own wall units, mostly
  with the static model, but little in DNS wall units; the resolved shear
  stress is over-predicted with the static and under-predicted with the
  dynamic model, matching the signs of the $C_f$ errors, and the
  streamwise normal-stress peak is over-estimated;
- *wall-modelled*, $Re_b=250{,}000$, against Lee & Moser at
  $Re_\tau=5185.9$, $C_f=0.00344$ (§4.3, Table 4, Fig. 12): the skin
  friction, $\langle u'u'\rangle$ and $\langle u'v'\rangle$ converge
  non-monotonically for both subgrid models and both aspect ratios, most
  markedly $\langle u'u'\rangle$, which the authors call consistent with
  Meyers & Sagaut's findings for wall-resolved LES; aspect ratio 1 converges better
  than 2; on the finest grids (reaching $\Delta z^+\approx10$) the $C_f$
  errors are 2.43% and 0.44% (static, dynamic) at aspect ratio 1 and
  0.26% and 1.30% at 2, always positive, which the authors relate to the
  bias of mean wall stress toward larger values with instantaneous
  wall-model input. The details are on
  [wall-modelled LES](/methods/wall-modelled-les.md).

**Entropy-stable modal DG and the wall condition in implicit LES.**
[Alberti et al. (2025b)](/sources/alberti-2025-c.md) run implicit LES with
a modal DG solver carried in conservative variables whose space operators
are evaluated from the $L^2$ projection onto the entropy variables, plus a
parameter-free element-wise correction that enforces the discrete entropy
balance (DEEB); with it the Ismail–Roe flux gives an entropy-conserving
(EC) and the exact Riemann flux an entropy-stable (ES) convective
discretization, with BR2 viscous terms of penalty $\eta_F$ (see
[entropy conservation](/properties/entropy-conservation.md) and
[implicit LES](/definitions/implicit-les.md)). They prove the isothermal
no-slip wall with mirrored velocity and the exact-Riemann wall pressure
entropy stable (ESW) and the one with extrapolated pressure entropy
conserving (ECW) (§II B).

- *Moderate resolution.* At $N=8$ (or 9) on $16\times16\times8$ to
  $32\times32\times16$ elements, 9 to 200 times fewer degrees of freedom
  than the DNS, the incompressible-limit channels ($M_b=0.18$) follow
  Moser, Kim & Mansour and the compressible ones the DNS of Modesti &
  Pirozzoli and of Coleman, Kim & Moser in mean velocity, Reynolds stresses
  and temperature; at $M_b=1.5$ the centreline temperatures are 1.396,
  1.377 and 1.367 at $Re_\tau=222$, 500 and 1000 (DNS 1.387 or 1.378, 1.372,
  1.369), and the wall heat-flux coefficient converges in $N$ (Table III:
  0.0503, 0.0434, 0.039 at $N=8$, against 0.048–0.049, 0.042, 0.038). At
  $M_b=3$, $Re_\tau=450$, the profiles leave the Modesti–Pirozzoli DNS
  beyond $y^+\approx45$ in velocity, which the authors attribute to the
  power-law against Sutherland viscosity of the references (centreline
  temperature 2.467 against 2.490 with the power law and 2.570 with
  Sutherland), and are insensitive to the CFL number, to $N=8$ or 9, to the
  entropy correction and to the domain length (Figs. 1–7). Without the
  correction the baseline DG in conservative variables "is not able to run"
  the compressible cases.
- *Severe under-resolution, near-incompressible.* At $N=6$ on $8\times8\times6$
  to $12^3$ elements (65 to 261 times fewer degrees of freedom than the
  DNS), with $\eta_F=1$ inside and 8 at the wall, the EC flux with the ESW
  wall is much more accurate than the ES flux, which over-shears the
  near-wall fluctuations, overshoots the mean velocity and underestimates
  the shear stress (Figs. 9–10); the ECW wall makes the profile
  "abundantly" undershoot the DNS and the ESW wall almost coincide with it
  (Fig. 15); raising $\eta_F$ from 1 to 5 shifts the mean velocity upward
  (Figs. 13–14). The authors summarize that too much dissipation in the
  first cells shears out the turbulent stresses and the mean flow
  approaches the DNS from above, too little gives over-predicted buffer-layer
  fluctuations and an under-predicted mean velocity (§IV).
- *Severe under-resolution, compressible.* At $N=8$ on $8\times8\times6$ to
  $12^3$ elements (176 to 1412 times fewer) the ES flux is best and the EC
  flux underpredicts the velocity; at $M_b=3$ the pure EC flux crashes and
  an upwind-biased Ismail–Roe flux with relaxation 0.1 to 1 is needed,
  which also improves the coarsest runs at $Re_\tau=500$ and 1000 (up to
  2100 times fewer degrees of freedom; Figs. 16–21).

The entropy projection costs 2.5% ($N=1$) to 6.6% ($N=9$) and the
correction below 1% of the CPU time (App. A, Table VI). The authors state
that the implicit-LES behaviour of the baseline scheme "should be fully
understood before isolating any potentially beneficial effect of
physics-inspired subgrid-scale models" (§I).

**Low-Mach corrections of WENO implicit LES.**
[Kokkinakis & Drikakis (2025b)](/sources/kokkinakis-2025-b.md) run the
weakly compressible channel at $Re_\tau\simeq395$ ($Re_b\simeq6887$, bulk
Mach number 0.2, adiabatic walls) in [CNS3D](/software/cns3d.md) as
implicit LES with ninth-order WENO in primitive variables, the HLLC flux
and five-stage SSP-RK4, on a $64^3$ grid, the mean Mach number falling
toward 0.01 at the wall (Fig. 4). They compare corrections that, between
reconstruction and Riemann solver, blend the left and right reconstructed
velocities toward their average by a factor set by the local Mach number:
the original correction (LM) of Thornber et al. on the velocity magnitude
or on the face-normal Mach number, the normal-velocity-only variant of
Simmonds et al. (LMn), tangential-only variants (LMt, LMtn), and their
NEHA, which limits the normal and tangential components each with its own
Mach number (see [WENO schemes](/methods/weno-scheme.md) and
[numerical dissipation](/properties/numerical-dissipation.md)). Mean
friction Reynolds numbers (Table II; RMS in brackets):

| Run | $\overline{Re}_\tau$ |
|---|---|
| WENO9, $64^3$ | 372.5 (4) |
| WENO9 + LM on the velocity magnitude | 367 (2.91) |
| WENO9 + LM on the normal Mach number | 402.2 (2.9) |
| WENO9 + LMn | 383 (3.3) |
| WENO9 + LMt | 372 (3.5) |
| WENO9 + LMtn | 371.1 (3.2) |
| WENO9 + NEHA | 392 (2.96) |
| WENO9, $128^3$ | 391 (2.6) |
| DNS | 392.24 |

LM produces "fuzzy", dispersed vortices near mid-height, LMn and LMt
suppress them, and NEHA gives the closest Q-criterion picture to the
$128^3$ run (Fig. 6); NEHA's mean velocity aligns almost perfectly with the
DNS, while plain WENO9 departs from $y^+\approx10$ upward and LM
over-corrects (Fig. 8), and NEHA's skewness and flatness of the streamwise
velocity are closest to the DNS near the wall (Figs. 9–10). NEHA on $64^3$
is more accurate than plain WENO9 on $128^3$ for $y^+<40$, the finer mesh
being slightly better above, and costs less than 10% over WENO9 (LM about
5%) (§VIII). Tangential limiting alone barely changes $\overline{Re}_\tau$
but improves on LMn when combined with it in NEHA (§VII).

**Wall-model input and wall fluxes in flux-reconstruction WMLES.**
[Gao et al. (2025b)](/sources/gao-2025-b.md), §II C–D and §III A, place
the input of an equilibrium wall model at the first solution point of the
wall-adjacent element, closest to each wall flux point, instead of the
face between the first and second off-wall cells recommended by Frère et
al. and Shi et al., keep a no-slip condition, and blend two inviscid wall
fluxes, a weakly prescribed one, accurate but unstable on non-trivial
grids, and a weak Riemann (HLLC) one, stable but giving a too steep mean
profile, with weight $C_2\in[1/12,1/5]$ on the latter (Fig. 2; see
[wall-modelled LES](/methods/wall-modelled-les.md)). The wall law of
Allmaras, Johnson & Spalart is inverted without iteration by a piecewise
fit in $Re_y$. On $48\times24\times24$ elements with $N=2$, 3, 4, the mean
velocity follows the log law at $Re_\tau=2000$ and 10,000 (first solution
point at $y^+\approx120$ at 10,000), and at 5200 it shows none of the
oscillations in the first element of the Frère et al. and Shi et al.
results; the Reynolds stresses deviate from the DNS near the wall, which
the authors attribute to the 12 elements (48 solution points at $N=3$)
across the half-channel (Figs. 3–5).

**Cold isothermal walls as a robustness test of WMLES.**
[Okano & Haga (2026)](/sources/okano-2026.md) use the compressible channel
with isothermal walls far below the recovery temperature $T_r$ (wall
temperature $T_w$; both page-local, $T_r$ from the centreline values with
recovery factor 0.89) as the test of a stabilization of
[wall-modelled LES](/methods/wall-modelled-les.md) in
[flux reconstruction](/methods/flux-reconstruction.md). The flow is driven
by a controlled momentum source holding the mass flow (gains 2 and $-0.2$
on the current and previous mass-flow errors) and an energy source
relaxing the bulk temperature over $0.3\delta/u_\tau$; without the latter
the bulk temperature falls through heat loss at the cold wall, as they
also cite from Mettu & Subbareddy (§5.1, Eqs. 17–20). Statistics are
averaged over 20 "flow through times", each defined in the paper by
$tu_\tau/\delta=1$. Results (§5, Tables 3–4, Apps. A–C):

- at $T_w/T_r=0.81$, $M_b=0.8$, $Re_b=3.4\times10^4$, the DNS of Yao &
  Hussain (as cited) gives $Re_\tau=1692$, $C_f\times10^3=4.47$ and wall
  heat-flux parameter $B_q\times10^2=1.13$ ($B_q=-q_w/(c_pu_\tau T_w\rho_w)$,
  page-local; with this sign their cooled-wall values are positive, whereas
  [Griffin et al. (2023)](/sources/griffin-2023.md) define $B_q$ without the
  minus sign, negative for cooled walls, and
  [Cao et al. (2024)](/sources/cao-2024.md) above print negative values); their near-wall artificial viscosity gives 1677, 4.69,
  1.09 and the earlier wall-normal [modal filter](/methods/explicit-modal-filtering.md)
  1676, 4.69, 1.09;
- at $T_w/T_r=0.4$, 0.2, 0.1 there is no reference; the filtered runs blow
  up at 0.2 and 0.1, and $u^+$ and the Reynolds shear stress in wall units
  rise as the wall is cooled, which the authors attribute to the smaller
  $u_\tau$ used for normalization (no compressible transformation applied;
  §5.2, Fig. 10);
- at $T_w/T_r=0.1$ refining from $40\times30\times20$ to $60\times46\times30$
  cells changes $C_f\times10^3$ from 4.02 to 4.00 and leaves
  $B_q\times10=1.35$, which the authors take to show that the grid
  criterion of Fukushima & Haga (as cited), derived for adiabatic walls,
  still holds (App. B, Tables B.7–B.8);
- in the Mach-3 cold-wall channel of Coleman et al. (as cited; the
  conditions of [Qi et al. (2022)](/sources/qi-2022-b.md) above,
  $T_w/T_r=0.18$) they obtain $Re_\tau=441$ and $B_q=0.142$ against 451 and
  0.137 (App. C, Table C.10).

The streamwise normal stress above $h_{\mathrm{wm}}$ hardly changes from
$Re_b=3.4\times10^4$ to $1.4\times10^5$, which the authors explain, citing
Maeyama & Kawai, by the inner-layer origin of its outer-layer growth,
unresolved in WMLES (§5.3, Fig. 12; see
[Maeyama & Kawai (2023)](/sources/maeyama-2023.md)).

**Slip-wall WMLES and wall-pressure spectra.**
[Gao et al. (2025)](/sources/gao-2025.md), §III A, run a compressible
channel at $M=0.3$ with a [slip-wall model](/methods/slip-wall-model.md)
in a high-order aeroacoustics finite-difference code (seven-point DRP
scheme, Vreman model, selective filter), the equilibrium wall model fed at
the second off-wall point. At $Re_\tau\approx2000$ on four uniform grids
from $(\delta/\Delta x,\delta/\Delta y,\delta/\Delta z)=(10,10,15)$ to
$(40,40,60)$, the mean velocity agrees with the DNS of Hoyas & Jiménez on
all grids and follows the log law for sample points from $y^+=55$ to 220,
"effectively circumventing" the
[log-layer mismatch](/definitions/log-layer-mismatch.md) (Fig. 5); the
Reynolds stresses deviate for $y/\delta<0.1$ on every grid and agree for
$y/\delta>0.2$ on the two middle grids (Fig. 6); the wall-pressure spectrum
on $(20,30,30)$ agrees with Farabee & Casarella over
$10\le\omega\delta/u_\tau\le300$, the coarsest grid over-predicting with a
premature roll-off, and the authors recommend $(20,20\text{–}30,30)$ points
per $\delta$, with spectral errors of 3–6 dB at low to mid frequency (Fig.
7). The same resolution reproduces the log law and the outer stresses at
$Re_\tau=576$, 1050, 2100 and 5100, with spectra consistently high at low
to mid frequency and too steep beyond $\omega\delta/u_\tau=500$, within
about 4 dB at 576 and 2100 and 5 dB at 1050; at $Re_\tau=1000$ their
$127\times41\times95$ grid agrees better with the DNS spectra than an
OpenFOAM WMLES on $127\times101\times127$ (Figs. 8–11). Their boundary
layer is on [turbulent boundary layers](/benchmarks/turbulent-boundary-layer.md).

**A GPU DNS solver.** [Monteiro et al. (2026)](/sources/monteiro-2026.md),
§4.3, validate RHEA-X, a second-order kinetic-energy-preserving
finite-difference compressible solver (see
[kinetic-energy preservation](/properties/kinetic-energy-preservation.md)),
at $Re_\tau=590$ in the low-Mach limit with constant transport properties
and a body force with feedback control: the mean velocity and the rms
velocities agree with Moser et al., the streamwise normal stress peaking at
$y^+\approx14$ (Fig. 4). The averaging time is not printed.

**Cited data-driven uses.** The review of [Fang et al. (2026)](/sources/fang-2026.md),
§3.4, cites an LSTM trained on channel DNS at "Re = 180" that predicts the
central shear Reynolds stress within 5% against about 12% for the
$k$-$\varepsilon$ model, and reinforcement-learning blowing and suction
giving up to 35.6% friction-drag reduction at "Re = 1000", without
defining either Reynolds number. [Witherden et al. (2025)](/sources/witherden-2025.md),
§4, list channel flow among the applications of [PyFR](/software/pyfr.md).

**One-dimensional turbulence in the channel.** The review of
[Chen et al. (2024b)](/sources/chen-2024-c.md) (§3.1–3.3, Figs. 11, 13–16)
collects channel results of [one-dimensional turbulence](/methods/one-dimensional-turbulence.md):
ODT as a near-wall closure of LES (Schmidt et al. 2003) validated against
DNS for $Re_\tau$ from 395 to 10 000 (mean velocity, Reynolds stresses and
the budget of the streamwise stress at $Re_\tau=590$); ODTLES with an
implicit–explicit time scheme agreeing with DNS up to $Re_\tau=2040$ on a
single-board computer (Glawe et al.); ODTLES of a no-slip channel, a channel
with a free-slip wall, a lid-driven cavity and a square duct (Gonzalez-Juez
et al. 2011); and the authors' conservative compressible ODT, whose mean
velocity in supersonic channels agrees with DNS in the viscous sublayer,
buffer and log layers (Chen et al. 2022, as reproduced; parameters not
given in the review). All are reproduced figures of the cited works.

**The channel in the history of turbulence simulation.** In the account
of [Kim & Leonard (2024)](/sources/kim-2024-b.md) (§2.5, §3.1, §3.4, §4.5,
§4.7–4.8) the channel is where LES and DNS met walls: Deardorff's (1970) LES
with 6,720 grid points and a log-law wall condition, Schumann's (1975) with
up to 65 K volumes, an SGS energy equation and wall conditions, the first
LES with the wall region computed (Moin et al. 1978), and the Moin & Kim
(1982) LES with Van Driest-like damping of the Smagorinsky model, which
removed the excessive near-wall dissipation and reached a statistically
steady state. Kim, Moin & Moser (1987) aimed at $Re_\tau=194$, the oil-channel
experiment of Kreplin & Eckelmann, and obtained $Re_\tau=180$, "a standard
reference point" since; their near-wall disagreement with the experiment
was traced to an experimental error (heat conduction near the wall),
confirmed by new measurements, which the authors call "probably the first
incident in which a numerical simulation prompted a reexamination of the
experimental data". They add that the curved-channel DNS of Moser & Moin
(1984, 1987) "preceded Kim et al. (1987), and it was probably the first DNS
of a wall-bounded turbulent flow"; that Kim et al. switched from
second-order Adams–Bashforth to third-order Runge–Kutta after publication
while "many investigators still use" the former; that the minimal channel
(Jiménez & Moin 1991) isolated a near-wall flow unit; and that Coleman et
al. (1995) ran the first supersonic channel DNS (all as cited).

**The channel in data-driven RANS.** The review of
[Sandberg & Zhao (2022)](/sources/sandberg-2022-b.md), §2.1, notes that
even in the channel the [Boussinesq hypothesis](/definitions/boussinesq-hypothesis.md)
is invalid near the wall because of Reynolds-stress anisotropy, yet the
mean flow is usually obtained with traditional models on a fine enough
near-wall grid. The review also cites results in which an eddy viscosity
learned inside the RANS iterations on channel data improved less on the
[periodic hill](/benchmarks/periodic-hill.md) than non-linear approaches
(Liu et al., §3.4), and a heat-flux network was tested on channels at
several Reynolds numbers (Sotgiu et al., §4.2.2).

## Qualifications

- [Wu & Lele (2026)](/sources/wu-2026.md) write $z$ wall-normal;
  [Rickard & Kasbaoui (2026)](/sources/rickard-2026.md) write $\delta_f$
  for the kernel width, written $\Delta_f$ here (page-local, as on
  [immersed boundary methods](/methods/immersed-boundary-method.md)),
  since $\Delta$ alone is the registry's LES filter width. [Aiello et al.
  (2026)](/sources/aiello-2026.md) print the sample spacing as
  "$\Delta t_s=1.5U_b/h$", which has the dimension of an inverse time
  *(compiler check, not in the sources)*; they measure all differences
  against their own entropy-conserving scheme, with no external DNS. [D'Ayer et al.
  (2026)](/sources/dayer-2026.md) print $L_x^+\approx1009$, while eight
  patterns of length $\sqrt3$ times four roughness heights of $\delta/20$
  give $L_x=2.77\delta$, i.e. $L_x^+\approx1109$ at $Re_\tau=400$
  *(compiler check, not in the sources)*.
- [Vadrot et al. (2023a)](/sources/vadrot-2023.md) report a large-$Re_\tau$
  log-layer mismatch of the log-law model of
  [Bae & Koumoutsakos (2022)](/sources/bae-2022.md) after retraining it in
  another solver at another Reynolds number, whereas Bae & Koumoutsakos
  report friction errors below 5% from $Re_\tau=5200$ to $10^6$ in their
  own solver. Vadrot et al. attribute the difference to the training
  Reynolds number, the learning settings and possibly the solver
  (§II.B.2). Their Eq. 12, presented as a rewriting of Eq. 2,
  prints $B$ where Eq. 2 with their roughness length gives $\kappa B$, and
  omits the square *(compiler check, not in the sources)*. They write $z$
  wall-normal; this page uses $y$.
- [Duan & Wang (2024)](/sources/duan-2024.md) set the eddy viscosity
  constant in each element and the interface SGS fluxes to zero; their
  filter-width recommendation is obtained with these choices. Their
  Fig. 10 legend reads "P2" for the $N=3$ case at $Re_\tau=180$.
- [Kim et al. (2024)](/sources/kim-2024.md) give the training grid of the
  channel as $16\times97\times16$ in one sentence and $16\times49\times16$
  in the next and in the Fig. 19 caption.
- [Steinhausen et al. (2023)](/sources/steinhausen-2023.md) give $y^+=0.24$
  for 25 µm and $y^+=0.14$ for 12 µm, which imply viscous lengths of about
  104 and 86 µm for flows fed by the same channel; the paper does not say
  where $y^+$ is evaluated *(compiler check, not in the sources)*.

- [Vadrot et al. (2023b)](/sources/vadrot-2023-b.md) write $z$ for the
  wall-normal coordinate; the table above translates their half-channel to
  $y$ wall-normal.
- [Fowler et al. (2022)](/sources/fowler-2022.md) give the wall-model height
  as $h_{\mathrm{wm}}^+\approx34$ in the a priori test (§2.3) and
  $h_{\mathrm{wm}}^+=33$ for the $Re_\tau=1000$ LES (Table 1), with
  $h_{\mathrm{wm}}=\delta/30$ in both; at $Re_\tau=1000$ the value is
  $1000/30\approx33.3$ *(compiler check, not in the sources)*. Their own
  symbol for the wall-model height is $\Delta$.
- [Lozano-Durán et al. (2022)](/sources/lozanoduran-2022.md) print the
  channel grids as $\Delta/\delta=1/3,1/5,1/10$ in §IV.C and as
  $1/3,1/6,1/10$ in the Fig. 8 caption.
- The sources differ on where the equilibrium wall model is matched: the
  second off-wall point on staggered grids
  ([Agrawal et al. (2022)](/sources/agrawal-2022.md)), the first off-wall
  cell centre without temporal filtering
  ([Lozano-Durán et al. (2022)](/sources/lozanoduran-2022.md)), half the
  first wall-normal cell ([Fowler et al. (2022)](/sources/fowler-2022.md)),
  $0.3\delta$ ([Griffin et al. (2023)](/sources/griffin-2023.md)), or the
  top node of the first spectral element, time-filtered over about five
  time steps ([Gillyns et al. (2022)](/sources/gillyns-2022.md)); see
  [log-layer mismatch](/definitions/log-layer-mismatch.md).
- The sources use different log-law constants as reference: $\kappa=0.40$,
  $B=5.5$ for the low-Reynolds-number channel
  ([Cao et al. (2022)](/sources/cao-2022.md), Eq. 8); $\kappa=0.41$, $B=5.2$
  ([Bae & Koumoutsakos (2022)](/sources/bae-2022.md)); $\kappa=0.38$ with
  intercept 4.1 in Reichardt's profile
  ([Gillyns et al. (2022)](/sources/gillyns-2022.md), who note 0.383 and
  4.25 as the more recent values); $\kappa=0.38$ as the DNS value
  ([Agrawal et al. (2022)](/sources/agrawal-2022.md)).
- [Bae & Koumoutsakos (2022)](/sources/bae-2022.md) was read in its
  Research Square preprint (v1, June 2021); its numbers may differ from the
  published version. The text gives the 5% error of the log-law-based model
  as an error in the friction velocity, the Fig. 3 caption as an error in
  the wall stress. The text names only $Re_\tau=2\times10^4$ and
  $5\times10^4$ as the failures of the velocity-based model, while the
  $10^5$ and $10^6$ cases of Table 1 also lie outside the trained
  $h_{\mathrm{wm}}^+$ range and are omitted from Fig. 4.
  [Vadrot et al. (2023b)](/sources/vadrot-2023-b.md) report a
  Reynolds-number-dependent log-layer mismatch for the published log-law
  RL model and attribute the difference from Bae & Koumoutsakos's results
  mainly to grid resolution; see
  [machine-learning wall models](/methods/machine-learning-wall-model.md).
- [Prakash et al. (2022)](/sources/prakash-2022.md) print the flow-through
  time as $T=\langle u\rangle_b/L_x$, the inverse of a time; say "fine mesh"
  for the medium mesh; and write in consecutive sentences that the gradient
  model without clipping over- and underpredicts the Reynolds shear stress
  (§III.B.3); which variant the second sentence means is not said. They print $\Delta x^+=78$ for the coarse mesh;
  $2\pi\cdot590/48=77.2$ *(compiler check, not in the sources)*.
- [Gillyns et al. (2022)](/sources/gillyns-2022.md) print the wall-stress
  error of the same configuration (6 elements, first element at
  $0.15\delta$) as 0.87% in Table 1 and 0.88% in Table 2, and state "< 9%"
  for the fluctuation errors at $Re_\tau=5200$ where Table 3 prints 9.00%.
  They rate the 4-element mesh "not sufficiently resolved" in §8 and "a fair
  compromise" in §9.
- [Cao et al. (2022)](/sources/cao-2022.md) were read in the arXiv v1
  preprint; they print the wall shear stress as $\partial U/\partial y$ at
  the wall, without the viscosity.
- [Kim et al. (2022)](/sources/kim-2022.md) (read in arXiv v2) write the
  Vreman constant in a form with $2.5C_s^2$; the value 0.08 is theirs. The
  averaging time of their statistics is not quantified.
- [Blind et al. (2023)](/sources/blind-2023.md) were read in arXiv v1, under
  a title that differs from the published one. Their Table 4, captioned as
  the $Re_\tau=550$ wall-modelled channel, holds the $Re_\tau=2000$ case,
  whose computed $Re_\tau$ on the last grid is 1555.60, not discussed in the
  text. Their element counts, $N_y$ and $\Delta_y$ columns are not mutually
  consistent (two elements over the half-height or the full height).
- [Zhao et al. (2023a)](/sources/zhao-2023.md) print the viscosity of the
  $Re_\tau=180$ case as $2.83\times10^{-4}$, while their own log-law
  procedure (Eqs. 25–26, $\kappa=0.40$, $B=5.5$, $U_c=1$) gives
  $U_\tau=1/(2.5\ln180+5.5)=0.0541$ and $\mu=U_\tau/180=3.0\times10^{-4}$,
  as do the realized values of Table 8 (e.g. $0.0515/171.33$), and the same
  procedure reproduces the printed $1.24\times10^{-4}$ at $Re_\tau=395$; and $\Delta z^+=8.33$ where $\pi\cdot180/64=8.84$
  *(compiler check, not in the sources)*. Their seventh-order runs use 4
  Gauss points per face, with which their accuracy test gives about fourth
  order (§4).
- [Wang et al. (2023b)](/sources/wang-2023-b.md) say that two of their
  channel cases ran on one GPU and two on two GPUs, while Table 8 states two
  GPUs for all. They draw the "may not be safe" conclusion from the
  instantaneous rms profiles (Fig. 14), while the statistics averaged over
  $200\,\delta/U_c$ agree between precisions (Figs. 10–13).
- [Lederer et al. (2023)](/sources/lederer-2023.md) print the friction
  Reynolds number with the half-height and call their bulk-Reynolds-number
  error "only a rough error estimate"; their averaging time is not printed.
- [Kang et al. (2023)](/sources/kang-2023.md) give the $Re_\tau=395$ LES
  spacings ($\Delta x^+=52.0$ on $48^3$) slightly above $2\pi\cdot395/48=51.7$
  *(compiler check, not in the sources)*.
- [Inagaki & Kobayashi (2023)](/sources/inagaki-2023.md) filter only in the
  wall-parallel directions; their "medium" and "coarse" resolutions are those
  of the filters, matched to the LES grids of App. C.
- [Morsbach et al. (2024)](/sources/morsbach-2024.md), §3.1, §3.3, run a
  channel of finite length with parallel end walls and synthetic inflow
  (83,790 elements, $N=5$) as a precursor that calibrates the inflow of a
  turbine cascade; it is a developing flow, not the periodic channel of this
  page (see [inflow turbulence generation](/methods/inflow-turbulence-generation.md)).
- [Carlsson et al. (2023)](/sources/carlsson-2023.md) show Reynolds stresses
  only at $Re_\tau=395$ and in the supersonic cases, although their
  conclusion calls the resolved stresses excellent at all three subsonic
  Reynolds numbers; the $Re_\tau=5000$ supersonic case has no DNS.

- [Cao et al. (2024)](/sources/cao-2024.md) print bulk velocity and
  density as integrals over $[-\delta,\delta]$ without the factor
  $1/(2\delta)$; their wall-unit spacings ($\Delta x^+=21.18$ for 128
  points and 16.92 for 160 points over $4\pi\delta$) imply
  $Re_\tau\approx216$ rather than the tabulated 211 and 213; and their
  mapping $y=\tanh(b_g(\eta/1.5\pi-1))/\tanh b_g$ with $b_g=2$ on the
  printed range $\eta\in[-1.5\pi,1.5\pi]$ spans about $[-1.04\delta,0]$,
  not $[-\delta,\delta]$ *(compiler check,
  not in the sources)*. They call the $160^3$ run of the same scheme
  "DNS" and the $128^3$ run implicit LES.
- [Mukha et al. (2025)](/sources/mukha-2025.md) label the meshes of Fig. 10
  "M0–M2" where the text uses M1–M3.
- [Maejima & Kawai (2025)](/sources/maejima-2025.md) print "$k_z^+\approx60$"
  for what is a wavelength $\lambda_z^+\approx60$ (§6.2.3), and their
  $\delta/\Delta x$ values are about 3% below $N_x/L_x$ *(compiler check,
  not in the sources)*.

- [Tomboulides et al. (2025)](/sources/tomboulides-2025.md) head their
  pipe section "$Re_\tau=1000$" while the text gives 1142, the value the
  printed $Re_b=44{,}000$ (on $D=1$, $U_b=1$) and DNS $u_\tau=0.0519$
  reproduce, $Re_\tau=u_\tau(D/2)/\nu=0.0519\times22{,}000=1141.8$
  *(compiler check, not in the sources)*.
- [Nuca et al. (2025)](/sources/nuca-2025.md) use a relative tolerance of
  $10^{-4}$ in the channel test and mention $10^{-3}$ for the airfoil; the
  global Reichardt fit, run here with the high-Reynolds constants, is an
  extrapolation in its parameter $C$: their Eq. 6, $C=B-\ln\kappa/\kappa$,
  gives $C\approx6.66$ for $\kappa=0.387$, $B=4.21$, against the fitted
  range 6.8–7.7 of Table II *(compiler check, not in the sources)*.

- [Zhao et al. (2021)](/sources/zhao-2021-c.md) print the same two
  values that the entry of [Zhao et al. (2023a)](/sources/zhao-2023.md)
  above records: $\mu=2.83\times10^{-4}$ at $Re_\tau=180$, where their own
  Eqs. 25–26 give $u_\tau=1/(2.5\ln180+5.5)=0.0541$ and
  $\mu=u_\tau/180=3.006\times10^{-4}$ (and the realized values of Table V
  $0.0535/177.89=3.007\times10^{-4}$), and $\Delta z^+=8.33$ for 64 points
  where $\pi\cdot180/64=8.84$ (Table VIII) *(compiler check, not in the
  sources)*. They credit the $Re_\tau=180$ DNS to "Moser et al." while
  their reference is Kim, Moin & Moser; their abstract and conclusion claim
  implicit-LES superiority for the Reynolds stress, which §V.B qualifies
  at 180; and they quote a WALE constant for 395 without WALE results
  there.
- [Lv et al. (2021)](/sources/lv-2021.md) print the log basis as
  $\ln((y+y_0)/y_0)$ in Eq. 3 and $\ln((y-y_0)/y_0)$ in Eq. 8; only the
  first is regular at the wall. They print neither the Mach number nor
  the averaging time of the channel runs. Their term $\tau_w/\rho=a_w^2$
  rests on the identification $a_w=u_\tau$ (Eq. 4); the wall gradient of
  the printed log basis, $\nu\,\partial(a_w\phi_w)/\partial y$ at $y=0$
  with $\phi_w=\kappa^{-1}\ln((y+y_0)/y_0)$ (page-local), is
  $\nu a_w/(\kappa y_0)$ *(compiler check, not in the sources)*.
- [Kumar & Ghosh (2022)](/sources/kumar-2022-b.md) print neither the
  wall-unit resolution nor the averaging time of their channel, and give
  the inflow channel of the shock train (same grid) as Mach 1.5,
  $Re_\tau=247$ (§3.2.3) against 1.49, 240 in Table 4.
- [Chen et al. (2022)](/sources/chen-2022-g.md) compare a finite-element
  VMS with a finite-difference classical LES on the same mesh, so their
  Figs. 1–3 compare model and discretization together; no wall damping is
  mentioned for the Smagorinsky run. Their stretching (Eq. 30) maps
  $j=0,\dots,N_y$ to $[0,1]$ while $L_y=2\delta$; with $N_y=64$ and
  $\alpha_s=1.5$ (page-local) the first spacing is $0.00488$, i.e.
  $\Delta y^+=0.879$ if read in units of $\delta$, the printed 0.88, and
  1.76 if scaled to the full height *(compiler check, not in the
  sources)*. Their generalized-α condition (Eq. 21),
  $\gamma=\tfrac12+\alpha_m+\alpha_f$, gives first-order convergence on
  $\dot a=-a$ with their own update equations and Eq. 23 ($\zeta=0.5$),
  and $\tfrac12+\alpha_m-\alpha_f$ second order *(compiler check, not in
  the sources)*; which value the code used is not stated. They write
  "outer layer ($y^+<50$)" in §4.2.
- [Hamedi & Vermeire (2022)](/sources/hamedi-2022.md) do not state the
  unit of their run length $T_f=170$ or the time integrator of the
  channel; their $\Delta x^+$ values correspond to $N+1$ points per element
  ($2\pi\cdot395/96=25.85$ at $N=3$) *(compiler check, not in the
  sources)*.
- [Qi et al. (2022)](/sources/qi-2022-b.md) call their cost "slightly
  longer" than dynamic Smagorinsky; the Table 5 times give a ratio of 1.75
  *(compiler check, not in the sources)*. They print the Prandtl number as
  "$Pr=\mu C_p\kappa$", not dimensionless, where their Eq. 2.7 uses
  $C_p\mu/Pr$ as conductivity. Their expansion parameter (Eq. 3.9),
  $\int2x^2G\,dx$, gives $\Delta^2/6$ for a box filter, while the gradient
  model they recover needs $\Delta^2/12$, the second moment without the
  factor 2 *(compiler check, not in the sources)*; the coefficient is fixed
  dynamically, so the model is not affected.
- **Printed forcing and resolution of Huang et al. (2022c).** Table I gives
  $Re_\delta=11\,180$, 20 580 and 48 500 at $Re_\tau=550$, 950 and 2000,
  whereas their Eq. (19), which the text says is used to estimate the body
  force, gives 11 426, 21 034 and 48 005; the tabulated $f_1$ follow from
  Eq. (18) with the tabulated $Re_\delta$ ($(550/11\,180)^2=2.42\times10^{-3}$)
  *(compiler check, not in the sources)*. They write "polynomial order
  $N_p=7$"; the printed spacings equal the element sizes divided by
  $N_p-1$ ($2\pi\delta/12/6=0.087\delta$, $\pi\delta/10/6=0.052\delta$,
  $0.224\delta/6=0.037\delta$) *(compiler check, not in the sources)*, which
  the paper does not comment on. The conclusions call the comparison of the
  two meshes "p-type refinement" and §III E calls it h-type refinement.
- [van Noordt et al. (2022)](/sources/vannoordt-2022.md) print the coarse
  grid as $\delta/20\times\delta/80$ with $\Delta x^+=270$, $\Delta y^+=68$,
  while at $Re_\tau=5200$ these spacings give 260 and 65; the fine row
  (173.3, 40.6, 156) is consistent with 5200 *(compiler check, not in the
  sources)*. Their averaging time is not printed.
- Diez Sanhueza et al. (2023) give the baseline error of their hardest case
  as 22.8% in §2.2 and as 23.4% in Table 3 and the abstract; the value above
  is the table's.

- [De Cosmo et al. (2025)](/sources/decosmo-2025.md) define $Re_b=3173$
  on the half-height; with it the printed Dean correlation gives 1.166 against the printed 1.156; their
  "3%" fits the Dean value ($1.186/1.156=1.026$), while against the DNS
  value named in the same sentence the excess is 1.5% *(compiler check,
  not in the sources)*. They select $Re_b$ and $Re_\tau=200$ "from the
  reference DNS in Banchetti et al." but plot DNS labelled $Re_\tau=180$,
  so which DNS gives which curve is not explicit. Their Table 5 lists the
  bump amplitudes $a$, $a'$ as dimensionless, whereas their own Eq. 32 and
  the printed height $0.0837\delta$ require lengths in metres *(compiler
  check, not in the sources)*.
- [Fang et al. (2025)](/sources/fang-2025.md) print
  $Ha=B_0L\sqrt{\sigma\rho_0/\nu}=\sqrt{Re\,N_{\mathrm{St}}}$, whereas their
  own definitions of $Re$ and $N_{\mathrm{St}}$ give
  $B_0L\sqrt{\sigma/(\rho_0\nu)}$; their friction velocity carries both
  $\nu$ and $1/Re$, and their bulk velocity is integrated in $dx$ over
  $0\le y\le2$ *(compiler check, not in the sources)*. They say their
  parameters ease comparison with Nishimura & Kasagi, whose printed title
  (their ref. 29) is a mixed-convection channel study; the MHD data they
  compare with are the THTLab data of Noguchi & Kasagi.
- [Wang et al. (2024d)](/sources/wang-2024-k.md) state in the abstract
  that the diffused interface fails in internal flows by under-estimating
  the wall shear stress, and in §III A that it over-estimates the friction
  velocity, i.e. the wall stress. Their channel figures label as "turbulent
  energy" a quantity whose axis reads $\langle v'w'\rangle/u_\tau^2$. Their
  driving term $g=u_\tau^2/\delta-(\overline u-\langle u_z\rangle)\delta t$
  (Eq. 24) adds an acceleration to a length *(compiler check, not in the
  sources)*. No averaging time is printed.
- [Xiao et al. (2025)](/sources/xiao-2025.md) call their thirteen WMLES
  grids uniform refinements in all three directions, but their row
  $1536\times256\times576$ keeps the $N_y=256$ of the preceding
  $1024\times256\times384$ *(compiler check, not in the sources)*; they
  summarize the dynamic-model WRLES errors as "less than approximately 3%"
  next to the $-3.22\%$ of their Table 3.
- [Alberti et al. (2025)](/sources/alberti-2025-b.md) print $N_{tot}=985$
  elements for the $11\times17\times5$ mesh at $Re_\tau=5200$; the product
  is 935, which their own degree-of-freedom count 32,725 ($935\times35$)
  confirms *(compiler check, not in the sources)*.
- [Akbarzadeh & Borazjani (2025)](/sources/akbarzadeh-2025.md) use $z$
  streamwise and $x$ spanwise (translated in the table) and do not state
  the wall model of their $24^3$ run or the averaging time.
- [Kokkinakis & Drikakis (2025b)](/sources/kokkinakis-2025-b.md) give
  the domain length as $6\pi\delta$ in the text while Fig. 5 labels
  $2\pi$, and the averaging time as $900\,u_b/\delta$ (printed), "just over
  21 flow-throughs"; $900/(6\pi)=47.7$ flow-throughs of a $6\pi\delta$ box
  *(compiler check, not in the sources)*. The noise amplitude of their
  initial condition is printed as 5% and as $s=10\%$, the wall at $y=0$ in
  their Eqs. 38 and 41 and at mid-height in Eqs. 43–44, and they print
  the wall-normal $y^+$ of the first cell but no streamwise or spanwise
  wall-unit spacing. Their DNS reference is Moser, Kim & Mansour
  ($Re_\tau=392.24$, "on $256^3$" as printed in Table II).
- [Monteiro et al. (2026)](/sources/monteiro-2026.md) print
  $\Delta x^+\approx9.8$ and $\Delta z^+\approx5.0$; with $Re_\tau=590$,
  $2\pi\delta$, $\pi\delta$ and 384 points, $\Delta x^+=9.65$ and
  $\Delta z^+=4.83$ *(compiler check, not in the sources)*.
- [Alberti et al. (2025b)](/sources/alberti-2025-c.md) caption Fig. 3 with
  a $20\times20\times12$ mesh where Table II gives $20\times20\times10$; write
  that their $M_b=3$ run uses "approximately 1/1000" of the DNS degrees of
  freedom while Table V gives $r=1412.3$; quote the case of Hamzehloo et
  al. as $Re_\tau=215$ (§I) and as $Re=222$ (§III A); and state that
  $M_b=3$, $Re_\tau=450$ "corresponds to an incompressible simulation at
  $Re=140$" (§III A) while their Fig. 8 collapses it on the incompressible
  $Re_\tau=180$ DNS under the Trettel–Larsson transformation (see
  [compressible velocity transformations](/definitions/compressible-velocity-transformation.md)).

# Citations

- [Agrawal et al. (2022)](/sources/agrawal-2022.md) — §V, Figs. 1–2; §VII.D, Figs. 7–10.
- [Lozano-Durán et al. (2022)](/sources/lozanoduran-2022.md) — §IV.B–C, Figs. 7–8; App. B, Figs. 23–24.
- [Fowler et al. (2022)](/sources/fowler-2022.md) — §2.3, Fig. 2; §5.1, Table 1, Figs. 4–10.
- [Vadrot et al. (2023b)](/sources/vadrot-2023-b.md) — §II–IV, Table III, Figs. 5–15, App. A–B.
- [Haering et al. (2022)](/sources/haering-2022.md) — §III B, Fig. 1; §V A, Table I, Figs. 2–8.
- [Griffin et al. (2023)](/sources/griffin-2023.md) — §4, Table 1, Figs. 8–15.
- [Flad & Gassner (2017)](/sources/flad-2017.md) — §6.2, App. E, Fig. 11.
- [Duraisamy et al. (2019)](/sources/duraisamy-2019.md) — §5.1 (cited calibration studies).
- [Duraisamy (2021)](/sources/duraisamy-2021.md) — §VII, Fig. 4.
- [Cao et al. (2022)](/sources/cao-2022.md) — §3.3, Eq. (8), Tables 5–7, Figs. 7–12.
- [Prakash et al. (2022)](/sources/prakash-2022.md) — §III.B.3, Tables 3–4, Figs. 8–10; §IV.
- [Gillyns et al. (2022)](/sources/gillyns-2022.md) — §§3–9, Eqs. (3)–(7), Tables 1–3, Figs. 3–13.
- [Bae & Koumoutsakos (2022)](/sources/bae-2022.md) — Results pp. 4–8, Table 1, Figs. 2–7; Methods pp. 12–14 (preprint v1).
- [Huang et al. (2022)](/sources/huang-2022.md) — §4.1 (cited channel results).
- [Cogo et al. (2022)](/sources/cogo-2022.md) — §4 (cited channel results).
- [Kim et al. (2022)](/sources/kim-2022.md) — §II A–F, Tables I–III; §III C–D, Figs. 7–13.
- [Blind et al. (2023)](/sources/blind-2023.md) — §3.1–3.3, Tables 1–4, Figs. 1–11 (arXiv v1).
- [Carlsson et al. (2023)](/sources/carlsson-2023.md) — §4.3, Table 2, Figs. 4–6; §5.
- [Zhao et al. (2023a)](/sources/zhao-2023.md) — §5.2, Tables 6–9, Figs. 8–17.
- [Wang et al. (2023b)](/sources/wang-2023-b.md) — §4.2, Tables 6–8, Figs. 9–14.
- [Lederer et al. (2023)](/sources/lederer-2023.md) — §4, §4.1, Tables 1–2, Figs. 1–6.
- [Kang et al. (2023)](/sources/kang-2023.md) — §3.5–3.7, Tables 8–13, Figs. 25–33.
- [Inagaki & Kobayashi (2023)](/sources/inagaki-2023.md) — §III–IV; App. B–C, Table I, Figs. 16–17.
- [Bernades et al. (2023)](/sources/bernades-2023.md) — §4.3, Figs. 8–10; §5.
- [Lozano-Durán & Bae (2023)](/sources/lozanoduran-2023.md) — §2.3; §4.4–4.6, Figs. 10–13.
- [Morsbach et al. (2024)](/sources/morsbach-2024.md) — §3.1, §3.3, Table 2.
- [Vadrot et al. (2023a)](/sources/vadrot-2023.md) — §II.A–B, Eqs. (2)–(12), Figs. 2–3; §III.A–B, Figs. 6–10; §IV, Table III, Figs. 11–12; §V.
- [Duan & Wang (2024)](/sources/duan-2024.md) — §1, Fig. 2; §3–4; §5.3–5.4, Figs. 9–15; §6.
- [Wang et al. (2024)](/sources/wang-2024.md) — §3.2, Figs. 3–4.
- [Kim et al. (2024)](/sources/kim-2024.md) — App. D, Fig. 19.
- [Steinhausen et al. (2023)](/sources/steinhausen-2023.md) — §2.1.
- [Cao et al. (2024)](/sources/cao-2024.md) — arXiv v1: §1; §3.3, Tables 4–5, Figs. 5–9.
- [Mukha et al. (2025)](/sources/mukha-2025.md) — arXiv v1: §II.B–C; §III.A–D, Tables I–IV, Figs. 1–10; §V.
- [Maejima & Kawai (2025)](/sources/maejima-2025.md) — §1; §3; §4.1, Tables 1–2, Fig. 5; §5; §6.1–6.2, Figs. 22–27; §7, Figs. 28–29; App. C.
- [Oulghelou et al. (2025)](/sources/oulghelou-2025.md) — arXiv v2: §4.2.1, Table 3, Fig. 4.
- [Löhrer & Fröhlich (2025)](/sources/lohrer-2025.md) — §5.3, Eqs. 5.12–5.14.
- [Elzaabalawy et al. (2023)](/sources/elzaabalawy-2023.md) — §5.2, §5.2.1, Tables 2–3, Figs. 7–16.
- [Aiello et al. (2026)](/sources/aiello-2026.md) — §3.3, Table 2; §4.1–4.2, Table 3, Figs. 1–3; §5.
- [D'Ayer et al. (2026)](/sources/dayer-2026.md) — submitted manuscript: §3.2, Eq. 28, Table 3, Figs. 7–10.
- [Ranjbar et al. (2026)](/sources/ranjbar-2026.md) — arXiv v1: §III.C, Figs. 15–16; §III.D.2–3.
- [Wu & Lele (2026)](/sources/wu-2026.md) — arXiv v2: §3.2.1; §6.2.1, Figs. 15–20.
- [Rickard & Kasbaoui (2026)](/sources/rickard-2026.md) — §1; §2.3; §3.2–3.3, Figs. 5–10; §4.1–4.2, Eqs. 4.2–4.27, Figs. 11–13; §5, Tables 1–2.
- [Tomboulides et al. (2025)](/sources/tomboulides-2025.md) — §3.1, Table 1, Figs. 1–3; §3.2, Table 2, Figs. 4–6.
- [Nuca et al. (2025)](/sources/nuca-2025.md) — §II; §VI, Table VII.
- [Lv et al. (2021)](/sources/lv-2021.md) — §I; §II A–C, Eqs. (1)–(12); §III; §IV A, §IV B 1, Table I, Figs. 5–12.
- [Zhao et al. (2021)](/sources/zhao-2021-c.md) — §III–IV, Eqs. (12)–(26), Tables I–VIII; §V.A–D, Figs. 2–21; §VI; App. A–B.
- [Kumar & Ghosh (2022)](/sources/kumar-2022-b.md) — §3.2.1–3.2.3, Table 4, Figs. 26–29.
- [Bose & Park (2018)](/sources/bose-2018.md) — §1, Fig. 2; §2.1, Fig. 4; §2.4; §4.1 (review; cited results).
- [Chen et al. (2022)](/sources/chen-2022-g.md) — §2.4, Eqs. (21)–(23); §3, Eq. (24); §4.1–4.2, Eq. (30), Table 1, Figs. 1–2; §5, Figs. 3–5; §6.2, Eq. (38), Figs. 7–8.
- [Hamedi & Vermeire (2022)](/sources/hamedi-2022.md) — §5.1, Eq. (54), Table 2, Figs. 19–25.
- [Qi et al. (2022)](/sources/qi-2022-b.md) — §3.2, Eqs. (3.9)–(3.21); §4.1, Tables 1–7, Figs. 2–13.
- [van Noordt et al. (2022)](/sources/vannoordt-2022.md) — §3.1, Tables 4–5, Figs. 12–14.
- [Sandberg & Zhao (2022)](/sources/sandberg-2022-b.md) — §2.1; §3.4; §4.2.2 (review; cited results).
- [Zhang et al. (2022)](/sources/zhang-2022-b.md) — §6.2, Fig. 18a (channel reference of a pressure decomposition).
- [Huang et al. (2022c)](/sources/huang-2022-c.md) — §II C; §III A, Eqs. (18)–(19), Table I; §III B–E, Figs. 3–9; §IV.
- [Idelsohn et al. (2024)](/sources/idelsohn-2024.md) — §2.10.1, Table 1, Figs. 6–7; §3.2.2, Fig. 28.
- [Devenport & Lowe (2022)](/sources/devenport-2022.md) — §5.4, footnote 6, Figs. 37–42 (review; cited channel DNS).
- [Xu et al. (2023)](/sources/xu-2023.md) — §2.1–2.2; §3.2; §4.1–4.3, Tables 3–7, Figs. 13–28.
- [Diez Sanhueza et al. (2023)](/sources/sanhueza-2023.md) — §2.1–2.2, Table 1; §5, Tables 2–3.
- [Hu et al. (2024)](/sources/hu-2024.md) — §5, Table 1; §6.1–6.2, Figs. 3, 5–8, 11–14.
- [Vermeire (2024)](/sources/vermeire-2024.md) — §4.2, Table 2, Figs. 9–18.
- [Wu et al. (2024)](/sources/wu-2024.md) — §3.1a, Table 2, Figs. 2–4.
- [Chen et al. (2024b)](/sources/chen-2024-c.md) — §3.1–3.3, Figs. 11, 13–16 (review; reproduced figures).
- [Kim & Leonard (2024)](/sources/kim-2024-b.md) — §2.5; §3.1; §3.4; §4.5; §4.7–4.8 (history).
- [Akbarzadeh & Borazjani (2025)](/sources/akbarzadeh-2025.md) — §3.2, Table 1, Figs. 3–5.
- [Alberti et al. (2025)](/sources/alberti-2025-b.md) — §2.1–2.3, Table 1; §3.1.1–3.1.3, Tables 2–5, Figs. 2–14; §4.
- [De Cosmo et al. (2025)](/sources/decosmo-2025.md) — §3.3, Eqs. 21–31, Tables 3–4, Figs. 6–10; §3.4, Eqs. 32–35, Table 5, Figs. 11–16.
- [Fang et al. (2025)](/sources/fang-2025.md) — §3.3, Eqs. 21–22, Table 5, Figs. 9–11; §3.4, Table 6, Figs. 12–15.
- [Wang et al. (2024d)](/sources/wang-2024-k.md) — §II D; §III A, Eqs. 23–24, Figs. 2–6; App. C, Fig. 16.
- [Xiao et al. (2025)](/sources/xiao-2025.md) — §2.1–2.2; §4.2, Table 3, Figs. 6–8; §4.3, Table 4, Figs. 9–12.
- [Fang et al. (2026)](/sources/fang-2026.md) — §3.4, Table 4 (cited works, review).
- [Witherden et al. (2025)](/sources/witherden-2025.md) — §4 (application list).
- [Alberti et al. (2025b)](/sources/alberti-2025-c.md) — §I; §II A–B, Eqs. 22–31; §III A 1–3, Tables I–V, Figs. 1–21; §IV; App. A, Table VI; App. C.
- [Gao et al. (2025)](/sources/gao-2025.md) — §II B; §III A, Tables II–III, Figs. 5–11.
- [Gao et al. (2025b)](/sources/gao-2025-b.md) — §II C–D, Eqs. 33–37; §III A, Figs. 2–5.
- [Kokkinakis & Drikakis (2025b)](/sources/kokkinakis-2025-b.md) — §IV–V, Eqs. 24, 34–36; §VI–VIII, Table II, Figs. 4–10.
- [Monteiro et al. (2026)](/sources/monteiro-2026.md) — §4.3, Figs. 3–4.
- [Okano & Haga (2026)](/sources/okano-2026.md) — §5.1–5.4, Eqs. (17)–(20), Tables 1–4, Figs. 7–8, 10–14; Apps. A–C, Tables A.5–A.6, B.7–B.8, C.10.
- [Germano et al. (1991)](/sources/germano-1991.md) — §III, Figs. 1–9 (a priori at $Re=3300$, 7900; transitional LES at $Re=8000$; turbulent LES at $Re=6100$).
