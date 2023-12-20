import requests

def post_logs_to_local_server(log_file_path, server_url):
    try:
        with open(log_file_path, 'r') as file:
            for line in file:
                payload = {'logs': line.strip()}  # Remove newline characters
                response = requests.post(server_url, data=payload)

                # Optionally, you can check the response status or print some information
                if response.status_code == 200:
                    print(f"Line sent successfully: {line.strip()}")
                else:
                    print(f"Failed to send line: {line.strip()}")
                    print(f"Response status code: {response.status_code}")
                    print(f"Response text: {response.text}")
            

    except Exception as e:
        print(f'An error occurred: {e}')

log_file_path = 'logs.txt'
local_server_url = 'http://localhost:8000/log_endpoint'

post_logs_to_local_server(log_file_path, local_server_url)



            
# with open(log_file_path, 'r') as file:
#             print("read")
#             logs = file.read()

#         payload = {'logs': logs}
#         response = requests.post(server_url, data=payload)

#         if response.status_code == 200:
#             print('Logs successfully posted to the local server.')
#         else:
#             print(f'Failed to post logs. Status code: {response.status_code}')