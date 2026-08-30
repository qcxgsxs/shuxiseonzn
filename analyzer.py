"""
分析与筛选逻辑（示例）
- 输入：一条商品记录（字典），包含必要字段
- 输出：True/False 是否满足筛选条件，并返回不通过原因
"""
from typing import Tuple, Dict, List

# 违禁品关键字样例（需要完善，建议维护一张违禁品词表数据库）
BANNED_KEYWORDS = [
    "易燃", "酒精", "炸药", "枪", "弹药", "毒品", "麻醉", "活体", "活的", "易腐", "电池(锂电池|内置锂电池)"
]

def contains_banned(item: Dict) -> Tuple[bool, List[str]]:
    text = " ".join(filter(None, [item.get("name",""), item.get("url","")])).lower()
    hits = [kw for kw in BANNED_KEYWORDS if kw.lower() in text]
    return (len(hits)>0, hits)

def passes_filters(item: Dict, min_cart_conv_pct=5.0, max_return_pct=15.0, min_sold=3) -> Tuple[bool, List[str]]:
    reasons = []
    # 购物车转换率
    conv = item.get("cart_conversion_pct")
    if conv is None or float(conv) < min_cart_conv_pct:
        reasons.append(f"购物车转换率不足（{conv} < {min_cart_conv_pct}）")
    # 退货率
    ret = item.get("return_rate_pct")
    if ret is None or float(ret) >= max_return_pct:
        reasons.append(f"退货率过高（{ret} >= {max_return_pct}）")
    # 变体评论数
    comments = item.get("comments_count", 0)
    if comments and int(comments) > 0:
        reasons.append(f"当前变体存在评论（{comments} 条）")
    # 已售出
    sold = item.get("sold_count", 0)
    if sold is None or int(sold) <= min_sold-1:
        reasons.append(f"已售出数量不足（{sold} <= {min_sold}）")
    # 违禁检测
    banned, hits = contains_banned(item)
    if banned:
        reasons.append(f"违禁物品匹配: {hits}")
    return (len(reasons)==0, reasons)

# 简单自测
if __name__ == "__main__":
    sample = {
        "name": "示例水龙头",
        "cart_conversion_pct": 47.0,
        "return_rate_pct": 5.0,
        "comments_count": 0,
        "sold_count": 10,
    }
    ok, reasons = passes_filters(sample)
    print("通过" if ok else "不通过", reasons)
