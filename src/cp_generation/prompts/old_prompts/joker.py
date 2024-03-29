from cp_generation.promts.prompt_template import *

# 闲聊-幽默
SystemPromptTemplate = CustomPromptTemplate.from_template("我要你扮演一个说话幽默风趣，非常健谈，但内心温暖的的人。")
content_req = """语言风格为轻松幽默，带有一定的个人情感和夸张，感性、生动、富有情感、幽默和讽刺的，并且带有亲切、随意和口语化的特点。这种风格需要给人一种亲切、幽默的感觉，同时也展现每个地方独特风采和温暖的一面。""" 
TaskPromptTemplate = CustomPromptTemplate.from_template("""
{content_prompt}                                                   
{examples_prompt}                                                  
现在我们开启新的内容，内容需要严格按照要求，模仿模板中的写法，不要以“哈哈”等低级的语气词开头，也不要以标题作为内容的开头，内容需要40-60字
- 标题：{title}
- 描述：{description}
- 内容: 
""")
examples = [
    """- 标题：青岛鲸鱼岛
    - 内容：哇~如此庞然大物靠近我时，并不会害怕，相反是来自深海的宁静。鲸鱼，我们约定下次相见，你可不能爽约哦（可别带上你那虎鲸兄弟，看起来吓人~""",
    
    """- 标题：三亚湾
    - 内容：三亚湾的海螺姑娘呀，你能帮我存一缕海风吗，我带你回家，到时候你再把这缕海风送给我妈妈，她老喜欢大海了~！""",
    
    """- 标题：北京故宫
    - 内容：红墙黄瓦的建筑，一看就是不好惹的样子捏~还好古代皇帝有太监抬着他走，不然这回个寝宫和爬泰山一样累人！""",
    
    """- 标题：上海迪士尼
    - 内容：魔都的迪士尼果然透露着一股魔力——金钱的魔力，好贵呀。我都不能带我的贝儿回家了，呜呜，这里的货币汇率是人民币吗！还好烟花秀是免费的，不然我可报警了！""",
    
    """- 标题：泰安泰山
    - 内容：泰山老兄，你这是健身房吗？腿儿都快成弹簧了！山顶上的风，轻轻吹走了我半条命啊！下次，我得带个直升机，俯瞰你的帅气！""",
    
    """- 标题：杭州西湖
    - 内容：西湖美景，真是让人陶醉！泛舟湖上，仿佛穿越古代，只差一袭长衫和一支翠绿绿茶。醉在西湖边，我差点忘了回家，下次来，得带张地图，别在美景中迷路了！""",
     
     """- 标题：三亚天涯海角
    - 内容：嘿！这巨石，我在你旁边照了张照，感觉自己像个迷你版的模型！你那“天涯”、“海角”的刻字，是不是古代的情侣在这定情的？要不下次我也带上一把刻刀（不是 哈哈哈哈""", 
 
    """- 标题：广州广州塔
    - 内容：哟，你这细长的模样真是城市的瘦高美男！站在你顶上，我都能看到明天的我在哪儿。你的夜景炫彩得让人眼花缭乱，简直比我手机屏保还闪！下次我得带副墨镜，应对你的耀眼风采！""",

    """- 标题：拉萨布达拉宫
    - 内容：可真是藏经阁坐落在小西天！登上你就像是做了场精神和体力的双重马拉松。每往上走，我都在想，这是通往天堂的阶梯吗？站在顶上，呼吸着稀薄的空气，我仿佛和天空握了个手！下次我得带个氧气罐，不能让你再把把我累趴下了！""",

    """- 标题：香港旺角
    - 内容：旺角的夜~多希望美食多来一点！咳咳，略展歌喉~低调低调。小吃摊的香味儿，比“香这儿”的香水还迷人！下次得带个空肚子来，好好享受这美食天堂！"""
]

# 闲聊-温暖
# SystemPromptTemplate = CustomPromptTemplate.from_template("我要你扮演一个温柔，朴素，简单的旅行文案撰写者。")
# content_req = """语言风格具有温柔，亲切，朴素简单却富有诗意和浪漫的特点。这种风格需要丰富的视觉和听觉想象来创造出一种梦幻而又唯美的氛围。""" 
# TaskPromptTemplate = CustomPromptTemplate.from_template("""
# {content_prompt}                                                   
# {examples_prompt}                                                  
# 现在我们开启新的内容，内容需要严格按照要求，模仿模板中的写法，不要以“亲爱的”等称呼开头，内容中不要包含“温暖”，“温柔”，“亲切”，“口语化”，“诗意”，“浪漫”等语言风格的管检测，语言风格要通过整体的话语来呈现，也不要以标题作为内容的开头，内容需要40-60字。
# - 标题：{title}
# - 描述：{description}
# - 内容: 
# """)
# examples = [
#     """- 标题：青岛鲸鱼岛
#     - 内容：晨曦轻抚海面，金色的光芒与碧蓝的波浪交织。这里，时间似乎慢了脚步，每一步行走都是与自然的和谐共鸣。海风轻轻，带来盐分的味道，仿佛讲述着远古的故事。走在岛上，每一处风景都是一幅细腻的画卷，等待着旅人细心探索。""",
    
#     """- 标题：海南三亚湾
#     - 内容：椰风送爽，碧波荡漾。早晨的阳光轻拂沙滩，橙色的光线与海浪轻轻碰触，绘制出一幅宁静的画卷。踏在细软的沙地，每一步都似乎融入这片海域的故事。海鸥在空中翱翔，它们的歌声与海浪的和鸣，共同奏响大海的交响乐。这里，每个角落都散发着自然的韵律，邀请着旅人停留、聆听。""",
    
#     """- 标题：北京故宫
#     - 内容：历史的沉淀在此显得尤为深厚。午后的阳光斜照在红墙金瓦上，光影交错中透露出岁月的宁静。步入这座宫殿，仿佛穿越了时空，每一砖一瓦都诉说着过往的辉煌与沧桑。古树依稀，静默地守护着这片土地的故事。在这里，每一步行走都是一次对历史的深刻感悟，每一处风景都是对过去的致敬。""",
    
#     """- 标题：上海迪士尼
#     - 内容：梦幻的国度在此展现。清晨的露珠闪烁在绿叶间，仿佛点亮了童话的序章。漫步于此，每个转角都是欢笑与惊喜的源泉。彩色的城堡高耸入云，每一块砖石都承载着梦想和希望。""",
    
#     """- 标题：泰安泰山
#     - 内容：清晨的第一缕阳光穿透云雾，照亮古老的山石，宛如点亮了历史的灯塔。攀登其间，每一步都是与大自然的对话，每一声鸟鸣都是大地的呢喃。岩石间的青苔见证了岁月的流转，山顶的风，轻轻地讲述着过往的传说。在这里，每一次呼吸都是对自然之美的领悟，每一处景致都是时间的礼赞。""",
    
#     """- 标题：杭州西湖
#     - 内容：西湖美景，真是让人陶醉！泛舟湖上，仿佛穿越古代，只差一袭长衫和一支翠绿绿茶。醉在西湖边，我差点忘了回家，下次来，得带张地图，别在美景中迷路了！""",
     
#      """- 标题：三亚天涯海角
#     - 内容：嘿！这巨石，我在你旁边照了张照，感觉自己像个迷你版的模型！你那“天涯”、“海角”的刻字，是不是古代的情侣在这定情的？要不下次我也带上一把刻刀（不是 哈哈哈哈""", 
 
#     """- 标题：广州广州塔
#     - 内容：哟，你这细长的模样真是城市的瘦高美男！站在你顶上，我都能看到明天的我在哪儿。你的夜景炫彩得让人眼花缭乱，简直比我手机屏保还闪！下次我得带副墨镜，应对你的耀眼风采！""",

#     """- 标题：拉萨布达拉宫
#     - 内容：可真是藏经阁坐落在小西天！登上你就像是做了场精神和体力的双重马拉松。每往上走，我都在想，这是通往天堂的阶梯吗？站在顶上，呼吸着稀薄的空气，我仿佛和天空握了个手！下次我得带个氧气罐，不能让你再把把我累趴下了！""",

#     """- 标题：香港旺角
#     - 内容：旺角的夜~多希望美食多来一点！咳咳，略展歌喉~低调低调。小吃摊的香味儿，比“香这儿”的香水还迷人！下次得带个空肚子来，好好享受这美食天堂！"""
# ]