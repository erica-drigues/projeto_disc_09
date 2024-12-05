class IMC:
    def __init__(self, peso, altura):
        self.__peso = peso
        self.__altura = altura

    # Getter padrão para peso
    def get_peso(self):
        return self.__peso

    # Setter padrão para peso
    def set_peso(self, peso):
        if peso <= 0:
            raise ValueError("Peso deve ser maior que zero.")
        self.__peso = peso

    # Getter padrão para altura
    def get_altura(self):
        return self.__altura

    # Setter padrão para altura
    def set_altura(self, altura):
        if altura <= 0:
            raise ValueError("Altura deve ser maior que zero.")
        self.__altura = altura

    def calcular_imc(self):
        """Calcula o IMC com base no peso e altura."""
        if self.__altura <= 0:
            raise ValueError("Altura deve ser maior que zero.")
        return self.__peso / (self.__altura * self.__altura)

    def classificar_imc(self):
        """Classifica o IMC de acordo com os padrões da OMS."""
        imc = self.calcular_imc()
        if imc < 18.5:
            return "Abaixo do peso"
        elif 18.5 <= imc < 24.9:
            return "Peso normal"
        elif 25 <= imc < 29.9:
            return "Sobrepeso"
        elif 30 <= imc < 34.9:
            return "Obesidade grau 1"
        elif 35 <= imc < 39.9:
            return "Obesidade grau 2"
        else:
            return "Obesidade grau 3"
