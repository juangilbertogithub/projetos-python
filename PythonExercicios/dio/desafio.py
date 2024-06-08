saldoAtual = float(input("Saldo Bancario: " ))
print("Saldo Atual: ", saldoAtual)

saldoDeposito = float(input("Saldo Depositado: " ))
print("Saldo Depositado: ", saldoDeposito)

saldoSaque = float(input("Saldo Saque: " ))
print("Saldo Sacado: ", saldoSaque)


def saldoDepositado():
    global saldoAtual
    saldoAtual = saldoAtual + saldoDeposito

def saldoSacado():
    global saldoAtual
    saldoAtual = saldoAtual - saldoSaque

saldoDepositado()
saldoSacado()

if saldoAtual <0:
    print('Saldo insuficiente.', saldoAtual)

else:
    print("Saldo Atualizado: ", saldoAtual)