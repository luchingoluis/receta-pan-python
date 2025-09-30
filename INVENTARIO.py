import json

# Diccionario de materiales con cantidades y costos
materiales = {
    "HARINA":    {"cantidad": 50, "costo_quintal": 36.5, "costo_kilo": 0.73, "costo_unidad": None, "costo_litro": None, "precio_gramo": None},
    "AZUCAR":    {"cantidad": 50, "costo_quintal": 37,   "costo_kilo": 0.74,   "costo_unidad": None, "costo_litro": None, "precio_gramo": None},
    "SAL":       {"cantidad": None, "costo_quintal": None, "costo_kilo": 0.37, "costo_unidad": None, "costo_litro": None, "precio_gramo": None},
    "GRASA":     {"cantidad": 50, "costo_quintal": 93,   "costo_kilo": 1.86, "costo_unidad": None, "costo_litro": None, "precio_gramo": None},
    "HUEVOS":    {"cantidad": 30, "costo_quintal": None, "costo_kilo": None, "costo_unidad": 0.10, "costo_litro": None, "precio_gramo": None, "gramos_por_huevo": 50},
    "LECHE":     {"cantidad": None, "costo_quintal": None, "costo_kilo": 0.67, "costo_unidad": None, "costo_litro": 0.67, "precio_gramo": None},
    "LEVADURA":  {"cantidad": None, "costo_quintal": None, "costo_kilo": 3.4, "costo_unidad": None, "costo_litro": None, "precio_gramo": None},
    "ESCENCIA":  {"cantidad": None, "costo_quintal": None, "costo_kilo": 9.14, "costo_unidad": None, "costo_litro": 9.14, "precio_gramo": None},
    "AGUA":      {"cantidad": None, "costo_quintal": None, "costo_kilo": None, "costo_unidad": None, "costo_litro": None, "precio_gramo": None},
    "POLVO HOR": {"cantidad": None, "costo_quintal": None, "costo_kilo": None, "costo_unidad": None, "costo_litro": None, "precio_gramo": None},
    "ACEITE":    {"cantidad": None, "costo_quintal": None, "costo_kilo": None, "costo_unidad": None, "costo_litro": round(1/0.38,2), "precio_gramo": None},
    "BICARBONATO": {"cantidad": None, "costo_quintal": None, "costo_kilo": 15.0, "costo_unidad": None, "costo_litro": None, "precio_gramo": None}
}

# Diccionario de recetas con porcentajes/ingredientes
recetas = {
    "Enrollado":    {"HARINA": 100, "SAL": 2, "AZUCAR": 10, "GRASA": 15, "HUEVOS": 10, "LEVADURA": 2, "AGUA": 57, "LECHE": "", "ESCENCIA": 0.01, "PESO": 90},
    "Cachos":       {"HARINA": 100, "SAL": 2, "AZUCAR": 10, "GRASA": 15, "HUEVOS": 10, "LEVADURA": 2, "AGUA": 57, "LECHE": "", "ESCENCIA": 0.01, "PESO": 90},
    "Cachos queso": {"HARINA": 100, "SAL": 2, "AZUCAR": 10, "GRASA": 15, "HUEVOS": 10, "LEVADURA": 2, "AGUA": 57, "LECHE": "", "ESCENCIA": 0.01, "PESO": 90},
    "Reventado":    {"HARINA": 100, "SAL": 2, "AZUCAR": 10, "GRASA": 15, "HUEVOS": 10, "LEVADURA": 2, "AGUA": 57, "LECHE": "", "ESCENCIA": 0.01, "PESO": 90},
    "Pan variado":  {"HARINA": 100, "SAL": 2, "AZUCAR": 10, "GRASA": 30, "HUEVOS": 10, "LEVADURA": 2, "AGUA": 47, "LECHE": "", "ESCENCIA": 0.01, "PESO": 90},
    "Pan integra":  {"HARINA": 100, "SAL": 2, "AZUCAR": 10, "GRASA": 30, "HUEVOS": 10, "LEVADURA": 2, "AGUA": 47, "LECHE": "", "ESCENCIA": 0.01, "PESO": 90},
    "Pan de dulce": {"HARINA": 100, "SAL": 0, "AZUCAR": 30, "GRASA": 30, "HUEVOS": 10, "LEVADURA": 2, "AGUA": 47, "LECHE": "", "ESCENCIA": 0.01, "PESO": 90},
    "Pan de agua":  {"HARINA": 100, "SAL": 2, "AZUCAR": 2, "GRASA": 2, "HUEVOS": 0, "LEVADURA": 2, "AGUA": 70, "LECHE": "", "ESCENCIA": 0.01, "PESO": 90},
    "Pan de casa":  {"HARINA": 100, "SAL": 2, "AZUCAR": 10, "GRASA": 35, "HUEVOS": 20, "LEVADURA": 2, "AGUA": "", "LECHE": 40, "ESCENCIA": 0.01, "PESO": 90},
    "Pan de yema":  {"HARINA": 100, "SAL": 2, "AZUCAR": 12, "GRASA": 35, "HUEVOS": 40, "LEVADURA": 2, "AGUA": "", "LECHE": 40, "ESCENCIA": 0.01, "PESO": 90},
    "Plancha de chocolate (65x45)": {
        "_tipo": "absoluto",
        "BASE_AREA_CM2": 65*45,
        "INGREDIENTES": {
            "HARINA": 1000,
            "AZUCAR": 850,
            "ACEITE": 500,
            "HUEVOS_U": 10,
            "COCOA ALCALINA": 100,
            "POLVO HOR": 50,
            "BICARBONATO": 25,
            "COLOR CARAMELO": None,
            "ESCENCIA VAINILLA NEGRA": None
        }
    },
    "Torta de chocolate 25cm": {
        "_tipo": "absoluto",
        "BASE_AREA_CM2": 65*45,
        "TARGET_DIAMETER_CM": 25,
        "INGREDIENTES": {
            "HARINA": 1000,
            "AZUCAR": 850,
            "ACEITE": 500,
            "HUEVOS_U": 10,
            "COCOA ALCALINA": 100,
            "POLVO HOR": 50,
            "BICARBONATO": 25,
            "COLOR CARAMELO": None,
            "ESCENCIA VAINILLA NEGRA": None
        }
    }
}


def mostrar_inventario():
    print("Materiales:")
    for nombre, datos in materiales.items():
        print(f"{nombre}: {datos}")
    print("\nRecetas:")
    for nombre, datos in recetas.items():
        print(f"{nombre}: {datos}")

if __name__ == "__main__":
    mostrar_inventario()