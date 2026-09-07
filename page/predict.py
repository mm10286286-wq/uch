
import streamlit as st
import joblib


# ==========================================
# 1. 導入訓練好的模型
# ==========================================
model = joblib.load("model/iris_model.pkl")


# ==========================================
# 2. 建立網頁標題
# ==========================================
st.title("🌸 Iris 鳶尾花分類預測")


st.write("請輸入花瓣的長度與寬度，讓模型預測鳶尾花品種。")


# ==========================================
# 3. 建立兩個 Input
# ==========================================

# Petal Length
pl = st.number_input(
    "花瓣長度 Petal Length (cm)",
    min_value=0.0,
    max_value=10.0,
    value=1.4,
    step=0.1
)

# Petal Width
pw = st.number_input(
    "花瓣寬度 Petal Width (cm)",
    min_value=0.0,
    max_value=5.0,
    value=0.2,
    step=0.1
)


# ==========================================
# 4. 建立預測按鈕
# ==========================================
if st.button("🔍 預測"):

    # 模型預測
    prediction = model.predict([[pl, pw]])

    # ==========================================
    # 5. 將數字類別轉換成品種名稱
    # ==========================================
    species = {
        0: "Iris Setosa｜山鳶尾",
        1: "Iris Versicolor｜變色鳶尾",
        2: "Iris Virginica｜維吉尼亞鳶尾"
    }

    predicted_species = species[prediction[0]]


    # ==========================================
    # 6. 輸出結果
    # ==========================================
    st.subheader("🌸 預測結果")

    st.write("花瓣長度 PL：", pl, "cm")
    st.write("花瓣寬度 PW：", pw, "cm")

    st.success(f"預測品種：{predicted_species}")

    st.write("預測類別：", prediction[0])
