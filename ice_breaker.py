from langchain.chains.llm import LLMChain
from langchain_community.llms.ollama import Ollama
from langchain_core.prompts import PromptTemplate
# from langfuse.callback import CallbackHandler

if __name__ == '__main__':
    # Tests the SDK connection with the server
    # langfuse_handler = CallbackHandler()
    # langfuse_handler.auth_check()
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
    res = chain.invoke({"information": information})
    print(res['text'])
