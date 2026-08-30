# 七彩星光（shuxiseonzn）

这是七彩星光（QCSX）Ozon/onzn 数据分析器与 AI 跟单插件的私有仓库骨架。

说明与注意事项：
- 本项目以合规为前提。任何访问卖家后台的敏感指标（购物车转换率、退货率、真实销量）必须由用户本人授权（提供卖家 API Key 或通过浏览器扩展在已登录的会话中抓取）。
- 公共页面抓取请遵守 robots.txt、平台服务条款与速率限制。
- 插件生成的跟卖草稿必须由用户手动确认并执行，插件不会自动提交发布。

结构概览：
- scraper.py        # 抓取器骨架（API 模式优先，页面抓取为备用）
- analyzer.py       # 筛选/违禁检测逻辑
- exporter.py       # 导出 TXT（每 500 行一文件）并去重
- currency_converter.py # 汇率转换模块（CNY ↔ RUB）
- ai_monitor.py     # AI 监控调度示例
- chrome_extension/ # 浏览器扩展骨架（manifest + content_script）
- requirements.txt  # 依赖
- README.md (this file)

如何运行（快速起步）
1. 克隆仓库到本地。
2. 创建并填写 `.env` 文件（如果使用 API 模式，填写 OZON_API_KEY、SAMPLE_URL 或 SAMPLE_SKU）。
3. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```
4. 运行示例抓取：
   ```bash
   python scraper.py
   ```

下一步：我会在仓库里继续提交更多模块、前端仪表盘模板、扩展打包说明和详细的部署/上架指南。请确认是否希望我继续往该 repo 推送并在 push 后给出运行示例。