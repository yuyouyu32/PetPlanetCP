from langchain.prompts import PromptTemplate

SystemPrompt = PromptTemplate.from_template("请你帮我整理或生成指定旅行地点的描述性文字")
AskPrompt = PromptTemplate.from_template("下面是我提供的一个旅行地点{key}描述：\n{des}\n 其中可能有一些无关旅行的信息，请你帮我整理一个旅行地点{key}的描述，剔除无关的信息，如占地面积，高度等与旅游无关的信息。如果你了解该地点有趣的描述也可以添加，最后不要用“总之{key}是一个值得一游的旅行目的地”这种没有信息的描述。")
GenPrompt = PromptTemplate.from_template("下面是我提供的一个旅行地点{key}, 请你根据你的相关旅行知识，请你帮我生成一个旅行地点{key}的描述，剔除无关的信息，如占地面积，高度，等等与旅游无关的信息，最后不要用“总之{key}是一个值得一游的旅行目的地”这种没有信息的描述。")
SummaryPrompt = PromptTemplate.from_template("下面是我提供的一个旅行地点{key}描述：\n{des}\n 请你用一两句话帮我总结一下这个旅行地点{key}的特色描述，大约200字左右。")
