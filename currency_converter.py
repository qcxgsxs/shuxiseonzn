"""
简单汇率转换：使用 exchangerate.host（免费、无 API key）或替换为你信任的汇率服务。
"""
import requests

API = "https://api.exchangerate.host/latest"

def convert(amount: float, from_currency: str, to_currency: str):
    resp = requests.get(API, params={"base": from_currency, "symbols": to_currency})
    resp.raise_for_status()
    data = resp.json()
    rate = data["rates"][to_currency]
    return amount * rate, rate

if __name__ == "__main__":
    val, rate = convert(100, "CNY", "RUB")
    print(f"100 CNY = {val:.2f} RUB (rate={rate})")
