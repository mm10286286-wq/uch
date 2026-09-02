import streamlit as st

# 1. 頁面基本設定 (必須在第一行)
st.set_page_config(
    page_title="星耀科技 | 您的3C電子專家",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. 注入自訂 CSS 來打造色彩繽紛的視覺效果
def local_css():
    st.markdown("""
    <style>
    /* 主標題漸層色彩 */
    .main-title {
        background: -webkit-linear-gradient(45deg, #FF4B4B, #9B59B6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 4rem;
        font-weight: 800;
        text-align: center;
        margin-bottom: 0px;
        padding-bottom: 10px;
    }
    /* 副標題色彩 */
    .sub-title {
        color: #1E90FF;
        font-size: 1.5rem;
        font-weight: 600;
        text-align: center;
        margin-top: 0px;
        margin-bottom: 30px;
    }
    /* 區塊標題底線設計 */
    .section-header {
        color: #2C3E50;
        font-weight: 700;
        border-bottom: 4px solid #FFD700;
        padding-bottom: 10px;
        margin-top: 40px;
        margin-bottom: 20px;
    }
    /* 產品卡片懸浮效果 */
    .product-card {
        background-color: #F8F9FA;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        border-top: 5px solid #00C9A7;
    }
    </style>
    """, unsafe_allow_html=True)

local_css()

# 3. 網站首圖與標題 (Hero Section)
st.markdown('<div class="main-title">🚀 星耀科技 (StarTech)</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">為您打造智慧生活，最新手機、頂級電腦一次滿足！</div>', unsafe_allow_html=True)

# 橫幅圖片
st.image("https://images.unsplash.com/photo-1550009158-9effb64fda5a?auto=format&fit=crop&w=1200&q=80", use_container_width=True)

st.markdown("---")

# 4. 公司強項展示 (核心競爭力)
st.markdown('<div class="section-header">💡 為什麼選擇我們？ (品牌強項)</div>', unsafe_allow_html=True)

# 利用 Streamlit 內建的彩色提示框來營造色彩繽紛感
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.error("🛡️ **原廠授權保固**\n\n全館商品 100% 正品，提供最長3年安心保固，維修無死角。")
with col2:
    st.info("⚡ **極速閃電出貨**\n\n現貨秒發，當日下午三點前下單，24小時內火速送達您手中。")
with col3:
    st.success("💰 **極致高性價比**\n\n挑戰全網最低價，搭配專屬會員折扣，讓您買得開心用得安心。")
with col4:
    st.warning("🤝 **專業技術客服**\n\n擁有專業工程師團隊，線上即時解決您的軟硬體疑難雜症。")

# 5. 專營品項展示 (Products)
st.markdown('<div class="section-header">🛒 專營熱門品項</div>', unsafe_allow_html=True)

# 建立兩排的產品展示區
row1_col1, row1_col2, row1_col3 = st.columns(3)

with row1_col1:
    st.image("https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?auto=format&fit=crop&w=800&q=80", caption="📱 旗艦智慧型手機")
    st.markdown("""
    <div class="product-card">
        <h4 style="color: #E74C3C;">旗艦與電競手機</h4>
        <p>涵蓋 Apple、Samsung、ROG 等最新款高階機型。無論是專業攝影還是極限手遊，為您提供無可挑惕的順暢體驗。</p>
    </div>
    """, unsafe_allow_html=True)

with row1_col2:
    st.image("https://images.unsplash.com/photo-1496181133206-80ce9b88a853?auto=format&fit=crop&w=800&q=80", caption="💻 筆記型與桌上型電腦")
    st.markdown("""
    <div class="product-card" style="border-top-color: #3498DB;">
        <h4 style="color: #3498DB;">筆電 & 客製化主機</h4>
        <p>輕薄文書筆電、創作者高效能工作站，以及頂級水冷電競主機組裝。根據您的需求，量身打造專屬設備。</p>
    </div>
    """, unsafe_allow_html=True)

with row1_col3:
    # 修正處：替換了失效的圖片連結，改為另一張穩定的智慧手錶/配件圖片
    st.image("https://images.unsplash.com/photo-1523275335684-37898b6baf30?auto=format&fit=crop&w=800&q=80", caption="🎧 智慧穿戴與質感配件")
    st.markdown("""
    <div class="product-card" style="border-top-color: #9B59B6;">
        <h4 style="color: #9B59B6;">智慧手錶 & 藍牙耳機</h4>
        <p>降噪耳機、智慧健康手錶、氮化鎵快充頭、抗摔手機殼。提供最全面的3C周邊，完善您的科技生態圈。</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# 6. 頁尾與聯絡資訊 (Footer)
st.markdown("<br>", unsafe_allow_html=True)
footer_col1, footer_col2, footer_col3 = st.columns([1,2,1])

with footer_col2:
    st.markdown("""
    <div style="text-align: center; background-color: #333333; color: white; padding: 20px; border-radius: 10px;">
        <h3>📞 準備好升級您的科技裝備了嗎？</h3>
        <p>立即聯繫我們獲取今日專屬優惠報價！</p>
        <p>客服信箱：service@startech.com.tw | 營業時間：週一至週日 10:00 - 22:00</p>
    </div>
    """, unsafe_allow_html=True)