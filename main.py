import singer 
import requests
import sys
import json

def storeDatas(data):

    # definindo o esquema 
    singer.write_schema(
        'schema1',
        {
            'properties':{
                "Modified": {"type": "string"},
                "Published": {"type": "string"},
                "access": {
                    "type": "object"
                },
                "assigner": {"type": "string"},
                "cwe": {"type": "number"},
                "id": {"type": "string"},
                "impact": {
                    "type": "object"
                },
                "last-modified": {"type": "string"},
                "references": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    }
                },
                "summary": {"type": "string"},
                "vulnerable_configuration": {
                    "type": "array"
                },
                "vulnerable_configuration_cpe_2_2": {
                    "type": "array"
                },
                "vulnerable_product": {
                    "type": "array"
                }
            }
        },[]
    )

    try:

        # salvando os dados
        for d in data:
            singer.write_records(
                'schema1',
                d
            )
    except:
        print('houve um erro na escritura dos dados!')
    finally:
        sys.exit(1)
    
    
    singer.write_state(value={"last-id": "CVE-2020-7294"})


if __name__ == "__main__":

    # recuperação dos dados
    req = requests.get('https://cve.circl.lu/api/last')
    data = req.json()

    storeDatas(data)