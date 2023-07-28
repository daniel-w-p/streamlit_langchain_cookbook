import streamlit as st
import db


class Work:
    dish_types = ['appetizer', 'soup', 'main course', 'dessert']
    response = None
    success = None
    @classmethod
    def run(cls, chain):
        st.title('AI Cookbook Inventor')

        # First form
        with st.form("cook_form"):
            dish = st.selectbox('Select dish type:', cls.dish_types)
            ingredient = st.text_input('What product should be main ingredient in your dish.')
            if st.form_submit_button('Get recipe'):
                cls.response = chain({'dish': dish, 'ingredient': ingredient})

        # Second form if is response with recipe
        if cls.response:
            with st.form("db_form"):
                if st.form_submit_button('Save recipe to base'):
                    cls.success = db.add(str(cls.response['title']).strip(), str(cls.response['recipe']).strip(), dish)
                    cls.response = None

        # if saved to database
        if cls.success is not None:
            if cls.success:
                st.success("Successfully added to cookbook!")
            else:
                st.error("Can't save to cookbook!")
            cls.success = None

        # Show title with recipe
        if cls.response:
            st.header(cls.response['title'])
            st.write(cls.response['recipe'])
