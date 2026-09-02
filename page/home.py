import streamlit as st

# =========================
# CSS
# =========================
#全世界的網頁 都是html+css做出來的
#html是網頁的骨架當作就是網頁的格式 比如 標題 文字 區塊 按鈕 連結 圖片等等
#css是網頁的美化 專門設定尺寸 延伸 位置 顏色 字型等等
#streamlit也可以使用html+css 但是streamlit本身是python寫的 所以streamlit提供了一個st.markdown() 可以讓你在裡面寫html+css
#markdown是網頁的標記語言 你可以把它想成是一個簡化版的html 但是streamlit的st.markdown()可以直接寫html+css
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;500;700;900&display=swap');

    * {
        font-family: 'Noto Sans TC', sans-serif;
    }

    .stApp {
        background: linear-gradient(135deg, #f8fbff 0%, #eef5ff 45%, #fff7fc 100%);
    }

    /* 隱藏 Streamlit 預設元素 (已將 header 隱藏移除，讓 >> 按鈕正常顯示) */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}

    /* Hero */
    .hero {
        padding: 70px 50px;
        border-radius: 30px;
        background:
            radial-gradient(circle at 85% 20%, rgba(255,255,255,0.35) 0%, transparent 25%),
            radial-gradient(circle at 10% 90%, rgba(255,255,255,0.25) 0%, transparent 25%),
            linear-gradient(135deg, #5B5FEF 0%, #7B3FF2 45%, #D946EF 100%);
        color: white;
        text-align: center;
        box-shadow: 0 20px 50px rgba(91,95,239,0.25);
        margin-bottom: 35px;
    }

    .hero h1 {
        font-size: 52px;
        font-weight: 900;
        margin-bottom: 15px;
        letter-spacing: 3px;
    }

    .hero p {
        font-size: 21px;
        line-height: 1.8;
        margin: 0 auto;
        max-width: 850px;
        color: rgba(255,255,255,0.95);
    }

    .hero-badge {
        display: inline-block;
        background: rgba(255,255,255,0.18);
        border: 1px solid rgba(255,255,255,0.35);
        padding: 8px 20px;
        border-radius: 50px;
        font-size: 15px;
        margin-bottom: 18px;
        backdrop-filter: blur(10px);
    }

    /* Section */
    .section-title {
        text-align: center;
        font-size: 34px;
        font-weight: 900;
        color: #20243a;
        margin-top: 45px;
        margin-bottom: 8px;
    }

    .section-subtitle {
        text-align: center;
        color: #697086;
        font-size: 16px;
        margin-bottom: 30px;
    }

    /* Cards */
    .card {
        background: rgba(255,255,255,0.92);
        padding: 28px;
        border-radius: 22px;
        min-height: 245px;
        box-shadow: 0 10px 30px rgba(40,50,90,0.08);
        border: 1px solid rgba(255,255,255,0.8);
        transition: all 0.3s ease;
    }

    .card:hover {
        transform: translateY(-6px);
        box-shadow: 0 18px 40px rgba(40,50,90,0.15);
    }

    .card-icon {
        font-size: 44px;
        margin-bottom: 12px;
    }

    .card h3 {
        color: #292D4F;
        font-size: 21px;
        margin-bottom: 10px;
    }

    .card p {
        color: #6B7280;
        line-height: 1.8;
        font-size: 15px;
    }

    /* Product card */
    .product-card {
        background: white;
        border-radius: 22px;
        overflow: hidden;
        box-shadow: 0 10px 30px rgba(40,50,90,0.09);
        height: 100%;
        border: 1px solid #edf0f7;
    }

    .product-info {
        padding: 22px;
    }

    .product-info h3 {
        color: #252A45;
        font-size: 20px;
        margin-bottom: 8px;
    }

    .product-info p {
        color: #73798B;
        font-size: 14px;
        line-height: 1.7;
    }

    .tag {
        display: inline-block;
        padding: 5px 12px;
        border-radius: 20px;
        color: white;
        font-size: 12px;
        font-weight: 700;
        margin-bottom: 10px;
    }

    .tag-blue { background: linear-gradient(90deg,#2563EB,#06B6D4); }
    .tag-purple { background: linear-gradient(90deg,#7C3AED,#DB2777); }
    .tag-orange { background: linear-gradient(90deg,#F97316,#EF4444); }
    .tag-green { background: linear-gradient(90deg,#059669,#10B981); }

    /* Stats */
    .stat-box {
        text-align: center;
        background: white;
        border-radius: 20px;
        padding: 25px 15px;
        box-shadow: 0 8px 25px rgba(40,50,90,0.07);
    }

    .stat-number {
        font-size: 34px;
        font-weight: 900;
        color: #6246EA;
    }

    .stat-label {
        color: #73798B;
        font-size: 14px;
        margin-top: 5px;
    }

    /* CTA */
    .cta {
        margin-top: 55px;
        padding: 50px 30px;
        border-radius: 28px;
        text-align: center;
        color: white;
        background: linear-gradient(120deg, #0F172A, #312E81, #701A75);
        box-shadow: 0 20px 45px rgba(49,46,129,0.25);
    }

    .cta h2 {
        font-size: 34px;
        font-weight: 900;
        margin-bottom: 12px;
    }

    .cta p {
        color: #E5E7EB;
        font-size: 16px;
        margin-bottom: 25px;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #8A90A3;
        padding: 35px 10px 15px 10px;
        font-size: 13px;
    }

    /* Streamlit button */
    .stButton > button {
        border: none;
        border-radius: 50px;
        padding: 10px 30px;
        font-weight: 700;
        background: linear-gradient(90deg, #6366F1, #D946EF);
        color: white;
        box-shadow: 0 8px 20px rgba(99,102,241,0.25);
        transition: 0.25s;
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 12px 25px rgba(99,102,241,0.35);
        color: white;
    }

    /* 手機版 */
    @media (max-width: 768px) {
        .hero {
            padding: 45px 20px;
        }

        .hero h1 {
            font-size: 35px;
        }

        .hero p {
            font-size: 16px;
        }

        .section-title {
            font-size: 28px;
        }
    }
</style>
""", unsafe_allow_html=True)


# =========================
# 公司名稱
# =========================
COMPANY_NAME = "星曜科技"
COMPANY_SLOGAN = "讓科技，成為生活最強的夥伴"


# =========================
# Hero 首頁主視覺
# =========================
st.markdown(f"""
<div class="hero">
    <div class="hero-badge">⚡ 專業 3C 電子產品銷售</div>
    <h1>📱 {COMPANY_NAME}</h1>
    <p>
        {COMPANY_SLOGAN}<br>
        精選手機、電腦、平板與各式 3C 周邊，
        為您提供專業、可靠、值得信賴的科技產品與服務。
    </p>
</div>
""", unsafe_allow_html=True)


# =========================
# 公司核心數據
# =========================
st.markdown('<div class="section-title">為什麼選擇我們？</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">專業、品質、服務，是我們一直堅持的核心價值</div>',
    unsafe_allow_html=True
)
# st columns() 可以建立多欄位的佈局，這裡建立四欄把很多功能包成一個區塊
#所以st.columns(4) 代表建立四欄的區塊水平排列 這裡的c1,c2,c3,c4就是四個欄位的變數 你可以在裡面放置任何streamlit的元件

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown("""
    <div class="stat-box">
        <div class="stat-number">10+</div>
        <div class="stat-label">年產業經驗</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="stat-box">
        <div class="stat-number">1000+</div>
        <div class="stat-label">產品選擇</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="stat-box">
        <div class="stat-number">99%</div>
        <div class="stat-label">客戶滿意度</div>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown("""
    <div class="stat-box">
        <div class="stat-number">365</div>
        <div class="stat-label">全年服務</div>
    </div>
    """, unsafe_allow_html=True)


# =========================
# 公司強項
# =========================
st.markdown('<div class="section-title">💎 我們的公司強項</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">從產品挑選到售後服務，提供完整的 3C 購物體驗</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
        <div class="card-icon">🏆</div>
        <h3>專業產品選品</h3>
        <p>
            嚴選市場熱門與高品質電子產品，
            從手機、電腦到周邊設備，提供多元且實用的產品選擇，
            幫助客戶找到最適合自己的科技產品。
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <div class="card-icon">💰</div>
        <h3>價格透明實惠</h3>
        <p>
            重視產品品質與價格之間的平衡，
            提供具有競爭力的價格，讓客戶用合理預算
            買到符合需求的產品。
        </p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
        <div class="card-icon">🛠️</div>
        <h3>完整售後服務</h3>
        <p>
            不只把產品交到客戶手上，
            更重視後續使用體驗，提供專業諮詢、
            產品使用協助與售後支援。
        </p>
    </div>
    """, unsafe_allow_html=True)


# =========================
# 專營品項
# =========================
st.markdown('<div class="section-title">🛍️ 專營品項</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">一次滿足個人、家庭與企業的科技需求</div>',
    unsafe_allow_html=True
)

p1, p2, p3 = st.columns(3)

with p1:
    st.markdown("""
    <div class="product-card">
    """, unsafe_allow_html=True)

    st.image(
        "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?auto=format&fit=crop&w=900&q=85",
        use_container_width=True
    )

    st.markdown("""
        <div class="product-info">
            <span class="tag tag-blue">SMARTPHONE</span>
            <h3>📱 智慧型手機</h3>
            <p>
                精選各品牌智慧型手機，涵蓋日常使用、
                商務工作、攝影娛樂與高效能旗艦機型。
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)

with p2:
    st.markdown("""
    <div class="product-card">
    """, unsafe_allow_html=True)

    st.image(
        "https://images.unsplash.com/photo-1496181133206-80ce9b88a853?auto=format&fit=crop&w=900&q=85",
        use_container_width=True
    )

    st.markdown("""
        <div class="product-info">
            <span class="tag tag-purple">COMPUTER</span>
            <h3>💻 筆記型電腦</h3>
            <p>
                提供商務辦公、學生學習、創意設計、
                工程工作與高效能娛樂等不同需求的電腦產品。
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)

with p3:
    st.markdown("""
    <div class="product-card">
    """, unsafe_allow_html=True)

    st.image(
        "https://images.unsplash.com/photo-1600080972464-8e5f35f63d08?auto=format&fit=crop&w=900&q=85",
        use_container_width=True
    )

    st.markdown("""
        <div class="product-info">
            <span class="tag tag-orange">3C ACCESSORIES</span>
            <h3>🎧 3C 電子周邊</h3>
            <p>
                耳機、鍵盤、滑鼠、充電器、傳輸線、
                行動電源與各式科技周邊，打造完整使用體驗。
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)


# =========================
# 更多品項
# =========================
st.markdown("<br>", unsafe_allow_html=True)

a1, a2, a3, a4 = st.columns(4)

accessories = [
    ("📟", "平板電腦", "行動娛樂與工作"),
    ("⌚", "智慧穿戴", "智慧手錶與穿戴設備"),
    ("🖥️", "桌上型電腦", "辦公與高效能運算"),
    ("🔌", "電腦周邊", "鍵盤、滑鼠及各式配件")
]

for col, (icon, title, desc) in zip([a1, a2, a3, a4], accessories):
    with col:
        st.markdown(f"""
        <div class="card" style="min-height:160px;text-align:center;">
            <div class="card-icon">{icon}</div>
            <h3>{title}</h3>
            <p>{desc}</p>
        </div>
        """, unsafe_allow_html=True)


# =========================
# 服務流程
# =========================
st.markdown('<div class="section-title">🚀 我們的服務</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">簡單、快速、專業，讓購買 3C 產品變得更輕鬆</div>',
    unsafe_allow_html=True
)

s1, s2, s3, s4 = st.columns(4)

services = [
    ("01", "需求了解", "了解您的預算與使用需求"),
    ("02", "專業推薦", "提供適合您的產品選擇"),
    ("03", "產品購買", "快速完成產品訂購"),
    ("04", "售後支援", "提供後續使用與服務協助")
]

for col, (num, title, desc) in zip([s1, s2, s3, s4], services):
    with col:
        st.markdown(f"""
        <div class="card" style="min-height:200px;">
            <div style="
                width:48px;
                height:48px;
                line-height:48px;
                text-align:center;
                border-radius:50%;
                background:linear-gradient(135deg,#6366F1,#D946EF);
                color:white;
                font-weight:900;
                margin-bottom:15px;
            ">{num}</div>
            <h3>{title}</h3>
            <p>{desc}</p>
        </div>
        """, unsafe_allow_html=True)


# =========================
# 公司理念
# =========================
st.markdown('<div class="section-title">❤️ 我們的品牌理念</div>', unsafe_allow_html=True)

st.markdown("""
<div style="
    background:white;
    padding:40px;
    border-radius:25px;
    box-shadow:0 10px 30px rgba(40,50,90,0.08);
    text-align:center;
    margin-top:20px;
">
    <div style="font-size:45px;">🌟</div>
    <h2 style="color:#292D4F;font-weight:900;">
        不只是賣產品，更希望成為您的科技生活夥伴
    </h2>
    <p style="
        max-width:800px;
        margin:auto;
        color:#6B7280;
        line-height:2;
        font-size:16px;
    ">
        面對快速變化的科技市場，我們持續關注最新產品與市場趨勢，
        用專業的角度協助客戶挑選真正適合自己的產品。
        無論是日常生活、工作辦公、娛樂或企業需求，
        我們都希望讓科技變得更簡單、更容易使用。
    </p>
</div>
""", unsafe_allow_html=True)


# =========================
# CTA
# =========================
st.markdown("""
<div class="cta">
    <h2>📲 找到最適合你的科技產品</h2>
    <p>
        有手機、電腦或 3C 產品需求嗎？<br>
        歡迎與我們聯繫，讓專業團隊為您提供合適的產品建議。
    </p>
</div>
""", unsafe_allow_html=True)

# 按鈕
b1, b2, b3 = st.columns([1, 1, 1])

with b2:
    if st.button("💬 立即諮詢", use_container_width=True):
        st.success("感謝您的詢問！歡迎透過電話、LINE 或官方社群與我們聯繫。")


# =========================
# 聯絡資訊
# =========================
st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<div style="
    background:rgba(255,255,255,0.75);
    border-radius:20px;
    padding:30px;
    text-align:center;
    border:1px solid #E8EAF2;
">
    <h3 style="color:#292D4F;">📞 聯絡我們</h3>
    <p style="color:#6B7280;line-height:2;">
        📍 公司地址：請填入您的公司地址<br>
        ☎️ 電話：請填入您的聯絡電話<br>
        📧 Email：請填入您的 Email<br>
        💬 LINE：請填入您的 LINE ID
    </p>
</div>
""", unsafe_allow_html=True)


# =========================
# Footer
# =========================
st.markdown(f"""
<div class="footer">
    <b>{COMPANY_NAME}</b> ｜ 手機・電腦・3C 電子產品專業服務<br>
    © 2026 {COMPANY_NAME}. All Rights Reserved.
</div>
""", unsafe_allow_html=True)