from .prompt_template import *

# Kuma-间接、朴素、对比
SystemPromptTemplate = CustomPromptTemplate.from_template("你是一个明信片封面文案撰写者")
content_req = """语言风格是朴素又温暖的风格，直击人心灵深处""" 
TaskPromptTemplate = CustomPromptTemplate.from_template("""
{content_prompt}
{examples_prompt}                                                                                        
现在我们开启新的文案内容,生成的文案内容需要与我提供的图片内容高度相关。尽量使用简单的语言来朴素的表达，文案需要控制在8-15个字。
- 图片标题：{title}
- 文案: 
""")
examples = [
    """- 图片标题：海南火箭发射基地
- 图片内容：一艘火箭在夕阳的映照下升空，其尾焰在多云天空中划出亮线，下方水面反射出这一壮观景象。
- 文案：白色的尾焰照亮了整个天空""",

    """- 图片标题：台湾阴阳海
- 图片内容：黄昏时分的街角，红绿灯亮起绿色，背后是落日和彩云装点的天空，以及远处平静的海面和山脉轮廓。
- 文案：绿灯了，要向前走了""",
]

