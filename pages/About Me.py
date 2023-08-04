# imoprt packeges
import streamlit as st

# commented out becaus streamlit.extras only work localy, not when the app is launched
#from streamlit_extras.app_logo import add_logo
#from streamlit_extras.add_vertical_space import add_vertical_space

# Change the tab-title
st.set_page_config(page_title="About me", page_icon=":girl:", layout="centered")

#------------------------------------------------------------------
# # sidebar:
#add_logo("assets/card.jpg", height=300)
#------------------------------------------------------------------

# Title of the webpage
st.header("About me")

# splitting the page into two columns, one with picture and one with text
with st.container():
   c1, c2 = st.columns((2,3))
   with c1:
      st.image("assets/h1.jpg")
   with c2:   
      st.markdown("I'm Elisabeth Kongsvik Vindfjell. Originally from Nordfjordeid, but now living in Bergen. "
            "I am currently pursuing a degree in economics at the Norwegian School of Economics, with a major in business analytics. ")

      st.markdown("Over the years, I've accumulated valuable experiences through diverse work roles, academic pursuits, and leadership responsibilities. "
            "Engaging in teamwork has taught me the significance of collaboration, effective communication, and adaptability.")

#----------------------------------------------------------------------------------------------------------------------------------------------------
# Expander for education
with st.expander("Educaton"):
   st.markdown("**Master's Degree in Economics and Administration at the Norwegian School of Economics | 2022 - 2024**")
   with st.container():
      image_col, text_col = st.columns((1,10))
      with image_col:
         st.image("assets/nhh.png")
      with text_col:
         st.markdown("• Specialization in Business Analytics")
         st.markdown("• Proficient in R and Python programming")
         st.markdown("• Topics covered include analysis and optimization")

   #add_vertical_space(2)

   st.markdown("**Bachelor's Degree in Economics and Administration at the Western Norway University of Applied Sciences | 2019 - 2022**")
   with st.container():
      image_col, text_col = st.columns((1,8))
      with image_col:
         st.image("assets/hvl.png")
      with text_col:
         st.markdown("• Specialization in Administration and Leadership")
         st.markdown("• Average grade: B")
         st.markdown("• Bachelor's thesis on employer branding")

#----------------------------------------------------------------------------------------------------------------------------------------------------
# Expander for experience
with st.expander("Experience"):
   st.markdown("**Kongsberg Maritime | june 2023 - sept 2023**")
   with st.container():
      image_col, text_col = st.columns((1,4))
      with image_col:
         st.image("assets/kongsberg.png")
      with text_col:
         st.markdown("• Data collection assistant")
         st.markdown("• Coding in Python")
         st.markdown("• building a dataset for training a GPT-model")

   #add_vertical_space(2)

   st.markdown("**Europris | june 2014 - Present**")
   with st.container():
      image_col, text_col = st.columns((1,4))
      with image_col:
         st.image("assets/europris.png")
      with text_col:
         st.markdown("• Employed in various positions from 100% to on-call")
         st.markdown("• Worked in multiple locations")
         st.markdown("• Responsible for ordering from two external suppliers")
         st.markdown("• In charge of training new employees")
         st.markdown("• Opening and closing responsibilities")
   
   #add_vertical_space(2)

   st.markdown("**Eid Barnehage - Læringsverkstaden | may 2019 - aug 2019**")
   with st.container():
      image_col, text_col = st.columns((1,4))
      with image_col:
         st.image("assets/eidbhg.jpg")
      with text_col:
         st.markdown("• Summer Employee")
         #st.markdown("• Started with .......................")
   
   #add_vertical_space(2)

   st.markdown("**Military Service | jan 2018 - dec 2018**")
   with st.container():
      image_col, text_col = st.columns((1,6))
      with image_col:
         st.image("assets/kv.png")
      with text_col:
         st.markdown("• Medic in the Coast Guard")
         st.markdown("• Medic Level 3, first aid, and DHLR courses")
         st.markdown("• Union representative")
         st.markdown("• Able Rating")

   #add_vertical_space(2)

   st.markdown("**CIRCLE K | june 2016 - june 2017**")
   with st.container():
      image_col, text_col = st.columns((1,6))
      with image_col:
         st.image("assets/ck.png")
      with text_col:
         st.markdown("• Sales Associate")
   
   #add_vertical_space(2)
  
   st.markdown("**Westres/Sjøkanten Cafe | sept 2013 - june 2014**")
   with st.container():
      image_col, text_col = st.columns((1,6))
      with image_col:
         st.image("assets/westres.png")
      with text_col:
         st.markdown("• Sales Associate")
   
#----------------------------------------------------------------------------------------------------------------------------------------------------
# Expander for volunteer work
with st.expander("Volunteer Work"):
   st.markdown("**Bergen Challenge | 2022**")
   with st.container():
      image_col, text_col = st.columns((1,4))
      with image_col:
         st.image("assets/bc.jpg")
      with text_col:
         st.markdown("• Student Games")
         st.markdown("• Sanitation Attendant ")

   #add_vertical_space(2)

   st.markdown("**Econa | 2021 - Present**")
   with st.container():
      image_col, text_col = st.columns((1,4))
      with image_col:
         st.image("assets/econa.png")
      with text_col:
         st.markdown("• Deputy head at Econa NHH 2023-")
         st.markdown("• Events Responsible at Econa NHH 2022-2023")
         st.markdown("• Marketing Responsible at Econa HVL 2021-2022 ")

   #add_vertical_space(2)

   st.markdown("**Eid Symjeklubb**")
   with st.container():
      image_col, text_col = st.columns((1,4))
      with image_col:
         st.image("assets/eidsk.jpg")
      with text_col:
         st.markdown("• **Head Instructor | 2021**")
         st.markdown("• During the summer")
         st.markdown("• Trained children in swimming")
         st.markdown("• **Instructor | 2012 - 2017**")
         st.markdown("• Instructor for swimming and water safety courses")
         st.markdown("• Coach for recruits and juniors")
         st.markdown("**Youth Representative on the Board | 2014 - 2015**")
   
   #add_vertical_space(2)

   st.markdown("**Volunteer during Youth Olympic Games 2016**")
   with st.container():
      image_col, text_col = st.columns((1,4))
      with image_col:
         st.image("assets/yog.png")
      with text_col:
         st.markdown("• Leadership development program spanning two years")
         st.markdown("• Selected as one of three young individuals in Sogn og Fjordane county")

#----------------------------------------------------------------------------------------------------------------------------------------------
# Expander for interest
with st.expander("Interests"):
   st.subheader("Travel")
   # splitting the container into three columns
   with st.container():
      i1, i2, i3 = st.columns((1,1,1))
      with i1:
         st.image("assets/t1.jpg")
      with i2:
         st.image("assets/t2.jpg")
      with i3:
         st.image("assets/t3.jpg")

   st.subheader("Swimming")
   with st.container():
      i1, i2, i3 = st.columns((1,1,1))
      with i1:
         st.image("assets/s1.jpg")
      with i2:
         st.image("assets/s2.jpg")
      with i3:
         st.image("assets/s3.jpg")

   st.subheader("Hiking")
   with st.container():
      i1, i2, i3 = st.columns((1,1,1))
      with i1:
         st.image("assets/h1.jpg")
      with i2:
         st.image("assets/h2.jpg")
      with i3:
         st.image("assets/h3.jpg")

#--------------------------------------------------------------------------------------------------------------------------------------------------------
# Expander for accomplishments
with st.expander("Accomplishments"):
   st.markdown("Volunteer of the Year in Sogn og Fjordane in 2016")
   # going to add a picthere here







