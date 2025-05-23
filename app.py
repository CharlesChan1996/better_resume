import pdfplumber
import gradio as gr
from langchain_community.llms import Ollama
from langchain.prompts import ChatPromptTemplate

# 初始化本地Ollama模型
llm = Ollama(model="qwen2.5:7b")

# 定义提示词模板
prompt_template = ChatPromptTemplate.from_template("""
你是一个简历优化专家，可以根据职位描述优化简历内容。

你将会获得以下两部分内容：

[简历文本开始]
{resume_text}
[简历文本结束]

[职位描述文本开始]
{job_description}
[职位描述文本结束]

功能：
1. 分析职位描述中的关键要求。
2. 优化简历文本内容，使其更匹配职位描述。
3. 提供结构化的优化结果。

优化原则：
- 保持原始事实准确性
- 使用更相关的关键词
- 突出与职位相关的成就
- 使用更有力的动作动词
- 检查修改是否存在错别字

请注意:
在某些泛化的非具体实际的技能类的需求，可以尽可能的填入以满足用人单位的需求。
例如：具有团队合作精神，能够与团队成员有效沟通；具备较强的问题分析及解决能力，能够快速适应新环境
类似这种比较宽泛的要求，可以尽可能写入简历和需求相一致

然而，特定的技能需求无法保持一致时，则不能编造：
例如简历中从未描述过会使用docker，则不能在简历中编造


输出要求：
请返回优化后的简历内容，保持原有的结构框架
提取里面的纲要信息，例如：个人信息、教育经历、工作经历、项目经历等
并在每个部分的开头添加标题层级标记


最后，请说明目前简历与岗位描述的匹配情况的评价，并给出优化前后的对比分析表
"""
)

# 创建处理链
chain = prompt_template | llm

def extract_text_from_pdf(pdf_file):
    """从PDF文件中提取结构化文本"""
    if pdf_file is None:
        return ""
    
    structured_text = []
    with pdfplumber.open(pdf_file.name) as pdf:
        for page in pdf.pages:
            # 提取页面文本并保留布局信息
            text = page.extract_text(
                x_tolerance=1,
                y_tolerance=1,
                keep_blank_chars=False,
                layout=True
            )
            structured_text.append(text)
    
    # 添加标题层级标记
    return "\n\n".join(structured_text)

def process_resume(pdf_file, job_description):
    """处理简历优化的主函数"""
    if not pdf_file or not job_description:
        return "请上传简历PDF并输入岗位描述"
    
    try:
        resume_text = extract_text_from_pdf(pdf_file)
        result = chain.invoke({
            "resume_text": resume_text,
            "job_description": job_description
        })
        return result
    except Exception as e:
        return f"处理出错: {str(e)}"

# 创建Gradio界面
with gr.Blocks(title="简历改写助手" ) as demo:
    gr.Markdown("## 简历改写助手")
    with gr.Row():
        with gr.Column(scale=1):
            pdf_upload = gr.File(label="上传简历(PDF)", type="filepath")
            job_desc = gr.Textbox(label="岗位描述", lines=10, placeholder="请输入岗位描述...")
            submit_btn = gr.Button("改写简历", variant="primary")
        with gr.Column(scale=2):
            result = gr.Markdown(label="优化结果")
    
    submit_btn.click(
        fn=process_resume,
        inputs=[pdf_upload, job_desc],
        outputs=result
    )

if __name__ == "__main__":
    demo.launch()