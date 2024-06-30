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

SYS_PROMPT = "You are EloquenceAI, a tool designed to generate text-based content such as emails, essays, and fictional dialogue according to the user's prompt and preferences."

def config_LLM():
    llm = Ollama(
        model = "llama3",
        verbose = False,
        temperature = 1.7,
        system = SYS_PROMPT,
        top_k = 50,
        top_p = 0.95
    )
    
    return llm

def gen_content(llm, attr: list) -> str:
    _type, subject, length, style, tone, example = attr
    
    # update llm attributes depending on user preferences
    if _type != "Essay":
        if length == "Very brief" or _type == "Pick-up line":
            llm.num_predict = 50
        elif length == "Short":
            llm.num_predict = 70
        elif length == "Lengthy":
            llm.num_predict = 300
    else:
        if length == "Very brief":
            llm.num_predict = 70
        elif length == "Short":
            llm.num_predict = 120
        elif length == "Lengthy":
            llm.num_predict = 1100
    
    prompt = f"""Only respond with the content you generate. The user has asked you to generate a {length} {_type} that is {llm.num_predict - 20} or fewer words long. The {_type} must follow this subject prompt: [{subject}]
    Make your writing style {style}"""
    
    if tone:
        prompt += f" and keep your tone {tone}"
    if example:
        prompt += f". Use this as an example <{example}>"
    
    prompt += "for e-mails, do not include a subject line."
    print("prompt:", prompt)
    response = llm.invoke(prompt)
    print("response:", response)
    return response