import streamlit as st
import sqlite3

uploaded_file = st.file_uploader("Upload a business card image", type=["jpg", "png"])

company_name = st.text_input("Company Name")
card_holder_name = st.text_input("Card Holder Name")
designation = st.text_input("Designation")
mobile_number = st.text_input("Mobile Number")
email_address = st.text_input("Email Address")
website_url = st.text_input("Website URL")
area = st.text_input("Area")
city = st.text_input("City")
state = st.text_input("State")
pin_code = st.text_input("Pin Code")

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

    if st.button("Extract Information"):
        extracted_data = {
            "company_name": company_name,
            "card_holder_name": card_holder_name,
            "designation": designation,
            "mobile_number": mobile_number,
            "email_address": email_address,
            "website_url": website_url,
            "area": area,
            "city": city,
            "state": state,
            "pin_code": pin_code,
        }

        st.header("Extracted Information")
        st.write("Company Name:", extracted_data["company_name"])
        st.write("Card Holder Name:", extracted_data["card_holder_name"])
        st.write("Designation:", extracted_data["designation"])
        st.write("Mobile Number:", extracted_data["mobile_number"])
        st.write("Email Address:", extracted_data["email_address"])
        st.write("Website URL:", extracted_data["website_url"])
        st.write("Area:", extracted_data["area"])
        st.write("City:", extracted_data["city"])
        st.write("State:", extracted_data["state"])
        st.write("Pin Code:", extracted_data["pin_code"])


conn = sqlite3.connect('business_cards.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS business_cards (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    image BLOB,
                    company_name TEXT,
                    card_holder_name TEXT,
                    mobile_number TEXT,
                    email_address TEXT,
                    website_url TEXT,
                    area TEXT,
                    city TEXT,
                    state TEXT,
                    pin_code TEXT
                 )''')

cursor.execute('''INSERT INTO business_cards (image, company_name, card_holder_name, designation,mobile_number, 
email_address, website_url, area,city, state, pin_code) 
 VALUES (image_ocr, company_name, card_holder_name,designation,mobile_number,email_address,website_url,area,city,state,pin_code)''', 
 (image_data, extracted_data["company_name"], extracted_data["card_holder_name"],
                extracted_data["designation"], extracted_data["mobile_number"],
                extracted_data["email_address"], extracted_data["website_url"],
                extracted_data["area"], extracted_data["city"],
                extracted_data["state"], extracted_data["pin_code"]))

conn.commit()
conn.close()
