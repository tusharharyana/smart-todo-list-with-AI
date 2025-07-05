import requests
import json
import re

def extract_json(text):
    try:
        json_data = re.search(r"\{.*\}", text, re.DOTALL).group()
        return json.loads(json_data)
    except Exception as e:
        print("Failed to extract JSON:", e)
        return {
            "improved_description": "Could not parse response",
            "priority_score": 0.5,
            "suggested_deadline": "2025-07-10",
            "recommended_category": "General"
        }

def suggest_task_features(task_data, context_data):
    prompt = f"""
You are a smart task assistant.

Task:
Title: {task_data.get('title')}
Description: {task_data.get('description')}

Context messages:
{chr(10).join(f"- {c}" for c in context_data)}

Based on this, return ONLY a JSON object like:
{{
  "improved_description": "...",
  "priority_score": 0.0 to 1.0,
  "suggested_deadline": "YYYY-MM-DD",
  "recommended_category": "..."
}}
"""

    try:
        response = requests.post(
            "http://192.168.35.24:1234/v1/chat/completions",
            headers={"Content-Type": "application/json"},
            json={
                "model": "mistral",
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.7,
                "max_tokens": 400,
            },
        )
        output = response.json()
        print("AI Response:", output)

        if 'choices' not in output or not output['choices']:
            raise ValueError("Missing 'choices' in response")

        content = output['choices'][0]['message']['content']
        return extract_json(content)

    except Exception as e:
        print("AI request failed:", e)
        return {
            "improved_description": "Could not connect to model",
            "priority_score": 0.5,
            "suggested_deadline": "2025-07-10",
            "recommended_category": "General"
        }
