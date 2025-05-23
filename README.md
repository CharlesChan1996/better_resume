# 简历优化助手

一个基于AI的简历优化工具，能够根据职位描述自动优化简历内容，提高简历与岗位的匹配度。

## ✨ 功能特点

- 上传PDF格式简历
- 输入目标职位描述
- 自动分析并优化简历内容
- 提供修改前后的对比
- 评估简历与岗位的匹配度

## 🛠️ 技术栈

- **前端界面**: Gradio
- **AI模型**: 本地运行的Ollama (qwen2.5:7b模型)
- **处理框架**: LangChain
- **PDF解析**: pdfplumber

## ⚙️ 安装指南

### 前置要求
- Python 3.8+
- Ollama服务已安装并运行

1. 克隆本仓库
   ```bash
   git clone https://github.com/yourusername/resume-optimizer.git
   cd resume-optimizer
   ```

2. 安装Python依赖
   ```bash
   pip install -r requirements.txt
   ```

3. 下载AI模型
   ```bash
   ollama pull qwen2.5:7b
   ```

## 🚀 使用方法

1. 启动应用
   ```bash
   python app.py
   ```

2. 在浏览器中打开显示的本地地址(通常是`http://127.0.0.1:7860`)

3. 使用界面:
   - 上传PDF格式简历
   - 输入目标职位描述
   - 点击"改写简历"按钮
   - 查看优化结果

## 📝 注意事项

1. 需要本地安装并运行Ollama服务
2. 确保已下载qwen2.5:7b模型
3. 建议在修改前备份原始简历
4. 最终结果仍需人工审核确认
5. 首次运行可能需要较长时间加载模型

## 📜 示例截图

![界面截图](screenshot.png) *(请替换为实际截图)*

## 🤝 贡献指南

欢迎通过以下方式贡献本项目：
1. 提交Issue报告问题或建议
2. Fork仓库并提交Pull Request
3. 改进文档或翻译

## 📄 许可证

本项目采用 [MIT License](LICENSE) 开源协议