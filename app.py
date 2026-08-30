from flask import Flask, jsonify, request
import threading
import time
import os
from scraper import fetch_product_public_page
from analyzer import passes_filters
from exporter import export_items
from currency_converter import convert

app = Flask(__name__)

# 简单内存存储（后续应替换为 DB）
SCRAPED = []
CANDIDATES = []

@app.route('/start-scan', methods=['POST'])
def start_scan():
    data = request.json or {}
    url = data.get('url') or os.getenv('SAMPLE_URL')
    if not url:
        return jsonify({'error': '缺少 url'}), 400

    def _job(u):
        try:
            item = fetch_product_public_page(u)
            SCRAPED.append(item)
            ok, reasons = passes_filters(item)
            if ok:
                CANDIDATES.append(item)
        except Exception as e:
            print('扫描失败', e)

    t = threading.Thread(target=_job, args=(url,))
    t.start()
    return jsonify({'status':'started'})

@app.route('/candidates', methods=['GET'])
def get_candidates():
    # 返回简单的候选列表（供前端轮询）
    out = []
    for it in CANDIDATES:
        out.append({
            'name': it.get('name'),
            'url': it.get('url'),
            'price': it.get('price_rub'),
            'sku': it.get('sku'),
        })
    return jsonify(out)

@app.route('/export', methods=['POST'])
def do_export():
    # 导出当前候选为 TXT（最多 500 条/文件）
    items = []
    for it in CANDIDATES:
        items.append({
            'A': it.get('name',''),
            'B': it.get('url',''),
            'C': f"{it.get('price_rub','')}",
            'D': it.get('weight_g',''),
            'E': it.get('sku',''),
            'F': it.get('cart_conversion_pct',''),
            'G': it.get('return_rate_pct',''),
            'H': it.get('sold_count',''),
        })
    files = export_items(items)
    return jsonify({'exported_files': files})

@app.route('/rate', methods=['GET'])
def rate():
    # 演示人民币->卢布转换（示例）
    amount = float(request.args.get('amount', '100'))
    val, rate = convert(amount, 'CNY', 'RUB')
    return jsonify({'amount_cny': amount, 'amount_rub': round(val,2), 'rate': rate})

@app.route('/status', methods=['GET'])
def status():
    return jsonify({'scraped_count': len(SCRAPED), 'candidates': len(CANDIDATES)})

if __name__ == '__main__':
    host = os.getenv('FLASK_HOST','0.0.0.0')
    port = int(os.getenv('FLASK_PORT','5000'))
    app.run(host=host, port=port)
