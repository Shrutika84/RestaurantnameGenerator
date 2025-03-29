from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain.chains import SequentialChain

# Initialize Ollama LLM
llm = Ollama(model="llama2", temperature=0.7)


def generate_restaurantnames_fooditems(cuisine):
    prompt_template_name = PromptTemplate(
        input_variables=['cuisine'],
        template="I want to open a restaurant for {cuisine} food. Suggest a fancy name for this."
    )

    name_chain = LLMChain(
        llm=llm,
        prompt=prompt_template_name,
        output_key="restaurant_name"
    )

    # Second prompt: Suggest menu items
    prompt_template_menu = PromptTemplate(
        input_variables=['restaurant_name'],
        template="Suggest some menu items for a restaurant named {restaurant_name}."
    )

    foooditem_chain = LLMChain(
        llm=llm,
        prompt=prompt_template_menu,
        output_key="menu_items"
    )


    sequencechain = SequentialChain(
        chains=[name_chain, foooditem_chain],
        input_variables=['cuisine'],
        output_variables=['restaurant_name', 'menu_items']

    )
    response = sequencechain({'cuisine': 'Arabic'})

    return response




if __name__ == "__main__":
    print(generate_restaurantnames_fooditems('Italian'))