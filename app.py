from flask import Flask, render_template, request
import joblib
import pandas as pd
import numpy as np
import pickle

app = Flask(__name__)

# Load model and necessary data
model = joblib.load("ipl_predictor.pkl")
X_data = joblib.load("X_data.pkl")
feature_columns = joblib.load("feature_columns.pkl")

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    player_data = None
    players = sorted(X_data['batsman'].unique())
    
    if request.method == "POST":
        selected_player = request.form.get("player")
        player_df = X_data[X_data['batsman'] == selected_player].sort_values("match_id")

        if not player_df.empty:
            latest_row = player_df.iloc[-1:][feature_columns]
            predicted_runs = model.predict(latest_row)[0]
            prediction = f"{selected_player} is predicted to score approximately {predicted_runs:.1f} runs."
            player_data = player_df[['match_id', 'runs_scored', 'strike_rate', 'rolling_avg_runs_3']].tail(5)
        else:
            prediction = f"Not enough data to predict for {selected_player}."

        return render_template("index.html", players=players, prediction=prediction, player_data=player_data)

    return render_template("index.html", players=players, prediction=prediction, player_data=player_data)

if __name__ == "__main__":
    app.run(debug=True)
