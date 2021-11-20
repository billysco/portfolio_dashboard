from re import S
import yfinance as yf
import pandas as pd

# List of Stocks
# pltr = yf.Ticker("PLTR")
# wfc = yf.Ticker("WFC")
# bac = yf.Ticker("BAC")
# bidu = yf.Ticker("BIDU")
# ai = yf.Ticker("AI")
# ba = yf.Ticker("BA")
# bprm = yf.Ticker("BRPM")
# crsr = yf.Ticker("CRSR")
# curi = yf.Ticker("CURI")
# ddog = yf.Ticker("DDOG")
# fsk = yf.Ticker("FSK")
# maps = yf.Ticker("MAPS")
# o = yf.Ticker("O")
# penn = yf.Ticker("PENN")
# tcehy = yf.Ticker("TCEHY")
# iipr = yf.Ticker("IIPR")
# lmnd = yf.Ticker("LMND")
# mrvl = yf.Ticker("MRVL")
# gmsqf = yf.Ticker("GMSQF")

# stocks = [pltr, wfc, bac, bidu, ai, ba, bprm, crsr, curi, ddog, fsk, maps, o, penn, tcehy, iipr, lmnd, mrvl, gmsqf]

class Stock:
    def __init__(self, ticker):
        self.ticker = ticker
        self.stock_data = yf.Ticker(ticker)
        self.price = self.stock_data.info['currentPrice']
        self.eps = self.stock_data.info['trailingEps']
        self.pe = self.price/self.eps
        self.ps = self.stock_data.info['priceToSalesTrailing12Months']
        self.mkt_cap = self.stock_data.info['marketCap']
        self.revenue = self.stock_data.info['totalRevenue']
        self.revenue_growth = self.stock_data.info['revenueGrowth']
        self.debt = self.stock_data.info['totalDebt']
        self.cash = self.stock_data.info['totalCash']
        self.revenue_per_share = self.stock_data.info['revenuePerShare']



pltr = Stock("PLTR")
wfc = Stock("WFC")
bac = Stock("BAC")
bidu = Stock("BIDU")
ai = Stock("AI")
ba = Stock("BA")
# bprm = Stock("BRPM")
crsr = Stock("CRSR")
curi = Stock("CURI")
ddog = Stock("DDOG")
fsk = Stock("FSK")
maps = Stock("MAPS")
o = Stock("O")
penn = Stock("PENN")
tcehy = Stock("TCEHY")
iipr = Stock("IIPR")
lmnd = Stock("LMND")
mrvl = Stock("MRVL")
gmsqf = Stock("GMSQF")

# print(gmsqf.price)

# list of funds
qqq = yf.Ticker("QQQ")
tqqq =  yf.Ticker("TQQQ")
icln = yf.Ticker("ICLN")
voo = yf.Ticker("VOO")
vti = yf.Ticker("VTI")
xlk = yf.Ticker("XLK")
gxc = yf.Ticker("GXC")
spy = yf.Ticker("SPY")
vnm = yf.Ticker("VNM")
voog = yf.Ticker("VOOG")

# Stocks want to know: Price, PE, PS, MKT Cap, Revenue, % Revenue Growth, important dates(earnings/dividends)
# pltr_price = pltr.info['currentPrice']
# pltr_eps = pltr.info['trailingEps']
# pltr_pe = pltr_price/pltr_eps
# plts_ps = pltr.info['priceToSalesTrailing12Months']
# pltr_mkt_cap = pltr.info['marketCap']
# pltr_revenue = pltr.info['totalRevenue']
# pltr_revenue_growth = pltr.info['revenueGrowth']
# pltr_debt = pltr.info['totalDebt']
# pltr_cash = pltr.info['totalCash']
# pltr_revenue_per_share = pltr.info['revenuePerShare']

# wfc_price = wfc.info['currentPrice']
# wfc_eps = wfc.info['trailingEps']
# wfc_pe = wfc_price/wfc_eps
# wfc_ps = wfc.info['priceToSalesTrailing12Months']
# wfc_mkt_cap = wfc.info['marketCap']
# wfc_revenue = wfc.info['totalRevenue']
# wfc_revenue_growth = wfc.info['revenueGrowth']
# wfc_debt = wfc.info['totalDebt']
# wfc_cash = wfc.info['totalCash']
# wfc_revenue_per_share = wfc.info['revenuePerShare']

# bac_price = bac.info['currentPrice']
# bac_eps = bac.info['trailingEps']
# bac_pe = bac_price/bac_eps
# bac_ps = bac.info['priceToSalesTrailing12Months']
# bac_mkt_cap = bac.info['marketCap']
# bac_revenue = bac.info['totalRevenue']
# bac_revenue_growth = bac.info['revenueGrowth']
# bac_debt = bac.info['totalDebt']
# bac_cash = bac.info['totalCash']
# bac_revenue_per_share = bac.info['revenuePerShare']

# bidu_price = bidu.info['currentPrice']
# bidu_eps = bidu.info['trailingEps']
# bidu_pe = bidu_price/bidu_eps
# bidu_ps = bidu.info['priceToSalesTrailing12Months']
# bidu_mkt_cap = bidu.info['marketCap']
# bidu_revenue = bidu.info['totalRevenue']
# bidu_revenue_growth = bidu.info['revenueGrowth']
# bidu_debt = bidu.info['totalDebt']
# bidu_cash = bidu.info['totalCash']
# bidu_revenue_per_share = bidu.info['revenuePerShare']

# ai_price = ai.info['currentPrice']
# ai_eps = ai.info['trailingEps']
# ai_pe = ai_price/ai_eps
# ai_ps = ai.info['priceToSalesTrailing12Months']
# ai_mkt_cap = ai.info['marketCap']
# ai_revenue = ai.info['totalRevenue']
# ai_revenue_growth = ai.info['revenueGrowth']
# ai_debt = ai.info['totalDebt']
# ai_cash = ai.info['totalCash']
# ai_revenue_per_share = ai.info['revenuePerShare']

# ba_price = ba.info['currentPrice']
# ba_eps = ba.info['trailingEps']
# ba_pe = ba_price/ba_eps
# ba_ps = ba.info['priceToSalesTrailing12Months']
# ba_mkt_cap = ba.info['marketCap']
# ba_revenue = ba.info['totalRevenue']
# ba_revenue_growth = ba.info['revenueGrowth']
# ba_debt = ba.info['totalDebt']
# ba_cash = ba.info['totalCash']
# ba_revenue_per_share = ba.info['revenuePerShare']

# bprm_price = bprm.info['currentPrice']
# bprm_eps = bprm.info['trailingEps']
# bprm_pe = bprm_price/bprm_eps
# bprm_ps = bprm.info['priceToSalesTrailing12Months']
# bprm_mkt_cap = bprm.info['marketCap']
# bprm_revenue = bprm.info['totalRevenue']
# bprm_revenue_growth = bprm.info['revenueGrowth']
# bprm_debt = bprm.info['totalDebt']
# bprm_cash = bprm.info['totalCash']
# bprm_revenue_per_share = bprm.info['revenuePerShare']

# crsr_price = crsr.info['currentPrice']
# crsr_eps = crsr.info['trailingEps']
# crsr_pe = crsr_price/crsr_eps
# crsr_ps = crsr.info['priceToSalesTrailing12Months']
# crsr_mkt_cap = crsr.info['marketCap']
# crsr_revenue = crsr.info['totalRevenue']
# crsr_revenue_growth = crsr.info['revenueGrowth']
# crsr_debt = crsr.info['totalDebt']
# crsr_cash = crsr.info['totalCash']
# crsr_revenue_per_share = crsr.info['revenuePerShare']

# curi_price = curi.info['currentPrice']
# curi_eps = curi.info['trailingEps']
# curi_pe = curi_price/curi_eps
# curi_ps = curi.info['priceToSalesTrailing12Months']
# curi_mkt_cap = curi.info['marketCap']
# curi_revenue = curi.info['totalRevenue']
# curi_revenue_growth = curi.info['revenueGrowth']
# curi_debt = curi.info['totalDebt']
# curi_cash = curi.info['totalCash']
# curi_revenue_per_share = curi.info['revenuePerShare']

# ddog_price = ddog.info['currentPrice']
# ddog_eps = ddog.info['trailingEps']
# ddog_pe = ddog_price/ddog_eps
# ddog_ps = ddog.info['priceToSalesTrailing12Months']
# ddog_mkt_cap = ddog.info['marketCap']
# ddog_revenue = ddog.info['totalRevenue']
# ddog_revenue_growth = ddog.info['revenueGrowth']
# ddog_debt = ddog.info['totalDebt']
# ddog_cash = ddog.info['totalCash']
# ddog_revenue_per_share = ddog.info['revenuePerShare']

# fsk_price = fsk.info['currentPrice']
# fsk_eps = fsk.info['trailingEps']
# fsk_pe = fsk_price/fsk_eps
# fsk_ps = fsk.info['priceToSalesTrailing12Months']
# fsk_mkt_cap = fsk.info['marketCap']
# fsk_revenue = fsk.info['totalRevenue']
# fsk_revenue_growth = fsk.info['revenueGrowth']
# fsk_debt = fsk.info['totalDebt']
# fsk_cash = fsk.info['totalCash']
# fsk_revenue_per_share = fsk.info['revenuePerShare']

# maps_price = maps.info['currentPrice']
# maps_eps = maps.info['trailingEps']
# maps_pe = maps_price/maps_eps
# maps_ps = maps.info['priceToSalesTrailing12Months']
# maps_mkt_cap = maps.info['marketCap']
# maps_revenue = maps.info['totalRevenue']
# maps_revenue_growth = maps.info['revenueGrowth']
# maps_debt = maps.info['totalDebt']
# maps_cash = maps.info['totalCash']
# maps_revenue_per_share = maps.info['revenuePerShare']