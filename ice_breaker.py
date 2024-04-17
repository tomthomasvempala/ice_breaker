import os

from langchain.chains.llm import LLMChain
from langchain_community.llms.ollama import Ollama
from langchain_core.prompts import PromptTemplate
from langfuse.callback import CallbackHandler
from langfuse import Langfuse


def fetch_all_pages(name=None, user_id=None, limit=50):
    page = 1
    all_data = []

    while True:
        response = langfuse.get_generations(name=name, limit=limit, user_id=user_id, page=page)
        if not response.data:
            break

        all_data.extend(response.data)
        page += 1

    return all_data


if __name__ == '__main__':
    # Tests the SDK connection with the server
    print(os.environ.get("LANGFUSE_PUBLIC_KEY"))
    langfuse_handler = CallbackHandler()
    langfuse_handler.auth_check()
    langfuse = Langfuse()
    print(fetch_all_pages())
    print("Hello Langchain")
    summary_template = """
    given information {information} about a person, I want you to create :
    1. A short summary
    2. Two interesting fact about them
    3. Write a poem about them
    """
    information = """
    Elon musk is CEO of Tesla. He also owns SpaceX.
    """

    summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template)
    llm = Ollama(model="llama2")
    chain = LLMChain(llm=llm, prompt=summary_prompt_template)
    # res = chain.invoke({"information": information}, {"callbacks": [langfuse_handler]})
    # print(res['text'])
