from langchain.prompts import PromptTemplate

SystemPrompt = PromptTemplate.from_template("请你帮我整理或生成指定城市特色人文活动的描述性文字")
AskPrompt = PromptTemplate.from_template("下面是我提供的一个城市特色人文活动{key}的描述：{des}其中可能包含一些与该活动无关的信息，请你帮我整理一个关于{key}的描述，剔除与体验该活动无关的信息，如活动的地理位置等。如果你了解该活动的更多信息也可以添加，但请避免使用“总之{key}是一个值得体验的活动”这种没有具体信息的描述。")
GenPrompt = PromptTemplate.from_template("下面是我提供的一个城市特色人文活动{key}，请你根据你的相关知识，请你帮我生成一个关于{key}的描述，剔除与体验活动无关的信息，如活动的地理位置等，最后不要用“总之{key}是一个值得体验的活动”这种没有具体信息的描述。")
SummaryPrompt = PromptTemplate.from_template("下面是我提供的一个城市特色人文活动{key}的描述：{des}请你用一两句话帮我总结一下这个活动{key}的特色描述，大约200字左右。")