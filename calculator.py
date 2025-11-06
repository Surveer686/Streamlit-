import streamlit as st
from datetime import date
import math

# ✅ Hide Streamlit default UI elements
custom_css = """
<style>
/* Hide Main Menu + Header toolbar + Bottom-right widgets */
#MainMenu {visibility: hidden;}
header {visibility: hidden;}
footer {visibility: hidden;}

/* Hide floating toolbar buttons */
.st-emotion-cache-1wbqy5l {display: none !important;} 
.st-emotion-cache-1v0mbdj {display: none !important;} 

/* Hide GitHub + Fork buttons */
.stActionButton {display: none !important;}
a[href*="github"] {display: none !important;}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# App title
st.title("All-in-One Smart Calculator")


# Tabs for different tools
basic_tab, sci_tab, age_tab = st.tabs([
    "Basic Calculator",
    "Scientific Calculator",
    "Age Calculator"
])

# ---------------------------------------------------------------------
# TAB 1: Basic Calculator
# ---------------------------------------------------------------------
with basic_tab:
    st.header("Basic Calculator")
    
    first_num = st.number_input("Enter first number:", key="b1")
    second_num = st.number_input("Enter second number:", key="b2")
    
    btn_col1, btn_col2, btn_col3, btn_col4 = st.columns(4)
    
    with btn_col1:
        if st.button("Add"):
            st.success(f"Result: {first_num + second_num}")
    
    with btn_col2:
        if st.button("Subtract"):
            st.success(f"Result: {first_num - second_num}")
    
    with btn_col3:
        if st.button("Multiply"):
            st.success(f"Result: {first_num * second_num}")
    
    with btn_col4:
        if st.button("Divide"):
            if second_num != 0:
                st.success(f"Result: {first_num / second_num}")
            else:
                st.error("You cannot divide by zero!")

# ---------------------------------------------------------------------
# TAB 2: Scientific Calculator
# ---------------------------------------------------------------------
with sci_tab:
    st.header("Scientific Calculator")
    
    sci_num = st.number_input("Enter a number:", key="sci-num")
    
    col_a, col_b, col_c = st.columns(3)

    # Column A — power operations
    with col_a:
        if st.button("Square Root"):
            if sci_num >= 0:
                st.success(f"Square root of {sci_num} = {math.sqrt(sci_num):.4f}")
            else:
                st.error("Negative number’s square root is not real!")
        
        if st.button("Square"):
            st.success(f"{sci_num} squared = {sci_num**2}")

        if st.button("Cube"):
            st.success(f"{sci_num} cubed = {sci_num**3}")

    # Column B — Trigonometry (in degrees)
    with col_b:
        if st.button("sin(x)"):
            st.success(f"sin({sci_num}°) = {math.sin(math.radians(sci_num)):.4f}")
        
        if st.button("cos(x)"):
            st.success(f"cos({sci_num}°) = {math.cos(math.radians(sci_num)):.4f}")
        
        if st.button("tan(x)"):
            st.success(f"tan({sci_num}°) = {math.tan(math.radians(sci_num)):.4f}")

    # Column C — Logarithmic & exponential
    with col_c:
        if st.button("log(x)"):
            if sci_num > 0:
                st.success(f"log({sci_num}) = {math.log10(sci_num):.4f}")
            else:
                st.error("Logarithm requires a positive number!")
        
        if st.button("ln(x)"):
            if sci_num > 0:
                st.success(f"ln({sci_num}) = {math.log(sci_num):.4f}")
            else:
                st.error("ln(x) requires a positive number!")
        
        if st.button("e^x"):
            st.success(f"e^{sci_num} = {math.exp(sci_num):.4f}")

    st.divider()
    
    # Power calculator
    st.subheader("Power Calculator (x^y)")
    base_val = st.number_input("Base number:", key="base")
    power_val = st.number_input("Power:", key="power")
    
    if st.button("Compute Power"):
        st.success(f"{base_val}^{power_val} = {base_val ** power_val}")

# ---------------------------------------------------------------------
# TAB 3: Age Calculator
# ---------------------------------------------------------------------
with age_tab:
    st.header("Age Calculator")
    
    dob = st.date_input("Select your birth date:",
                        value=date(2000, 1, 1),
                        max_value=date.today())
    
    if st.button("Calculate Age"):
        today = date.today()

        # Age breakdown
        years = today.year - dob.year
        months = today.month - dob.month
        days = today.day - dob.day

        # Adjust if birthday has not occurred yet this year
        if months < 0 or (months == 0 and days < 0):
            years -= 1
            months += 12
        
        if days < 0:
            months -= 1
            previous_month = today.month - 1 if today.month > 1 else 12
            
            if previous_month in [1, 3, 5, 7, 8, 10, 12]:
                month_days = 31
            elif previous_month in [4, 6, 9, 11]:
                month_days = 30
            else:
                month_days = 29 if (today.year % 4 == 0) else 28
            
            days += month_days
        
        st.success(f"You are {years} years, {months} months, {days} days old!")

        # Extra breakdown of life duration
        total_days = (today - dob).days
        st.info(f"Total days lived: {total_days:,}")
        st.info(f"Total hours lived: {total_days * 24:,}")
        st.info(f"Total minutes lived: {total_days * 24 * 60:,}")

        # Next birthday countdown
        next_bday = date(today.year, dob.month, dob.day)
        if next_bday < today:
            next_bday = date(today.year + 1, dob.month, dob.day)
        
        left = (next_bday - today).days
        st.info(f"Days until next birthday: {left}")

# Footer
st.divider()
st.caption("Created using Streamlit")
