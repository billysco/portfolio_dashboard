import yfinance as yf
import pandas as pd

# List of Stocks
pltr = yf.Ticker("PLTR")
wfc = yf.Ticker("WFC")
bac = yf.Ticker("BAC")
bidu = yf.Ticker("BIDU")
ai = yf.Ticker("AI")
ba = yf.Ticker("BA")
bprm = yf.Ticker("BRPM")
crsr = yf.Ticker("CRSR")
curi = yf.Ticker("CURI")
ddog = yf.Ticker("DDOG")
fsk = yf.Ticker("FSK")
maps = yf.Ticker("MAPS")
o = yf.Ticker("O")
penn = yf.Ticker("PENN")
tcehy = yf.Ticker("TCEHY")
iipr = yf.Ticker("IIPR")
lmnd = yf.Ticker("LMND")
mrvl = yf.Ticker("MRVL")
gmsqf = yf.Ticker("GMSQF")

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
pltr_price = pltr.info['currentPrice']
pltr_eps = pltr.info['trailingEps']
pltr_pe = pltr_price/pltr_eps
