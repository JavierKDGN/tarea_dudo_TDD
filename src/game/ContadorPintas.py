class ContadorPintas:
    @staticmethod
    def contar(dados, pinta, ases_como_comodin=True):
        count = 0
        ases = 0
        for d in dados:
            if d.getValue() == pinta:
                count += 1
            if d.getValue() == 1:
                ases += 1
        if (not ases_como_comodin) or pinta==1 or count==0: return count
        return count + ases

