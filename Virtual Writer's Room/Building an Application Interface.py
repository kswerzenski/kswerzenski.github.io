# Importing necessary packages
import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

# Loading environment variables
load_dotenv(dotenv_path=r'C:\Users\krist\OneDrive\Documents\Data Science MS\DSC670\Project\OPENAI_API_KEY.env')

# Retrieving the API key
api_key = os.getenv("OPENAI_API_KEY")
if api_key is None:
    st.error("Error: Missing API key. Please check your .env file.")
    st.stop()

# Initializing OpenAI client
client = OpenAI(api_key=api_key)


# Defining a function to get feedback from the fine-tuned model
def get_feedback(user_input):
    try:
        with st.spinner("Generating feedback... Please wait."):
            completion = client.chat.completions.create(
                model="ft:gpt-3.5-turbo-0125:personal::AykBr6aP",
                messages=[
                    {"role": "system",
                     "content": "You are a focus group reviewing a script for an un-produced film or television show. "
                                "Provide constructive feedback on clarity, pacing, and dialogue. Consider engagement, "
                                "emotional impact, and storytelling effectiveness in your analysis."},
                    {"role": "user", "content": user_input}
                ],
                max_tokens=500
            )
        return completion.choices[0].message.content
    except Exception as e:
        return f"Error: {e}"


# Setting UI page configuration
st.set_page_config(
    page_title="Virtual Writer's Room",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Creating a sidebar on the interface
with st.sidebar:
    st.title("📜 About This App")
    st.write("This AI-powered **Virtual Writer's Room** provides real-time feedback on scripts and story concepts.")
    st.write("📝 **How It Works:** Enter your script, scene, or story idea, click *Get Feedback*, and receive "
             "AI-powered critique and suggestions.")
    st.markdown("---")
    st.subheader("📌 Example Prompts")
    st.write("1. Give some feedback on this script from the perspective of a young adult audience: [insert script]")
    st.write("2. Provide ideas on how to effectively pace this story: [insert story concept]")
    st.write("3. Review the following short script. What are some of the major themes of this story, and how could "
             "the script be improved to strengthen those themes? [insert script]")

# Setting up the main UI
st.title("🎭 Virtual Writer's Room")

st.markdown(
    "<h3 style='text-align: center; color: grey;'>Share your script, scene, or story concept and "
    "get AI-powered feedback!</h3>",
    unsafe_allow_html=True
)

# Getting user input
user_input = st.text_area("Enter your script or story concept:", height=250, placeholder="Type or paste your "
                                                                                         "scene here")

# Generating feedback
if st.button("🎬 Get Feedback"):
    if user_input.strip():
        feedback = get_feedback(user_input)
        st.subheader("Feedback:")
        st.write(feedback)
    else:
        st.warning("⚠️ Please enter a script or scene before clicking 'Get Feedback'.")
