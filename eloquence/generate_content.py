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

SYS_PROMPT = "You are Eloquence, designed to generate text-based content such as emails, essays, and fictional dialogue according to the user's preferences."

def config_LLM():
    llm = Ollama(
        model = "llama3",
        verbose = False,
        # callback_manager = CallbackManager([StreamingStdOutCallbackHandler()]),
        temperature = 1.82,
        system = SYS_PROMPT,
        top_k = 50,
        top_p = 0.95
    )
    
    return llm

def gen_content(llm, attr: list) -> str:
    _type, length, style, tone, example = attr
    
    prompt = f"""Only respond with the content you generate. Generate a(n) {_type} that is {length} in terms of length. 
    Make your writing style {style}"""
    
    if tone:
        prompt += f" and keep your tone {tone}."
    if example:
        prompt += f" Use this as an example <{example}>"
    
    
    print("prompt:", prompt)
    return ""