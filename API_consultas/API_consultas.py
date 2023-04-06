from flask import Flask, jsonify, request
import json

# 1. Objetivo -  Desenvolver uma API que gerencia consultas médicas.

# 2. URL base - localhost

# 3. Endpoints - funcionalidades:

# ** Pessoas Profissionais **
# cadastrar profissional                     - localhost/pprofis (POST)
# editar cadastro de pessoa profissional     - localhost/pprofis/<int:id_pprofis> (PUT)
# deletar cadastro de pessoa profissional    - localhost/pprofis/<int:id_pprofis> (DELETE)

# ** Consultas **
# pesquisar consultas  por id_profis         - localhost/consultas/<int:id_pprofis> (GET)
# cadastrar consulta                         - localhost/consultas (POST)
# editar consulta                            - localhost/consultas/<int:id_consulta> (PUT)
# deletar cadastro de consulta               - localhost/consultas/<int:id_consulta> (DELETE)


# 4. Quais recursos - consultas e pessoas_profissionais
# Abertura dos arquivos json


with open("pessoas_profissionais.json","r", -1, "utf-8") as jsonFile:
    pprofis = json.load(jsonFile)
    jsonFile.close()

with open("consultas.json","r", -1, "utf-8") as jsonFile:
    consultas = json.load(jsonFile)
    jsonFile.close()


app = Flask(__name__)

# Pesquisar Consulta por id_pprofis
@app.route('/consultas/<int:id_pprofis>', methods=['GET'])
def pesquisar_consulta_id_pprofis(id_pprofis):
    c_pprofis = [] # necessário caso a pessoa profissional
                   # tenha mais de uma consulta registrada
    for c in consultas:
        if c.get("id_profissional") == id_pprofis:
            c_pprofis.append(c)

    return jsonify(c_pprofis)

# # Cadastrar Pessoa Profissional
@app.route('/pprofis', methods=['POST'])
def cadastrar_pprofissional():
    nova_pprofis = request.get_json()
    pprofis.append(nova_pprofis)
    # Escrevendo o arquivo json
    with open("pessoas_profissionais.json", "w", -1, "utf-8") as jsonFile:
        json.dump(pprofis,jsonFile)
        jsonFile.close()

    return jsonify(pprofis)


# Cadastrar Consulta
@app.route('/consultas', methods=['POST'])
def cadastrar_consulta():
    nova_consulta = request.get_json()
    consultas.append(nova_consulta)
    # Escrevendo o arquivo json
    with open("consultas.json", "w", -1, "utf-8") as jsonFile:
        json.dump(consultas, jsonFile)
        jsonFile.close()

    return jsonify(consultas)


# Editar Pessoa Profissional
@app.route('/pprofis/<int:id_pprofis>', methods=['PUT'])
def editar_pprofis(id_pprofis):
    pprofis_alterado = request.get_json()
    for indice, p in enumerate(pprofis):
        if p.get("id_profssional") == id_pprofis:
            pprofis[indice].update(pprofis_alterado)
            #Escrevendo o arquivo json
            with open("pessoas_profissionais.json", "w", -1, "utf-8") as jsonFile:
                json.dump(pprofis, jsonFile)
                jsonFile.close()

            return jsonify(pprofis[indice])


# Editar Consulta
@app.route('/consultas/<int:id_consulta>', methods=['PUT'])
def editar_consulta_por_id(id_consulta):
    consulta_alterada = request.get_json()
    for indice, c in enumerate(consultas):
        if c.get("id_consulta") == id_consulta:
            consultas[indice].update(consulta_alterada)
            #Escreve arquivo json
            with open("consultas.json", "w", -1, "utf-8") as jsonFile:
                json.dump(consultas, jsonFile)
                jsonFile.close()

            return jsonify(consultas[indice])


# Deletar Pessoa Profissional
@app.route('/pprofis/<int:id_pprofis>', methods=['DELETE'])
def delete_pprofis(id_pprofis):
    for indice, p in enumerate(pprofis):
        if p.get("id_profssional") == id_pprofis:
            del pprofis[indice]
            # Escrevendo o arquivo json
            with open("pessoas_profissionais.json", "w", -1, "utf-8") as jsonFile:
                json.dump(pprofis, jsonFile)
                jsonFile.close()
            return jsonify(pprofis)


# Deletar Consulta
@app.route('/consultas/<int:id_consulta>', methods=['DELETE'])
def delete_consulta(id_consulta):
    for indice, c in enumerate(consultas):
        if c.get("id_consulta") == id_consulta:
            del consultas[indice]
            # Escrevendo o arquivo json
            with open("pessoas_profissionais.json", "w", -1, "utf-8") as jsonFile:
                json.dump(pprofis, jsonFile)
                jsonFile.close()

            return jsonify(consultas)


app.run(port=5000, host='localhost', debug=True)
