import pytest
from src import code4

# 例外処理がうまく動作するかのtest
def test_user_name_validation():
    with pytest.raises(ValueError) as e:
        code4.user_name_validation(None)

    assert str(e.value) == "名前が設定されていません"

    # # これでもメッセージなしならこれでok
    # with pytest.raises(ValueError):
    #     code4.user_name_validation(None)

