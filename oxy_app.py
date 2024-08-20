import streamlit as st

def calculate_remaining_time(psi, flow_rate):
    remaining_time = (0.28 * (psi)) / flow_rate
    return remaining_time

def main():
    st.title("Tank Time Calculator")
    st.write("Enter the PSI (Pounds per Square Inch) and Flow Rate (Liters per Min) to calculate the remaining time for the tank.")
    
    psi = st.number_input("Enter PSI:", min_value=0)
    flow_rate = st.number_input("Enter Flow Rate:", min_value=0)
    
    if st.button("Calculate Remaining Time"):
        if psi >= 0:
            remaining_time = calculate_remaining_time(psi, flow_rate)
            st.write(f"Remaining Time: {remaining_time:.2f} minutes")
        else:
            st.error("PSI must be greater than or equal to 0")

if __name__ == "__main__":
    main()
