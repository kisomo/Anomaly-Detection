#  Anomaly-Detection
In this repo we explore different Anomaly detection algorithms and compare their performance using various metrics. 
## 1). Autoencoder
Autoencoder is a bottle-neck type neural network that learns a compressed representation of the data by projecting it
down to a lower dimension.
Autoencoders are trained on normal data to learn the representation of the normal state. During inference, 
if an input significantly deviates from this learned representation, the AutoEncoder will likely reconstruct it poorly. 
and this poor reconstruction is a signal of an anomaly.
## 2). One-Class SVM
It works by learning a decision boundary around the training data, which is assumed to represent the "normal" behavior. 
The algorithm maps data into a high-dimensional space using a kernel function and then finds a hyperplane that maximally 
separates the origin from the normal data points, enclosing them within a boundary. Any new data point falling outside this 
boundary is classified as an anomaly. The algorithm is effective in high-dimensional spaces and when anomalies are rare and 
distinctly different from normal data.
## 3). Isolation Forest
It works by recursively partitioning the data using random feature splits to construct a tree structure. Anomalies, 
being few and distinct, tend to be isolated quickly with fewer splits, resulting in shorter path lengths in the tree. 
The algorithm builds an ensemble of such random trees (a forest) and calculates the average path length for each data point 
across the trees. Points with shorter average path lengths are more likely to be anomalies. This approach is computationally 
efficient and effective for high-dimensional datasets.
## 4). Local Outlier Factor (LOF)
It  detects anomalies by measuring the local density of data points and identifying those with significantly lower
density compared to their neighbors. For each data point, LOF calculates a "local reachability density" based on the distance
to its nearest neighbors and compares this density with the densities of those neighbors. Points with a substantially lower 
density relative to their neighbors are considered anomalies, as they are less similar to their surrounding data. LOF is effective 
for datasets with varying density regions, as it focuses on local context rather than a global threshold for anomaly detection.
## 5). Conlusion
 SVM performs very well.
 Hyper-parameter tunning is needed in all the algorithms to improve performance.
 The dataset was highly imbalanced and therefore micro-averaging was used.




