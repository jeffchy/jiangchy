---
title: 'Machine Learning Note(一)'
date: 2017-01-27 16:04:09
tags:
- Machine Learning
categories:
- Note
---
<!-- more -->
### Supervised Learning
supervised learning algorithm：知道正确的结果，并且借此计算出更多的正确结果。是一种**回归问题**
classification：分类问题，用来解决Discrete valued output，如通过一个已经有的肿瘤大小-肿瘤类型的数据来估算出他为恶性、非恶性肿瘤的概率
feature：衡量数据的特征，一个角度下的数据
support vector machine： deal with infinite number of feature.
# 关于监督学习 Supervised learning：摘自Coursera课程材料：
In supervised learning, we are given a data set and already know what our correct output should look like, having the idea that there is a relationship between the input and the output.
Supervised learning problems are categorized into "regression" and "classification" problems.

### Unsupervisor Learing
并没有在一开始给一个明确的数据。应用于，市场细分，社交网络分析
Unsupervised learning allows us to approach problems with little or no idea what our results should look like. We can derive structure from data where we don't necessarily know the effect of the variables.
We can derive this structure by **clustering** the data based on relationships among the variables in the data.

### Linear regression
监督学习的过程：通过一个**Learning Algorithm**学习一个**training set**，得到一个方法，将input转化为最符合的output

cost function(square error function),一个能够表示数据的回归程度(拟合程度)的目标函数，We can measure the accuracy of our hypothesis function by using a cost function.  
hypothesis&cost function

### CONTOUR PLOT
A contour plot is a graph that contains many contour lines. A contour line of a two variable function has a constant value at all points of the same line. An example of such a graph is the one to the right below.
Plotting those values on our graph to the right seems to put our point in the center of the inner most 'circle'.

### Gradient Descent(梯度下降法)
[coursera](https://www.coursera.org/learn/machine-learning/supplement/2GnUg/gradient-descent)