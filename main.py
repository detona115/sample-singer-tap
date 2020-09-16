import singer 
import requests
import sys
import json

def storeDatas(data):
    singer.write_schema(
        'schema1',
        {
            'properties':{

            }
        }
    )

    try:
        singer.write_records(
            'schema1',

        )
    except:
        print('houve um erro na escritura dos dados!')
    finally:
        sys.exit(1)
    
    
    singer.write_state()


if __name__ == "__main__":

    
    req = requests.get('https://cve.circl.lu/api/last')
    data = json.dumps(req.json(), indent=2)

    storeDatas(data)