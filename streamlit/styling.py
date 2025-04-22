import streamlit as st

def custom_styling():
    st.markdown(
        """
        <style>
            .main {
                background-image: linear-gradient(to bottom right, #6079AF, #ADD8E6);
            }

            .title {
                font-size: 50px;
                font-weight: bold;
                color: black;
            }
            
            .subtitle {
                font-size: 30px;
                font-weight: bold;
                color: white;
                margin-top: -40px
            }
                
            .header {
                font-size: 20px;
                font-weight: bold;
                color: white;
            }

            .text {
                font-size: 16px;
                color: white;
                max-width: 500px;
            }
            
            .stTabs [data-baseweb="tab"] {
                font-family: Arial, sans-serif;
                font-size: 16px;
                color:  white;
                position : relative
            }
            
            .stTabs [data-baseweb="tab"]:hover {
                font-size: 30px;
                color: #003152;
            }
            
            .stTabs [data-baseweb="tab"][aria-selected="true"] {
                font-weight: bold;
                color: #003152;
            }

            .stButton > button {
                background-color: #003152;
                color: white;
                border: none;
                padding: 8px 25px;
                border-radius: 25px;
                font-size: 16px;
                font-weight: bold;
                display: flex;
                align-items: center;
                justify-content: center;
                gap: 8px;
                cursor: pointer;
                transition: background-color 0.3s;
            }

            .stButton > button:hover {
                background-color: #6079AF;
                color: red;
            }
            
            .stSelectbox div[data-baseweb="select"] > div {
                background-color: #6079AF;
            }
            
            .stSelectbox div[data-baseweb="select"] .css-1uccc91-singleValue {
                background-color: #6079AF;
            }
            
            .stSelectbox div[data-baseweb="select"] .css-1n7v3ny-option {
                background-color: #6079AF;
            }
            
            .stNumberInput input {
                background-color: #6079AF;
            }
            
            .stNumberInput input:focus {
                background-color: #6079AF;
            }
            
            .stDateInput input {
                background-color: #6079AF;
            }
            
            .stDateInput input:focus {
                background-color: #6079AF;
            }
            
            .stChart {
                background-color: transparent;
                padding: 10px;
                border-radius: 5px;
            }

    
            /* Input field styling */
            .stTextInput > div > div > input {
                background-color: white;
                color: #333;
                border-radius: 5px;
                border: 1px solid #ddd;
                padding: 8px 12px;
            }

            .stTextInput > div > div > input:focus {
                border-color: #FFC107;
                box-shadow: 0 0 0 2px rgba(255, 193, 7, 0.2);
            }

            /* Error message styling */
            .stAlert {
                background-color: #ff4444;
                color: white;
                border-radius: 5px;
                padding: 10px;
                margin: 10px 0;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
