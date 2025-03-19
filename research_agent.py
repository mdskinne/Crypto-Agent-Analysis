import asyncio
import re
from agents import Agent, Runner, function_tool
from financialdatasets import fetch_crypto_prices


# ✅ Global dictionary to store fetched cryptocurrency data
crypto_data_store = {}

# Function to extract the ticker symbol from a user query
def extract_ticker(user_input: str):
    """
    Extracts a cryptocurrency ticker from a user's prompt.
    Assumes tickers follow standard conventions like 'BTC-USD', 'ETH-USD', etc.
    """
    match = re.search(r"\b[A-Z]{2,5}-USD\b", user_input)  # Example: BTC-USD, ETH-USD
    ticker = match.group(0) if match else None
    print(f"🔍 Extracted Ticker: {ticker}")  # Debugging
    return ticker

# Define the crypto data fetching tool as an async function
async def crypto_data_tool(user_input: str):
    global crypto_data_store  # Ensure data persists

    print(f"📩 Received user input: {user_input}")

    ticker = extract_ticker(user_input)
    if not ticker:
        print("❌ No ticker found in prompt.")
        crypto_data_store["error"] = "Could not determine the cryptocurrency ticker."
        return

    print(f"✅ Extracted ticker: {ticker}")

    # Fetch data
    prices = fetch_crypto_prices(ticker)

    print(f"🔍 API Response Type: {type(prices)}")
    print(f"📊 Full API Response: {prices}")  # Debugging full response

    if not prices:
        print(f"❌ No data returned for {ticker}. The API response might be empty.")
        crypto_data_store[ticker] = {"error": f"Could not retrieve data for {ticker}."}
        return

    # Extract the actual data list if it's inside a dictionary
    if isinstance(prices, dict) and "prices" in prices:
        prices = prices["prices"]  # ✅ Extract the full price history list
        print(f"✅ Extracted Full Price History List: {prices}")  # Debugging

    # Ensure prices is a valid list
    if not isinstance(prices, list) or len(prices) == 0:
        print("❌ No valid historical data found.")
        return

    print(f"✅ {len(prices)} historical records fetched for {ticker}.")

    # ✅ Store full price history instead of just latest data
    if ticker not in crypto_data_store:
        crypto_data_store[ticker] = []  # Initialize list if it doesn't exist

    crypto_data_store[ticker].extend(prices)  # Append the full dataset

    print(f"📁 Full historical data successfully stored for {ticker}!")
    print(f"📦 Stored Crypto Data (Inside Tool): {len(crypto_data_store[ticker])} records stored.")



async def main(user_prompt):
    global crypto_data_store  # ✅ Ensure main() recognizes stored data

    agent = Agent(
        name="Research Agent",
        instructions="""
        You have access to the Financial Datasets API to pull financial data.
        Your job is to determine the cryptocurrency ticker from the user's prompt 
        and use the `crypto_data_tool` function to fetch and store the latest available data.
        """,
        tools=[function_tool(crypto_data_tool)],  # ✅ Register function as a tool
    )

    
    
    await Runner.run(agent, user_prompt)  # Run with correct tool integration

    # 🔍 Check stored data AFTER the agent finishes running
    print(f"📦 Stored Crypto Data (Final in main()): {crypto_data_store}")

if __name__ == "__main__":
    asyncio.run(main())