import numpy
import matplotlib
import openpyxl

chf_path = 'C:\\Users\\jernej.smole\\Desktop\\work\\recomendationAuswertung\\daten\\CHF_Site Analytics Repor.xlsx'
czk_path = 'C:\\Users\\jernej.smole\\Desktop\\work\\recomendationAuswertung\\daten\\CZK_Site Analytics Repor.xlsx'
dkk_path = 'C:\\Users\\jernej.smole\\Desktop\\work\\recomendationAuswertung\\daten\\DKK_Site Analytics Repor.xlsx'
eur_path = 'C:\\Users\\jernej.smole\\Desktop\\work\\recomendationAuswertung\\daten\\EUR_Site Analytics Repor.xlsx'
gbp_path = 'C:\\Users\\jernej.smole\\Desktop\\work\\recomendationAuswertung\\daten\\GBP_Site Analytics Repor.xlsx'
nok_path = 'C:\\Users\\jernej.smole\\Desktop\\work\\recomendationAuswertung\\daten\\NOK_Site Analytics Repor.xlsx'
pln_path = 'C:\\Users\\jernej.smole\\Desktop\\work\\recomendationAuswertung\\daten\\PLN_Site Analytics Repor.xlsx'
sek_path = 'C:\\Users\\jernej.smole\\Desktop\\work\\recomendationAuswertung\\daten\\SEK_Site Analytics Repor.xlsx'


print(chf_path)

chf = openpyxl.load_workbook(
    'C:/Users/jernej.smole/Desktop/work/recomendationAuswertung/daten/CHF_Site Analytics Repor.xlsx')

print(chf)
