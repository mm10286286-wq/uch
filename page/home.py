import streamlit as st


# ============================================================
# 1. 頁面基本設定
# ============================================================

st.set_page_config(
    page_title="建行科技 | 您的 3C 科技夥伴",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# ============================================================
# 2. HTML / CSS 工具函式
#    避免 Streamlit Markdown 將縮排 HTML 誤判成程式碼
# ============================================================

def compact_html(html: str) -> str:
    return "".join(
        line.strip()
        for line in html.strip().splitlines()
    )


def render_html(html: str) -> None:
    st.markdown(
        compact_html(html),
        unsafe_allow_html=True,
    )


# ============================================================
# 3. 北歐手繪風 CSS
# ============================================================

CSS = """
<style>

:root {
    --paper: #F7F3EA;
    --paper-light: #FFFDF8;
    --ink: #34483D;
    --ink-soft: #65736A;
    --sage: #8EA28F;
    --sage-light: #DCE5DD;
    --blue-gray: #7895A1;
    --terracotta: #C4846C;
    --sand: #D9CFBE;
    --olive: #A8A478;
}


/* ============================================================
   整體背景
============================================================ */

.stApp {
    background-color: var(--paper);

    background-image:
        radial-gradient(
            #D8D2C4 0.7px,
            transparent 0.7px
        );

    background-size: 22px 22px;
}


.block-container {
    max-width: 1280px;

    padding-top: 2rem;
    padding-bottom: 4rem;
}


/* ============================================================
   字型
============================================================ */

html,
body,
[class*="css"] {

    font-family:
        "Microsoft JhengHei",
        "PingFang TC",
        "Segoe UI",
        sans-serif;
}


p {
    line-height: 1.85;
}


/* ============================================================
   Hero
============================================================ */

.hero-box {

    background: var(--paper-light);

    border:
        3px solid
        var(--ink);

    border-radius:
        28px 20px 30px 22px;

    padding:
        44px 28px 38px 28px;

    margin-bottom: 30px;

    box-shadow:
        9px 9px 0
        var(--sand);

    text-align: center;
}


.hero-decoration {

    font-size: 1.45rem;

    letter-spacing: 8px;

    margin-bottom: 8px;
}


.main-title {

    color: var(--ink);

    font-size:
        clamp(
            2.7rem,
            6vw,
            4.4rem
        );

    font-weight: 900;

    letter-spacing: 4px;

    margin-bottom: 8px;
}


.company-en {

    color: #9A6B58;

    font-size: 0.95rem;

    letter-spacing: 5px;

    margin-bottom: 14px;
}


.sub-title {

    color: #5E7164;

    font-size:
        clamp(
            1rem,
            2vw,
            1.35rem
        );

    font-weight: 700;
}


.hero-copy {

    text-align: center;

    color: var(--ink-soft);

    font-size: 1.05rem;

    line-height: 2;

    margin:
        26px auto 8px auto;

    max-width: 820px;
}


/* ============================================================
   區塊標題
============================================================ */

.section-header {

    color: var(--ink);

    font-size:
        clamp(
            1.65rem,
            3vw,
            2.1rem
        );

    font-weight: 900;

    display: inline-block;

    padding:
        4px 12px 8px 12px;

    border-bottom:
        4px dashed
        var(--terracotta);

    margin-top: 48px;

    margin-bottom: 10px;
}


.section-description {

    color: var(--ink-soft);

    font-size: 1rem;

    margin-bottom: 24px;
}


/* ============================================================
   品牌特色卡片
============================================================ */

.feature-card {

    background:
        var(--paper-light);

    border:
        2px solid
        #596D60;

    border-radius:
        20px 28px 18px 25px;

    box-shadow:
        5px 6px 0
        rgba(
            82,
            98,
            87,
            0.14
        );

    padding:
        24px 20px;

    min-height: 245px;

    margin-bottom: 16px;

    transition:
        transform 0.18s ease,
        box-shadow 0.18s ease;
}


.feature-card:hover {

    transform:
        translateY(-4px)
        rotate(-0.3deg);

    box-shadow:
        7px 9px 0
        rgba(
            82,
            98,
            87,
            0.17
        );
}


.feature-icon {

    font-size: 2.35rem;

    margin-bottom: 8px;
}


.feature-title {

    color: #394B40;

    font-size: 1.18rem;

    font-weight: 900;

    margin-bottom: 11px;
}


.feature-text {

    color: #606C64;

    font-size: 0.94rem;

    line-height: 1.85;
}


/* ============================================================
   商品卡片
============================================================ */

.product-card {

    background:
        var(--paper-light);

    border:
        2px solid
        #53675A;

    border-top:
        7px solid
        var(--sage);

    border-radius:
        22px 18px 26px 20px;

    box-shadow:
        6px 7px 0
        rgba(
            95,
            105,
            93,
            0.13
        );

    padding: 24px;

    min-height: 270px;

    margin-top: 8px;

    margin-bottom: 24px;
}


.product-title {

    color: #405448;

    font-size: 1.25rem;

    font-weight: 900;

    margin-bottom: 12px;
}


.product-text {

    color: #606A63;

    font-size: 0.94rem;

    line-height: 1.85;
}


/* ============================================================
   商品 Tag
============================================================ */

.tag {

    display: inline-block;

    background: #E8E4D8;

    color: #56655A;

    padding:
        5px 11px;

    border-radius: 20px;

    border:
        1px dashed
        #87998B;

    font-size: 0.78rem;

    margin-right: 5px;

    margin-top: 10px;
}


/* ============================================================
   商品圖片
============================================================ */

[data-testid="stImage"] img {

    border-radius: 24px;

    border:
        3px solid
        #56685B;

    box-shadow:
        7px 8px 0
        #D7D0C2;
}


/* ============================================================
   品牌理念
============================================================ */

.quote-box {

    background:
        var(--sage-light);

    border:
        2px dashed
        #66796B;

    border-radius: 28px;

    padding:
        36px 28px;

    margin:
        44px 0 16px 0;

    text-align: center;
}


.quote-title {

    color: #384A3E;

    font-size:
        clamp(
            1.35rem,
            3vw,
            1.75rem
        );

    font-weight: 900;

    margin-top: 8px;
}


.quote-text {

    color: #5A6B60;

    font-size: 1.02rem;

    line-height: 2;

    margin-top: 14px;
}


/* ============================================================
   聯絡表單提示
============================================================ */

.contact-note {

    background: #F0E8DC;

    border-left:
        5px solid
        var(--terracotta);

    border-radius: 10px;

    padding:
        14px 18px;

    color: #655F58;

    margin-bottom: 18px;
}


/* ============================================================
   Streamlit Form
============================================================ */

div[data-testid="stForm"] {

    background:
        rgba(
            255,
            253,
            248,
            0.78
        );

    border:
        2px solid
        #C9C0B1;

    border-radius: 22px;

    padding:
        18px 20px 8px 20px;
}


/* ============================================================
   按鈕
============================================================ */

div.stButton > button,
div[data-testid="stFormSubmitButton"] > button {

    border-radius: 999px;

    border:
        2px solid
        #4C6254;

    background:
        #4C6254;

    color: white;

    font-weight: 800;

    min-height: 46px;
}


div.stButton > button:hover,
div[data-testid="stFormSubmitButton"] > button:hover {

    border-color:
        #35483D;

    background:
        #35483D;

    color: white;
}


/* ============================================================
   Footer
============================================================ */

.footer-box {

    background:
        #3E5045;

    color:
        #F7F3EA;

    padding:
        34px 24px;

    border-radius:
        28px 20px 28px 20px;

    text-align: center;

    border:
        3px solid
        #2F4037;

    box-shadow:
        7px 8px 0
        #CABFAE;

    margin-top: 28px;
}


.footer-box h3 {

    color: #FFF8EC;

    font-size: 1.55rem;

    margin:
        8px 0 12px 0;
}


.footer-box p {

    color: #E8E3D8;

    margin:
        6px 0;
}


.footer-line {

    border-top:
        1px dashed
        #88978D;

    margin:
        20px auto;

    max-width: 620px;
}


hr {

    border: none;

    border-top:
        2px dashed
        #B8B1A4;

    margin:
        40px 0;
}


/* ============================================================
   手機版
============================================================ */

@media (max-width: 768px) {

    .block-container {

        padding-top: 1.2rem;

        padding-left: 1rem;

        padding-right: 1rem;
    }


    .hero-box {

        padding:
            30px 16px;

        box-shadow:
            6px 6px 0
            var(--sand);
    }


    .hero-decoration {

        letter-spacing: 3px;
    }


    .main-title {

        letter-spacing: 2px;
    }


    .feature-card,
    .product-card {

        min-height: auto;
    }
}

</style>
"""


render_html(CSS)


# ============================================================
# 4. 品牌特色卡片函式
# ============================================================

def feature_card(
    icon: str,
    title: str,
    text: str,
) -> None:

    render_html(
        f"""
<div class="feature-card">
<div class="feature-icon">{icon}</div>
<div class="feature-title">{title}</div>
<div class="feature-text">{text}</div>
</div>
"""
    )


# ============================================================
# 5. 商品卡片函式
# ============================================================

def product_card(
    icon: str,
    title: str,
    text: str,
    tags: list[str],
    accent_color: str = "#8EA28F",
) -> None:

    tags_html = "".join(
        f'<span class="tag">{tag}</span>'
        for tag in tags
    )

    render_html(
        f"""
<div
class="product-card"
style="border-top-color:{accent_color};"
>
<div class="product-title">
{icon} {title}
</div>
<div class="product-text">
{text}
</div>
<div>
{tags_html}
</div>
</div>
"""
    )


# ============================================================
# 6. Hero Section
# ============================================================

render_html(
    """
<div class="hero-box">

<div class="hero-decoration">
🌿 ✦ 💻 ✦ 📱 ✦ 🌱
</div>

<div class="main-title">
建行科技
</div>

<div class="company-en">
JIANXING TECHNOLOGY
</div>

<div class="sub-title">
簡單科技・自在生活・找到真正適合您的數位夥伴
</div>

</div>
"""
)


# ============================================================
# Hero 圖片
# ============================================================

st.image(
    "https://images.unsplash.com/photo-1496181133206-80ce9b88a853"
    "?auto=format&fit=crop&w=1600&q=85",
    use_container_width=True,
)


render_html(
    """
<div class="hero-copy">

在建行科技，我們相信好的科技不需要複雜。

<br>

從手機、電腦到智慧周邊，
我們替您精選真正好用、耐用，
且適合生活的科技產品。

</div>
"""
)


# ============================================================
# 7. 為什麼選擇我們
# ============================================================

render_html(
    """
<div class="section-header">
🌱 為什麼選擇建行科技？
</div>

<div class="section-description">
用專業選擇產品，用簡單的方式解決您的科技需求。
</div>
"""
)


col1, col2, col3, col4 = st.columns(4)


# ============================================================
# 卡片 1
# ============================================================

with col1:

    feature_card(
        "🛡️",
        "原廠安心保固",
        """
精選原廠與正規通路商品，
提供完整售後服務與保固。

<br><br>

從購買到使用，
都有建行科技陪著您。
""",
    )


# ============================================================
# 卡片 2
# ============================================================

with col2:

    feature_card(
        "📦",
        "快速安心出貨",
        """
熱門商品現貨供應，
完成訂單後快速安排出貨。

<br><br>

讓您期待的新科技，
不需要等太久。
""",
    )


# ============================================================
# 卡片 3
# ============================================================

with col3:

    feature_card(
        "🌿",
        "精選高性價比",
        """
不只是追求便宜，
而是幫您找到真正值得購買的產品。

<br><br>

每一分預算，
都花在真正重要的地方。
""",
    )


# ============================================================
# 卡片 4
# ============================================================

with col4:

    feature_card(
        "💬",
        "專業科技顧問",
        """
不懂規格沒有關係。

<br><br>

告訴我們您的需求與預算，
我們會協助您找到最適合的設備。
""",
    )


# ============================================================
# 8. 精選科技生活
# ============================================================

render_html(
    """
<div class="section-header">
🛒 精選科技生活
</div>

<div class="section-description">
不追求繁複的規格堆疊，而是選擇真正適合您的產品。
</div>
"""
)


row1_col1, row1_col2, row1_col3 = st.columns(3)


# ============================================================
# 智慧型手機
# ============================================================

with row1_col1:

    st.image(
        "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9"
        "?auto=format&fit=crop&w=900&q=80",
        use_container_width=True,
    )

    product_card(
        "📱",
        "旗艦智慧型手機",
        """
Apple、Samsung、Google、ASUS 等熱門品牌。

從日常使用、攝影、影音到高效能遊戲，
依照您的預算與需求推薦真正適合的手機。
""",
        [
            "Apple",
            "Samsung",
            "Android",
            "Gaming",
        ],
        "#C4846C",
    )


# ============================================================
# 筆記型電腦
# ============================================================

with row1_col2:

    st.image(
        "https://images.unsplash.com/photo-1496181133206-80ce9b88a853"
        "?auto=format&fit=crop&w=900&q=80",
        use_container_width=True,
    )

    product_card(
        "💻",
        "筆電與工作設備",
        """
商務筆電、學生筆電、
創作者工作站與電競設備。

從簡單文書到 AI、影像剪輯與程式開發，
為不同工作情境搭配適合設備。
""",
        [
            "商務",
            "電競",
            "創作者",
            "AI PC",
        ],
        "#7895A1",
    )


# ============================================================
# 智慧穿戴
# ============================================================

with row1_col3:

    st.image(
        "https://images.unsplash.com/photo-1523275335684-37898b6baf30"
        "?auto=format&fit=crop&w=900&q=80",
        use_container_width=True,
    )

    product_card(
        "⌚",
        "智慧穿戴與配件",
        """
智慧手錶、藍牙耳機、
充電設備、保護殼及行動周邊。

用簡單好看的科技配件，
讓您的數位生活更加完整。
""",
        [
            "智慧手錶",
            "耳機",
            "充電",
            "配件",
        ],
        "#A2788C",
    )


# ============================================================
# 9. 更多服務
# ============================================================

render_html(
    """
<div class="section-header">
🧰 我們還能為您做什麼？
</div>

<div class="section-description">
從個人設備到企業採購，
提供更完整的科技解決方案。
</div>
"""
)


row2_col1, row2_col2, row2_col3 = st.columns(3)


# ============================================================
# 客製電腦
# ============================================================

with row2_col1:

    product_card(
        "🖥️",
        "客製化桌上型電腦",
        """
不用自己研究複雜零組件。

告訴我們用途與預算，
我們協助搭配 CPU、GPU、
RAM、SSD 與散熱系統。

從辦公室到高階電競，
都能打造適合您的主機。
""",
        [
            "客製主機",
            "RTX",
            "Gaming",
        ],
        "#A8A478",
    )


# ============================================================
# 智慧家庭
# ============================================================

with row2_col2:

    product_card(
        "🏡",
        "智慧家庭設備",
        """
智慧攝影機、
Wi-Fi 網路設備、
智慧插座與居家科技。

讓科技自然融入生活，
打造安全、方便而舒適的
智慧居家環境。
""",
        [
            "Wi-Fi",
            "IoT",
            "智慧家庭",
        ],
        "#8DA9A0",
    )


# ============================================================
# 企業採購
# ============================================================

with row2_col3:

    product_card(
        "🏢",
        "企業設備採購",
        """
提供公司、工作室與團隊
電腦、螢幕及周邊設備採購服務。

協助設備規劃與規格統整，
讓企業採購更簡單、更有效率。
""",
        [
            "企業採購",
            "設備規劃",
            "商務",
        ],
        "#B18B78",
    )


# ============================================================
# 10. 品牌理念
# ============================================================

render_html(
    """
<div class="quote-box">

<div style="font-size:2.2rem;">
☕ 🌿 💻
</div>

<div class="quote-title">
科技，應該讓生活變得更簡單。
</div>

<div class="quote-text">

我們不只是販售產品，
更希望成為您值得信任的科技夥伴。

<br><br>

不需要懂所有規格，
您只需要告訴我們：

<strong>
「我想拿它來做什麼？」
</strong>

<br><br>

剩下的，交給建行科技。

</div>

</div>
"""
)


# ============================================================
# 11. 聯絡區
# ============================================================

render_html(
    """
<div class="section-header">
✉️ 與我們聊聊
</div>

<div class="section-description">
想換手機、買電腦，
或不知道該怎麼選？
告訴我們您的需求，
我們協助您整理方向。
</div>

<div class="contact-note">
🌿 填寫用途、預算與偏好即可，
不需要先研究複雜規格。
</div>
"""
)


# ============================================================
# 12. 聯絡表單
# ============================================================

with st.form(
    "contact_form",
    clear_on_submit=False,
):

    contact_col1, contact_col2 = st.columns(2)


    # ========================================================
    # 左側
    # ========================================================

    with contact_col1:

        name = st.text_input(
            "您的姓名 *",
            placeholder="例如：王先生",
        )


        email = st.text_input(
            "Email",
            placeholder="example@email.com",
        )


    # ========================================================
    # 右側
    # ========================================================

    with contact_col2:

        product_type = st.selectbox(
            "想了解的產品",
            [
                "請選擇",
                "智慧型手機",
                "筆記型電腦",
                "桌上型電腦",
                "智慧穿戴",
                "3C 周邊配件",
                "智慧家庭",
                "企業設備採購",
                "其他",
            ],
        )


        budget = st.selectbox(
            "預算範圍",
            [
                "尚未決定",
                "10,000 元以下",
                "10,000 ～ 30,000 元",
                "30,000 ～ 50,000 元",
                "50,000 ～ 100,000 元",
                "100,000 元以上",
            ],
        )


    # ========================================================
    # 需求說明
    # ========================================================

    message = st.text_area(
        "告訴我們您的需求 *",

        placeholder=(
            "例如：想找一台 3 萬元左右，"
            "可以做文書、Python 程式開發，"
            "偶爾剪輯影片的筆電。"
        ),

        height=150,
    )


    # ========================================================
    # Submit
    # ========================================================

    submitted = st.form_submit_button(
        "🌿 確認諮詢內容",
        use_container_width=True,
    )


# ============================================================
# 13. 表單驗證
# ============================================================

if submitted:

    if not name.strip():

        st.warning(
            "請先輸入您的姓名。"
        )


    elif not message.strip():

        st.warning(
            "請簡單告訴我們您的需求。"
        )


    else:

        st.success(
            f"{name}，表單內容已完成確認。"
        )


        # 顯示使用者輸入資訊
        with st.expander(
            "📋 查看您的諮詢內容"
        ):

            st.write(
                f"**姓名：** {name}"
            )

            st.write(
                f"**Email：** "
                f"{email if email else '未填寫'}"
            )

            st.write(
                f"**產品：** {product_type}"
            )

            st.write(
                f"**預算：** {budget}"
            )

            st.write(
                "**需求：**"
            )

            st.write(
                message
            )


# ============================================================
# 14. Footer
# ============================================================

st.markdown("---")


footer_col1, footer_col2, footer_col3 = st.columns(
    [1, 4, 1]
)


with footer_col2:

    render_html(
        """
<div class="footer-box">

<div style="font-size:2rem;">
🌿
</div>

<h3>
建行科技
</h3>

<p>
讓科技更簡單，讓生活更舒服。
</p>

<p>
📧 客服信箱：
service@jianxing-tech.com.tw
</p>

<p>
🕙 營業時間：
週一至週日 10:00 - 22:00
</p>

<div class="footer-line">
</div>

<p
style="
font-size:0.84rem;
opacity:0.8;
"
>
© 2026 建行科技
JIANXING TECHNOLOGY
・ All Rights Reserved.
</p>

</div>
"""
    )