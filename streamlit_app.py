import streamlit

streamlit.title('My parents New Healthy Dinner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 kale, spinach & rocket smoothie')
streamlit.text(' 🐔 Hard-boiled Free-Range eggs')
streamlit.text('🥑🍞Avacado Toast')


streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list=my_fruit_list.set_index('Fruit')

#lets put some list to select from the fruit list
fruits_selected=streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show=my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)
