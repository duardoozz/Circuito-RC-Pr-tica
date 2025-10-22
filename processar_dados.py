import matplotlib.pyplot as plt
import pandas as pd

# Lê o arquivo (sem cabeçalho)
dados = pd.read_csv("dados_carga.txt", sep=" ", header=None)
dados.columns = ["Tempo", "Resistor", "Capacitor"]

# 1. Descarga no Resistor
plt.figure()
plt.plot(dados["Tempo"], dados["Resistor"])
plt.title("Descarga no Resistor (R)")
plt.xlabel("Tempo (ms)")
plt.ylabel("Tensão (V)")
plt.grid(True)
plt.savefig("descarga_resistor.png", dpi=300)

# 2. Carga no Capacitor
plt.figure()
plt.plot(dados["Tempo"], dados["Capacitor"], color="orange")
plt.title("Carga no Capacitor (C)")
plt.xlabel("Tempo (ms)")
plt.ylabel("Tensão (V)")
plt.grid(True)
plt.savefig("carga_capacitor.png", dpi=300)

# 3. Comparação R x C
plt.figure()
plt.plot(dados["Tempo"], dados["Resistor"], label="Resistor (R)")
plt.plot(dados["Tempo"], dados["Capacitor"], label="Capacitor (C)")
plt.title("Comparação: Carga no C e Descarga no R")
plt.xlabel("Tempo (ms)")
plt.ylabel("Tensão (V)")
plt.legend()
plt.grid(True)
plt.savefig("comparacao_RC.png", dpi=300)