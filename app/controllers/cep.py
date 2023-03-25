from flask import jsonify, request
from unidecode import unidecode
import xmltodict
import requests
import json


def cep_details():
    data = request.json
    
    try:
        cep = unidecode(data["cep"])
        response_cep = requests.get(f'http://viacep.com.br/ws/{cep}/json/')
        cep_json = response_cep.json()
        
        city = unidecode(cep_json["localidade"])
        city = city.replace(' ', '%20')

        response_local = requests.get(f'http://servicos.cptec.inpe.br/XML/listaCidades?city={city}')
        xml_dict = xmltodict.parse(response_local.content)
        local_str = json.dumps(xml_dict, indent=4)
        local_json = json.loads(local_str)
        
        try:
            id_city = local_json['cidades']['cidade']['id']
        except:
            id_city = local_json['cidades']['cidade'][0]['id']
                
        response_weather = requests.get(f'http://servicos.cptec.inpe.br/XML/cidade/{id_city}/previsao.xml')
        xml_dict = xmltodict.parse(response_weather.content)
        weather_str = json.dumps(xml_dict, indent=4)
        weather_json = json.loads(weather_str)["cidade"]["previsao"]
        
        response = cep_json
        response["previsoes"] = weather_json
        
        return jsonify(response) 
    except:
        return {'mensagem': 'Erro na resposta'}