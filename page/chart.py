import streamlit as st
import pandas as pd
import plotly.express as px

# 設定網頁標題
st.set_page_config(page_title="銷售分析儀表板", layout="wide")

st.title("銷售數據資料視覺化")

# 讀取資料 (使用 cache 加速讀取)
@st.cache_data
def load_data():
    return pd.read_csv('data/sales.csv')

try:
    # 載入 CSV
    df = load_data()
    
    # 將畫面切分為兩欄
    col1, col2 = st.columns(2)

    with col1:
        # --- 1. 業務單位銷售數量分析 ---
        qty_df = df.groupby('業務單位', as_index=False)['銷售數量'].sum()
        
        # 繪製 Plotly Bar Chart
        fig_qty = px.bar(
            qty_df, 
            x='業務單位', 
            y='銷售數量', 
            color='業務單位', 
            title='業務單位銷售數量分析',
            color_discrete_sequence=['#f6bd60', '#f7ede2', '#f5cac3', '#84a59d', '#f28482']
        )
        
        # 控制 Bar 的寬度不超過全圖的 15%
        # Plotly 的 width 參數是基於類別所佔的區塊比例，因此： 0.15 * 類別數量
        qty_categories_count = len(qty_df)
        qty_bar_width = min(0.15 * qty_categories_count, 0.8) # 設置上限避免分類過多時重疊
        fig_qty.update_traces(width=qty_bar_width)
        
        # 顯示圖表
        st.plotly_chart(fig_qty, use_container_width=True)

    with col2:
        # --- 2. 業務單位銷售金額分析 ---
        amt_df = df.groupby('業務單位', as_index=False)['銷售金額'].sum()
        
        # 繪製 Plotly Bar Chart
        fig_amt = px.bar(
            amt_df, 
            x='業務單位', 
            y='銷售金額', 
            color='業務單位', 
            title='業務單位銷售金額分析',
            color_discrete_sequence=['#2b2d42', '#8d99ae', '#edf2f4', '#ef233c', '#d90429']
        )
        
        # 控制 Bar 的寬度不超過全圖的 15%
        amt_categories_count = len(amt_df)
        amt_bar_width = min(0.15 * amt_categories_count, 0.8)
        fig_amt.update_traces(width=amt_bar_width)
        
        # 顯示圖表
        st.plotly_chart(fig_amt, use_container_width=True)

except FileNotFoundError:
    st.error("找不到 `data/sales.csv` 檔案。請確認資料夾結構中包含 `data` 資料夾與檔案。")
except Exception as e:
    st.error(f"發生錯誤：{e}")