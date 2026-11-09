def verificar_stock(productos):
    bajos_stock = []
    for producto in productos:
        if producto["stock"] < producto["stock_minimo"]:
            bajos_stock.append(producto["nombre"])
    return bajos_stock

if __name__ == "__main__":
    inventario = [
        {"nombre": "Sensor A", "stock": 5, "stock_minimo": 10},
        {"nombre": "Sensor B", "stock": 15, "stock_minimo": 10},
        {"nombre": "Cable USB", "stock": 2, "stock_minimo": 5}
    ]
    
    productos_bajos = verificar_stock(inventario)
    
    if productos_bajos:
        print("Productos con stock bajo:")
        for prod in productos_bajos:
            print(f"- {prod}")
    else:
        print("Todo el stock está bien")
