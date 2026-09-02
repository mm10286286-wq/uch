import streamlit as st
import pandas as pd
import plotly.express as px


# ============================================================
# 頁面標題
# ============================================================

st.title("📊 部門業務銷售比較")

st.write("選擇業務單位，查看該單位各業務員的銷售金額加總。")

st.divider()


# ============================================================
# 讀取 CSV 資料
# ============================================================

try:
    df = pd.read_csv("data/sales.csv")

except FileNotFoundError:
    st.error("找不到 data/sales.csv，請確認檔案路徑。")
    st.stop()


# ============================================================
# 檢查必要欄位
# ============================================================

required_columns = [
    "業務單位",
    "業務員",
    "銷售金額"
]

missing_columns = [
    col for col in required_columns
    if col not in df.columns
]

if missing_columns:
    st.error(
        f"sales.csv 缺少以下欄位：{', '.join(missing_columns)}"
    )
    st.stop()


# ============================================================
# 資料清理
# ============================================================

# 移除業務單位空值
df = df.dropna(
    subset=[
        "業務單位",
        "業務員"
    ]
)


# 將銷售金額轉成數字
# 如果 CSV 裡有 1,000 或 $1,000，也可以處理
df["銷售金額"] = (
    df["銷售金額"]
    .astype(str)
    .str.replace(",", "", regex=False)
    .str.replace("$", "", regex=False)
    .str.strip()
)

df["銷售金額"] = pd.to_numeric(
    df["銷售金額"],
    errors="coerce"
)


# 無法轉換成數字的資料移除
df = df.dropna(
    subset=["銷售金額"]
)


# ============================================================
# 取得業務單位 unique
# ============================================================

business_units = (
    df["業務單位"]
    .dropna()
    .unique()
    .tolist()
)


# ============================================================
# 下拉式選單
# ============================================================

selected_unit = st.selectbox(
    "請選擇業務單位",
    business_units
)


# ============================================================
# 根據選擇的業務單位篩選資料
# ============================================================

filtered_df = df[
    df["業務單位"] == selected_unit
].copy()


# ============================================================
# 根據業務員加總銷售金額
# ============================================================

sales_summary = (
    filtered_df
    .groupby(
        "業務員",
        as_index=False
    )["銷售金額"]
    .sum()
)


# ============================================================
# 依照銷售金額由高到低排序
# ============================================================

sales_summary = sales_summary.sort_values(
    by="銷售金額",
    ascending=False
)


# ============================================================
# 顯示基本資訊
# ============================================================

st.subheader(f"🏢 {selected_unit}")

col1, col2 = st.columns(2)


with col1:
    st.metric(
        label="業務員人數",
        value=f"{sales_summary['業務員'].nunique()} 人"
    )


with col2:
    st.metric(
        label="總銷售金額",
        value=f"${sales_summary['銷售金額'].sum():,.0f}"
    )


st.divider()


# ============================================================
# Plotly Bar Chart
# ============================================================

st.subheader("📊 業務員銷售金額")


fig = px.bar(
    sales_summary,
    x="業務員",
    y="銷售金額",
    text="銷售金額",
    title=f"{selected_unit}－各業務員銷售金額"
)


# ============================================================
# 圖表格式
# ============================================================

fig.update_traces(
    texttemplate="%{text:,.0f}",
    textposition="outside",
    hovertemplate=(
        "業務員：%{x}<br>"
        "銷售金額：%{y:,.0f}"
        "<extra></extra>"
    )
)


fig.update_layout(
    xaxis_title="業務員",
    yaxis_title="銷售金額",
    showlegend=False
)


fig.update_yaxes(
    tickformat=","
)


# ============================================================
# 顯示圖表
# ============================================================

st.plotly_chart(
    fig,
    use_container_width=True
)


# ============================================================
# 顯示彙總資料
# ============================================================

st.divider()

st.subheader("📋 業務員銷售統計")


display_df = sales_summary.copy()

display_df["銷售金額"] = display_df[
    "銷售金額"
].map(
    lambda x: f"{x:,.0f}"
)


st.dataframe(
    display_df,
    use_container_width=True,
    hide_index=True
)