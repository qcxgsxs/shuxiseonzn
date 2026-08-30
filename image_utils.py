from PIL import Image
import os

"""
image_utils.py

生成扩展/前端所需的多尺寸 icon 文件（16/48/128/512）
用法：在仓库根目录运行 `python image_utils.py`
前提：assets/icon.png 已存在（建议 512x512 PNG）

该脚本不会覆盖已存在的 icon-*-png，除非设置 OVERWRITE=True
"""

ASSETS_DIR = os.path.join(os.path.dirname(__file__), 'assets')
SRC_ICON = os.path.join(ASSETS_DIR, 'icon.png')
SIZES = [16, 48, 128, 512]
OVERWRITE = False


def generate_icons():
    if not os.path.exists(ASSETS_DIR):
        print('assets/ 目录不存在，请先上传 icon.png 与 bg*.png 到 assets/ 再运行此脚本。')
        return 1
    if not os.path.exists(SRC_ICON):
        print('未找到 assets/icon.png，请确认已上传并命名为 icon.png')
        return 2

    im = Image.open(SRC_ICON).convert('RGBA')
    for s in SIZES:
        out_path = os.path.join(ASSETS_DIR, f'icon-{s}.png')
        if os.path.exists(out_path) and not OVERWRITE:
            print(f'{out_path} 已存在（跳过）。如需覆���，将 OVERWRITE 设置为 True）')
            continue
        im_resized = im.resize((s, s), Image.LANCZOS)
        im_resized.save(out_path, format='PNG')
        print(f'已生成 {out_path}')
    return 0


if __name__ == '__main__':
    code = generate_icons()
    if code == 0:
        print('图标生成完成。请在扩展 manifest 和 frontend 中确认引用路径。')
    else:
        print('图标生成未完成（返回码', code, ')')
