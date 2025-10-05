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

Gravitational wave detection requires sophisticated signal processing to identify weak astrophysical signals buried in instrumental noise. Traditional matched filtering approaches face computational challenges with diverse signal morphologies and non-stationary noise. This work presents a deep learning methodology integrating Continuous Wavelet Transform (CWT) preprocessing with Long Short-Term Memory (LSTM) autoencoder architecture for gravitational wave detection. The CWT provides optimal time-frequency decomposition capturing chirp evolution and transient characteristics essential for compact binary coalescence identification. We first develop the model using synthetic datasets incorporating binary black hole merger signals with masses ranging from 10 to 80 solar masses. These signals are then embedded in colored Gaussian noise representative of Advanced LIGO sensitivity. The trained model demonstrates strong performance metrics. We then apply the CWT-LSTM model to gravitational wave data from multiple LIGO observing runs. We use 1639 clean noise samples for training the anomaly detection model, while the test dataset contained a mix of 114 confirmed gravitational wave events and 410 noise samples. The model demonstrates strong performance with an AUC of 1.000 and Average Precision (AP) of 1.000, achieving a precision of 1.0 at the optimal threshold with a recall of 1.0. The reconstruction error distribution shows clear separation between noise and gravitational wave signals, with noise samples clustering around lower reconstruction error values and signals around higher reconstruction error values. This unsupervised approach enables discovery of signals with unknown morphologies that could provide complementary "blind search" capability for detecting exotic astrophysical sources and novel physics beyond current theoretical models.

---
[← Back to Home](/)
