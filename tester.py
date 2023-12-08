"""Para testar o codigo"""
from models.conta import Conta

from models.cliente import Cliente


andrew: Cliente = Cliente(
    "Maike Andrew", "andrew.maike10@gmail.com", "123.456.789-00", "04/12/1995"
)
hanna: Cliente = Cliente(
    "Hanna Milene", "milenehanna@gmail.com", "112.333.444.00", "12/03/2000"
)

print(andrew)
# print (hanna)

contaa: Conta = Conta(andrew)
contah: Conta = Conta(hanna)

print(contaa)
# print(contah)
