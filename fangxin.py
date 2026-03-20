# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 00:30:50 2026

@author: jen55
"""

import streamlit as st

# --- Logo 檔案名稱設定 ---
logo_filename = "logo.PNG" 

# 1. 🛑 頁面配置
st.set_page_config(
    page_title="芳心居家長照機構",
    page_icon="👩‍⚕️",
    layout="centered", 
    initial_sidebar_state="collapsed" 
)

# 2. 🎨 企業級 CSS 樣式表 (專業緊湊版)
st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* 極致縮減內容區塊寬度與頂部空隙，確保緊湊精緻 */
[data-testid="stMain"] .block-container {
max-width: 42rem !important; 
margin: 0 auto !important; 
padding-top: 0rem; 
padding-bottom: 2rem;
padding-left: 1rem;
padding-right: 1rem;
}

.stApp { background-color: #FDFBF7; }

/* 莫蘭迪湖水綠漸層 Banner - 縮減邊距 */
.hero-banner {
background: linear-gradient(135deg, #4aa3a3 0%, #2a7a7a 100%);
color: white;
padding: 20px 15px; 
border-radius: 12px;
text-align: center;
margin-top: 0px; 
margin-bottom: 20px; 
box-shadow: 0 6px 15px rgba(42, 122, 122, 0.1);
}
.hero-title { font-size: 2.1rem; font-weight: 900; margin-bottom: 5px; color: white; letter-spacing: 1px;}
.hero-subtitle { font-size: 1rem; font-weight: 300; opacity: 0.9; }

/* 區塊大標題 */
.section-title {
color: #2a7a7a;
font-size: 1.5rem;
font-weight: bold;
border-bottom: 3px solid #2a7a7a;
padding-bottom: 5px;
margin-top: 25px; 
margin-bottom: 15px;
display: inline-block;
}

div[data-testid="stColumn"] {
display: flex;
align-items: flex-start;
}

/* 專業白底卡片設計 */
.service-card {
background: white;
padding: 20px;
border-radius: 10px;
border-top: 6px solid #4aa3a3; 
box-shadow: 0 4px 10px rgba(0,0,0,0.05);
height: 100%; 
width: 100%;
display: flex;
flex-direction: column;
justify-content: flex-start;
margin-top: 0px !important; 
}

/* 卡片內文字樣式調整 */
h3 { font-size: 1.3rem !important; margin-bottom: 10px !important;}
ul { font-size: 0.95rem; line-height: 1.6; padding-left: 1.2rem; }
p { font-size: 0.95rem !important; }

/* 品牌金句標籤 (緊湊且不外露程式碼) */
.slogan-badge {
text-align: center;
margin-top: 5px; 
margin-bottom: 15px; 
padding: 8px 20px;
background-color: white; 
border-radius: 20px; 
box-shadow: 0 2px 5px rgba(0,0,0,0.05);
border: 1px solid #eaeaea;
display: inline-block; 
width: auto;
}
.slogan-text {
font-size: 1.8rem; 
font-weight: bold;
color: #2a7a7a; 
font-family: "微軟正黑體", "Heiti TC", sans-serif;
margin: 0;
letter-spacing: 2px;
}
</style>
""", unsafe_allow_html=True)

# 3. 🚀 網站內容排版

# --- A. 頂部導覽列 (Logo 與 機構名稱) ---
col_logo, col_name = st.columns([1, 4])
with col_logo:
    try:
        st.image(logo_filename, use_container_width=True) 
    except:
        st.warning(f"請放入 {logo_filename}")

with col_name:
    # 💡 關鍵修改：將標題顏色改為您截圖中的「深酒紅 (#7A1723)」
    st.markdown("""
        <h1 style='
            color: #7A1723; /* 👈 完美對應您上傳的深酒紅字體顏色 */
            margin-top: 15px; 
            margin-bottom: 0; 
            font-size: 2.6rem; 
            font-weight: 900; 
            font-family: "微軟正黑體", "Heiti TC", sans-serif; 
            letter-spacing: 1px;
        '>芳心居家長照機構</h1>
    """, unsafe_allow_html=True)

# --- B. 重新設計：品牌金句標籤 (置中、縮短距離、防外露) ---
st.markdown("""
<div style="text-align: center; width: 100%;">
<div class="slogan-badge">
<p class="slogan-text">交給芳心，家屬放心</p>
</div>
</div>
""", unsafe_allow_html=True)

# --- C. Hero Banner (視覺焦點橫幅) ---
st.markdown("""
<div class="hero-banner">
<div class="hero-title">專業護理入宅，有溫度的照顧</div>
<div class="hero-subtitle">讓長輩在家享有尊嚴與舒適的生活品質。</div>
</div>
""", unsafe_allow_html=True)

# --- D. 📍 我們的服務項目區塊 ---
st.markdown("<div class='section-title'>🧹 我們的專業服務</div>", unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("""
<div class="service-card">
<h3 style="color: #2a7a7a; margin-top: 0;">🏠 居家照顧服務</h3>
<p style="color: #666; font-size: 0.9rem;">由受過專業訓練的居家服務員到宅協助。</p>
<ul>
<li><strong>身體照顧：</strong>更換衣物、如廁處理、尿袋清潔。</li>
<li><strong>生活照顧：</strong>簡易清潔、整理床鋪、備餐、代購。</li>
<li><strong>陪同外出：</strong>陪同就醫、協助散步運動。</li>
</ul>
</div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
<div class="service-card" style="border-top-color: #f59e0b;">
<h3 style="color: #d97706; margin-top: 0;">🧹 居家喘息服務</h3>
<p style="color: #666; font-size: 0.9rem;">成為家庭照顧者最強的後盾，讓您獲得休息。</p>
<ul>
<li>暫時接手照護工作，減輕家屬壓力。</li>
<li><strong>服務內容：</strong>身體照顧、陪伴聊天、安全看視。</li>
<li>可依家屬需求，彈性選擇在家中提供。</li>
</ul>
</div>
    """, unsafe_allow_html=True)

# --- E. 🗺️ 服務地區與對象區塊 ---
st.markdown("<div class='section-title'>🗺️ 服務地區與對象</div>", unsafe_allow_html=True)

col3, col4 = st.columns(2, gap="large")

with col3:
    st.markdown("""
<div class="service-card" style="border-top-color: #f59e0b; text-align: left;">
<h3 style="color: #d97706; margin-top: 0;">🚚 服務地區</h3>
<p style="color: #333; font-size: 1rem; line-height: 1.7;">
深耕大台南，為以下地區鄉親服務：<br>
<strong>佳里區、麻豆區、學甲區</strong>
</p>
<p style="color: #666; font-size: 0.85rem; margin-top: 15px;">
💡 詳細範圍歡迎直接來電洽詢。
</p>
</div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
<div class="service-card" style="border-top-color: #2e8b57; text-align: left;">
<h3 style="color: #2e8b57; margin-top: 0;">👵 補助資格 (長照 3.0)</h3>
<ul style="padding-left: 1rem; flex-grow: 1;">
<li><strong>65歲以上</strong> 失能長者</li>
<li><strong>50歲以上</strong> 失智症者</li>
<li>領有<strong>身心障礙證明</strong>之失能者</li>
<li><strong>PAC 個案</strong> (中風/癌症復能需求)</li>
</ul>
<div style="background-color: #f0fff0; padding: 8px; border-radius: 5px; color: #006400; font-size: 0.85rem; text-align: center; margin-top: 10px;">
<strong>低收入戶 政府補助 100%</strong>
</div>
</div>
    """, unsafe_allow_html=True)

# --- F. 📞 聯絡我們 ---
st.markdown("<div class='section-title' style='border-bottom: none;'></div>", unsafe_allow_html=True)

st.markdown("""
<div style="background-color: white; padding: 25px; border-radius: 15px; border: 2px solid #eaeaea; box-shadow: 0 8px 25px rgba(0,0,0,0.05); text-align: center;">
<h2 style="color: #333; margin-top: 0;">需要協助？請立即與我們聯繫</h2>
<p style="color: #666; font-size: 1rem;">護理師將為您提供最專業的諮詢</p>
<div style="font-size: 2.2rem; color: #2a7a7a; font-weight: 900; margin: 12px 0;">
<a href="tel:0965833585" style="text-decoration: none; color: #2a7a7a;">📞 0965-833-585</a>
<span style="font-size: 1.2rem; color: #666; font-weight: normal;"> (葉主任)</span>
</div>
<hr style="border-top: 1px dashed #ddd; margin: 18px 0;">
<div style="font-size: 1.1rem; color: #444; margin: 6px 0;"><strong>☎ 機構辦公室：</strong> (06) 723-3756</div>
<div style="font-size: 1.1rem; color: #444; margin: 6px 0;"><strong>🏠 機構地址：</strong> 台南市佳里區中興街22號1F</div>
</div>
""", unsafe_allow_html=True)

# --- G. 頁尾 ---
st.markdown("<div style='text-align: center; color: #bbb; margin-top: 30px; font-size: 0.85rem;'>© 2026 芳心居家長照機構 All Rights Reserved.</div>", unsafe_allow_html=True)