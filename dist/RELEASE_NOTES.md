Release notes - 七彩星光 (release draft)

版本：v0.1.0 (Repository release)
发布说明：
- 初始打包：包含 Chrome/Edge 扩展代码（chrome_extension/）、前端静态页面（frontend/）、assets、以及上架所需元数据与隐私政策模板。
- 功能亮点：页面抓取器（Playwright 占位）、违禁词库、导出器、扩展草稿预填功能（仅预填，不自动提交）。

如何安装（开发者 / 本地加载）
1. 在 Chrome/Edge 打开扩展管理页面并启用“开发者模式”。
2. 选择“加载已解压的扩展”，指向仓库的 chrome_extension/ 目录。
3. 如果你希望在商店上正式发布，请使用 pack_and_zip.sh 生成 zip，并在商店后台上传。见 dist/README.md。

注：如果你希望我代为上传并直接提交商店审查，请通过安全通道把 service-account JSON（Chrome Web Store API）及 Partner Center 凭证发送给我，或在商店控制台邀请我为协作者（我将立即代理上传并发布）。
