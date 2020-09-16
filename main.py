import singer 
import requests

def storeDatas(data):
    singer.write_schema(
        'schema1',
        {
            'properties':{

            }
        }
    )

    singer.write_records(
        'schema1',

    )
    
    singer.write_state()


if __name__ == "__main__":
    pass