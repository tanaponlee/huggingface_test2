import gradio as gr
from mylib.calculator import add


def greet(phrase):
    greeting = f"Hello {phrase}!"
    return greeting




with gr.Blocks() as demo:
    name = gr.Textbox(label="Name")
    output = gr.Textbox(label="Output Box")
    greet_btn = gr.Button("Greet")
    greet_btn.click(fn=greet, inputs=name, outputs=output)

    a = gr.Number(label="a")
    b = gr.Number(label="b")
    calculate_btn = gr.Button("Calculate")
    output_calc = gr.Textbox(label="Calculation Result")
    calculate_btn.click(fn=add, inputs=[a, b], outputs=output_calc)
demo.launch()