+++
date = '2025-09-21T12:14:00-07:00'
draft = false
title = 'Research'
+++

# Research

My research focuses on physics-first machine-learning approaches to gravitational-wave data analysis, with applications to both ground-based detectors (LIGO) and future space-based missions (LISA). I develop template-free and unsupervised methods designed for robustness, interpretability, and discovery.

![Me at LIGO](/img/bunny_suit.JPG)

Me at the Hanford LIGO interferometer facility during detector characterization work.

---

## Publications
See the full list here: [/publications/](/publications/)

---

## Latest Projects

[Gauge Freedom and Metric Dependence in Neural Representation Spaces](https://github.com/jericho-cain/neural-representation-gauge)

[Preprint](https://arxiv.org/abs/2603.06774)

Neural network representations are often analyzed as vectors in a fixed Euclidean space. However, their coordinates are not uniquely defined. If a hidden representation is transformed by an invertible linear map, the network function can be preserved by applying the inverse transformation to downstream weights. Representations are therefore defined only up to invertible linear transformations. We study neural representation spaces from this geometric viewpoint and treat them as vector spaces with a gauge freedom under the general linear group. Within this framework, commonly used similarity measures such as cosine similarity become metric-dependent quantities whose values can change under coordinate transformations that leave the model function unchanged. This provides a common interpretation for several observations in the literature, including cosine-similarity instability, anisotropy in embedding spaces, and the appeal of representation comparison methods such as SVCCA and CKA. Experiments on multilayer perceptrons and convolutional networks confirm that inserting invertible transformations into trained models can substantially distort cosine similarity and nearest-neighbor structure while leaving predictions unchanged. These results indicate that analysis of neural representations should focus either on quantities that are invariant under this gauge freedom or on explicitly chosen canonica coordinates. 

[Likelihood-Based One-Class Scoring in CWT Latent Space for Confusion-Limited LISA Gravitational-Wave Detection](https://github.com/jericho-cain/lisa-cwt-oneclass-likelihood)

[Preprint](https://arxiv.org/abs/2602.20212)

We study one-class scoring for resolvable-source detection in confusion-limited LISA time-series data represented as continuous-wavelet-transform (CWT) scalograms. With data generation and preprocessing held fixed, we benchmark geometry-style scoring against likelihood-style latent-density scoring, while also evaluating morphology-augmented and contrastive variants. Geometry-only and geometry+morphology methods provide modest gains over the reconstruction baseline, and contrastive variants do not show stable improvement. Likelihood scoring on AE latents is consistently stronger: across three seeds, latent-only likelihood reaches ROC-AUC 0.8555±0.0181 and PR-AUC 0.9219±0.0118, versus ROC-AUC 0.7663±0.0450 and PR-AUC 0.8667±0.0255 for AE+manifold. These results indicate that explicit latent density modeling can outperform local off-manifold distance in this confusion-limited regime. We provide seed-based comparisons, unified ROC/PR visual summaries, and reproducible experimental artifacts to support follow-on work in LISA anomaly detection. 

[Detectability Scaling Laws for Environmental Phase Modulation in Gravitational-Wave Signals](https://arxiv.org/abs/2602.17725)

[Preprint](https://arxiv.org/abs/2602.17725)

Environmental effects such as hierarchical triple motion can introduce cumulative phase modulation in gravitational-wave signals through time-dependent line-of-sight acceleration. Whether such smooth time-warp distortions are observable depends jointly on deformation strength and signal-to-noise ratio (SNR), yet this relationship has not been quantified in a template-free framework. We study the detectability of these distortions using time-frequency representations derived from the continuous wavelet transform. Instead of reconstruction error alone, we examine trajectory-based statistics, in particular the evolution of the power-weighted frequency centroid. We find that environmental modulation can be detected using a single-sample statistic referenced to an isolated-binary distribution, without requiring matched templates. Across a grid of cumulative phase distortions and SNR, detection performance collapses onto a single scaling parameter defined as the product of phase distortion and SNR. The ROC-AUC follows a sigmoid transition in this parameter. Moderate distortions are detectable at low SNR, whereas smaller distortions require higher SNR. These results indicate that smooth environmental phase modulation is not generically absorbed by intrinsic waveform variability; instead, detectability is governed by a simple scaling between cumulative phase distortion and signal strength. 


[Manifold Learning for Source Separation in Confusion-Limited Gravitational-Wave Data](https://github.com/jericho-cain/cwt-manifold-grav-wav).

[Preprint](https://arxiv.org/abs/2511.12845)

The Laser Interferometer Space Antenna (LISA) will operate in a fundamentally different data-analysis regime than ground-based detectors such as LIGO. Rather than rare signals buried in instrumental noise, LISA observations are expected to be dominated by a dense superposition of unresolved Galactic binaries, forming a confusion-limited background. A central challenge is identifying resolvable sources that deviate meaningfully from this background.

In this project, I investigate whether manifold-learning techniques can aid source separation in confusion-dominated gravitational-wave data. I develop a convolutional autoencoder trained exclusively on synthetic confusion-background data and augment the standard reconstruction-error anomaly score with a geometric term derived from the local structure of the learned latent-space manifold. This combined score exploits not only reconstruction fidelity but also deviations from the geometric structure characteristic of the background.

Tests on synthetic LISA datasets with injected massive black hole binaries, extreme mass ratio inspirals, and individual Galactic binaries demonstrate that incorporating latent-space geometry substantially improves source discrimination compared to reconstruction error alone. These results suggest that the learned latent manifold captures physically meaningful structure in the confusion background and that manifold-aware anomaly detection may provide a practical, template-free tool for LISA data analysis.

Manuscript submitted to Classical and Quantum Gravity.


[Template-Free Gravitational Wave Detection with CWT-LSTM Autoencoders: A Case Study of Run-Dependent Calibration Effects in LIGO Data](https://github.com/jericho-cain/cwt-lstm-ae-grav-wav). 

[Jericho Cain 2026 Class. Quantum Grav. 43 035019](https://iopscience.iop.org/article/10.1088/1361-6382/ae415e)

Gravitational-wave searches traditionally rely on matched filtering against large banks of theoretical waveforms, which can be computationally expensive and inherently biased toward known signal morphologies. In this project, I develop a template-free, unsupervised detection framework that combines physically motivated time–frequency representations with sequence-based machine learning.

The method applies a continuous wavelet transform (CWT) to LIGO strain data to produce time–frequency representations aligned with the chirp-like evolution of compact binary coalescences. An LSTM-based autoencoder is then trained exclusively on detector noise, allowing gravitational-wave signals to be identified as anomalies without the use of waveform templates or labeled training data.

During development, I identified a previously underappreciated issue: when training across multiple LIGO observing runs, the autoencoder’s latent structure clustered by observing run rather than by astrophysical signal properties. This behavior revealed systematic batch effects associated with evolving detector calibration and preprocessing, rather than true physical differences. Adopting a per-run training strategy—consistent with established LIGO analysis practice—eliminated these effects and substantially improved detection performance.

Applied to O4 LIGO data, the resulting pipeline achieves high-efficiency, high-purity detection using a purely unsupervised approach, demonstrating that physics-informed anomaly detection can perform competitively with supervised methods while remaining sensitive to signals with unexpected or poorly modeled morphologies. This work highlights both the promise of template-free methods for discovery-oriented searches and the importance of careful treatment of non-stationarity in multi-epoch gravitational-wave datasets.



---
[← Back to Home](/)
