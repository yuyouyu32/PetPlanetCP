from langchain.prompts import PromptTemplate

SystemPrompt = PromptTemplate.from_template("请你帮我整理或生成指定城市特色美食的描述性文字")
AskPrompt = PromptTemplate.from_template("下面是我提供的一个城市特色美食{key}描述：\n{des}\n 其中可能有一些无关美食的信息，请你帮我整理一个关于{key}的描述，剔除无关的信息，如原料产地等与品尝体验无关的信息。如果你了解该美食相关的描述也可以添加，最后不要用“总之{key}是一个值得一尝的美食”这种没有信息的描述。")
GenPrompt = PromptTemplate.from_template("下面是我提供的一个城市特色美食{key}, 请你根据你的相关美食知识，请你帮我生成一个关于{key}的描述，剔除无关的信息，如原料产地，等等与品尝体验无关的信息，最后不要用“总之{key}是一个值得一尝的美食”这种没有信息的描述。")
SummaryPrompt = PromptTemplate.from_template("下面是我提供的一个城市特色美食{key}描述：\n{des}\n 请你用一两句话帮我总结一下这个美食{key}的特色描述，大约200字左右。")