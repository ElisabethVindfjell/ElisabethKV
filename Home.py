import streamlit as st
import webbrowser
#from streamlit_extras.app_logo import add_logo
#from streamlit_extras.add_vertical_space import add_vertical_space

st.set_page_config(page_title="Elisabeth Vindfjell", page_icon=":computer:", layout="centered")

#------------------------------------------------------------------
# sidebar:

#add_logo("assets/card.jpg", height=300)

#------------------------------------------------------------------

url = 'https://no.linkedin.com/in/elisabeth-vindfjell'
url_git = 'https://github.com/ElisabethVindfjell'

st.header("Welcome to my Webpage :earth_africa:")
st.subheader(" - My Digital Portfolio and Projects 	:open_file_folder:")
c1, c2 = st.columns(2)

with c1:
    st.image("assets/h4.jpg", use_column_width=True)
with c2:

    st.markdown("Hello there! My Name is Elisabeth Vindfjell. This webpage serves as an interactive resume, providing you with valuable insights into my background and expertise. "
                "Primarily focused on coding, it sheds light on my skillset and accomplishments in the realm of technology.")
    st.subheader("Who Am I?")
    st.markdown("I am a student currently pursuing a master's degree in economics with a love for coding and problem-solving. " 
                "Through this platform, I aim to present my skillset in Python and Streamlit. In addition to my proficiency in Python, " 
                "I am well-versed in coding with R and have experience utilizing Python's Dash framework. " 
                "You can read more about me and my experience in the 'About me'-page located in the sidebar.")

st.subheader("Get in Touch")
st.markdown("Do you have any questions or want to know more about me, my projects, or the code powering this webpage? Feel free to contact me! "
            "I'm always eager to engage in discussions and collaborations.")   

#add_vertical_space(1)

st.markdown("Thank you for visiting my webpage, and I hope you find it informative and inspiring. "
            "Let's connect!")

if st.button('Check out my GitHub', use_container_width=True):
    webbrowser.open_new_tab(url_git)
if st.button("Let's connect on LinkedIn", use_container_width=True):
    webbrowser.open_new_tab(url)

with st.container():
    c1, c2 = st.columns((1,1))
    with c1:
        st.metric(label="Phone", value= "+47 949 85 939",)
    with c2:
        st.metric(label="Mail", value= "ekv@hotmail.no",)   
