import requests
import pandas as pd
from datetime import datetime

def fetch_certificates():
    print('Fetching certificates...')
    url = 'https://services.arcgis.com/8Pc9XBTAsYuxx9Ny/arcgis/rest/services/certif_of_occupancy_daily_data/FeatureServer/0/query'
    
    params = {
        'where': '1=1',
        'outFields': '*', 
        'outSR': '4326',
        'f': 'json'
    }
    
    try:
        response = requests.get(url, params=params)
        print(f'Response status: {response.status_code}')
        data = response.json()
        
        if 'features' in data:
            df = pd.DataFrame([f['attributes'] for f in data['features']])
            output_file = f'data/certificates_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv'
            df.to_csv(output_file, index=False)
            print(f'Saved {len(df)} records to {output_file}')
            return df
        else:
            print('No features found')
            return None
    except Exception as e:
        print(f'Error: {str(e)}')
        return None

if __name__ == '__main__':
    certificates = fetch_certificates()
    if certificates is not None:
        print('\nMost recent certificates:')
        print(certificates.head())