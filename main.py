import streamlit as st
import joblib
import numpy as np
#from xgboost import XGBClassifier

# Load the trained model
model = joblib.load('xgboost_model.joblib')

# Page config
st.set_page_config(page_title="💧 Water Quality Classifier", layout="centered")

# Sidebar
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2900/2900596.png", width=100)
    st.title("🌊 Water Quality App")
    st.markdown("This app uses a trained model to determine if water is **safe** or **unsafe** based on input features.")

def main():
    st.title("💧 Water Quality Classifier")
    st.markdown("Enter the following parameters to classify the water quality:")

    with st.expander("🔍 Input Water Parameters"):
        col1, col2, col3 = st.columns(3)

        with col1:
            feature1 = st.number_input("pH", value=0.0)
            feature4 = st.number_input("Hardness", value=0.0)
            feature7 = st.number_input("Sulfate", value=0.0)

        with col2:
            feature2 = st.number_input("Turbidity", value=0.0)
            feature5 = st.number_input("Solids", value=0.0)
            feature8 = st.number_input("Conductivity", value=0.0)

        with col3:
            feature3 = st.number_input("Trihalomethanes", value=0.5)
            feature6 = st.number_input("Chloramines", value=0.0)
            feature9 = st.number_input("Organic Carbon", value=0.0)

    if st.button("🚰 Classify Water Quality"):
        features = np.array([[feature1, feature4, feature5, feature6, feature7,
                              feature8, feature9, feature3, feature2]])
        #prediction = model.predict(features)
        #quality = "✅ Safe" if prediction[0] == 1 else "⚠️ Unsafe"
        #st.success(f"The water quality is classified as: **{quality}**")
        result = model.predict(features)[0]
        st.markdown("---")
        if result == 1:
            st.success("✅ The water is **POTABLE** (Safe to drink).")
        else:
            st.error("❌ The water is **NOT POTABLE** (Unsafe to drink).")
    st.markdown("---")
    st.markdown("Made with ❤️ using Streamlit")

if __name__ == "__main__":
    main()
