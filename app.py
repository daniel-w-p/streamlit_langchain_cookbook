import os
from apikey import apikey

from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain

from work import Work

os.environ['OPENAI_API_KEY'] = apikey

# prompts template
title_template = PromptTemplate(
    input_variables=['ingredient', 'dish'],
    template="Come up with a recipe title; only title; for a {dish} dish whose main ingredient is {ingredient}."
)

recipe_template = PromptTemplate(
    input_variables=['title'],
    template="Come up with a recipe for dish based on this title; TITLE: {title} " +
             "Make each of ingredients new line like dots unordered list and each instruction like ordered in new line."
)

# create langchain instance
llm = OpenAI(temperature=0.9)
title_chain = LLMChain(llm=llm, prompt=title_template, output_key='title')
recipe_chain = LLMChain(llm=llm, prompt=recipe_template, output_key='recipe')
chain = SequentialChain(chains=[title_chain, recipe_chain],
                        input_variables=['ingredient', 'dish'],
                        output_variables=['title', 'recipe'])

# show app
Work.run(chain)
