# Black-Scholes Option Pricing Model

An interactive Streamlit app for pricing European call and put options using the Black-Scholes formula, with real-time payoff visualization.

## Features


Calculates European call and put option prices using the Black-Scholes model
Interactive sidebar controls for all model inputs (asset price, strike, time to maturity, risk-free rate, volatility)
Live payoff diagram comparing call and put payoffs at expiration
Built with Streamlit for a clean, responsive UI


## Formula

The Black-Scholes formula for a call option:

C = S * N(d1) - K * e^(-rT) * N(d2)

For a put option:

P = K * e^(-rT) * N(-d2) - S * N(-d1)

Where:

d1 = (ln(S/K) + (r + σ²/2) * T) / (σ * √T)
d2 = d1 - σ * √T


S — current asset price
K — strike price
T — time to maturity (in years)
r — risk-free interest rate
σ — volatility
N — cumulative distribution function of the standard normal distribution


## Installation

Clone the repository and install the dependencies:

bashgit clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>
pip install streamlit numpy matplotlib scipy

## Usage

Run the app with Streamlit:

bashstreamlit run app.py

Then use the sidebar to adjust the asset price, strike price, time to maturity, risk-free rate, and volatility. The call and put prices, along with a payoff chart, update automatically.

## Assumptions

This model assumes European-style options (exercisable only at expiration) and no dividends paid on the underlying asset.

## Tech Stack


Streamlit — web app framework
NumPy — numerical computations
SciPy — normal distribution functions
Matplotlib — payoff chart visualization
