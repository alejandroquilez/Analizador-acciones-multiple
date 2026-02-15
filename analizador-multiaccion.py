import yfinance as yf
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

# Función para descargar datos .de una acción
def descargar_datos(ticker):
    print(f"Descargando datos de {ticker}...")
    datos = yf.Ticker(ticker).history(period="1mo")
    return datos

def calcular_retorno(ticker):

    precio_inicial = float(datos['Close'].iloc[0])
    precio_final = float(datos['Close'].iloc[-1])
    
    retorno = ((precio_final - precio_inicial)/ precio_inicial) * 100
    
    return retorno, precio_inicial, precio_final


print ("===Analizador Multiacción===\n")

retornos = []
tickers = []


for i in range(1,6):
    ticker = input("Introduce el ticker (ej: AAPL, TSLA):").upper()
    datos = descargar_datos(ticker)


    if datos.empty:
        print("No se encontraron datos")
    else: 
        retorno, precio_inicial, precio_final = calcular_retorno(datos)
        
        
    tickers.append(ticker)
    retornos.append(retorno)
    
print("--- Resultados Mensuales ---")
for i, ticker in enumerate(tickers):
    print(f"{i+1}. {ticker}: {retornos[i]:.2f} %")
    
    

a = max(retornos)
Maxi = retornos.index(a)

b = min(retornos)
Mini = retornos.index(b)

print(f"La mejor acción ha sido {tickers[Maxi]}, con un retorno del {a:.2f}%.")
print(f"La peor acción ha sido {tickers[Mini]}, con un retorno del {b:.2f}%.")


colores = ['g' if r >= 0 else 'r' for r in retornos]
plt.bar(tickers, retornos, color = colores)
plt.title("Retorno mensual de las acciones analizadas")
plt.xlabel("Acciones")
plt.ylabel("Retorno (%)")
plt.axline((0, 0), (1, 0), linewidth = 1, color = 'k')
plt.grid(visible = True)
plt.gca().set_axisbelow(True)
plt.show()