#ActClase 10.1: Construcción de programas estructurados con funciones
def calcular_costos():
    # Datos de entrada
    precio_compra = float(input("Precio de tu compra: "))
    es_vip = input("¿Eres cliente VIP? (si/no): ").strip().lower() == 'si'
    region = input("Indica si tu envío es a America, Europa o Asia: ").strip().capitalize()
    es_descarga = input("¿Tu producto es una descarga digital? (si/no): ").strip().lower() == 'si'
    
    peso_producto = 0
    if not es_descarga:
        peso_producto = float(input("Peso de tu producto en kg: "))

        descuento = 0
    if es_vip:
        descuento = 0.20
    elif precio_compra > 5000:
        descuento = 0.12

    monto_descuento = precio_compra * descuento
    precio_con_descuento = precio_compra - monto_descuento

    impuestos = 0
    if region == 'America':
        impuestos = 0.05
    elif region == 'Europa':
        impuestos = 0.12
    elif region == 'Asia':
        impuestos = 0.08

    monto_impuesto = precio_con_descuento * impuestos
    precio_con_impuestos = precio_con_descuento + monto_impuesto

    gastos_envio = 0
    if not es_descarga:
        if peso_producto < 5:
            gastos_envio = 35
        else:
            gastos_envio = 35 + 5 * (peso_producto - 5)

    costo_total = precio_con_impuestos + gastos_envio

    print(f"\n--- Desglose de costos ---")
    print(f"Precio original: ${precio_compra:.2f}")
    print(f"Descuento: ${monto_descuento:.2f}")
    print(f"Precio con descuento: ${precio_con_descuento:.2f}")
    print(f"Impuestos ({impuestos * 100}%): ${monto_impuesto:.2f}")
    print(f"Precio con impuestos: ${precio_con_impuestos:.2f}")
    print(f"Gastos de envío: ${gastos_envio:.2f}")
    print(f"Costo total: ${costo_total:.2f}")

calcular_costos()
