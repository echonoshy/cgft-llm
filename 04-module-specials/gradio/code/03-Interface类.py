

# 1. 输入输出的个数
# 2. 组件属性：label, placeholder, lines, info
# 3. 描述性文本：title, description, article, examples
# 4. 默认输入参数：additional_inputs


import gradio as gr

def greet(name: str, age: int, height: float) -> (str, str, str):
    return "hi " + name , str(age) + " years old", str(height) + " cm"

demo = gr.Interface(
    fn=greet,
    inputs=[gr.Textbox(label="NAME", placeholder="Enter your name", info="info", lines=5),
            gr.Number(label="AGE")],
    outputs=[gr.Textbox(label="GREETING"), gr.Textbox(label="AGE"), gr.Textbox(label="HEIGHT")],
    title="Greet",
    description="This is a greet demo",
    article="This is a greet demo",
    examples=[["John Doe", 20, 170], ["Jane Doe", 25, 160]],
    additional_inputs=[
        gr.Number(label="HEIGHT", info="info")
    ]
)
demo.launch()
