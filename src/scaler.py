# 実践的なコードでtestしてみたい
import numpy as np
import pandas as pd

class MyStandardScaler():
    def __init__(self):
        self._mu = None
        self._sigma = None

    def fit(self, X:np.ndarray):
        self._mu = np.mean(X, axis = 0)
        self._std = np.std(X, axis = 0)
        return self
        
    def transform(self, X:np.ndarray)->np.ndarray:
        ret = (X - self._mu) / self._std
        return ret
    
    def fit_transform(self, X):
        self.fit(X)
        return self.transform(X)
    
# s = MyStandardScaler()
# X = np.array([[-1,-2,-3],[0,0,0],[1,2,3]])
# X = np.array([[0,0,0],[2,2,2]])
# ret = s.fit_transform(X)
# print(s._mu)
# print(ret)