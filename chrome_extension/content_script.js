// content script 示例：当用户在卖家后台打开跟卖草稿页面时，我们可以尝试寻找表单并预填
// 说明：此脚本仅做预填草稿（不会自动提交），用户需手动确认并发布
(async function() {
  console.log("七彩星光 跟卖助手 已加载");
  function prefillForm(data) {
    try {
      let priceInput = document.querySelector('input[name="price"]');
      if (priceInput && data.price) priceInput.value = data.price;
      let titleInput = document.querySelector('input[name="title"]');
      if (titleInput && data.title) titleInput.value = data.title;
      // 将其他商家图片/描述作为参考提示插入页面
      if (data.reference_html) {
        const container = document.createElement('div');
        container.style.border = '2px dashed #fff3';
        container.style.padding = '8px';
        container.style.marginTop = '8px';
        container.style.background = 'rgba(0,0,0,0.35)';
        container.innerHTML = '<strong>参考内容（请手动核验与上传）：</strong>' + data.reference_html;
        document.body.prepend(container);
      }
      console.log("已预填跟卖草稿（请人工确认并提交）");
    } catch (e) {
      console.error("预填失败", e);
    }
  }

  setTimeout(() => {
    const sampleData = { price: "999.00", title: "七彩星光跟卖草稿示例", reference_html: '<p>示例参考图片/描述</p>' };
    prefillForm(sampleData);
  }, 2000);
})();
