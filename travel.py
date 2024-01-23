import streamlit as st
import openai
from openai import OpenAI


client = OpenAI()

def get_travel_suggestions(query):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a travel expert assistant."},
                {"role": "user", "content": query}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Streamlit app setup
st.title("Travel Suggestion Bot")
st.write("Tell me about your travel preferences, and I'll suggest some destinations and activities!")

month_of_travel = st.selectbox("Month of travel:", ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])
climate = st.selectbox("Preferred climate:", ["Warm", "Cold", "Temperate", "No preference"])
budget = st.selectbox("Budget:", ["Low", "Medium", "High"])
interests = st.text_input("Interests (e.g., beaches, mountains, cities, culture):")
duration = st.selectbox("Travel duration:", ["Weekend", "1 week", "2 weeks", "Longer"])
accommodation = st.selectbox("Preferred accommodation:", ["Hotel", "Hostel", "Rental (e.g., Airbnb)", "No preference"])
travel_group = st.selectbox("Traveling:", ["Alone", "With partner", "With family", "With friends"])
experience_type = st.selectbox("Type of experience:", ["Adventure", "Relaxation", "Cultural exploration", "No preference"])
dietary_pref = st.selectbox("Dietary preferences:", ["No restrictions", "Vegetarian", "Vegan", "Halal", "Kosher", "Other"])
preferred_regions = st.multiselect("Preferred regions (optional):", ["Africa", "Asia", "Europe", "North America", "South America", "Australia/Oceania", "Antarctica"])
avoid_regions = st.multiselect("Regions to avoid (optional):", ["Africa", "Asia", "Europe", "North America", "South America", "Australia/Oceania", "Antarctica"])

if st.button("Get Suggestions"):
    query = (f"I'm planning to travel in {month_of_travel}. Looking for a {climate.lower()} place with a {budget.lower()} budget for a {duration.lower()} trip. "
             f"I prefer staying in a {accommodation.lower()}, interested in {interests}, and I'm traveling {travel_group.lower()}. "
             f"I'm looking for a {experience_type.lower()} experience. My dietary preference is {dietary_pref.lower()}. "
             f"Prefer to visit: {', '.join(preferred_regions)}. Avoiding: {', '.join(avoid_regions)}. ONLY PROVIDE THE LIST OF TOP 5 DESTINATIONS AND A SINGLE LINE EXPLAINING WHY EACH WOULD BE A BEST FIT TO VISIT! MAKE THE DESTINATION A HEADING AND THEN PROVIDE THE ONE LINE DESCRIPTION ON THE NEXT LINE!")
    suggestions = get_travel_suggestions(query)
    st.text_area("Travel Suggestions:", value=suggestions, height=300)
