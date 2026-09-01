import gradio as gr
import os
from fastapi import Response

def get_image_size(image):
    if image is None:
        return "No image uploaded."
    size_bytes = os.path.getsize(image)
    size_mb = size_bytes / (1024 * 1024)
    return f"Image size: {size_mb:.4f} MB"

with gr.Blocks() as demo:
    image_input = gr.File(
        label="Upload Image",
        file_types=[".jpg", ".jpeg", ".png"],
    )
    submit_btn = gr.Button("Submit")
    output = gr.Textbox(label="Result")

    submit_btn.click(fn=get_image_size, inputs=image_input, outputs=output)

@demo.app.get("/ping", include_in_schema=False)
def ping():
    return Response(status_code=200)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
