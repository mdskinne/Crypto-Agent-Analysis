import asyncio
from flask import Flask, render_template, request
import research_agent
import reporting_agent
from research_agent import crypto_data_store

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    """Render the homepage with input form and results."""
    result = None  # ✅ Initialize result

    if request.method == "POST":
        crypto_symbol = request.form["crypto_symbol"].strip().upper()

        if not crypto_symbol:
            result = "❌ Please enter a cryptocurrency symbol."
        else:
            # ✅ Run async function using `asyncio.run()`
            result = asyncio.run(run_analysis(crypto_symbol))

    return render_template("index.html", result=result)

async def run_analysis(crypto_symbol):
    """Run Research & Reporting Agents asynchronously and return the analysis."""
    user_prompt = f"Fetch historical data for {crypto_symbol}"

    # ✅ Step 1: Run Research Agent
    await research_agent.main(user_prompt)

    # ✅ Step 2: Check if Data Was Successfully Stored
    if crypto_symbol not in crypto_data_store or not crypto_data_store[crypto_symbol]:
        return f"❌ No historical data found for {crypto_symbol}. Try another symbol."

    # ✅ Step 3: Run Reporting Agent and Capture Output
    report = await reporting_agent.main(crypto_symbol)

    # ✅ Fix: Ensure `report` is a string (convert tuple to string if necessary)
    if isinstance(report, tuple):
        report = "\n".join(map(str, report))  # ✅ Convert tuple elements to a formatted string

    formatted_report = report.replace("\n", "<br>")  # ✅ Convert newlines for HTML display

    return f"<h3>📄 Analysis for {crypto_symbol}:</h3><pre style='white-space: pre-wrap;'>{formatted_report}</pre>"

if __name__ == "__main__":
    app.run(debug=True)



