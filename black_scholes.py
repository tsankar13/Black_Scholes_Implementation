import streamlit as st

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def black_scholes(S, K, T, r, sigma, option_type = 'call'):
    #by default we have a call option, but we can specify this later
    #The black scholes formula determines a price for European stock options based on a calculation using the following variables
    #The formula is as follows for a call option:
    #C = (S)(N)(d1) - Ke^(-rt)N(d2)


    #C is the call option price
    #S is the current asset price
    #K is the strike price
    #T is the time to maturity in years
    #r is the risk-free interest rate
    #sigma is the volatility
    #N is a normal distribution (essentially a cumulative distribution function)

    #Return type: a float of the option price
    #-------------------------------------------
    #Step 1: Calculating the d components of the model
    d1 = (np.log(S/K) + (r + (sigma**2)/2) * T)/(sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    #Well what are the d components? ->

    #Step 2: Depending on the option type, what formula should we use:
    #For call options:
    if (option_type == 'call'):
        C = (S) * (norm.cdf(d1)) - (K) * (np.exp(-r*T)) * (norm.cdf(d2))

    #For put options:
    elif option_type == 'put':
        C = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)

    return C


print(black_scholes(10,10, 10, 10, 10, 'call'))

# --- UI: Streamlit Configuration ---
st.set_page_config(page_title="Black-Scholes Option Pricer", layout="wide")
st.title("📈 Black-Scholes Option Pricing Model")

# --- Sidebar: User Inputs ---
st.sidebar.header("Model Inputs")
S = st.sidebar.number_input("Current Asset Price ($S$)", value=100.0)
K = st.sidebar.number_input("Strike Price ($K$)", value=100.0)
T = st.sidebar.slider("Time to Maturity (Years)", min_value=0.01, max_value=5.0, value=1.0)
r = st.sidebar.slider("Risk-Free Interest Rate", min_value=0.0, max_value=0.20, value=0.05, step=0.01)
sigma = st.sidebar.slider("Volatility ($\sigma$)", min_value=0.01, max_value=1.0, value=0.20, step=0.01)

# --- Main Area: Calculation & Output ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("Option Price")
    call_price = black_scholes(S, K, T, r, sigma, 'call')
    put_price = black_scholes(S, K, T, r, sigma, 'put')
    
    st.metric("Call Option Price", f"${call_price:.2f}")
    st.metric("Put Option Price", f"${put_price:.2f}")

with col2:
    st.subheader("Payoff Visualization")
    # Generate a range of prices for the chart
    s_range = np.linspace(S * 0.5, S * 1.5, 100)
    
    # Simple payoff logic (Price at Expiry - Strike)
    call_payoff = np.maximum(s_range - K, 0)
    put_payoff = np.maximum(K - s_range, 0)
    
    fig, ax = plt.subplots()
    ax.plot(s_range, call_payoff, label='Call Payoff', color='green')
    ax.plot(s_range, put_payoff, label='Put Payoff', color='red')
    ax.axvline(S, color='grey', linestyle='--', label='Current Price')
    ax.set_xlabel("Price at Expiration")
    ax.set_ylabel("Payoff")
    ax.legend()
    st.pyplot(fig)

st.divider()
st.info("Note: This model assumes European options and no dividends.")
    
