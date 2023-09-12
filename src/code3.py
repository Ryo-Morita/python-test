# モック
import requests

def get_json_data(id):
    '''
        動かない関数
        サーバーがまだ動いてないなどの想定
    '''
    res = requests.get("http://xxxx", params = {"id":id})
    res_json = res.json()
    return res_json

def get_user_names(user_ids):
    user_names = {}
    for id in user_ids:
        json_data = get_json_data(id) # 関数呼び出し
        user_names[id] = json_data["name"]
    return user_names