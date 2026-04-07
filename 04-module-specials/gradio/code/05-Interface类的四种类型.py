# 4种接口类型

# 1. input + output (输入组件和输出组件不是同一个)

def greet(name: str) -> str:
    return "Hello " + name

demo = gr.Interface(
    fn=greet,
    inputs="text",
    outputs="text",
)

demo.launch()


# 2. input only (仅有输入组件) - 常用表单提交

# def input_only(name: str):
#     print(name)
#     return None
    
# demo = gr.Interface(
#     fn=input_only,
#     inputs="text",
#     outputs=None,
# )

# demo.launch()


# 3. output only (仅有输出组件) - 常用数据展示
# def output_only():
#     return "Hello World"

# demo = gr.Interface(
#     fn=output_only,
#     inputs=None,
#     outputs="text",
# )
# demo.launch()



# 4. Unified Interface (输入输出组件都是同一个)

# def unified_interface(name: str) -> str:
#     return "Hello " + name

# textbox = gr.Textbox(label="Name")

# demo = gr.Interface(
#     fn=unified_interface,
#     inputs=textbox,
#     outputs=textbox,
# )

# demo.launch()

