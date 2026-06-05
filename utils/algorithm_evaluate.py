# 算法决策透明度生成模块
import json
from openai import OpenAI
import config

def evaluate_resume_transparently(desensitized_resume_text, job_requirement):
    """
    对脱敏简历进行无偏见能力评估，并输出结构化透明度报告
    """
    if not desensitized_resume_text or not job_requirement:
        return "请完整填写已脱敏简历和岗位需求"
    
    client = OpenAI(api_key=config.API_KEY, base_url=config.BASE_URL)
    
    # 约束模型行为与输出Schema，保障算法透明度
    system_prompt = """
    你是一位负责任的AI招聘审计官。你将收到一份经过脱敏处理的简历和一份岗位需求。
    你必须严格仅基于求职者的“专业技能、项目经验、核心产出”进行客观资历画像提取。
    严禁推测或引入任何关于性别、年龄、地域的隐性偏见。
    
    你必须严格以下列 JSON 格式输出，不要输出任何其他文本或Markdown代码块标记：
    {
        "技能匹配度": "XX%",
        "核心优势": ["优势1", "优势2"],
        "客观不足与拒绝原因": "具体列出与岗位不匹配的技术栈或经验缺口",
        "伦理合规审查声明": "本评估过程已通过代码级特征遮蔽，并严格基于能力指标推理。"
    }
    """
    
    user_content = f"【岗位需求】:\n{job_requirement}\n\n【已脱敏简历】:\n{desensitized_resume_text}"
    
    try:
        response = client.chat.completions.create(
            model=config.MODEL_NAME,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_content}
            ],
            temperature=0.2
        )
        raw_json = response.choices[0].message.content
        # 确保返回的是合规的合法JSON并格式化
        parsed = json.loads(raw_json)
        return json.dumps(parsed, ensure_ascii=False, indent=4)
    except Exception as e:
        return f"透明度报告生成失败，原因：{str(e)}。请确保模型响应了正确的JSON格式。"