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

## Latest Project

[Gravitational Wave Hunting with CWT-LSTM Autoencoder in LIGO Data](https://github.com/jericho-cain/cwt-lstm-ae-grav-wav). 

Gravitational wave detection requires sophisticated signal processing to identify weak astrophysical signals buried in instrumental noise. Traditional matched filtering approaches face computational challenges with diverse signal morphologies and non-stationary noise. This work presents an unsupervised deep learning methodology integrating Continuous Wavelet Transform (CWT) preprocessing with Long Short-Term Memory (LSTM) autoencoder architecture for template-free gravitational wave detection. The CWT provides optimal time-frequency decomposition capturing chirp evolution and transient characteristics essential for compact binary coalescence identification. We train and evaluate our model on LIGO H1 data from Observing Run 4 (O4, 2023--2024), comprising 102 confirmed gravitational wave events from the GWTC-4.0 catalog and 1991 noise segments. During development, we discovered that reconstruction errors from multi-run training (O1--O4) clustered by observing run rather than astrophysical parameters, revealing systematic batch effects from GWOSC's evolving calibration procedures. Following LIGO's established practice of per-run optimization, we adopted single-run (O4) training, which eliminated these batch effects and improved recall from 52\% to 96\% while maintaining 97\% precision. The final model achieves exceptional performance on O4 test data: 97.0\% precision, 96.1\% recall, F1-score 96.6\%, and ROC-AUC 0.994 (102 test signals, 399 noise segments). The reconstruction error distribution shows clean unimodal separation between noise (mean 0.48) and signals (mean 0.77), with only 4 missed detections and 3 false alarms. This unsupervised, template-free approach demonstrates that anomaly detection can achieve performance competitive with supervised methods while enabling discovery of signals with unexpected morphologies beyond current theoretical models. Our identification and resolution of cross-run batch effects provides methodological guidance for future machine learning applications to multi-epoch gravitational wave datasets.

---
[← Back to Home](/)
