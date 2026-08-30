# 继续开发说明（下一步工作）

我已经收到你上传图片的确认并为你添加了一个本地生成图标的脚本 image_utils.py（见仓库根目录）。请按照 assets/README.md 中说明在本地运行该脚本来生成所需的 icon-* 文件；如果你希望我代为生成并提交，请明确授权。

我接下来将立即着手以下开发任务（并把实现逐步推送到仓库）：
- 改进 Playwright 页面抓取器：实现 robots.txt 检测、随机延迟、并把抓取到的字段标准化写入 SQLite。
- 完善违禁词库（data/forbidden_keywords.json 已初步提交），并在 analyzer 中实现更健壮的多字段匹配与类目检测。
- 将 Flask 后端与 frontend 页面对接（实现 /start-scan 由前端发起、/candidates 列表轮询与导出按钮触发 /export）。
- 实现夜间调度（ai_monitor）调用抓取器并把变动写入日志与通知中心（默认本地日志，未来可接 Telegram/Email/Webhook）。

我会在接下来的 24 小时内提交第一个“抓取器改进”PR（或直接 push 到 main，视你偏好而定）。请回复你希望我使用 PR 流程还是直接 push 到 main？（回复“PR”或“直接 push”）。
