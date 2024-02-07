from .prompt_template import *


# SystemPromptTemplate = CustomPromptTemplate.from_template("你将扮演一只贪吃有趣的拟人化猫咪，现在是冬天，正在中国各地旅行，最终的目的是回到漠河老家。")
# content_req = """现在，你需要写一张给你好友的明信片,明信片中需要描述你在{local}参与的人文活动{name}"""
# TaskPromptTemplate = CustomPromptTemplate.from_template("""
# {content_prompt}
# {examples_prompt}
# 现在我们开启新的内容，需要模仿模板中的写法，并与我提供的人文活动及其描述紧密联系。
# 人文活动: {name}
# 人文活动描述: {description}
# 语言朴素简单，有故事感，不需要加上称呼和结尾，内容中最好不要出现{local}，只需要输出闲聊内容，内容需要控制在15-40字。
# 明信片内容：
# """)

# examples = [
# ]


SystemPromptTemplate = CustomPromptTemplate.from_template("你将扮演一只贪吃有趣的拟人化猫咪，现在是冬天，正在中国各地旅行，最终的目的是回到漠河老家。")
content_req = """现在，你需要写一张给你好友的明信片,明信片中需要描述你在{local}参与的人文活动{name}"""
TaskPromptTemplate = CustomPromptTemplate.from_template("""
{content_prompt}
人文活动: {name}
人文活动描述: {description}
语言朴素简单，有故事感，不需要加上称呼和结尾，内容中最好不要出现{local}，只需要输出闲聊内容，内容需要控制在15-40字。
明信片内容：
""")