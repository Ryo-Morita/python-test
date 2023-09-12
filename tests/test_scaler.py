from src.scaler import MyStandardScaler
import numpy as np

# test前にする処理をsetupというらしい。
# 以下のsetupはpytestのお作法になっているわけでなないかも。
# .setup_class()で事前の処理を書けるっぽい
# classmethodの第一引数はlcsになっているが、selfと意味は一緒(というか慣例的にclsとしているだけで、hogeとしてもいい)

class TestMyStandardScaler(object):
    @classmethod
    def setup_class(cls):
        print("Start")
        cls.scaler = MyStandardScaler()
        cls.X1 = np.array([[-1,-2,-3],[0,0,0],[1,2,3]])
        cls.X2 = np.array([[0,0,0],[2,2,2]])

    def test_mu(self):
        self.scaler.fit(self.X1)
        assert np.all(self.scaler._mu == np.array([0,0,0]))

    def test_fit_transform(self):
        ret = self.scaler.fit_transform(self.X2)
        assert np.all(ret == np.array([[-1,-1,-1],[1,1,1]]))
