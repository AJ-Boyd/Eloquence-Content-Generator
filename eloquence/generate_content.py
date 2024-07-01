"""
auth: AJ Boyd
date: 6/29/2024
file: generate_content.py
desc: generates new content according to the user's preferences
"""

from langchain_community.llms import Ollama
from langchain_core.callbacks import CallbackManager, StreamingStdOutCallbackHandler
from langchain_core.prompts import PromptTemplate
import re, random

SYS_PROMPT = "You are EloquenceAI, a tool designed to generate text-based content such as emails, stories, and fictional dialogue according to the user's prompt and preferences. All content must have proper grammar"

def config_LLM():
    llm = Ollama(
        model = "llama3",
        verbose = False,
        temperature = 1.3,
        system = SYS_PROMPT,
        top_k = 60,
        top_p = 0.95,
        num_predict = -2
    )
    
    return llm

def gen_content(llm, attr: list) -> str:
    _type, subject, model, length, style, tone, example = attr
    
    # update llm attributes depending on user preferences
    llm.model = model
    
    if "Story" == _type or "AITA" in _type:
        if length == "Very brief":
            approx_length = 70
        elif length == "Short":
            approx_length = 120
        elif length == "Lengthy":
            approx_length = 1050
        else:
            approx_length = 540
    else:
        if length == "Very brief" or _type == "Pick-up line":
            approx_length = 70
        elif length == "Short":
            approx_length = 90
        elif length == "Lengthy":
            approx_length = 300
        else:
            approx_length = 150
    
    
    prompt = f"""Only respond with the content you generate. The user has asked you to generate a {length} {_type} that is {approx_length - 40} or fewer words long. The {_type} is to be centered around this general subject: [{subject}]
    Make your writing style {style}. """
    
    if tone:
        prompt += f"Keep your tone {tone}. "
    if example:
        prompt += f"Use this as an example <{example}> "
    
    prompt += "Do not include a subject line or title unless prompted otherwise."
    print("prompt:", prompt)
    response = llm.invoke(prompt)
    print("response:", response)
    return response