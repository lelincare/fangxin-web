# 芳心居家長照機構官網 — 部署與維護說明

## 網站結構

```
芳心網站/
├── index.html          首頁
├── about.html            關於我們
├── services.html         服務項目
├── eligibility.html      申請資格與補助說明
├── resources.html        教育資源
├── contact.html          聯絡我們
├── css/style.css         共用樣式
├── js/main.js            共用互動邏輯(導覽選單、捲動動畫、背景音樂、內容讀取)
├── content/*.json        各頁面內容資料(文字/連結,修改時直接編輯這些檔案)
├── images/
│   ├── logo.png            機構 Logo
│   ├── gallery/            團隊/服務照片
│   └── uploads/            預留資料夾(未使用)
├── audio/                 背景音樂放這裡(見 audio/README.md)
└── netlify.toml           Netlify 部署設定
```

**架構說明**：純靜態網站，沒有後台管理系統(不使用 CMS)。原因是只有 Tsai 會編輯內容，不需要額外的登入後台，內容異動時直接請 Claude 修改 `content/*.json` 或 HTML/CSS 檔案，改完重新部署即可，比維護一套後台系統更省事、更少故障點。

---

## 一、上傳到 GitHub

```bash
cd 芳心網站
git init
git add .
git commit -m "芳心居家長照機構官網 初版"
git branch -M main
git remote add origin https://github.com/你的帳號/fangxin-website.git
git push -u origin main
```

（如果還沒建立 repo，先到 GitHub 建一個空的 repository，再執行上面指令。）

---

## 二、連接 Netlify 部署

1. 登入 https://app.netlify.com
2. 點選 **Add new site → Import an existing project**
3. 選擇剛剛建立的 GitHub repo
4. Build 設定保持預設（`netlify.toml` 已經寫好 publish 目錄是根目錄、不需要 build 指令），直接點 **Deploy**
5. 部署完成後會拿到一個免費網址，例如 `fangxin-care.netlify.app`

之後也可以比照協會官網的做法，改用 **Netlify ZIP API 方式部署**（`POST /api/v1/sites` 建站 + `POST /api/v1/sites/{id}/deploys` 上傳 zip，Token 讀取 `.env` 的 `NETLIFY_TOKEN`），寫一支 `fangxin_website_deploy.py`（可參考 `gov_docs_deploy.py` / `tlcpea_website_deploy.py` 的寫法），這樣之後每次改完內容就能直接跑腳本部署，不需要每次手動 git push。

---

## 三、之後要改內容怎麼辦

**不需要碰任何後台系統**，直接跟 Claude 說要改什麼（例如「補助比例改一下」「服務項目文字調整」「地址改了」），Claude 會直接修改對應的 `content/*.json` 或 HTML 檔案，改完你重新部署（git push 或跑 zip 部署腳本）即可生效。

---

## 四、補上背景音樂

見 `audio/README.md`，去 Pixabay Music 之類的免費素材網站下載一首輕音樂，命名為 `bgm.mp3`，放進 `audio/` 資料夾，重新部署即可生效。

---

## 五、AI 生成寫實照片，替換佔位圖

`images/gallery/` 底下目前是 6 張標示「待替換照片」的佔位圖。用 `gemini_client.py` 批次生成寫實風照片，主題聚焦：

- **居服員到宅照顧情境**：協助盥洗、陪伴聊天、居家清潔、陪同散步等
- **團隊形象**：護理師團隊、居服員群像

生成後直接覆蓋 `images/gallery/placeholder-01.jpg` 等檔案（檔名不變最省事），重新部署即可。

> 若考慮用真實個案或員工照片，請留意個資法特種個資與肖像權相關的同意事項（先前已討論過）。

---

## 六、補上教育影片

`content/resources.json` 裡目前是佔位的 `REPLACE_WITH_YOUTUBE_ID`。把 YouTube 影片網址中 `v=` 後面那串字（例如 `youtube.com/watch?v=ABC123xyz` 中的 `ABC123xyz`）貼給 Claude，Claude 直接改檔案。

---

## 七、聯絡表單通知設定

表單已經用 Netlify Forms 處理，不需要任何後端程式碼。要設定收到通知的信箱：

1. Netlify 後台 → **Site configuration → Forms → Form notifications**
2. 新增 **Email notification**，填入要接收諮詢通知的信箱（例如葉主任信箱）
3. 之後訪客送出表單，會直接寄信通知，同時也能在 Netlify 後台 **Forms** 分頁看到所有提交紀錄

免費方案每月 100 次提交額度，機構規模完全夠用。

---

## 八、之後想換成自訂網域

Netlify 後台 → **Domain management → Add a domain**，依指示設定 DNS 即可。

---

## 疑難排解

- **改了內容但網站沒更新**：檢查 Netlify 後台的 **Deploys** 分頁，看是否有部署失敗的紀錄，或確認是否忘記 git push / 重新跑部署腳本
- **表單收不到信**：確認 Form notifications 有設定信箱，也檢查垃圾郵件匣
