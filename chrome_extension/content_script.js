// content script 示例：当用户在卖家后台打开跟卖草稿页面时，我们可以尝试寻找表单并预填
// 说明：此脚本仅做预填草稿（不会自动提交），用户需手动确认并发布
(async function() {
  console.log("七彩星光 跟卖助手 已加载");
  // 示例：尝试从 localStorage 或 extension storage 获取草稿数据（这里假设已注入）
  // TODO: 实际使用时通过 extension message 将具体跟卖数据传到 content script
  // 下面为伪代码演示如何预填
  function prefillForm(data) {
    try {
      // 根据卖家后台页面的 form 字段选择器进行选择并赋值
      let priceInput = document.querySelector('input[name="price"]');
      if (priceInput && data.price) priceInput.value = data.price;
      let titleInput = document.querySelector('input[name="title"]');
      if (titleInput && data.title) titleInput.value = data.title;
      // 图片/详情必须由用户手动上传或使用平台允许的接口
      console.log("已预填跟卖草稿（请人工确认并提交）");
    } catch (e) {
      console.error("预填失败", e);
    }
  }
  // 示例触发：页面加载 2 秒后尝试预填（演示）
  setTimeout(() => {
    // 这里的 sampleData 在真实扩展中从后台或用户操作传入
    const sampleData = { price: "999.00", title: "七彩星光跟卖草稿示例" };
    prefillForm(sampleData);
  }, 2000);
})();
