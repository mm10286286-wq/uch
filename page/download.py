import streamlit as st
import pandas as pd
from io import BytesIO

# ==========================================
# 網頁基本設定
# ==========================================
st.set_page_config(
    page_title="業務銷售報表系統",
    page_icon="📥",
    layout="wide"
)

st.title("📥 業務銷售報表匯出與檢視系統")

# ==========================================
# 資料讀取與預處理
# ==========================================
@st.cache_data
def load_data():
    # 讀取 CSV 檔案
    df = pd.read_csv("data/sales.csv")
    return df

try:
    df = load_data()
except FileNotFoundError:
    st.error("找不到 `data/sales.csv` 檔案，請確認檔案路徑是否正確。")
    st.stop()

# ==========================================
# 篩選條件 
# ==========================================
st.markdown("### 🔍 報表篩選條件")

col1, col2 = st.columns(2)

with col1:
    # 1. 根據 "業務單位" 的 unique 值製作下拉式選單
    unit_list = df['業務單位'].unique().tolist()
    selected_unit = st.selectbox("請選擇業務單位", unit_list)

with col2:
    # 2. 根據選定的 "業務單位" 篩選出對應的 "業務員"
    filtered_by_unit = df[df['業務單位'] == selected_unit]
    salesperson_list = filtered_by_unit['業務員'].unique().tolist()
    selected_salesperson = st.selectbox("請選擇業務員", salesperson_list)

st.divider()

# ==========================================
# 資料運算與頁面顯示
# ==========================================
# 根據選定的 '業務單位' 與 '業務員' 篩選原始資料
final_df = df[(df['業務單位'] == selected_unit) & (df['業務員'] == selected_salesperson)]

if final_df.empty:
    st.warning(f"目前找不到 **{selected_unit}** 的 **{selected_salesperson}** 相關銷售紀錄。")
else:
    # 計算加總數值
    total_sales_amount = final_df['銷售金額'].sum()
    total_sales_qty = final_df['銷售數量'].sum()

    # 建立「成果報告」的 DataFrame
    summary_df = pd.DataFrame({
        "銷售總金額": [total_sales_amount],
        "銷售總數量": [total_sales_qty]
    })

    # --- 1. 在畫面上顯示：成果預覽 ---
    st.markdown(f"#### 📊 成果總覽：{selected_unit} - {selected_salesperson}")
    col_a, col_b = st.columns(2)
    col_a.metric("銷售總數量", f"{total_sales_qty:,}")
    col_b.metric("銷售總金額", f"${total_sales_amount:,.0f}")
    
    st.markdown("<br>", unsafe_allow_html=True)

    # --- 2. 在畫面上顯示：原始資料預覽 ---
    st.markdown("#### 📋 原始資料詳細清單")
    st.dataframe(final_df, use_container_width=True, hide_index=True)

    # ==========================================
    # 製作 Excel 檔案與下載按鈕
    # ==========================================
    # 寫入記憶體 (BytesIO)
    output = BytesIO()
    
    # 使用 pd.ExcelWriter 將不同的 DataFrame 寫入同一個 Excel 檔案的不同 Sheet 中
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        # Sheet 1: 成果報告
        summary_df.to_excel(writer, index=False, sheet_name='成果報告')
        
        # Sheet 2: 原始資料
        final_df.to_excel(writer, index=False, sheet_name='原始資料')
        
    # 取得寫入完畢的 Excel 二進位資料
    excel_data = output.getvalue()

    st.divider()
    
    # 設定下載檔案名稱： 業務單位_業務員.xlsx
    file_name = f"{selected_unit}_{selected_salesperson}.xlsx"
    
    st.download_button(
        label=f"📥 下載 {file_name}",
        data=excel_data,
        file_name=file_name,
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        type="primary"
    )