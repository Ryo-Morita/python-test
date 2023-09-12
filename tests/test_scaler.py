from src.scaler import MyStandardScaler
import numpy as np

# test前にする処理をsetupというらしい。
# 以下のsetupはpytestのお作法になっているわけでなないので、注意(Xを毎回定義しているので面倒な形になってる)

class TestMyStandardScaler(object):
    def test_mu(self):
        X = np.array([[-1,-2,-3],[0,0,0],[1,2,3]])
        scaler = MyStandardScaler()
        scaler.fit(X)
        assert np.all(scaler._mu == np.array([0,0,0]))

    def test_fit_transform(self):
        X = np.array([[0,0,0],[2,2,2]])
        scaler = MyStandardScaler()
        ret = scaler.fit_transform(X)
        assert np.all(ret == np.array([[-1,-1,-1],[1,1,1]]))
