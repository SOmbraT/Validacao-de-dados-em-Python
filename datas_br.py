from datetime import datetime, timedelta

class DatasBr:
    def __init__(self):
        self.momento_cadrasto = datetime.today()

    def __str__(self):
        return self.format_data()

    def mes_cadastro(self):
        meses_do_ano = [
            "janeiro", "fervereiro", "março",
            "abril", "maio", "junho","julho",
            "agosto", "setembro", "outubro",
            "novembro", "dezembro"
        ]
        mes_cadastro = self.momento_cadrasto.month - 1
        print(mes_cadastro)
        return meses_do_ano
    
    def dia_semana(self):
        dia_semana = [
            "segunda", "terça", "quarta",
            "quinta", "sexta", "sabado",
            "domingo"
        ]
        dia_semana = self.momento_cadrasto.weekday()
        return dia_semana
    
    def format_data(self):
        data_formatada = self.momento_cadrasto.strftime("%d/%m/%Y %H:%M")
        return data_formatada
    
    def tempo_cadastro(self):
        tempo_cadastro = datetime.today() + timedelta(days = 30) - self.momento_cadrasto
        return tempo_cadastro