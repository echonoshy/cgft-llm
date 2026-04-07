
# 1. 全局状态 global state
# 2. 对话状态 session state


import gradio as gr

# Global State
# scores = []

# def show_scores(score: int) -> list[int]:
#     scores.append(score)
#     return scores

# demo = gr.Interface(
#     fn=show_scores,
#     inputs=gr.Number(label="Score"),
#     outputs=gr.Textbox(label="Scores"),
# )
# demo.launch()


# ----------------------------------------------------------- # 


# Session State

# 1. 要有一个gr.State对象接受
# 2. 输入中包含state
# 3. 输出中包含state

# Demo 1
def show_scores(score: int, history: []) -> tuple[int, list[int]]:
    print(history)
    history.append(score)
    output = {
        "score": score,
        "history": history
    }

    return output, history

demo = gr.Interface(
    fn=show_scores,
    inputs=[gr.Number(label="Score"), gr.State(value=[])],
    outputs=["json", gr.State()],
)

demo.launch()


# Demo 2

# def show_scores(score: int, history: str) -> tuple[int, str]:
#     print(history)
#     history += " " + str(score)
#     output = {
#         "score": score,
#         "history": history
#     }

#     return output, history

# demo = gr.Interface(
#     fn=show_scores,
#     inputs=[gr.Number(label="Score"), gr.State(value="")],
#     outputs=["json", gr.State()],
# )

# demo.launch()
