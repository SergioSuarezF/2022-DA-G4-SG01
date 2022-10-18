class Producto():
    def __init__(self, codigoBarras, nombre, fechaVencimiento, precio):
        self.codigoBarras = codigoBarras
        self.nombre = nombre
        self.fechaVencimiento = fechaVencimiento
        self.precio = precio

    def mostrarProducto(self):
        show = "|||||||||||PRODUCTO|||||||||||\nN° Código: {}\nNombre: {}\nFecha de vencimiento: {}\nPrecio: S/.{}\n"
        print(show.format(self.codigoBarras,self.nombre,self.fechaVencimiento,self.precio))

class Venta():
    def __init__(self, nVenta, comprobante, total):
        self.nVenta = nVenta
        self.comprobante = comprobante
        self.total = total

    def mostrarVenta(self):
        showV = "|||||||||||VENTA|||||||||||\nN° Venta: {}\nComprobante: {}\nTotal: S/.{}\n"
        print(showV.format(self.nVenta,self.comprobante,self.total))

class Cliente():
    def __init__(self, dni, nombreCompleto, metodoPago, saldo, deuda):
        self.dni = dni
        self.nombreCompleto = nombreCompleto
        self.metodoPago = metodoPago
        self.saldo = saldo
        self.deuda = deuda

    def mostrarCliente(self):
        sh = "|||||||||||CLIENTE|||||||||||\nDNI: {}\nNombre completo: {}\nMetodo pago: {}\nSaldo: S/.{}\nDeuda: {}"
        print(sh.format(self.dni,self.nombreCompleto,self.metodoPago,self.saldo,self.deuda))


opc = input("Desea ingresar al programa? S/N: ")
while(opc == 's' or opc == 'S'):
    print("")
    print("|||||||||||||||||||||||||||")
    print("|||      Bienvenido     |||")
    print("|||||||||||||||||||||||||||")
    print("")
    print("------------Menu-----------")
    print("")
    opcP = int(input("Cuantos productos ingresará? "))
    nProd = 1
    while (opcP >= 1 and nProd >= 1):
        print("***Ingresar datos del producto ",nProd,": ")
        codeBar = int(input("Ingresar codigo: "))
        nameProd = input("Ingresar nombre: ")
        exDate = input("Ingresar fecha de vencimiento: ")
        price = int(input("Ingresar precio: "))
        Producto1 = Producto(codeBar,nameProd,exDate,price)
        Producto1.mostrarProducto()
        nProd = nProd + 1
        opcP = opcP - 1
               
    opcC = int(input("Cuantos clientes ingresará? "))
    nCli = 1
    while (opcC >= 1 and nCli >= 1):
        print("***Ingresar datos del cliente: ***\n")
        idCode = int(input("Ingresar DNI: "))
        compName = input("Ingresar nombre: ")
        methPay = input("Ingreasar metodo de pago: ")
        balance = int(input("Ingresar saldo disponible: "))
        debt = input("¿Es deudor?: ")
        Cliente1 = Cliente(idCode,compName,methPay,balance,debt)
        Cliente1.mostrarCliente()
        nCli = nCli + 1
        opcC = opcC - 1

    opcV = int(input("Cuantas ventas ingresará? "))
    nVen = 1
    while (opcV >= 1 and nVen >= 1):
        print("***Ingresar datos de la venta: ***\n")
        nSell = int(input("Ingresar N° de venta: "))
        purchase = input("Ingresar tipo de comprobante: ")
        tot = int(input("Ingresar total: "))
        Venta1 = Venta(nSell,purchase,tot)
        Venta1.mostrarVenta()
        nVen = nVen + 1
        opcV = opcV - 1


        

