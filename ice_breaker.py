import os

from langchain.chains.llm import LLMChain
from langchain_community.llms.ollama import Ollama
from langchain_core.prompts import PromptTemplate
from langfuse.callback import CallbackHandler
from langfuse import Langfuse


def fetch_all_pages(name=None, user_id=None, limit=50):
    page = 1
    generations = []
    observations = []
    while True:
        response = langfuse.get_generations(name=name, limit=limit, user_id=user_id, page=page)
        new_res = langfuse.get_observations(name=name, limit=limit, user_id=user_id, page=page,type="OBSERVATION")
        if not response.data:
            break

        generations.extend(response.data)
        observations.extend(new_res.data)
        page += 1

    return generations,observations


if __name__ == '__main__':
    langfuse_handler = CallbackHandler()
    langfuse_handler.auth_check()
    langfuse = Langfuse()

    print("Hello Langchain")
    summary_template = """
    You are an Data structures and algorithms expert AI bot. 
    You will answer only these type of questions and decline to answer questions related to another domains.
    You are helpful and wants to answer other question.
    given question:  {question}  
    """
    question = """
    Elon musk is CEO of Tesla. He also owns SpaceX.
    """

    summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template)
    llm = Ollama(model="qwen:0.5b")
    chain = LLMChain(llm=llm, prompt=summary_prompt_template)
    while True:
        question = input()
        if question == "exit":
            break
        else:
            res = chain.invoke({"question": question}, {"callbacks": [langfuse_handler]})
            print(res['text'])
