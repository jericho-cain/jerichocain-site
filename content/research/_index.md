+++
date = '2025-09-21T12:14:00-07:00'
draft = false
title = 'Research'
+++

<div class="research">

<section class="research-hero">
  <div class="research-intro">
    <p class="research-kicker">Physics-first machine learning for gravitational-wave discovery</p>
    <p class="research-lede">
      My research focuses on physics-first machine-learning approaches to gravitational-wave data analysis, with applications to both ground-based detectors (LIGO) and future space-based missions (LISA). I develop template-free and unsupervised methods designed for robustness, interpretability, and discovery.
    </p>
    <div class="research-actions">
      <a class="btn" href="/publications/">View publications</a>
      <a class="btn btn-secondary" href="#latest-projects">Latest projects</a>
    </div>
  </div>

  <figure class="research-photo">
    <img src="/img/bunny_suit.JPG" alt="Jericho Cain at the Hanford LIGO interferometer facility">
    <figcaption>At the Hanford LIGO interferometer facility during detector characterization work.</figcaption>
  </figure>
</section>

<section class="research-focus-grid" aria-label="Research focus areas">
  <article class="focus-card">
    <h2>Signals without templates</h2>
    <p>I build anomaly-detection pipelines that do not depend on large waveform banks, making them better suited for discovery-oriented searches and unexpected morphologies.</p>
  </article>
  <article class="focus-card">
    <h2>LIGO to LISA</h2>
    <p>My work spans both current ground-based detectors and future space-based missions, with an emphasis on the different statistical and computational challenges each regime creates.</p>
  </article>
  <article class="focus-card">
    <h2>Geometry and interpretability</h2>
    <p>I am especially interested in latent-space structure, invariance, and physically meaningful representations that make machine-learning systems easier to trust and analyze.</p>
  </article>
</section>

## Latest Projects {#latest-projects}

<div class="research-projects">

<article class="project-card">
  <div class="project-meta">
    <span class="project-tag">Representation Learning</span>
    <span class="project-status">Preprint</span>
  </div>
  <h3><a href="https://github.com/jericho-cain/neural-representation-gauge">Gauge Freedom and Metric Dependence in Neural Representation Spaces</a></h3>
  <p class="project-links"><a href="https://arxiv.org/abs/2603.06774">Read preprint</a></p>
  <p>Neural network representations are often analyzed as vectors in a fixed Euclidean space, even though their coordinates are not uniquely defined. This project treats hidden representations geometrically, as vector spaces defined only up to invertible linear transformations. Within that framework, commonly used similarity measures such as cosine similarity become metric-dependent quantities whose values can change under coordinate transformations that leave the model function unchanged. The result is a common interpretation for observations such as cosine-similarity instability, anisotropy in embedding spaces, and the appeal of methods like SVCCA and CKA. Experiments on multilayer perceptrons and convolutional networks show that invertible transformations can substantially distort cosine similarity and nearest-neighbor structure while leaving predictions unchanged, suggesting that representation analysis should prioritize gauge-invariant quantities or explicitly chosen canonical coordinates.</p>
</article>

<article class="project-card">
  <div class="project-meta">
    <span class="project-tag">LISA</span>
    <span class="project-status">Preprint</span>
  </div>
  <h3><a href="https://github.com/jericho-cain/lisa-cwt-oneclass-likelihood">Likelihood-Based One-Class Scoring in CWT Latent Space for Confusion-Limited LISA Gravitational-Wave Detection</a></h3>
  <p class="project-links"><a href="https://arxiv.org/abs/2602.20212">Read preprint</a></p>
  <p>We study one-class scoring for resolvable-source detection in confusion-limited LISA time-series data represented as continuous-wavelet-transform scalograms. With data generation and preprocessing held fixed, we benchmark geometry-style scoring against likelihood-style latent-density scoring while also evaluating morphology-augmented and contrastive variants. Geometry-only and geometry-plus-morphology methods provide modest gains over the reconstruction baseline, but likelihood scoring on autoencoder latents is consistently stronger. Across three seeds, latent-only likelihood outperforms AE+manifold scoring in both ROC-AUC and PR-AUC, indicating that explicit latent density modeling can outperform local off-manifold distance in this confusion-limited regime.</p>
</article>

<article class="project-card">
  <div class="project-meta">
    <span class="project-tag">Wavelet Methods</span>
    <span class="project-status">Preprint</span>
  </div>
  <h3><a href="https://arxiv.org/abs/2602.17725">Detectability Scaling Laws for Environmental Phase Modulation in Gravitational-Wave Signals</a></h3>
  <p class="project-links"><a href="https://arxiv.org/abs/2602.17725">Read preprint</a></p>
  <p>Environmental effects such as hierarchical triple motion can introduce cumulative phase modulation in gravitational-wave signals through time-dependent line-of-sight acceleration. This project studies detectability in a template-free framework using continuous-wavelet-transform time-frequency representations and trajectory-based statistics, especially the evolution of the power-weighted frequency centroid. Detection performance collapses onto a single scaling parameter given by phase distortion times signal-to-noise ratio, with ROC-AUC following a sigmoid transition. The main takeaway is that smooth environmental phase modulation is not generically absorbed by intrinsic waveform variability; detectability is governed by a simple scaling between cumulative phase distortion and signal strength.</p>
</article>

<article class="project-card">
  <div class="project-meta">
    <span class="project-tag">LISA</span>
    <span class="project-status">Submitted</span>
  </div>
  <h3><a href="https://github.com/jericho-cain/cwt-manifold-grav-wav">Manifold Learning for Source Separation in Confusion-Limited Gravitational-Wave Data</a></h3>
  <p class="project-links"><a href="https://arxiv.org/abs/2511.12845">Read preprint</a></p>
  <p>The Laser Interferometer Space Antenna will operate in a fundamentally different data-analysis regime than ground-based detectors such as LIGO: instead of rare signals buried in instrumental noise, LISA observations are expected to be dominated by a dense superposition of unresolved Galactic binaries. In this project, I investigate whether manifold-learning techniques can aid source separation in that confusion-dominated setting. I develop a convolutional autoencoder trained exclusively on synthetic confusion-background data and augment the standard reconstruction-error anomaly score with a geometric term derived from the local structure of the learned latent-space manifold. Tests on synthetic datasets with injected massive black hole binaries, extreme mass ratio inspirals, and individual Galactic binaries show that incorporating latent-space geometry substantially improves source discrimination compared with reconstruction error alone.</p>
  <p class="project-note">Manuscript submitted to <em>Classical and Quantum Gravity</em>.</p>
</article>

<article class="project-card">
  <div class="project-meta">
    <span class="project-tag">LIGO</span>
    <span class="project-status">Published</span>
  </div>
  <h3><a href="https://github.com/jericho-cain/cwt-lstm-ae-grav-wav">Template-Free Gravitational Wave Detection with CWT-LSTM Autoencoders: A Case Study of Run-Dependent Calibration Effects in LIGO Data</a></h3>
  <p class="project-links"><a href="https://iopscience.iop.org/article/10.1088/1361-6382/ae415e">Read article</a></p>
  <p>Gravitational-wave searches traditionally rely on matched filtering against large banks of theoretical waveforms, which can be computationally expensive and inherently biased toward known signal morphologies. In this project, I develop a template-free, unsupervised detection framework that combines continuous-wavelet-transform representations with sequence-based machine learning. The method trains an LSTM autoencoder exclusively on detector noise so that gravitational-wave signals appear as anomalies without waveform templates or labeled training data. During development, I found that training across multiple LIGO observing runs caused the latent structure to cluster by observing run rather than by astrophysical signal properties, revealing systematic batch effects tied to calibration and preprocessing. A per-run training strategy eliminated those effects and substantially improved detection performance on O4 LIGO data.</p>
  <p class="project-note"><a href="https://iopscience.iop.org/article/10.1088/1361-6382/ae415e">Jericho Cain 2026, <em>Classical and Quantum Gravity</em> 43 035019</a></p>
</article>

</div>

<div class="research-footer">
  <a href="/">← Back to Home</a>
</div>

</div>
