---
type: Software
title: "Relexi"
description: "Relexi is the open-source reinforcement-learning framework of the FLEXI group that trains turbulence-model policies on HPC systems by launching FLEXI LES as environments and exchanging states and actions through SmartSim; this page records its components, training settings and the hardware and costs reported."
status: established
aliases: [relexi, RL framework for FLEXI]
tags: [software, reinforcement-learning, les, dg]
timestamp: 2026-10-26T07:19:00Z
---

# Relexi

**Relexi** is the framework in which the
[reinforcement-learning closures](/methods/reinforcement-learning-closure.md)
of the FLEXI group are trained. It couples a reinforcement-learning agent
to running LES of the [DGSEM](/methods/discontinuous-galerkin-spectral-element-method.md)
code [FLEXI](/software/flexi.md) on HPC systems: each training iteration
launches several FLEXI runs, which are the environments of the Markov
decision process, and the agent sets model parameters in them while they
run (Kurz et al. 2023, §3.5; Beck & Kurz 2023, §IV B). Its code is public
(github.com/flexi-framework/relexi; Kurz et al. 2023, footnote 1). The
framework's own paper (Kurz et al. 2022, Software Impacts) is cited by
both sources but not ingested in this bundle.

## Components (Kurz et al. 2023, §3.5)

- **Agent side.** TensorFlow for the networks and TF-Agents for the
  reinforcement-learning algorithm (PPO in both sources).
- **Orchestration and communication.** SmartSim launches the FLEXI
  instances and carries the solver–agent exchange of states and actions.
- **Environment.** FLEXI LES of forced
  [homogeneous isotropic turbulence](/benchmarks/homogeneous-isotropic-turbulence.md),
  initialized from filtered DNS. Rewards are computed from the LES energy
  spectrum against the DNS spectrum and are needed only in training, not
  when the trained policy is applied.
- **Policy evaluation.** One element-local convolutional network per DG
  element, with weights shared across elements; Kurz et al. (2023, §3.4)
  describe each element as an agent of a multi-agent problem.

## Uses and reported costs

| Source | Closure trained | Hardware and cost |
|---|---|---|
| [Kurz et al. (2023)](/sources/kurz-2023.md), §4.1 | element-local Smagorinsky coefficient, Gaussian actions, 24–48 DOF per direction, $N=5,7$ | HAWK (HLRS): up to 1024 CPU cores for the simulations and one GPU node for policy execution and training; 1 to 5 days per configuration |
| [Beck & Kurz (2023)](/sources/beck-2023.md), §IV B | constant and quadratic element-local Smagorinsky coefficients, DG/finite-volume blending factor, beta-distributed actions, 24 and 36 DOF, $N=3,5,8$ | 16 parallel episodes per iteration, 8 cores per LES at 24 DOF and 16 at 36 DOF, at most 0.8 CPU-hours per LES; 2000 iterations |

Both use episodes of 5 time units with an action every 0.1 time units
(50 actions per episode), Adam with learning rate $10^{-4}$ and 5 epochs
per iteration (Kurz et al. 2023, §3.5; Beck & Kurz 2023, §IV B). Kurz et
al. ran 16 or 32 episodes per update and found 32 faster "consistently"
(§4.1). The trained models and the training code of Kurz et al. are also
public (github.com/flexi-framework/DRL_LES, footnote 4).

## Qualifications

- What the sources describe is the framework as used, not its design:
  neither gives the data-exchange protocol, the scaling of SmartSim with
  the number of environments, or the overhead of the coupling.
- Kurz et al. (2023, §4.2) time the trained policy, not the framework: on
  one CPU core, at 48 DOF, the unoptimized policy took about 10% more
  time than the dynamic procedure of the Smagorinsky model.

# Citations

- [Kurz et al. (2023)](/sources/kurz-2023.md) — arXiv v2: footnotes 1 and 4 (code), §3.4 (multi-agent interpretation), §3.5 (TensorFlow, TF-Agents, SmartSim, FLEXI, training settings), §4.1 (hardware, training time), §4.2 (policy cost).
- [Beck & Kurz (2023)](/sources/beck-2023.md) — §IV B (Relexi coupling of FLEXI and the agent, training settings and cost).
