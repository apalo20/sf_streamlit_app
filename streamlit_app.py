import streamlit
import pandas as pd
import requests
#import snowflake
import snowflake.connector

streamlit.title('My Parent Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')


streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')



my_fruit_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
my_fruit_list =my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include
#streamlit.multiselect("Pick Your Fruit",list(my_fruit_list.index))
fruits_selected=streamlit.multiselect("Pick Your Fruit",list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)

#New Section to show fruityvice api response
streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','apple')
streamlit.write('The user entered ', fruit_choice)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+"apple")

#streamlit.text(fruityvice_response.json())

# transforms json key-value pair in to daframe
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
# Displays the dataframe table on the app
streamlit.dataframe(fruityvice_normalized)

