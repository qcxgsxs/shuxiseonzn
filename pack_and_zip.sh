#!/bin/bash
# pack_and_zip.sh
# 打包 Chrome/Edge 扩展与 assets 到 dist/shuxiseonzn-extension.zip
# 在仓库根目录运行：
#   chmod +x pack_and_zip.sh
#   ./pack_and_zip.sh

set -e
DIST_DIR=dist
EXT_DIR=chrome_extension
ASSETS_DIR=assets
OUT_ZIP=${DIST_DIR}/shuxiseonzn-extension.zip

rm -rf "$DIST_DIR"
mkdir -p "$DIST_DIR"

# Ensure manifest and assets exist
if [ ! -d "$EXT_DIR" ]; then
  echo "Error: ${EXT_DIR} directory not found" >&2
  exit 1
fi
if [ ! -d "$ASSETS_DIR" ]; then
  echo "Warning: ${ASSETS_DIR} directory not found. Proceeding without assets." >&2
fi

# Copy files to a temporary folder to preserve structure
TMP_DIR="${DIST_DIR}/tmp_package"
rm -rf "$TMP_DIR"
mkdir -p "$TMP_DIR"

cp -r "$EXT_DIR"/* "$TMP_DIR/"
if [ -d "$ASSETS_DIR" ]; then
  cp -r "$ASSETS_DIR" "$TMP_DIR/"
fi

# Create zip
cd "$DIST_DIR"
zip -r "$(basename "$OUT_ZIP")" tmp_package/* > /dev/null
cd - > /dev/null
rm -rf "$TMP_DIR"

echo "Created $OUT_ZIP"
