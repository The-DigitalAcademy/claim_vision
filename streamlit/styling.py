import streamlit as st

def custom_styling():
    st.markdown(
        """
        <style>
            .main {
                background-color: white;
            }

            .title {
                font-family: "Open Sans", sans-serif;
                font-size: 50px;
                font-weight: bold;
                color: black;
            }
            
            .container {
                background-color: #1f1247ff;
                padding: 10px;
                border-radius: 0px;
                color: white;
                height: 250px;
                display: flex;
                justify-content: center;
                align-items: center;
                text-align: center;
                margin-top: -55px;
            }
            
            .con-links {
                display: flex;
                flex-direction: column;
                justify-content: center
                align-items: center;
                gap: 20px;
            }
       
            .subtitle {
                font-family: "Open Sans", sans-serif;
                font-weight: 300;
                font-size: 35px;
                color: white;
            }
                
            .subheader {
                font-family: "Open Sans", sans-serif;
                font-size: 25px;
                color: black;
                margin-top: -50px
            }

            .text {
                font-family: "Open Sans", sans-serif;
                font-size: 16px;
                color: black;
                max-width: 500px;
            }
            
            .stTabs {
                margin: 20px;
            }
                   
            .stTabs [data-baseweb="tab"] {
                font-family: "Open Sans", sans-serif;
                font-size: 16px;
                color:  black;
                position : relative;
            }
            
            .stTabs [data-baseweb="tab"]:hover {
                font-size: 30px;
                color: #77be5cff;
            }
            
            .stTabs [data-baseweb="tab"][aria-selected="true"] {
                font-weight: bold;
                color: #77be5cff;
            }

            .stButton > button {
                font-family: "Open Sans", sans-serif;
                background-color: #1f1247ff;
                color: white;
                border: none;
                padding: 8px 25px;
                border-radius: 25px;
                height: 50px;
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
                background-color: #77be5cff;
                color: white;
            }
            
            .stSelectbox div[data-baseweb="select"] > div {
                background-color: transparent;
                border: 2px solid #77be5cff;
                color: black;
            }
            
            label {
                color: black !important;
                font-weight: bold
            }
            
            .stSelectbox div[data-baseweb="select"] .css-1uccc91-singleValue {
                background-color: #77be5cff;
            }
            
            .stSelectbox div[data-baseweb="select"] .css-1n7v3ny-option {
                background-color: #77be5cff;
            }
            
            .stNumberInput input {
                background-color: white;
                border: 2px solid #77be5cff;
                border-radius: 4px;
                padding-top: 6px;
                padding-bottom: 6px;
                height: auto;
                box-sizing: border-box;
                color: black;
            }
            
            .stNumberInput input:focus {
                background-color: white;
                outline: none;
            }
            
            .stNumberInput > div > div > input[type=number] {
                border-radius: 0;
                padding: 0;
                margin: 0;
            }
            
            .stNumberInput > div > div > button:first-of-type {
                background-color: #77be5cff;
            }
            
            .stNumberInput > div > div > button:last-of-type {
                background-color: #77be5cff;
            }

            .stDateInput input {
                background-color: white;
                border: 2px solid #77be5cff;
                border-radius: 2px;
                outline: none;
                color: black;
            }

            
            div[data-baseweb="radio"] > div {
                background-color: white;
                border: 1px solid #000;
                border-radius: 50%;
                width: 16px;
                height: 16px;
                display: inline-block;
                position: relative;
            }
            
            .stRadio > div div {
                color: black !important;
                font-weight: normal;
            }

            .dataframe {
                border: 2px solid #1f1247ff;
                border-collapse: collapse;
                width: 30%;
            }
            
            .dataframe th, .dataframe td {
                border: 1px solid #ddd;
                padding: 8px;
                text-align: left;
            }
            
            .dataframe th {
                background-color: #1f1247ff;
                color: white;
            }
            
            div[data-testid="stMetricValue"] {
                color: black !important;
                font-size: 30px !important;
            }        

        </style>
        """,
        unsafe_allow_html=True,
    )

hide_fullscreen = """
        <style>
        button[title="View fullscreen"] {
            visibility: hidden;
        }
        </style>
    """
st.markdown(hide_fullscreen, unsafe_allow_html=True)