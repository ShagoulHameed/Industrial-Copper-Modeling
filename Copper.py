import streamlit as st
import joblib
import numpy as np
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
        .sidebar .sidebar-content {
            background-color: #f0f2f6;
        }
        .sidebar .sidebar-content .sidebar-header {
            font-size: 1.2em;
            color: #2E7D32;
        }
        .sidebar .sidebar-content .nav-link {
            font-size: 1.1em;
        }
    </style>
""", unsafe_allow_html=True)

# Functions
def predict_selling_price(ctry, status, itmtp, aplcn, wth, prdrf, qtlg, cstlg, tknslg, itmdt, itmmn, itmyr, deldtdy, deldtmn, deldtyr):
    # Change the datatypes "string" to "int"
    itdd = int(itmdt)
    itdm = int(itmmn)
    itdy = int(itmyr)
    dydd = int(deldtdy)
    dydm = int(deldtmn)
    dydy = int(deldtyr)

    # Load the model using joblib
    model_regg = joblib.load("C:/Users/HameedS/OneDrive - Kantar/Desktop/Pythonmy/Classification_model.pkl")

    user_data = np.array([[ctry, status, itmtp, aplcn, wth, prdrf, qtlg, cstlg, tknslg, itdd, itdm, itdy, dydd, dydm, dydy]])

    y_pred = model_regg.predict(user_data)

    return y_pred[0]

st.title(":blue[**INDUSTRIAL COPPER MODELING**]")

with st.sidebar:
    st.image("C:/Users/HameedS/OneDrive - Kantar/Desktop/Pythonmy/maxresdefault.jpg", use_column_width=True)
    option = option_menu('Navigation', options=["HOME", "PREDICT SELLING PRICE", "PREDICT STATUS"])

if option == "HOME":
     st.header("Project Overview")

     st.write("""
        The Industrial Copper Modeling project aims to optimize pricing and lead classification within the copper industry. The project addresses common issues such as data skewness and noise, which can compromise manual prediction accuracy. By leveraging machine learning techniques, this project offers a more efficient and accurate solution.

        **Key Features of the Model:**
        - **Data Preprocessing:** Includes data normalization, feature scaling, and outlier detection to ensure clean and usable data.
        - **Regression Model for Pricing:** A machine learning regression model predicts the continuous variable 'Selling_Price' by analyzing historical data and current trends.
        - **Classification Model for Lead Status:** A lead classification model evaluates and classifies leads into 'WON' or 'LOST' categories, improving decision-making for sales strategies.
        - **User Interface:** A Streamlit-based interface allows users to input relevant data and receive real-time predictions for selling prices and lead status.

        **Steps Involved in the Solution:**
        1. **Exploring Skewness and Outliers:** Analyze the dataset to identify and address any skewness or outliers that may affect model performance.
        2. **Data Transformation and Cleaning:** Transform the data into a suitable format and perform necessary cleaning and preprocessing steps to prepare it for modeling.
        3. **Building the Regression Model:** Develop a regression model to accurately predict selling prices, using advanced machine learning algorithms.
        4. **Building the Classification Model:** Create a classification model to predict the status (WON/LOST) of leads, aiding in effective sales management.
        5. **Developing the Streamlit App:** Implement a user-friendly Streamlit application where users can input data and obtain predictions for selling price and lead status.

        This comprehensive approach ensures that the copper industry can make data-driven decisions, optimize pricing strategies, and improve lead conversion rates.
        """)
    # Placeholder for an image
     st.image("C:/Users/HameedS/OneDrive - Kantar/Desktop/Pythonmy/maxresdefault.jpg", caption="Industrial Copper Modeling", use_column_width=True)

elif option == "PREDICT STATUS":
    st.header("PREDICT STATUS (Won / Lose)")
    st.write(" ")

    col1, col2 = st.columns(2)

    with col1:
        country = st.number_input(label="**Enter the Value for COUNTRY**/ Min:25.0, Max:113.0")
        item_type = st.number_input(label="**Enter the Value for ITEM TYPE**/ Min:0.0, Max:6.0")
        application = st.number_input(label="**Enter the Value for APPLICATION**/ Min:2.0, Max:87.5")
        width = st.number_input(label="**Enter the Value for WIDTH**/ Min:700.0, Max:1980.0")
        product_ref = st.number_input(label="**Enter the Value for PRODUCT_REF**/ Min:611728, Max:1722207579")
        quantity_tons_log = st.number_input(label="**Enter the Value for QUANTITY_TONS (Log Value)**/ Min:-0.322, Max:6.924", format="%0.15f")
        customer_log = st.number_input(label="**Enter the Value for CUSTOMER (Log Value)**/ Min:17.21910, Max:17.23015", format="%0.15f")
        thickness_log = st.number_input(label="**Enter the Value for THICKNESS (Log Value)**/ Min:-1.71479, Max:3.28154", format="%0.15f")

    with col2:
        selling_price_log = st.number_input(label="**Enter the Value for SELLING PRICE (Log Value)**/ Min:5.97503, Max:7.39036", format="%0.15f")
        item_date_day = st.selectbox("**Select the Day for ITEM DATE**", [str(i) for i in range(1, 32)])
        item_date_month = st.selectbox("**Select the Month for ITEM DATE**", [str(i) for i in range(1, 13)])
        item_date_year = st.selectbox("**Select the Year for ITEM DATE**", ["2020", "2021"])
        delivery_date_day = st.selectbox("**Select the Day for DELIVERY DATE**", [str(i) for i in range(1, 32)])
        delivery_date_month = st.selectbox("**Select the Month for DELIVERY DATE**", [str(i) for i in range(1, 13)])
        delivery_date_year = st.selectbox("**Select the Year for DELIVERY DATE**", ["2020", "2021", "2022"])

    button = st.button(":violet[***PREDICT THE STATUS***]", use_container_width=True)

    if button:
        status = predict_selling_price(country, item_type, application, width, product_ref, quantity_tons_log,
                                       customer_log, thickness_log, selling_price_log, item_date_day,
                                       item_date_month, item_date_year, delivery_date_day, delivery_date_month,
                                       delivery_date_year)

        if status == 1:
            st.write("## :green[**The Status is WON**]")
        else:
            st.write("## :red[**The Status is LOSE**]")

elif option == "PREDICT SELLING PRICE":
    st.header("**PREDICT SELLING PRICE**")
    st.write(" ")

    col1, col2 = st.columns(2)

    with col1:
        country = st.number_input(label="**Enter the Value for COUNTRY**/ Min:25.0, Max:113.0")
        status = st.number_input(label="**Enter the Value for STATUS**/ Min:0.0, Max:8.0")
        item_type = st.number_input(label="**Enter the Value for ITEM TYPE**/ Min:0.0, Max:6.0")
        application = st.number_input(label="**Enter the Value for APPLICATION**/ Min:2.0, Max:87.5")
        width = st.number_input(label="**Enter the Value for WIDTH**/ Min:700.0, Max:1980.0")
        product_ref = st.number_input(label="**Enter the Value for PRODUCT_REF**/ Min:611728, Max:1722207579")
        quantity_tons_log = st.number_input(label="**Enter the Value for QUANTITY_TONS (Log Value)**/ Min:-0.3223343801166147, Max:6.924734324081348", format="%0.15f")
        customer_log = st.number_input(label="**Enter the Value for CUSTOMER (Log Value)**/ Min:17.21910565821408, Max:17.230155364880137", format="%0.15f")

    with col2:
        thickness_log = st.number_input(label="**Enter the Value for THICKNESS (Log Value)**/ Min:-1.7147984280919266, Max:3.281543137578373", format="%0.15f")
        item_date_day = st.selectbox("**Select the Day for ITEM DATE**", [str(i) for i in range(1, 32)])
        item_date_month = st.selectbox("**Select the Month for ITEM DATE**", [str(i) for i in range(1, 13)])
        item_date_year = st.selectbox("**Select the Year for ITEM DATE**", ["2020", "2021"])
        delivery_date_day = st.selectbox("**Select the Day for DELIVERY DATE**", [str(i) for i in range(1, 32)])
        delivery_date_month = st.selectbox("**Select the Month for DELIVERY DATE**", [str(i) for i in range(1, 13)])
        delivery_date_year = st.selectbox("**Select the Year for DELIVERY DATE**", ["2020", "2021", "2022"])

    button = st.button(":violet[***PREDICT THE SELLING PRICE***]", use_container_width=True)

    if button:
        price = predict_selling_price(country, status, item_type, application, width, product_ref, quantity_tons_log,
                                      customer_log, thickness_log, item_date_day,
                                      item_date_month, item_date_year, delivery_date_day, delivery_date_month,
                                      delivery_date_year)

        st.write(f"## :green[**The Predicted Selling Price is {price}**]")
