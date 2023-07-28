# AI Cookbook Inventor

Simple app build with Streamlit, using langchain to get dish recipe from AI

## Description
This project is a Python-based application that employs the power of AI and language processing technologies to generate unique recipes based on user input. The application utilizes Streamlit for the user interface, and Langchain to formulate recipes.

The concept of the app: users inputs the name of a product they want to be the main ingredient of their dish, and the type of dish they want to prepare (e.g., soup, stew, appetizer, etc.). The app then uses Langchain to send a request to create a recipe for the given dish along with a suitable name. The AI-generated recipes can be stored in the application's database for future reference.

## Usage
First you must get your own apikey from https://platform.openai.com/account/api-keys and replace <your_key> in apikey.py:

    apikey = '<your_key>'

To run the application, execute the following command in the project's directory:

    streamlit run app.py

Navigate to the displayed local URL, then you can start inputting your main ingredient and the type of dish you want to prepare, and let the AI do the rest!