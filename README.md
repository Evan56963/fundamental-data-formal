# Fundamental-formal

本專案是一個用於查詢並儲存股票、加密貨幣等資產的基本面資料的工具，支援台股、美股、台灣興櫃、加密貨幣、外匯等市場，還有美國NFP、CPI。資料來源主要為 Yahoo Finance、FredAPI，並儲存至 SQL Server 資料庫。

## 主要功能

- 透過命令列查詢多種市場的資產基本面資料
- 自動格式化並顯示各項財務指標
- 資料自動儲存至 SQL Server，避免重複匯入

## 專案架構

- `main.py`：命令列工具入口，負責參數解析與資料顯示
- `services/`：服務層，負責資料流轉與邏輯處理
- `providers/`：資料提供層，負責從 Yahoo Finance 取得基本面資料
- `repositories/`：資料儲存層，負責與 SQL Server 資料庫互動
- `config/`：資料庫連線設定
- `.env.local`：資料庫連線環境變數

## 安裝需求

請先安裝 Python 3.8+，並安裝必要套件：

```
pip install -r requirements.txt
```

## 使用方式

查詢台股：
```
python main.py 2330 --tw
```

查詢美股：
```
python main.py AAPL --us
```

查詢加密貨幣：
```
python main.py BTC --crypto
```

查詢美國 CPI：
```
python main.py --cpi
```

查詢美國 NFP：
```
python main.py --nfp
```

顯示支援市場類型：
```
python main.py --help
```

## 資料庫設定

請於 `.env.local` 設定 SQL Server 連線資訊。

環境變數範例
```
DB_SERVER=localhost
DB_NAME=database
DB_USER=username
DB_PASSWORD=password
DB_DRIVER=ODBC Driver 17 for SQL Server
FRED_API_KEY=API KEY
```
## 注意事項

- 資料來源為 Yahoo Finance、FredAPI，部分指標可能因市場不同而缺漏。
- 僅支援 SQL Server 資料庫。

---
