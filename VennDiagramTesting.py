import streamlit as st
from matplotlib import pyplot as plt
from upsetplot import UpSet, from_contents

# Streamlit app title
st.title("UpSet Plot Example")


# Define the lists
mammals = ["3", "4"]
herbivores = ["4", "5"]
domesticated = ["4", "6"]
blabla = ["4", "8"]

# Convert lists to UpSetPlot data
example = from_contents(
    {"mammal": mammals, "herbivore": herbivores, "domesticated": domesticated,"blabla":blabla}
)

# Create the UpSet plot
#ax_dict = UpSet(example, show_counts="{:,}").plot()
fig = plt.figure(figsize=(10, 6))  # Adjust the size as needed
ax_dict = UpSet(example, show_counts="{:,}").plot(fig=fig)



# Display the plot in Streamlit
st.pyplot(fig)