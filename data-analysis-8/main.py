import streamlit as st
import joblib
import pandas as pd

st.set_page_config(page_title="Iris Species Prediction", page_icon="🌸")

@st.cache_resource
def load():
    model = joblib.load("D:/mydata/Desktop/model.pkl")
    features = joblib.load("D:/mydata/Desktop/features.pkl")
    targets = joblib.load("D:/mydata/Desktop/target.pkl")
    return model, features, targets

model, feature_names, targets = load()

st.title("🌸 Iris Flower Species Predictor")
st.write("Enter the flower measurements to predict its species.")

# Iris feature ranges (in centimeters)
ranges = {
    "sepal length (cm)": (4.0, 8.0, 5.1, 0.1),
    "sepal width (cm)":  (2.0, 4.5, 3.5, 0.1),
    "petal length (cm)": (1.0, 7.0, 1.4, 0.1),
    "petal width (cm)":  (0.1, 2.5, 0.2, 0.1),
}

st.sidebar.header("🌿 Flower Measurements")

inputs = {}

for feat in feature_names:
    lo, hi, default, step = ranges.get(
        feat, (0.0, 10.0, 1.0, 0.1)
    )

    inputs[feat] = st.sidebar.slider(
        feat,
        min_value=float(lo),
        max_value=float(hi),
        value=float(default),
        step=float(step)
    )

if st.button("Predict Species", type="primary"):
    X_input = pd.DataFrame(
        [[inputs[f] for f in feature_names]],
        columns=feature_names
    )

    pred = model.predict(X_input)[0]

    # Map numeric predictions to species names if necessary
    if isinstance(pred, (int, float)) and pred in range(3):
        species = [
            "Setosa",
            "Versicolor",
            "Virginica"
        ][int(pred)]
    else:
        species = str(pred)

    st.success(f"Predicted Iris Species: {species}")

    # Display prediction probabilities when supported
    if hasattr(model, "predict_proba"):
        proba = model.predict_proba(X_input)[0]

        # Use model class labels to match probabilities correctly
        classes = getattr(
            model, "classes_", list(targets)
        )

        proba_df = pd.DataFrame({
            "Species": [
                (
                    ["Setosa", "Versicolor", "Virginica"][int(c)]
                    if isinstance(c, (int, float))
                    and c in range(3)
                    else str(c)
                )
                for c in classes
            ],
            "Probability": proba
        })

        proba_df["Probability (%)"] = (
            proba_df["Probability"] * 100
        ).round(2)

        st.subheader("Prediction Probabilities")
        st.bar_chart(
            proba_df.set_index("Species")["Probability (%)"]
        )

        st.dataframe(
            proba_df[["Species", "Probability (%)"]],
            hide_index=True,
            use_container_width=True
        )
