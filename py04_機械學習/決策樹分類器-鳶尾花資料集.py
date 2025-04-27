import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.decomposition import PCA

# 載入資料與降維
iris = load_iris()
X = iris.data
y = iris.target
target_names = iris.target_names

pca = PCA(n_components=2)
X_reduced = pca.fit_transform(X)

# 訓練模型（使用2D降維後資料）
clf = DecisionTreeClassifier()
clf.fit(X_reduced, y)

# 繪製決策邊界（建立網格點）
x_min, x_max = X_reduced[:, 0].min() - 1, X_reduced[:, 0].max() + 1
y_min, y_max = X_reduced[:, 1].min() - 1, X_reduced[:, 1].max() + 1
xx, yy = np.meshgrid(np.linspace(x_min, x_max, 300),
                     np.linspace(y_min, y_max, 300))
grid = np.c_[xx.ravel(), yy.ravel()]

# 對每個網格點進行預測
Z = clf.predict(grid).reshape(xx.shape)

# 畫出區塊
plt.figure(figsize=(8, 6))
plt.contourf(xx, yy, Z, alpha=0.4, cmap=plt.cm.rainbow)

# 畫出原始資料點
for i, label in enumerate(target_names):
    plt.scatter(X_reduced[y == i, 0], X_reduced[y == i, 1],
                label=label, edgecolor='k', s=60)

plt.title("Decision Boundary (PCA-reduced Iris Data + Decision Tree)")
plt.xlabel("PCA Component 1")
plt.ylabel("PCA Component 2")
plt.legend()
plt.grid(True)
plt.show()
