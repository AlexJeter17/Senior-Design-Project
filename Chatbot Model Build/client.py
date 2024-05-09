import requests

def send_prompt_to_api(prompt):
    url = 'http://localhost:5000/'  # Ensure this is the correct URL
    headers = {'Content-Type': 'application/json'}
    data = {'prompt': prompt}
    response = requests.post(url, json=data, headers=headers)
    return response.json()

while True:
    user_input = input("Enter your prompt (or type 'exit' to quit): ")
    if user_input.lower() == 'exit':
        break
    result = send_prompt_to_api(user_input)
    print("Generated Response:", result['response'])
