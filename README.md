# Anomaly-Detection
Anomaly Detetction using Local Outlier Factor, Autoencoder and integration

![AdobeStock_106786408](https://github.com/Abdennacer-Badaoui/Anomaly-Detection/assets/106801897/d48ea556-5c6c-4fc6-9ecc-ee170ea81c57)


This project focuses on detecting anomalies in datasets using two different techniques: Local Outlier Factor (LOF) and Autoencoders. Additionally, it explores the integration of these methods to enhance anomaly detection performance.

## Introduction
Anomaly detection, also known as outlier detection, is a critical process in data analysis, used to identify data points that deviate significantly from the majority of the data. Anomalies can indicate rare events, errors, or fraud. This project implements two popular anomaly detection methods — Local Outlier Factor (LOF) and Autoencoder — and investigates their integration for improved performance.

## Techniques Used
### Local Outlier Factor (LOF)
Local Outlier Factor (LOF) is an unsupervised anomaly detection method that identifies anomalies by measuring the local density deviation of a data point with respect to its neighbors. The core idea is that anomalies are points that have a significantly lower density than their neighbors.

- Advantages:
  
Effective for detecting local anomalies.

Does not require prior labeling of data.

 - Disadvantages:
   
Sensitive to the choice of the number of neighbors.

Computationally expensive for large datasets.

### Autoencoder
An Autoencoder is a type of neural network used for unsupervised learning of efficient codings. It works by compressing the input into a lower-dimensional representation and then reconstructing the output from this representation. Anomalies are detected based on reconstruction error: the larger the error, the more likely it is an anomaly.

### Advantages:

Can capture complex patterns in data.
Effective for high-dimensional datasets.
### Disadvantages:

Requires careful tuning of network architecture and parameters.
Needs a substantial amount of normal data for training.


