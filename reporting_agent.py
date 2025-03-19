import asyncio
from agents import Agent, Runner, trace
from agents.tool import WebSearchTool
from research_agent import crypto_data_store  # ✅ Import stored historical data

async def main(crypto_symbol):
    """Reporting Agent now takes historical data as input"""
    
    # ✅ Ensure data exists before running analysis
    ticker = crypto_symbol
    if ticker not in crypto_data_store or not crypto_data_store[ticker]:
        print(f"❌ No historical data found for {ticker}. Cannot generate report.")
        return

    historical_data = crypto_data_store[ticker]  # ✅ Fetch stored historical data
    print(f"📊 Reporting Agent received {len(historical_data)} records for {ticker}.")

    # ✅ Convert historical data into a format the agent can understand
    data_summary = f"Historical Data for {ticker}:\n{historical_data}"

    # ✅ Modify the user prompt to include historical data
    analysis_prompt = f"Analyze the following historical data and generate a crypto report: {data_summary}"

    agent = Agent(
        name="Crypto Agent",
        instructions=""""
        "Objective: Your goal is to analyze THE GIVEN DATA for a specific cryptocurrency and provide a comprehensive, accurate, and concise summary and analysis."
        """,
        tools=[WebSearchTool()]
    )

    with trace("Generating Crypto Report"):
        result = await Runner.run(agent, analysis_prompt)  # ✅ Pass historical data

    return ("📄 Generated Report:\n", result.final_output)

if __name__ == "__main__":
    asyncio.run(main("Analyze historical data"))