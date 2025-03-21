from flask import Flask, jsonify
from datetime import date
app = Flask(__name__)

tempo = date.today()
@app.route('/dia_atual/<dia>-<mes>-<ano>')
def valores(dia, mes, ano):
    """
    API para calcular a diferença entre duas datas (dia, mes e ano)

    ## Endpoint:
    'GET /dia_atual/<dia>-<mes>-<ano>'

    ## Parâmetros:
     - 'dia', 'mes', 'ano' **Data no formato "DD/MM/YYYY"** (exemplo: "20-03-2025").
       - **Qualquer outro formato resultará em erro.**

    ## Resposta (JSON):
     '''json

     {
        "data_atual": "20/03/2025",
        "data_inserida": "20/03/2025",
        "diferenca_dias": 0,
        "diferenca_mes": 0,
        "diferenca_ano": 0,
        "status": "presente",
        }

    ## Erros possíveis:
    - Se 'dia_atual' não estiver no formato correspondente ao formato "DD/MM/YYYY", retorna erro **400 Bad Request.**
      '''json
    """
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
        return jsonify({"erro": "Data incorreta"})
    except TypeError:
        return jsonify({"erro": "Data incorreto"})


    # return jsonify({'message': 'Hello World!'})

if __name__ == '__main__':
    app.run(debug=True)
