
import pandas as pd
import openai
import sys
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Replace with your actual OpenAI API key or load from env
openai.api_key = "YOUR_OPENAI_API_KEY"

def load_data(path):
    return pd.read_csv(path)

def train_model(df):
    X = df[['grades', 'attendance', 'participation_score']]
    y = df['at_risk']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model

def generate_advice(row):
    prompt = (
        f"A student has the following data:\n"
        f"- Grades: {row['grades']}\n"
        f"- Attendance: {row['attendance']}\n"
        f"- Participation Score: {row['participation_score']}\n"
        f"The predicted performance is: {row['performance']}.\n"
        f"Give a one-paragraph explanation of why and recommend actions."
    )
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=100
        )
        return response.choices[0].message.content.strip()
    except:
        return "Feedback generation failed."

def main(path):
    df = load_data(path)
    model = train_model(df)
    df['predicted_risk'] = model.predict(df[['grades', 'attendance', 'participation_score']])
    df['performance'] = df['predicted_risk'].map({0: 'Good', 1: 'At Risk'})
    df['GenAI_Feedback'] = df.apply(generate_advice, axis=1)
    summary = df[['grades', 'attendance', 'participation_score', 'performance', 'GenAI_Feedback']].to_string(index=False)
    print(summary)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python model.py <path_to_csv>")
    else:
        main(sys.argv[1])
