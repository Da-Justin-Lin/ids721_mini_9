import streamlit as st
from transformers import pipeline

model_name = "gpt2"

text_generator = pipeline("text-generation", model=model_name)

def main():
    # Updated page configuration for dark mode appearance
    st.set_page_config(
        page_title="Dark Mode LLM Interface",
        page_icon="🌒",
        layout="centered",
        initial_sidebar_state="collapsed"
    )

    # Custom CSS for dark mode
    st.markdown(
        """
        <style>
            .main {background-color: #000000;}
            h1 {text-align: center; color: #FFFFFF;}
            /* Text area focus state */
            .stTextArea>div>div>textarea:focus {
                border: 2px solid #0A84FF !important;
            }
            .stTextArea>div>div>textarea {
                background-color: #333333;
                color: #FFFFFF;
                border-radius: 10px;
                border: 2px solid #555555; /* Default border color */
            }
            .stButton>button {
                border: 2px solid #0A84FF;
                border-radius: 10px;
                color: #000000;
                background-color: #0A84FF;
                font-size: 18px;
                transition: background-color 0.3s, color 0.3s;
            }
            /* Button hover state */
            .stButton>button:hover {
                border: 2px solid #3083DC;
                background-color: #3083DC;
                color: #FFFFFF;
            }
        </style>
        """, unsafe_allow_html=True
    )

    # Header section with updated dark mode styling
    st.markdown(
        """
        <div style="background-color: #0A84FF; padding: 25px; border-radius: 15px;">
            <h1>Dark Mode Language Model Playground</h1>
        </div>
        <br>
        """, unsafe_allow_html=True
    )

    # Introduction section adjusted for dark mode
    st.markdown(
        """
        <div style="padding: 25px; border-radius: 15px; background-color: #1A1A1A;">
            <p style="color: #FFFFFF;">Dive into the depths of a highly advanced language model with this dark mode themed application. Enter any prompt below to generate text that spans various genres and styles, from deep narratives to light-hearted dialogues.</p>
            <p style="color: #FFFFFF;">Type your prompt and press <span style="font-weight: bold; color: #0A84FF;">Generate</span> to begin the exploration. Witness the model's ability to understand and creatively expand on your ideas with unprecedented depth and nuance.</p>
            <p style="color: #FFFFFF;"><strong>Remember:</strong> The model's output reflects its broad training, capable of presenting diverse and imaginative responses based on your prompts.</p>
        </div>
        """, unsafe_allow_html=True
    )

    # User input area with dark theme adjustments
    text_input = st.text_area("Enter your text here to start generating:", height=150,
                              placeholder="Type your prompt here...")

    if st.button("Generate"):
        if text_input:
            with st.spinner('Generating...'):
                generated_texts = text_generator(text_input, max_length=150, do_sample=True)
                generated_text = generated_texts[0]['generated_text']

                last_period_index = generated_text.rfind('. ')
                if last_period_index != -1:
                    generated_text = generated_text[:last_period_index + 1]

                st.markdown("### Generated Text:", unsafe_allow_html=True)
                st.write(generated_text)
        else:
            st.error("Please input text for generation.")

if __name__ == "__main__":
    main()
