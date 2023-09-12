# python-test
- https://www.youtube.com/watch?v=Hl8UNYrp0Vg&list=WL&index=1&t=906s
- python 3.9で実行

単一のtestコードを実施する場合
```
cd python-test/tests
pytest test_code.py
``````

フォルダ内の全testコードを実施する場合
```
pytest 
``````

以下のようなメッセージが出るので、全部passしていればok
```
=================================================================== test session starts ====================================================================
platform darwin -- Python 3.9.4, pytest-6.2.3, py-1.10.0, pluggy-0.13.1
rootdir: /Users/ryo.morita/python/python-test/tests
plugins: anyio-2.2.0
collected 7 items 
test_code.py 

中略

==================================================================== 7 passed in 1.13s =====================================================================
```