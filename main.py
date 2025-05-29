import tkinter as tk
from tkinter import ttk, messagebox

# ------------------------
# Datos por estación y fecha
# ------------------------

resumen_e1 = {
    "2025-05-17": {"PM10": 77.6, "PM2.5": 32.5, "SO2": 10.9, "NO2": 28.5, "O3": 12.2, "CO": 1783},
    "2025-05-18": {"PM10": 79.2, "PM2.5": 37.1, "SO2": 11.3, "NO2": 30.5, "O3": 14.4, "CO": 1470},
    "2025-05-19": {"PM10": 89.8, "PM2.5": 41.9, "SO2": 12, "NO2": 34.4, "O3": 12.9, "CO": 1690},
    "2025-05-20": {"PM10": 58.4, "PM2.5": 26.2, "SO2": 10.3, "NO2": 34.4, "O3": 14.5, "CO": 1508},
    "2025-05-21": {"PM10": 113.2, "PM2.5": 46.5, "SO2": 9.1, "NO2": 36.9, "O3": 21.2, "CO": 1447},
    "2025-05-22": {"PM10": 92.7, "PM2.5": 41.5, "SO2": 13.3, "NO2": 36.1, "O3": 21.5, "CO": 1087},
    "2025-05-23": {"PM10": 97.8, "PM2.5": 38.5, "SO2": 15.2, "NO2": 35.2, "O3": 20.5, "CO": 1889},
}

resumen_e2 = {
    "2025-05-17": {"PM2.5": 23.8, "PM10": 41.4, "SO2": 5.6, "NO2": 24.75, "O3": 16.7, "CO": 1459.2},
    "2025-05-18": {"PM2.5": 25.1, "PM10": 40.5, "SO2": 3.4, "NO2": 23.74, "O3": 18.25, "CO": 1605.3},
    "2025-05-19": {"PM2.5": 27.6, "PM10": 44.4, "SO2": 2.1, "NO2": 25.22, "O3": 17.56, "CO": 1609.8},
    "2025-05-20": {"PM2.5": 18.5, "PM10": 29.6, "SO2": 3.2, "NO2": 28.2, "O3": 10.56, "CO": 1538.4},
    "2025-05-21": {"PM2.5": 26.6, "PM10": 42.7, "SO2": 8.9, "NO2": 27.18, "O3": 11.73, "CO": 1487.9},
    "2025-05-22": {"PM2.5": 23.9, "PM10": 33.6, "SO2": 3.8, "NO2": 29.61, "O3": 12.7, "CO": 1645.9},
    "2025-05-23": {"PM2.5": 19.86, "PM10": 20.8, "SO2": 3.3, "NO2": 23.34, "O3": 15.09, "CO": 1558.4},
}

# ------------------------
# Propuestas por fecha
# ------------------------

propuestas = {
    "2025-05-17": "Propuesta 1: Reducción de material particulado\nMedidas: Riego de caminos sin pavimentar, instalación de barreras vegetales, cobertura de materiales en transporte, restricción de vehículos pesados en zonas residenciales.\nObjetivo: Disminuir partículas PM10 y PM2.5.\nTecnología: Baja, aplicable localmente con recursos municipales.",
    "2025-05-18": "Propuesta 2: Control de emisiones gaseosas (SO₂, NO₂)\nMedidas: Sustitución de combustibles, mantenimiento de sistemas de combustión, instalación de filtros en chimeneas, uso de convertidores catalíticos en vehículos, control técnico vehicular.\nObjetivo: Reducir gases contaminantes de fuentes fijas y móviles.\nTecnología: Media-alta, requiere inversión técnica.",
    "2025-05-19": "Propuesta 3: Reducción de emisiones de monóxido de carbono (CO)\nMedidas: Evitar ralentí prolongado, mejorar ventilación en espacios cerrados, revisiones del sistema de escape, promoción de combustibles limpios.\nObjetivo: Minimizar exposición al CO en zonas urbanas y cerradas.\nTecnología: Media, requiere cambios operativos y conductuales.",
    "2025-05-20": "Propuesta 4: Promoción de movilidad eléctrica y transporte sostenible\nMedidas: Fomentar el uso de vehículos eléctricos, bicicletas y sistemas de transporte público eléctrico; instalar infraestructura de carga.\nObjetivo: Disminuir emisiones de NOx, CO₂ y material particulado provenientes del transporte.\nTecnología: Alta; requiere inversión en infraestructura y normativas de incentivos.",
    "2025-05-21": "Propuesta 5: Gestión integral de residuos sólidos\nMedidas: Evitar la quema de residuos, implementar sistemas de separación y reciclaje, captura de biogás en rellenos sanitarios.\nObjetivo: Reducir emisiones de CO, metano (CH₄) y compuestos orgánicos volátiles (COVs).\nTecnología: Media; requiere infraestructura de gestión de residuos y normativas locales.",
    "2025-05-22": "Propuesta 6: Reforestación urbana y creación de corredores verdes\nMedidas: Plantación de árboles nativos, recuperación de espacios públicos verdes, establecimiento de techos y muros verdes.\nObjetivo: Captura de contaminantes atmosféricos (PM, CO₂), mejora de microclimas urbanos.\nTecnología: Baja; fácilmente implementable con participación comunitaria y planificación local.",
    "2025-05-23": "Propuesta 7: Monitoreo ambiental continuo y sistemas de alerta\nMedidas: Instalación de estaciones de monitoreo de calidad del aire, implementación de sistemas de alerta temprana ante niveles críticos de contaminación.\nObjetivo: Generar datos en tiempo real para toma de decisiones y protección de la salud pública.\nTecnología: Alta; requiere sensores, conectividad y análisis de datos."
}

# ------------------------
# Fechas disponibles
# ------------------------

fechas_disponibles = list(propuestas.keys())

# ------------------------
# Función para mostrar la información
# ------------------------

def mostrar_info():
    distrito = combo_distrito.get()
    fecha = combo_fecha.get()

    if distrito != "Chorrillos":
        messagebox.showwarning("ATENCIÓN", "Solo hay datos para Chorrillos.")
        return
    if fecha == "":
        messagebox.showwarning("ATENCIÓN", "Selecciona una fecha.")
        return

    # Estación E1
    texto1 = f"📅 Fecha: {fecha}\n📍 Estación: Escuela de Militares (E1)\n"
    for cont, val in resumen_e1.get(fecha, {}).items():
        texto1 += f"  - {cont.strip()}: {val}\n"

    # Estación E2
    texto2 = f"📅 Fecha: {fecha}\n📍 Estación: Pantanos de Villa (E2)\n"
    for cont, val in resumen_e2.get(fecha, {}).items():
        texto2 += f"  - {cont.strip()}: {val}\n"

    # Propuesta
    propuesta_texto = f"📌 {propuestas.get(fecha, 'Sin propuesta asignada')}"

    # Mostrar todo en los cuadros
    cuadro_texto_e1.config(state='normal')
    cuadro_texto_e1.delete("1.0", tk.END)
    cuadro_texto_e1.insert(tk.END, texto1)
    cuadro_texto_e1.config(state='disabled')

    cuadro_texto_e2.config(state='normal')
    cuadro_texto_e2.delete("1.0", tk.END)
    cuadro_texto_e2.insert(tk.END, texto2)
    cuadro_texto_e2.config(state='disabled')

    cuadro_texto_propuesta.config(state='normal')
    cuadro_texto_propuesta.delete("1.0", tk.END)
    cuadro_texto_propuesta.insert(tk.END, propuesta_texto)
    cuadro_texto_propuesta.config(state='disabled')

# ------------------------
# Interfaz gráfica
# ------------------------

ventana = tk.Tk()
ventana.title("Calidad del Aire - Chorrillos")
ventana.geometry("900x850")

# ComboBox de distrito
tk.Label(ventana, text="Selecciona tu distrito:").pack(pady=5)
combo_distrito = ttk.Combobox(ventana, values=["Chorrillos"], state="readonly")
combo_distrito.pack()

# ComboBox de fecha
tk.Label(ventana, text="Selecciona la fecha:").pack(pady=5)
combo_fecha = ttk.Combobox(ventana, values=fechas_disponibles, state="readonly")
combo_fecha.pack()

# Botón
tk.Button(ventana, text="Determinar", command=mostrar_info).pack(pady=15)

# Cuadro E1
tk.Label(ventana, text="Información - Escuela de Militares (E1)").pack()
cuadro_texto_e1 = tk.Text(ventana, height=10, width=110, wrap="word", state='disabled')
cuadro_texto_e1.pack(pady=5)

# Cuadro E2
tk.Label(ventana, text="Información - Pantanos de Villa (E2)").pack()
cuadro_texto_e2 = tk.Text(ventana, height=10, width=110, wrap="word", state='disabled')
cuadro_texto_e2.pack(pady=5)

# Cuadro de propuesta
tk.Label(ventana, text="📘 Propuesta Ambientales").pack()
cuadro_texto_propuesta = tk.Text(ventana, height=10, width=110, wrap="word", state='disabled')
cuadro_texto_propuesta.pack(pady=10)

ventana.mainloop()