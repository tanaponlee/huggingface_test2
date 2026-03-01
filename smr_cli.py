#!/usr/bin/env python
"""
Build a command-line interface (CLI) for the summarization application using the `transformers` library from Hugging Face and click. This CLI will allow users to input a text file and receive a summarized version of the content.

"""
import click
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer   
import os 
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

tokenizer = AutoTokenizer.from_pretrained("sshleifer/distilbart-cnn-12-6")
model = AutoModelForSeq2SeqLM.from_pretrained("sshleifer/distilbart-cnn-12-6")


@click.command()
@click.argument("input_text", type=str)
def summarize(input_text):
    """Summarize the content of the input text"""
    print(f"input: {input_text}")
    input_ids = tokenizer.encode(input_text, return_tensors="pt")
    outputs = model.generate(input_ids)
    decoded = tokenizer.decode(outputs[0], skip_special_tokens=True)
    print(f"\n\noutput:{decoded}")

if __name__ == "__main__":
    summarize()