import yfinance as yf
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

# Función para descargar datos .de una acción
def descargar_datos(ticker):
    print(f"Descargando datos de {ticker}...")
    datos = yf.Ticker(ticker).history(period="1mo")
    return datos

def calcular_retorno(datos):

    precio_inicial = float(datos['Close'].iloc[0])
    precio_final = float(datos['Close'].iloc[-1])
    
    retorno = ((precio_final - precio_inicial)/ precio_inicial) * 100
    
    return retorno, precio_inicial, precio_final

def calcular_volatilidad(datos):
    # Calcula el cambio porcentual diario
    cambios = datos['Close'].pct_change() * 100
    # Volatilidad = desviación estándar de los cambios
    volatilidad = cambios.std()
    return volatilidad

def calcular_sharpe(datos):
    # Calcula el sharpe ratio
    retorno_sharpe, _, _ = calcular_retorno(datos)
    vol = calcular_volatilidad(datos) 
    sharpe = retorno_sharpe/vol 
    
    return sharpe
      
def graficar_doble(tickers, retornos, sharpes):
    fig, (plt1, plt2) = plt.subplots(1, 2, figsize = (12, 5))
    
    colores_ret = ['g' if r >= 0 else 'r' for r in retornos]
    colores_sharpe = ['g' if s >= 1 else 'y' if 1 > s > 0.5 else 'r' for s in sharpes]
    
    plt1.bar(tickers, retornos, color = colores_ret, label = 'Retornos')
    plt1.axhline(y = 0, linewidth = 1, color = 'k')
    plt1.set_title("Retorno de los tickers analizados")
    plt1.grid(visible = True)
    plt1.set_xlabel("Acciones")
    plt1.set_ylabel("Retorno (%)")
    
    
    plt2.bar(tickers, sharpes, color = colores_sharpe, label = 'Sharpes')
    plt2.set_title("Sharpe Ratios de los tickers analizados")
    plt2.grid(visible = True)
    plt2.axhline(y = 1, linewidth = 1, color = 'k')
    plt2.set_xlabel("Acciones")
    plt2.set_ylabel("Sharpe Ratios")
    
    plt.savefig('Comparación_completa.png')
    plt.show()


print ("===Analizador Multiacción===\n")

retornos = []
tickers = []
sharpes = []

# Cálculos necesarios para el análisis 

for i in range(1,6):
    ticker = input("Introduce el ticker (ej: AAPL, TSLA):").upper()
    datos = descargar_datos(ticker)


    if datos.empty:
        print("No se encontraron datos")
    else: 
        retorno, precio_inicial, precio_final = calcular_retorno(datos)
        sharpe = calcular_sharpe(datos)
        tickers.append(ticker)
        retornos.append(retorno)
        sharpes.append(sharpe)
        

# Resultados:

print("--- Resultados Mensuales ---")
for i, ticker in enumerate(tickers):
    print(f"{i+1}. {ticker}: {retornos[i]:+.2f} % | Sharpe Ratio: {sharpes[i]:.2f}")
    
    

mejor_retorno = max(retornos)
Maxi = retornos.index(mejor_retorno)

peor_retorno = min(retornos)
Mini = retornos.index(peor_retorno)

print(f"La mejor acción ha sido {tickers[Maxi]}, con un retorno del {mejor_retorno:+.2f}%.")
print(f"La peor acción ha sido {tickers[Mini]}, con un retorno del {peor_retorno:+.2f}%.")

# Visualización de resultados 


sharpe_max = max(sharpes)
sharpe_max_ind = sharpes.index(sharpe_max)
print(f"Mejor Sharpe ratio: {tickers[sharpe_max_ind]} ({sharpe_max:.2f}) <== Mejor relación riesgo/retorno")

graficar_doble(tickers, retornos, sharpes)