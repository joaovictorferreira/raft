import time

class Processo:

    def __init__(self, id):
        self.id = id
        self.lider = id
        self.ativo = True

    def recebe_id(self, novo_id):
        if novo_id > self.lider:
            self.lider = novo_id

processos = [Processo(0), Processo(1), Processo(2)]

def envio_id():
    ativos = [p for p in processos if p.ativo]
    for processo in ativos:
        processo.lider = processo.id
        for i in ativos:
            processo.recebe_id(i.id)

def processo_caiu():
    ativos = [p for p in processos if p.ativo]
    lider = max(ativos, key=lambda p: p.id)
    lider.ativo = False
    print(f"Líder {lider.id} caiu")
    time.sleep(4)
    eleicao()

def eleicao():
    envio_id()
    for processo in processos:
        if processo.ativo:
            print(f"Processo {processo.id} elegeu {processo.lider}")

if __name__ == "__main__":
    eleicao()
    processo_caiu()