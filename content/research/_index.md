+++
date = '2025-09-21T12:14:00-07:00'
draft = false
title = 'Research'
+++

# Research

My research spans **gravitational-wave astrophysics**, **deep learning**, **machine learning**, **atmospheric physics**, and **theoretical acoustics**.  
These days I work full-time in tech as an **AI researcher**, but I continue gravitational wave research on the side — at the intersection of deep learning and gravitational wave astronomy.

![Me at LIGO](/img/bunny_suit.JPG)

---

## Publications
See the full list here: [/publications/](/publications/)

---

## Latest Projects
[Manifold Learning for Source Separation in Confusion-Limited Gravitational-Wave Data](https://github.com/jericho-cain/cwt-manifold-grav-wav).

The Laser Interferometer Space Antenna (LISA) will observe gravitational waves in a regime that differs sharply from what ground-based detectors such as LIGO handle. Instead of searching for rare signals buried in loud instrumental noise, LISA's main challenge is that its data stream contains millions of unresolved galactic binaries. These blend together into a confusion background, and the problem becomes distinguishing sources that genuinely stand out from that sea of signals. In this work we explore whether manifold-learning tools can help with that separation task. We built a CNN autoencoder trained solely on the confusion background and used its reconstruction error, but also sought to take advantage of the geometric structure that forms in the latent space. To do this, we added a simple manifold-based normalization term to the anomaly score. The model was trained on synthetic LISA data including both instrumental noise and the unresolved confusion signal, and then tested on datasets where resolvable sources such as massive black hole binaries, extreme mass ratio inspirals, and individual galactic binaries were injected. A grid search over $\alpha$ and $\beta$ in the combined score,
\(
\alpha \cdot \mathrm{AE}_{\mathrm{error}} + \beta \cdot \mathrm{manifold}_{\mathrm{norm}},
\)
revealed the best performance near $\alpha = 0.5$ and $\beta = 2.0$. This indicates that the latent-space geometry provides more discriminatory information than the raw reconstruction error. With this combination, the method reaches an AUC of $0.752$, with precision $0.81$ and recall $0.61$, which is roughly a $35\%$ improvement over using the autoencoder alone. The comparatively large weight on the manifold term ($\beta = 2.0$) suggests that the latent space is not merely a training artifact but carries a meaningful geometric imprint of the confusion background. Overall, these results show that manifold-learning techniques could be a practical addition to LISA data-analysis pipelines, helping isolate resolvable sources within a heavily confusion-limited dataset.



[Gravitational Wave Hunting with CWT-LSTM Autoencoder in LIGO Data](https://github.com/jericho-cain/cwt-lstm-ae-grav-wav). 

Gravitational wave detection requires sophisticated signal processing to identify weak astrophysical signals buried in instrumental noise. Traditional matched filtering approaches face computational challenges with diverse signal morphologies and non-stationary noise. This work presents an unsupervised deep learning methodology integrating Continuous Wavelet Transform (CWT) preprocessing with Long Short-Term Memory (LSTM) autoencoder architecture for template-free gravitational wave detection. The CWT provides optimal time-frequency decomposition capturing chirp evolution and transient characteristics essential for compact binary coalescence identification. We train and evaluate our model on LIGO H1 data from Observing Run 4 (O4, 2023--2024), comprising 102 confirmed gravitational wave events from the GWTC-4.0 catalog and 1991 noise segments. During development, we discovered that reconstruction errors from multi-run training (O1--O4) clustered by observing run rather than astrophysical parameters, revealing systematic batch effects from GWOSC's evolving calibration procedures. Following LIGO's established practice of per-run optimization, we adopted single-run (O4) training, which eliminated these batch effects and improved recall from 52\% to 96\% while maintaining 97\% precision. The final model achieves exceptional performance on O4 test data: 97.0\% precision, 96.1\% recall, F1-score 96.6\%, and ROC-AUC 0.994 (102 test signals, 399 noise segments). The reconstruction error distribution shows clean unimodal separation between noise (mean 0.48) and signals (mean 0.77), with only 4 missed detections and 3 false alarms. This unsupervised, template-free approach demonstrates that anomaly detection can achieve performance competitive with supervised methods while enabling discovery of signals with unexpected morphologies beyond current theoretical models. Our identification and resolution of cross-run batch effects provides methodological guidance for future machine learning applications to multi-epoch gravitational wave datasets.

---
[← Back to Home](/)
