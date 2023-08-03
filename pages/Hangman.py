import streamlit as st
import string
import time
import dataclasses

# [start] [persistent states]__________________________________________
@dataclasses.dataclass
class gameState:
    # HangMan
    hm_word: str = ""
    hm_word_letters = set(hm_word)
    hm_alphabet = set(string.ascii_uppercase)
    hm_used_letters = set()
    hm_word_list = []
    hm_n_lifes: int = 10
    hm_idxml_key: int = 0


@st.cache_resource(experimental_allow_widgets=True)
def _gameState() -> gameState:
    return gameState()


hm = _gameState()


# [start] [HangMan]____________________________________________________

st.title("Hangman")

def HangMan():
    word = st.text_input(
        f"Enter a word :", type="password", key=f"word_{hm.hm_idxml_key}"
    )
    if hm.hm_word == "":
        if word == "":
            st.warning("**Please enter the hidden word.**")
        else:
            hm.hm_word = word.upper()
            hm.hm_word_letters = set(hm.hm_word)
            st.experimental_rerun()
    elif hm.hm_word != "":
        st.success("**Game in progress...**")

    word_list = [letter if letter in hm.hm_used_letters else "-" for letter in hm.hm_word]

    st.markdown("___")
   

    
    with st.container():
        text, img = st.columns((1,1))
    
    with text:
        b_reset, b_show_answer = st.columns([3, 3])
        show_answer = b_show_answer.button("🔍 Show Answer")
        st.markdown(
            f"""
            <br>
                You have used these letters:
            <br>
                {" ".join(hm.hm_used_letters)}
            <br>
                You have {hm.hm_n_lifes} lives left
            <br>
                Current word: 
            <br>
             
            <br>
            """,
            unsafe_allow_html=True,
        )
        st.subheader(f"""{"".join(word_list)}
                     """)

        holder1, holder2, holder3 = st.empty(), st.empty(), st.empty()
        user_letter = holder1.text_input(
            "Guess a letter:", max_chars=1, key=str(hm.hm_idxml_key + 1)
        ).upper()

    

    if (
        len(hm.hm_word_letters) > 0 and hm.hm_n_lifes > 0 and user_letter != ""
    ) and hm.hm_word:

        if user_letter in hm.hm_alphabet - hm.hm_used_letters:
            hm.hm_used_letters.add(user_letter)
            if user_letter in hm.hm_word_letters:
                hm.hm_word_letters.remove(user_letter)
                holder2.success("Good guess. Keep going!")
            else:
                holder2.error("Character is not in word. Try again!")
                hm.hm_n_lifes -= 1

        elif user_letter in hm.hm_used_letters:
            holder2.info("You have already used that character. Try again!")

        elif user_letter not in hm.hm_alphabet and user_letter != "":
            holder2.error("Invalid character. Try again!")

    elif (
        len(hm.hm_word_letters) == 0 or hm.hm_n_lifes == 0 or show_answer
    ) and hm.hm_word:
        holder1.empty()

        if "".join(word_list) == hm.hm_word:
            holder1.success(
                f"\nCongratulations! You guessed the word [{hm.hm_word}] correctly!!"
            )
            st.balloons()
        else:
            holder2.info(f"The word is {hm.hm_word}")
            holder3.error("Game over! Try again!")
            time.sleep(0.25)

    time.sleep(0.25)

    if user_letter != "":
        hm.hm_idxml_key += 1
        st.experimental_rerun()

    if b_reset.button("🛑 Reset Game ⚙") or show_answer:
        hm.hm_word = ""
        hm.hm_word_letters = set(hm.hm_word)
        hm.hm_used_letters = set()
        hm.hm_word_list = []
        hm.hm_n_lifes = 10
        hm.hm_idxml_key += 1
        st.experimental_rerun()

    pictures = {'0': 'assets/state10.png', '1': 'assets/state9.png',
                 '2': 'assets/state8.png', '3': 'assets/state7.png', 
                 '4': 'assets/state6.png', '5': 'assets/state5.png', 
                 '6': 'assets/state4.png', '7': 'assets/state3.png',
                 '8': 'assets/state2.png', '9': 'assets/state1.png',
                 '10': 'assets/state0.png'}
    
    filename = pictures[str(hm.hm_n_lifes)] 

    with open(filename, 'rb') as f:
        image = f.read()

    with img:
        st.image(image)


if __name__ == "__main__":
    HangMan()