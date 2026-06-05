# 简历脱敏模块
import re

def desensitize_resume(text):
    """
    通过正则表达式对简历进行脱敏与匿名化处理，剥离不相关的社会学关联特征
    """
    if not text:
        return ""

    text = re.sub(r'\d{17}[\dXx]|\d{15}', '【身份证号已隐藏】', text)
    text = re.sub(r'(性别[:：]?\s*)(男|女)', r'\1【性别已隐藏】', text)
    text = re.sub(r'(出生年月|年龄)[:：]?\s*([^\n]+)', r'\1：【年龄与出生年月已隐藏】', text)
    text = re.sub(r'(籍贯|民族|出生地)[:：]?\s*[\u4e00-\u9fa5]{2,5}', r'\1【地域特征已隐藏】', text)
    
    return text