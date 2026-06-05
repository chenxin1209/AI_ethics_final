# 偏见词检测模块
from openai import OpenAI
import config

def biased_words_detection(jd_text):
    """
    对HR输入的招聘启事进行算法偏见合规性审查与重写
    """
    if not jd_text:
        return "请输入招聘需求", "等待审查..."
    
    # 定义显性歧视词库（卡点机制）
    bias_keywords = ["限男性", "男性优先", "限女性", "女性优先", "35岁以下", "35岁以内", "形象气质佳", "仅限本地人"]
    found_words = [word for word in bias_keywords if word in jd_text]
    
    if found_words:
        warning_msg = f"警告：检测到涉嫌就业歧视的词汇：{', '.join(found_words)}。该表述违反劳动法公平就业原则。"
    else:
        warning_msg = "伦理初审通过：未检测到明显的显性就业歧视词汇。"

    # 初始化大模型客户端
    client = OpenAI(api_key=config.API_KEY, base_url=config.BASE_URL)
    
    # 编码《招聘伦理价值手册》
    system_prompt = """
    你是一位极致公平、践行‘科技向善’原则的资深人力资源合规审计专家。
    你的任务是审查HR输入的岗位招聘需求。如果其中含有性别、年龄、地域、外貌等歧视性表述，
    你必须将其自动重写为符合劳动法、注重包容性的合规文本。
    请直接输出重写后的文本，不要带有任何解释或前缀。
    """
    
    try:
        response = client.chat.completions.create(
            model=config.MODEL_NAME,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"请审计并重写以下招聘需求，消除隐性偏见：\n{jd_text}"}
            ],
            temperature=0.3
        )
        rewritten_text = response.choices[0].message.content
    except Exception as e:
        rewritten_text = f"对齐失败，大模型服务异常。建议手动删除不合规词汇：{found_words}。"
        
    return warning_msg, rewritten_text