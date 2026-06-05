# 大模型公平招聘与偏见消除系统

本项目为《人工智能的伦理与治理》期末作业项目。系统针对生成式AI在简历筛选与招聘环节中继承并放大的历史社会偏见（性别、年龄、地域等），设计并实现了一个外围式的偏见消除系统。

---

## 系统文件架构

项目采用模块化架构设计，文件结构如下：

```text
AI_ethics_final/
│
├── .gitignore         # Git忽略配置文件
├── config.py          # 配置文件
├── utils/             # 核心模块目录
│   ├── __init__.py
│   ├── resume_desensitize.py           # 模块1：简历脱敏模块
│   ├── biased_words_detection.py       # 模块2：偏见词检测过滤模块
│   └── algorithm_evaluate.py           # 模块3：算法透明度报告生成模块
│
├── gradio_demo.py     # 系统主入口：基于 Gradio 驱动的 Web 交互界面
├── test/              # 测试用例目录
│   ├── job.txt        # 测试用例：职位描述文本文件
│   └── resume.txt     # 测试用例：简历文本文件
│
└── requirements.txt   # 项目依赖声明文件
```
---
## 核心模块设计及功能说明
### 模块1：简历脱敏模块（resume_desensitize.py）
功能：对输入的简历文本进行脱敏处理，隐去可能引入偏见的个人信息（如姓名、性别、年龄、地域等）。
技术实现：使用正则表达式识别并替换敏感信息，确保后续处理基于更中立的文本输入。
### 模块2：偏见词检测过滤模块（biased_words_detection.py）
功能：检测并过滤简历中可能引入偏见的词汇或表达，确保后续处理基于更中立的文本。
技术实现：构建一个包含常见偏见词汇的词库，使用文本分析方法识别并替换这些词汇，减少潜在的偏见影响。
### 模块3：算法透明度报告生成模块（algorithm_evaluate.py）
功能：分析和评估简历筛选算法的决策过程，生成透明度报告，帮助用户理解算法的决策依据和潜在偏见。
技术实现：通过分析算法的输入输出关系，识别可能存在的偏见因素，并生成易于理解的报告，提升系统的透明度和用户信任度。

---
## 部署与运行说明
### 克隆仓库与环境配置
克隆仓库并进入项目目录：
```bash
git clone https://github.com/chenxin1209/AI_ethics_final.git
cd AI_ethics_final
``` 
确保本地已安装 Python 3.10 或以上版本，在项目根目录下执行以下命令安装依赖：
```bash
pip install -r requirements.txt
``` 
### 配置环境变量
Windows(CMD):
```cmd
set DEEPSEEK_API_KEY=sk-xxxxxx
```
Windows(PowerShell):
```powershell
$env:DEEPSEEK_API_KEY="sk-xxxxxx"
```
Linux/MacOS(Bash):
```bash
export DEEPSEEK_API_KEY=sk-xxxxxx
``` 
### 运行系统
在项目根目录下执行以下命令启动 Gradio Web 界面：
```bash
python gradio_demo.py
```
---
## 测试用例
测试用例位于 `test/` 目录下，使用Gemini生成，包含简历文本文件`resume.txt`以及职位描述文件`job.txt`。用户可以通过 Gradio 界面上传这些测试用例，验证系统的脱敏和偏见过滤效果，并查看生成的算法透明度报告。
---
## 许可
本项目采用MIT许可证
