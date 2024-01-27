# Travel Suggestion Bot

## Overview
The Travel Suggestion Bot is a Streamlit-based web application that offers personalized travel suggestions. Utilizing the power of OpenAI's GPT-3.5 model, it generates tailored travel advice based on various user inputs. This tool is perfect for anyone looking to plan their next trip with considerations for personal preferences and interests.

## Features
- **Personalized Travel Recommendations**: Users receive travel destination suggestions based on their preferences such as climate, budget, interests, and more.
- **Multi-Criteria Input**: The bot considers various factors like travel duration, accommodation type, and travel companions to tailor its suggestions.
- **AI-Powered Insights**: Leverages OpenAI's GPT-3.5 model to provide insightful and relevant travel advice.

## Installation
To set up the Travel Suggestion Bot, ensure Python is installed on your system. If not, download it from [python.org](https://www.python.org/downloads/).

1. **Clone the Repository:**
   ```bash
   git clone git@github.com:Aryan-Rusia-2/Travel-Suggestion-Bot.git
   cd Travel-Suggestion-Bot
   ```

2. **Create and Activate a Virtual Environment (Recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Configuration
1. **OpenAI API Key:**
   - Obtain your API key from [OpenAI](https://beta.openai.com/signup/).
   - Set the API key as an environment variable in your desktop, or else you can create a .env file 

## Running the Application
Execute the following command to start the Streamlit app:
```bash
streamlit run app.py
```
Access the app via your web browser at the URL provided by Streamlit.

## How to Use
- Enter your travel preferences in the application's input fields.
- Click "Get Suggestions" for customized travel advice.
- Review the suggested destinations and activities tailored to your preferences.

## Contributions
Contributions are welcome! For major changes, please open an issue first to discuss what you would like to change. Ensure to follow good coding practices.
