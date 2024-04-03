import os
import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown


from dotenv import load_dotenv

load_dotenv(".env")


def to_markdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


google_api_key = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=google_api_key)


# for m in genai.list_models():
#   if 'generateContent' in m.supported_generation_methods:
#     print(m.name)

model = genai.GenerativeModel('gemini-pro')

# %%time
response = model.generate_content("What is large language models?")

# print(response.text)
