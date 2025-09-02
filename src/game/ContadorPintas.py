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
        if ases_como_comodin:
            if count != 0:
                if pinta != 1:
                    return count+ases
                else:
                    return count
            else:
                return 0
        else:
            return count

