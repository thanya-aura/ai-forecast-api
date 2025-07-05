import pandas as pd
from typing import Dict
import openai
import os

# Load OpenAI API key securely from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_forecast(df: pd.DataFrame) -> Dict:
    """
    Analyze forecast vs actuals:
    - Calculates variance
    - Computes average variance
    - Generates GPT commentary
    """
    if "Actual" not in df.columns or "Forecast" not in df.columns:
        raise ValueError("Missing required columns: 'Actual' and 'Forecast'")

    df["Variance"] = df["Forecast"] - df["Actual"]
    average_variance = df["Variance"].mean()

    commentary = generate_gpt_commentary(df)

    return {
        "average_variance": round(average_variance, 2),
        "rows": len(df),
        "commentary": commentary
    }

def generate_gpt_commentary(df: pd.DataFrame) -> str:
    """
    Generates GPT-powered commentary from forecast vs actuals DataFrame.
    """
    prompt = f"""Analyze this forecast vs actuals:
{df.head().to_string(index=False)}"""

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a senior financial analyst."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error generating commentary: {str(e)}"
