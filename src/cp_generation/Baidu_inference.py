import json
import requests

# Baidu
def get_access_token():
    """
    使用 API Key，Secret Key 获取access_token，替换下列示例中的应用API Key、应用Secret Key
    """
        
    url = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=uEFcOQL51OpXMejaB5NLl2B5&client_secret=itckeuCsN5Ffq0Yy13EjhtImjvg1GVjt"
    
    payload = json.dumps("")
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json().get("access_token")
    
def get_copywriter_from_Baidu(sys_prompt: str, user_prompt: str):
    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions_pro?access_token=" + get_access_token()
    
    payload = json.dumps({
        "messages": [
            {
                "role": "user",
                "content": user_prompt
            }
        ]
        ,
        "system": sys_prompt
    })
    headers = {
        'Content-Type': 'application/json'
    }
    
    response = requests.request("POST", url, headers=headers, data=payload)
    copyright = response.json().get("result")
    total_tokens = response.json().get("usage").get("total_tokens")
    cost = 0.12 * total_tokens / 1000
    return copyright, cost
