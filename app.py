from flask import Flask, jsonify
from datetime import date
app = Flask(__name__)

tempo = date.today()
@app.route('/dia_atual/<dia>-<mes>-<ano>')
def valores(dia, mes, ano):
    try:
        dia= int(dia)
        mes = int(mes)
        ano = int(ano)
        data_inserida = date(ano, mes, dia)
        variacao_inserido_atual = tempo - data_inserida
        if variacao_inserido_atual.days < 0:
            print('data inserida esta no futuro')
            status = 'futuro'

        elif variacao_inserido_atual.days > 0:
            print('data inserida esta no passado')
            status = 'passado'
        else:
            print('data inserida no mesmo dia')
            status = 'presente'
        # data atual
        data_atual = tempo.strftime('%d/%m/%Y')
        # data q escolhi
        data_inserida = data_inserida.strftime('%d/%m/%Y')

        # abs é pra tirar o negativo do numero
        diferenca_dias = abs(variacao_inserido_atual.days)
        diferenca_mes = diferenca_dias // 30
        diferenca_ano = diferenca_dias // 360

        return jsonify({
                    "status": status,
                    "data_inserida": data_inserida,
                    "data_atual": data_atual,
                    "diferenca_dias": diferenca_dias,
                    "diferenca_mes": diferenca_mes,
                    "diferenca_ano": diferenca_ano,

        })

    except ValueError:
        return  "Data incorreto"







    # return jsonify({'message': 'Hello World!'})

if __name__ == '__main__':
    app.run(debug=True)
