import gradio as gr
# 导入解耦后的核心伦理模块
from utils.resume_desensitize import desensitize_resume
from utils.biased_words_detection import biased_words_detection
from utils.algorithm_evaluate import evaluate_resume_transparently

with gr.Blocks(theme=gr.themes.Soft(), title="公平招聘系统") as demo:
    gr.Markdown("# 大模型公平招聘与偏见消除系统")
    
    # 交互模块：招聘启事偏见检测
    with gr.Tab("招聘启事偏见检测"):
        with gr.Row():
            with gr.Column():
                jd_input = gr.Textbox(label="输入原始招聘需求 (JD)", lines=5, placeholder="例如：招后端开发工程师，限男性，35岁以下...")
                audit_btn = gr.Button("运行伦理合规审计", variant="primary")
            with gr.Column():
                warning_output = gr.Textbox(label="伦理合规警告", interactive=False)
                rewrite_output = gr.Textbox(label="重写后的合规文本", lines=5, interactive=False)
        audit_btn.click(biased_words_detection, inputs=[jd_input], outputs=[warning_output, rewrite_output])

    # 交互模块：简历脱敏与透明度审计
    with gr.Tab("简历脱敏与透明度审计"):
        with gr.Row():
            with gr.Column():
                job_req_input = gr.Textbox(label="输入目标岗位需求", lines=3, value="计算机相关专业，熟练掌握Python，有大规模分布式系统架构经验。")
                resume_input = gr.Textbox(label="输入求职者原始简历", lines=8, placeholder="张伟，男，1992年出生，籍贯山东。有5年后端开发经验...")
                desensitize_btn = gr.Button("第一步：执行数据伦理脱敏", variant="secondary")
            with gr.Column():
                desensitized_output = gr.Textbox(label="脱敏后的简历", lines=5, interactive=False)
                eval_btn = gr.Button("第二步：生成算法决策透明度报告", variant="primary")
                report_output = gr.Code(label="《算法决策透明度报告》", language="json")
                
        desensitize_btn.click(desensitize_resume, inputs=[resume_input], outputs=[desensitized_output])
        eval_btn.click(evaluate_resume_transparently, inputs=[desensitized_output, job_req_input], outputs=[report_output])

if __name__ == "__main__":
    demo.launch(server_name="127.0.0.1", server_port=7665, share=True)