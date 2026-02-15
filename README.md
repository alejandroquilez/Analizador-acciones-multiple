# Analizador Multiacción

Programa en Python que, a partir de un input de varias acciones, analiza su retorno mensual y genera una gráfica de barras de resultados. 

## Funcionalidades

- Análisis simultáneo de n acciones.
- Cálculo del retorno mensual.
- Identificación de mejor y peor acción.
- Gráfico de resultados con código de colores.

## Tecnologías

- Python 3.14.0
- Matplotlib, yfinance

## Instalación
```bash
pip install yfinance matplotlib
```

## Uso
```bash
python analizador_multiple.py
```

El programa pedirá 5 tickers (símbolos de acciones). Ejemplo:
- AAPL (Apple)
- MSFT (Microsoft)
- TSLA (Tesla)
- NVDA (Nvidia)
- GOOGL (Google)

## 📊 Ejemplo de salida
```

--- Resultados Mensuales ---
1. AAPL: -1.52 %
2. MSFT: -12.64 %
3. TSLA: -4.95 %
4. NVDA: -0.18 %
5. GOOGL: -8.97 %
La mejor acción ha sido NVDA, con un retorno del -0.18%.
La peor acción ha sido MSFT, con un retorno del -12.64%.

![Gráfico de Comparación](Figure_1.png)

```

