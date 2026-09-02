import os
import pandas as pd
import streamlit as st
import mysql.connector


# ============================================================
# Streamlit 網頁基本設定
# ============================================================
st.set_page_config(
    page_title="NBA Players 資料下載",
    page_icon="🏀",
    layout="wide"
)


# ============================================================
# Excel 輸出設定
# ============================================================
OUTPUT_FOLDER = "info"
OUTPUT_FILE = os.path.join(OUTPUT_FOLDER, "players.xlsx")


# ============================================================
# 連接 MySQL
# 連線資料由 .streamlit/secrets.toml 取得
# ============================================================
def connect_database():
    #從 secrets.toml 取得資料庫連線資訊
    # 建立 MySQL 連線
    #st.secrets 會自動讀取 .streamlit/secrets.toml 的內容
    # 這裡的程式碼會嘗試建立與 MySQL 資料庫的連線
    try:
        connection = mysql.connector.connect(
            host=st.secrets["mysqldb"]["host"],
            user=st.secrets["mysqldb"]["user"],
            password=st.secrets["mysqldb"]["password"],
            port=int(st.secrets["mysqldb"]["port"]),
            database=st.secrets["mysqldb"]["database"]
        )

        return connection

    except mysql.connector.Error as e:
        st.error(f"❌ MySQL 連線失敗：{e}")
        return None

    except Exception as e:
        st.error(f"❌ secrets.toml 設定錯誤：{e}")
        return None


# ============================================================
# 讀取 players 資料表
# ============================================================
def load_players():
    connection = connect_database()

    if connection is None:
        return None

    try:
        sql = """
        SELECT *
        FROM players
        """

        df = pd.read_sql_query(
            sql,
            connection
        )

        return df

    except Exception as e:
        st.error(f"❌ 讀取 players 資料失敗：{e}")
        return None

    finally:
        if connection.is_connected():
            connection.close()


# ============================================================
# 匯出 Excel
# ============================================================
def export_excel(df):
    try:
        # 如果 info 資料夾不存在，自動建立
        os.makedirs(
            OUTPUT_FOLDER,
            exist_ok=True
        )

        # 匯出 Excel
        df.to_excel(
            OUTPUT_FILE,
            index=False,
            engine="openpyxl"
        )

        return True

    except Exception as e:
        st.error(f"❌ Excel 匯出失敗：{e}")
        return False


# ============================================================
# Streamlit 主程式
# ============================================================
def main():
    st.title("🏀 NBA Players 資料下載系統")

    st.write(
        "從 MySQL 的 `nba.players` 資料表讀取資料，"
        "並匯出成 Excel。"
    )

    st.divider()

    # ========================================================
    # 顯示資料庫連線資訊
    # 不顯示密碼
    # ========================================================
    with st.expander("🛢️ 資料庫連線資訊"):
        st.write(f"Host：{st.secrets['mysqldb']['host']}")
        st.write(f"Port：{st.secrets['mysqldb']['port']}")
        st.write(f"Database：{st.secrets['mysqldb']['database']}")
        st.write(f"User：{st.secrets['mysqldb']['user']}")

    # ========================================================
    # 讀取資料
    # ========================================================
    with st.spinner("正在讀取 MySQL players 資料..."):
        df = load_players()

    # ========================================================
    # 判斷資料是否成功取得
    # ========================================================
    if df is None:
        st.stop()

    # ========================================================
    # 顯示資料筆數
    # ========================================================
    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            label="Players 資料筆數",
            value=len(df)
        )

    with col2:
        st.metric(
            label="欄位數量",
            value=len(df.columns)
        )

    st.divider()

    # ========================================================
    # 顯示資料
    # ========================================================
    st.subheader("📊 Players 資料")

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    # ========================================================
    # Excel 匯出
    # ========================================================
    st.subheader("📥 Excel 匯出")

    if st.button(
        "📁 匯出 players.xlsx",
        type="primary",
        use_container_width=True
    ):
        success = export_excel(df)

        if success:
            st.success(
                f"✅ 匯出成功！檔案位置：{OUTPUT_FILE}"
            )

    # ========================================================
    # 如果 Excel 已存在
    # 顯示下載按鈕
    # ========================================================
    if os.path.exists(OUTPUT_FILE):
        with open(OUTPUT_FILE, "rb") as file:
            excel_data = file.read()

        st.download_button(
            label="⬇️ 下載 players.xlsx 到電腦",
            data=excel_data,
            file_name="players.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            use_container_width=True
        )


# ============================================================
# 執行程式
# ============================================================
if __name__ == "__main__":
    main()
