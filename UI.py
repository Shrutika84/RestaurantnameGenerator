import streamlit as st
import langchain_helper as lang
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain_community.llms import Ollama

llm = Ollama(model="llama2", temperature=0.7)

st.title("Restaurant name Generator")


cuisine =   st.sidebar.selectbox("Pick a Cuisine", ("Indian", "Italian", "Mexican", "American"))


# First prompt: Suggest a restaurant name
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


if cuisine:
    response = lang.generate_restaurantnames_fooditems(cuisine)

    st.header(response['restaurant_name'])

    menu_items = response['menu_items'].split(",")

    st.write("**Menu Items**")
    for item in menu_items:
        st.write("-", item)

