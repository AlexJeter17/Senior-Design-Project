# from flask import Flask, request, jsonify
# from transformers import GPT2LMHeadModel, GPT2Tokenizer

# app = Flask(__name__)

# # Load the model and tokenizer
# tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
# model = GPT2LMHeadModel.from_pretrained('gpt2')
# model.eval()

# def generate_response(prompt):
#     inputs = tokenizer.encode(prompt, return_tensors="pt")
#     outputs = model.generate(inputs, max_length=100, num_return_sequences=1)
#     return tokenizer.decode(outputs[0], skip_special_tokens=True)

# @app.route('/generate', methods=['POST'])
# def generate():
#     data = request.get_json()
#     prompt = data.get('prompt')
#     if prompt is None or prompt.strip() == "":
#         return jsonify({'error': 'No prompt provided'}), 400
#     response = generate_response(prompt)
#     return jsonify({'response': response})

# if __name__ == '__main__':
#     app.run(debug=True, host='127.0.0.1', port=5000)

########Beginning of User input through terminal #####################

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['POST'])  # Ensure this line allows POST
def handle_prompt():
    data = request.get_json()  # This will get the JSON data sent by the client
    prompt = data.get('prompt')
    response = {'response': f"Processed: {prompt}"}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

