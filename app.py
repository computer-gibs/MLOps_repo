import gradio as gr
from transformers import FSMTForConditionalGeneration, FSMTTokenizer

mname_en_ru = "facebook/wmt19-en-ru"
mname_ru_en = "facebook/wmt19-ru-en"
tokenizer_en_ru = FSMTTokenizer.from_pretrained(mname_en_ru)
tokenizer_ru_en = FSMTTokenizer.from_pretrained(mname_ru_en)
model_en_ru = FSMTForConditionalGeneration.from_pretrained(mname_en_ru)
model_ru_en = FSMTForConditionalGeneration.from_pretrained(mname_ru_en)

def translate(input_text, mode="en-ru"):
    if mode == "en-ru":
        tokenizer = tokenizer_en_ru
        model = model_en_ru
    else:
        tokenizer = tokenizer_ru_en
        model = model_ru_en

    input_ids = tokenizer.encode(input_text, return_tensors="pt")
    outputs = model.generate(input_ids)
    decoded = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return decoded

input_text = gr.inputs.Textbox(lines=3, label="Input Text")
output_text = gr.outputs.Textbox(label="Translated Text")
mode = gr.inputs.Radio(["en-ru", "ru-en"], label="Translation Mode")

iface = gr.Interface(fn=translate, inputs=[input_text, mode], outputs=output_text)
iface.launch()