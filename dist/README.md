七彩星光 — 仓库发布包说明

此目录包含用于分发的“ready-to-upload” 内容。由于当前我无法直接把扩展提交到 Chrome Web Store（需要你的 service-account JSON 或在商店内邀请协作者），我已把“可上架材料”整理并提交到仓库，便于你或任何被授权的人立即下载并在本地上传到商店。

位置：/dist/

包含内容说明：
- pack_and_zip.sh  —— 用于在仓库根目录将 chrome_extension/ 与 assets/ 打包为 dist/shuxiseonzn-extension.zip。
- upload_chrome.py —— 自动上传脚本（需 Google service-account JSON）。
- store_metadata.md —— 上架元数据草稿（标题/描述/权限/隐私声明）。
- privacy_policy.md —— 隐私政策模板（建议托管为公开 URL，例如 GitHub Pages）。

快速下载与本地上架步骤（若你不需要我代为提交）
1. 在仓库页面点击 Code -> Download ZIP，或 clone 仓库到本地。
2. 在本地运行：
   chmod +x pack_and_zip.sh
   ./pack_and_zip.sh
   这会生成 dist/shuxiseonzn-extension.zip
3. 登录 Chrome Web Store Developer Dashboard，创建新 item，上传 dist/shuxiseonzn-extension.zip，填写 store_metadata.md 中的字段并提交审核。
4. 对于 Edge，登录 Microsoft Partner Center，创建新 add-on 并上传同样的 zip。

我已在仓库的 main 分支创建了这个 dist/ 目录的说明文件；实际的 zip 需要在本地运行 pack_and_zip.sh 生成，或你授权给我代为上传并 publish（需要你通过安全通道提供凭证或在控制台添加协作者）。

仓库 dist 路径： https://github.com/qcxgsxs/shuxiseonzn/tree/main/dist

我会在此对话第一时间通知你任何进一步的发布动作或当你授权我代表你上传到商店并完成上架时把商店公开链接发给你。