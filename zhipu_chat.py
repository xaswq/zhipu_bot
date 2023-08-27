# pip install zhipuai 请先在终端进行安装
import zhipuai

def converse_with_zhipuai():
    zhipuai.api_key = "xxxxxx"

    # 初始化对话列表
    prompt_list = []

    while True:
        # 获取用户输入
        user_input = input("你：")

        # 更新prompt列表
        prompt_list.append({"role": "user", "content": user_input})

        # 使用API获取回复
        response = zhipuai.model_api.sse_invoke(
            model="chatglm_std",
            prompt=prompt_list,
            temperature=0.9,
            top_p=0.7,
            incremental=True
        )

        # 解析回复并添加到prompt_list
        assistant_reply = ""
        for event in response.events():
            if event.event == "add":
                assistant_reply += event.data
            elif event.event in ["error", "interrupted", "finish"]:
                break
        
        # 打印回复并添加到prompt_list
        print(f"助手：{assistant_reply}")
        prompt_list.append({"role": "assistant", "content": assistant_reply})
        #print(prompt_list)

        # 可选：为了不让对话无限进行，你可以设置一个退出机制，例如当用户输入"退出"时。
        if user_input.lower() == "退出":
            break
 

converse_with_zhipuai()
