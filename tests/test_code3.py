# 一部関数が動作しない場合のテスト
from src import code3

def get_json_data_mock(id):
    '''
        代理の関数
    '''
    return {'name':'mogmog'}

def test_get_user_names(monkeypatch):
    monkeypatch.setattr(
        code3, # モックに差し替えたい関数のモジュール
        'get_json_data',# モックに差し替えたい関数名(文字列),
        get_json_data_mock # モックの関数
    )

    result = code3.get_user_names(['001', '009'])

    assert list(result.keys()) == ['001', '009']
    assert list(result.values()) == ["mogmog", 'mogmog']