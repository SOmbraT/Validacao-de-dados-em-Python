from validate_docbr import CPF, CNPJ

class Documento:
    @staticmethod
    def cria_documento(documento):
        if len(documento) == 11:
            return DocCpf(documento)
        elif len(documento) == 14:
            return DocCnpj(documento)
        else:
            raise ValueError("Quantidade de dígitos está incorreta!!")


class DocCpf:
    def __init__(self, documento):
        if self.validade(documento):
            self.cpf = documento
        else:
            raise ValueError("Cpf inválido!")
        
    def __str__(self):
        return self.format
    
    def validade(self, documento):
        validador = CPF()
        return validador.validate(documento)
        
    def format(self):
        mascara = CPF()
        return mascara.mask(self.cpf)
    

class DocCnpj:
    def __init__(self, documento):
        if self.validade(documento):
            self.cnpj = documento
        else:
            raise ValueError("Cnpj inválido!")
        
    def __str__(self):
        return self.format
    
    def validade(self, documento):
        validade_cnpj = CNPJ()
        return validade_cnpj.validate(documento)
        
    def format(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)

