"""
导出模块（TXT），每个文件 500 行，8 列（TAB 分隔）
确保不重复：需要数据库或已导出 ID 集合，这里示例使用本地 SQLite/简单文件记录
"""
import os
import math
import sqlite3
from datetime import datetime

DB = "qcsx.db"
EXPORT_DIR = "exports"
os.makedirs(EXPORT_DIR, exist_ok=True)

def init_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("""
    CREATE TABLE IF NOT EXISTS exported_items (
        sku TEXT PRIMARY KEY,
        exported_at TEXT
    )
    """)
    conn.commit()
    conn.close()

def already_exported(sku):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("SELECT 1 FROM exported_items WHERE sku = ?", (sku,))
    r = c.fetchone()
    conn.close()
    return r is not None

def mark_exported(skus):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    now = datetime.utcnow().isoformat()
    for s in skus:
        c.execute("INSERT OR IGNORE INTO exported_items (sku, exported_at) VALUES (?,?)", (s, now))
    conn.commit()
    conn.close()

def export_items(items):
    """
    items: list of dict with keys A..H as specified
    每 500 行拆分一个文件
    """
    init_db()
    unique_items = [it for it in items if not already_exported(it['E'])]
    total = len(unique_items)
    if total == 0:
        print("没有新商品要导出")
        return []
    parts = math.ceil(total / 500)
    filenames = []
    for i in range(parts):
        chunk = unique_items[i*500:(i+1)*500]
        fname = os.path.join(EXPORT_DIR, f"qcsx_export_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}_part{i+1}.txt")
        with open(fname, "w", encoding="utf-8") as f:
            for it in chunk:
                # A..H -> name,url,price,weight,sku,cart_conv,return_rate,sold_count
                line = "\t".join([
                    it.get("A",""),
                    it.get("B",""),
                    it.get("C",""),
                    it.get("D",""),
                    str(it.get("E","")),
                    str(it.get("F","")),
                    str(it.get("G","")),
                    str(it.get("H","")),
                ])
                f.write(line + "\n")
        filenames.append(fname)
        mark_exported([it['E'] for it in chunk])
    return filenames

if __name__ == "__main__":
    # 测试导出
    sample_items = []
    for i in range(3):
        sample_items.append({
            "A": f"商品{i}",
            "B": f"https://www.ozon.ru/product/{1000+i}",
            "C": "523人民币/7653卢布",
            "D": "123克/0.123千克",
            "E": str(52363781 + i),
            "F": "47%",
            "G": "5%",
            "H": str(10+i),
        })
    print(export_items(sample_items))
