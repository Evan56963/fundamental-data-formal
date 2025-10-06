import pyodbc
from config.database_config import DatabaseConfig

class FundamentalDataRepository:
    """基本面數據儲存庫類"""
    def __init__(self):
        config = DatabaseConfig()
        self.conn_str = config.get_connection_string()

    def _get_table_name(self, market: str):
        return f'fundamental_data_{market}'

    def _ensure_table(self, market: str):
        table = self._get_table_name(market)
        with pyodbc.connect(self.conn_str) as conn:
            cursor = conn.cursor()
            cursor.execute(f"""
                IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='{table}' AND xtype='U')
                CREATE TABLE {table} (
                    symbol NVARCHAR(50) PRIMARY KEY,
                    shortName NVARCHAR(255),
                    sector NVARCHAR(255),
                    industry NVARCHAR(255),
                    marketCap BIGINT,
                    trailingPE FLOAT,
                    forwardPE FLOAT,
                    priceToBook FLOAT,
                    dividendYield FLOAT,
                    beta FLOAT,
                    country NVARCHAR(50),
                    currency NVARCHAR(10),
                    exchange NVARCHAR(50),
                    priceToSales FLOAT,
                    enterpriseToRevenue FLOAT,
                    enterpriseToEbitda FLOAT,
                    pegRatio FLOAT,
                    debtToEquity FLOAT,
                    returnOnEquity FLOAT,
                    returnOnAssets FLOAT,
                    profitMargins FLOAT,
                    operatingMargins FLOAT,
                    grossMargins FLOAT,
                    revenueGrowth FLOAT,
                    earningsGrowth FLOAT,
                    currentRatio FLOAT,
                    quickRatio FLOAT,
                    totalCash BIGINT,
                    totalDebt BIGINT,
                    totalRevenue BIGINT,
                    netIncomeToCommon BIGINT,
                    bookValue FLOAT,
                    sharesOutstanding BIGINT,
                    fiftyTwoWeekHigh FLOAT,
                    fiftyTwoWeekLow FLOAT,
                    averageVolume BIGINT,
                    dividendRate FLOAT,
                    payoutRatio FLOAT,
                    exDividendDate NVARCHAR(20),
                    lastUpdate DATETIME DEFAULT GETDATE()
                )
            """)
            conn.commit()

    def save_fundamental_data(self, market: str, data: dict):
        self._ensure_table(market)
        table = self._get_table_name(market)
        with pyodbc.connect(self.conn_str) as conn:
            cursor = conn.cursor()
            symbol = data['symbol']
            # 檢查是否已存在
            cursor.execute(f"SELECT COUNT(*) FROM {table} WHERE symbol=?", symbol)
            exists = cursor.fetchone()[0] > 0

            if exists:
                # 已存在則不重複匯入
                return
            else:
                # INSERT
                columns = ','.join(data.keys())
                placeholders = ','.join(['?' for _ in data])
                values = list(data.values())
                cursor.execute(
                    f"INSERT INTO {table} ({columns}) VALUES ({placeholders})",
                    *values
                )
            conn.commit()