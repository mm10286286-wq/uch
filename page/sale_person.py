import streamlit as st
import pandas as pd
import plotly.express as px

# ==========================================
# 網頁基本設定
# ==========================================
st.set_page_config(
    page_title="銷售資料分析",
    page_icon="📊",
    layout="wide"
)

st.title("📊 銷售資料分析儀表板")

# ==========================================
# 資料讀取與預處理
# ==========================================
# 使用 st.cache_data 避免每次操作選單時重複讀取檔案，提升效能
@st.cache_data
def load_data():
    # 讀取 CSV 檔案
    df = pd.read_csv("data/sales.csv")
    
    # 將 '銷售日期' 轉換為 datetime 格式，並提取 '年-月'
    df['銷售日期'] = pd.to_datetime(df['銷售日期'])
    df['年月'] = df['銷售日期'].dt.strftime('%Y-%m')
    
    return df

try:
    df = load_data()
except FileNotFoundError:
    st.error("找不到 `data/sales.csv` 檔案，請確認檔案路徑是否正確。")
    st.stop()

# ==========================================
# 篩選條件 (放置於主畫面並排顯示)
# ==========================================
st.markdown("### 🔍 篩選條件")

# 建立三個欄位，讓選單水平並排，版面更簡潔
col1, col2, col3 = st.columns(3)

with col1:
    # 1. 根據 "業務單位" 的 unique 值製作下拉式選單
    unit_list = df['業務單位'].unique().tolist()
    selected_unit = st.selectbox("請選擇業務單位", unit_list)

with col2:
    # 2. 根據選定的 "業務單位" 篩選出對應的 "業務員"
    filtered_by_unit = df[df['業務單位'] == selected_unit]
    salesperson_list = filtered_by_unit['業務員'].unique().tolist()
    selected_salesperson = st.selectbox("請選擇業務員", salesperson_list)

with col3:
    # 3. 根據 "銷售產品" 的 unique 值製作下拉式選單 
    product_list = df['銷售產品'].unique().tolist()
    selected_product = st.selectbox("請選擇銷售產品", product_list)

st.divider() # 畫一條分隔線區隔條件與圖表

# ==========================================
# 資料篩選與圖表繪製
# ==========================================
# 根據 '業務員' 與 '銷售產品' 進行最終資料篩選
final_df = df[(df['業務員'] == selected_salesperson) & (df['銷售產品'] == selected_product)]

# 檢查篩選後是否有資料
if final_df.empty:
    st.warning(f"目前找不到 **{selected_salesperson}** 銷售 **{selected_product}** 的相關紀錄。")
else:
    # 根據 '年月' 分組，並計算 '銷售金額' 加總
    grouped_df = final_df.groupby('年月')['銷售金額'].sum().reset_index()

    # 利用 Plotly Express 繪製長條圖 (Bar Chart)
    fig = px.bar(
        grouped_df, 
        x='年月', 
        y='銷售金額',
        text='銷售金額', # 在柱狀圖上方顯示數值
        title=f"業績趨勢：{selected_salesperson} - {selected_product}",
        labels={'年月': '銷售月份', '銷售金額': '總銷售金額'}
    )
    
    # 調整圖表外觀：文字位置與 X 軸刻度
    fig.update_traces(textposition='outside')
    fig.update_layout(xaxis_tickangle=-45)

    # 將 Plotly 圖表顯示在 Streamlit 畫面上
    st.plotly_chart(fig, use_container_width=True)
    
    # 額外顯示資料表格供參考
    st.subheader("📝 詳細數據")
    st.dataframe(grouped_df, use_container_width=True)