
# 網站裡面的每一頁一定都會import streamlit as st
#因為我們需要 使用 Streamlit 提供的各種功能來建立網頁介面 winget


import streamlit as st

# ============================================================
# 網頁設定
# ============================================================
st.set_page_config(
    page_title="公司資料系統",
    page_icon="🏢",
    layout="wide",
    # 確保預設狀態為展開
    # initial_sidebar_state="expanded"   這個會把我的側邊欄預設展開
)

# 我們習慣會把其他分頁 收在一個資料夾裡面 方便我們管理
# 這個資料夾的名稱通常是 page 也可以取其他名稱，只要你在程式中引用正確的路徑即可

# ============================================================
# 自訂 CSS：僅設定側邊欄寬度 (不隱藏按鈕)
# ============================================================
# 如果你不需要自訂寬度，可以把這整段 st.markdown 刪除
st.markdown(
    """
    <style>
        /* 僅設定側邊欄寬度，完全保留原生收合與展開按鈕的功能 */
        [data-testid="stSidebar"] {
            min-width: 350px !important; 
            max-width: 350px !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# ============================================================
# 建立頁面
# ============================================================

# st.Page 用來建立各個頁面
#st.Page就像是在建立一個新的頁面，你可以設定這個頁面的檔案路徑、標題、圖示以及是否為預設頁面
#每個頁面都會對應到側邊欄的一個選項，使用者點擊後就會切換到對應的頁面

home_page = st.Page("page/home.py", #依照相對路徑把頁面檔案放進來
                    title="公司頁",   #這個title 就是你在側邊攔顯示名稱
                    icon="🏠", #這個icon 就是你在側邊欄顯示的圖示
                    
                    )
chart_page = st.Page("page/chart.py", title="部門比較頁", icon="📊")
department_page = st.Page("page/department.py", title="業務員比較頁", icon="📈",default=True  #這個default=True 就是設定這個頁面為預設頁面
                    )
sell_person_page = st.Page("page/sale_person.py", title="業務員分析頁", icon="🧑‍💼")
predict_page = st.Page("page/predict.py", title="Iris 分析頁", icon="🌸")
download_page = st.Page("page/download.py", title="報表下載頁", icon="📥")
nba_page = st.Page("page/nba.py", title="NBA 資料頁", icon="🏀")

# ============================================================
# 建立側邊導覽列
# ============================================================
#當你的頁面建立完成後，就可以使用 st.navigation 來建立側邊導覽列，讓使用者可以在不同頁面之間切換


pg = st.navigation(
    #navigation 收一個dictionary，key 是側邊欄的分類名稱，value 是對應的頁面列表
    #key 是側邊欄的分類名稱，value 是對應的頁面列表
    #value 是一個list
    #每個分類底下可以放多個頁面，使用者點擊分類後會看到對應的頁面列表   
    {"公司資訊": [
        home_page
        ], 
    "資料分析": [
        chart_page,
        department_page,
        sell_person_page,
        download_page,
    
        ], 
        "NBA 資料": [
                nba_page
                ],
        "iris_分析": [
            predict_page
        ],
    },
    position="sidebar",#position 設定側邊欄位置 (可以是 "sidebar" 或 "top")
    expanded=True #expanded 設定側邊欄是否預設展開 (True 或 False)
)

# ============================================================
# Sidebar 其他資訊
# ============================================================

# ============================================================
# 執行頁面
# ============================================================
pg.run()