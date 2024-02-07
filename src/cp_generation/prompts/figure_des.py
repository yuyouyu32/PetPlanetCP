from .prompt_template import *

SystemPromptTemplate = CustomPromptTemplate.from_template("")
content_req = """我会提供给你明信片图片的名称，你需要给我描述明信片图片其中的内容"""
TaskPromptTemplate = CustomPromptTemplate.from_template("""
{content_prompt}
景点: {name}
内容需要控制在40-60字。
明信片图片描述：
""")