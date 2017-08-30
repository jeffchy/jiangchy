---
title: Machine Learning Note (ii)
date: 2017-02-04 23:36:16
tags:
- Machine Learning
categories:
- Note
---
<!-- more -->
### Gradient Decent的优化
# Feature scaling
get every feature into approximately in -1 and 1 to make the gradient decent converge more quickly.
# mean normalization
x = x - u(mean)
mean normalization (x - u) / (max - min)
# how to judge if an learning rate is well enough
plot the cost function corresponding to times of iterations.
alpha too small: slow converge
alpha too big: cannot converge

# narmal equations
![alt](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/dykma6dwEea3qApInhZCFg_333df5f11086fee19c4fb81bc34d5125_Screenshot-2016-11-10-10.06.16.png?expiry=1486425600000&hmac=ayW0nzCcyQm-vwcdnwgOQbQy8gRoN_IAr-54Q1qG63o)
有的数据情况下不工作。
就是直接用最小二乘法算出结果，不需要迭代，不需要选择learning rate。但是复杂度为O(n3),所以数据过大的时候使用梯度下降比较好。
method to solve for theta analytically
# how to solve?
least square 
直接算出来 A'Ax = A'b 
注意，上图中的X'X如果没有inverse怎么办呢？
没有inverse说明，X本身有线性相关的列，所以删掉一些线性相关的列就可以了，或者是有太多的features，数据不够多，即m<n。
**X’X is invertible if X is invertible**