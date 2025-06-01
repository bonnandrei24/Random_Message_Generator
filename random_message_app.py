# %%
import random
import streamlit as st

# List of quotes
quotes = [
    "What's meant for you will always be yours, and it will find you in any way.",
    "It has always been hard, but you have always been brave.",
    "Don't forget, you matter, and you always will.",
    "Be yourself; everyone else is already taken.",
    "Embrace the beauty of uncertainty. It’s a place of infinite possibility.",
    "Don't forget to be kind to yourself. You deserve the same love and care that you give to others.",
    "You will overcome all the barriers you face. You will succeed.",
    "Life finds a way to get you where you're meant to be",
    "You are what you believe yourself to be. ",
    "It is okay to be different, unique, and to be yourself.",
    "The darkness in your mind doesn't erase the light that you carry in your heart.",
    "The moon wears its scars in full view, and so can you — a testament that even broken light can be beautiful.",
    "Wings are not built by standing still but by fighting against the winds; your struggles are teaching you to soar.",
    "Leaves fall not because they are weak but because it is part of the dance with the seasons; so trust that even your losses are part of your strength.",\
    "Beautiful thing about life is that you can always start again. A single mistake does not define you. Every day brings a new chance to grow.",
    "Take the risk. If it scares you, pursue it more. Big dreams are scary but it will be worth it.",
    "You're doing your best with what you know. You're more than allowed to give yourself the appreciation you deserve, even if no one else does.",\
    "You're doing better than you think, keep going.",
    "Hoping that the love you give, is what you also receive."
    "Be proud of yourself for making this far.",
    "Instead of worrying of what could go wrong, you should see the uncertainty as a sign that there's room for it to all work out."
  
]

def get_random_quote():
    return random.choice(quotes)

# Streamlit app layout
st.set_page_config(page_title="Random Message", page_icon="💬")

st.title("💬 Message for yourself")

st.write("Click to get a message")

if st.button("New Message"):
    st.success(get_random_quote())

