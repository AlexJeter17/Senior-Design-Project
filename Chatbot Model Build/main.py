# Import necessary libraries
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch
import argparse

# Load the pre-trained GPT-2 model and tokenizer
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')
model.eval()  # Set the model to evaluation mode

# Function to generate a response from the model
def generate_response(prompt):
    # Encode the prompt into tokens
    inputs = tokenizer.encode(prompt, return_tensors="pt")
    # Generate a response using the model
    outputs = model.generate(inputs, max_length=50, num_return_sequences=1)
    # Decode the generated tokens back into text
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

# Define test cases with prompts and expected outputs
test_cases = [
    {"prompt": "Suggest a marketing strategy for a 30-year-old male interested in technology, using Twitter.", "expected": "Engage with tech influencers on Twitter to promote your product."},
    {"prompt": "Develop a content strategy for a female Instagram user interested in fitness.", "expected": "Create weekly fitness challenges and use popular fitness hashtags."},
]

# Function to handle command-line arguments
def get_args():
    parser = argparse.ArgumentParser(description="Generate responses using GPT-2 model")
    parser.add_argument("-p", "--prompt", type=str, help="Provide a prompt for the model to generate a response")
    return parser.parse_args()

# Main function to execute based on CLI input
def main():
    args = get_args()
    if args.prompt:
        response = generate_response(args.prompt)
        print(f"Prompt: {args.prompt}")
        print(f"Generated Response: {response}\n")
    else:
        # Default to predefined test cases if no prompt is provided
        for test in test_cases:
            response = generate_response(test['prompt'])
            print(f"Prompt: {test['prompt']}")
            print(f"Generated Response: {response}")
            print(f"Expected Response: {test['expected']}\n")

if __name__ == "__main__":
    main()


# Run the script with the following command in the terminal: python main.py --prompt "What's the best social media strategy for increasing engagement?"

#
#
#
#   The following code allows for a more interactive 'main.py', one that allows the terminal to continue until user wants to exit
#
#
#

# Import necessary libraries
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch
import argparse

# Load the pre-trained GPT-2 model and tokenizer
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')
model.eval()  # Set the model to evaluation mode

# Function to generate a response from the model
def generate_response(prompt):
    # Encode the prompt into tokens
    inputs = tokenizer.encode(prompt, return_tensors="pt")
    # Generate a response using the model
    outputs = model.generate(inputs, max_length=50, num_return_sequences=1)
    # Decode the generated tokens back into text
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

# Interactive mode function
def interactive_mode():
    print("Interactive Mode: Enter 'quit' to exit.")
    while True:
        user_input = input("Enter your prompt: ")
        if user_input.lower() == 'quit':
            break
        response = generate_response(user_input)
        print(f"Generated Response: {response}\n")

# Function to handle command-line arguments
def get_args():
    parser = argparse.ArgumentParser(description="Generate responses using GPT-2 model")
    parser.add_argument("-p", "--prompt", type=str, help="Provide a prompt for the model to generate a response")
    return parser.parse_args()

# Main function to execute based on CLI input
def main():
    args = get_args()
    if args.prompt:
        response = generate_response(args.prompt)
        print(f"Prompt: {args.prompt}")
        print(f"Generated Response: {response}\n")
    else:
        interactive_mode()

if __name__ == "__main__":
    main()


#
#
#
#   The following code allows for a more clean output to 'main.py'
#
#
#


# Import necessary libraries
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch
import argparse

# Load the pre-trained GPT-2 model and tokenizer
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')
model.eval()  # Set the model to evaluation mode

# Function to generate a response from the model
def generate_response(prompt):
    # Encode the prompt into tokens
    inputs = tokenizer.encode(prompt, return_tensors="pt")
    # Generate a response using the model
    outputs = model.generate(inputs, max_length=50, num_return_sequences=1)
    # Decode the generated tokens back into text
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

# Function to print responses in a formatted manner
def print_response(prompt, response):
    print("\n--------------------------------------------------")
    print(f"Prompt: {prompt}")
    print(f"Response: {response}")
    print("--------------------------------------------------\n")

# Interactive mode function
def interactive_mode():
    print("Interactive Mode: Enter 'quit' to exit.")
    while True:
        user_input = input("\nEnter your prompt: ")
        if user_input.lower() == 'quit':
            break
        response = generate_response(user_input)
        print_response(user_input, response)

# Function to handle command-line arguments
def get_args():
    parser = argparse.ArgumentParser(description="Generate responses using GPT-2 model")
    parser.add_argument("-p", "--prompt", type=str, help="Provide a prompt for the model to generate a response")
    return parser.parse_args()

# Main function to execute based on CLI input
def main():
    args = get_args()
    if args.prompt:
        response = generate_response(args.prompt)
        print_response(args.prompt, response)
    else:
        interactive_mode()

if __name__ == "__main__":
    main()


#
#
#
#   The following code allows for error handling in 'main.py'
#
#
#

# Import necessary libraries
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch
import argparse

# Load the pre-trained GPT-2 model and tokenizer
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')
model.eval()  # Set the model to evaluation mode

# Function to generate a response from the model with error handling
def generate_response(prompt):
    try:
        # Encode the prompt into tokens
        inputs = tokenizer.encode(prompt, return_tensors="pt")
        # Generate a response using the model
        outputs = model.generate(inputs, max_length=50, num_return_sequences=1)
        # Decode the generated tokens back into text
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        return response
    except Exception as e:
        print(f"An error occurred while generating a response: {str(e)}")
        return "Error: Unable to generate a response."

# Function to print responses in a formatted manner
def print_response(prompt, response):
    print("\n--------------------------------------------------")
    print(f"Prompt: {prompt}")
    print(f"Response: {response}")
    print("--------------------------------------------------\n")

# Interactive mode function
def interactive_mode():
    print("Interactive Mode: Enter 'quit' to exit.")
    while True:
        user_input = input("\nEnter your prompt: ")
        if user_input.lower() == 'quit':
            break
        response = generate_response(user_input)
        print_response(user_input, response)

# Function to handle command-line arguments
def get_args():
    parser = argparse.ArgumentParser(description="Generate responses using GPT-2 model")
    parser.add_argument("-p", "--prompt", type=str, help="Provide a prompt for the model to generate a response")
    return parser.parse_args()

# Main function to execute based on CLI input
def main():
    args = get_args()
    if args.prompt:
        response = generate_response(args.prompt)
        print_response(args.prompt, response)
    else:
        interactive_mode()

if __name__ == "__main__":
    main()


#
#
#
#   The following code allows for logging errors and logging progress
#
#
#

# Import necessary libraries
import logging
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import argparse

# Set up logging
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load the pre-trained GPT-2 model and tokenizer
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')
model.eval()  # Set the model to evaluation mode
logging.info("Loaded GPT-2 model and tokenizer.")

# Function to generate a response from the model with error handling
def generate_response(prompt):
    try:
        inputs = tokenizer.encode(prompt, return_tensors="pt")
        outputs = model.generate(inputs, max_length=50, num_return_sequences=1)
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        logging.info(f"Generated response for the prompt: {prompt}")
        return response
    except Exception as e:
        logging.error(f"An error occurred while generating a response: {str(e)}")
        return "Error: Unable to generate a response."

# Function to print responses in a formatted manner
def print_response(prompt, response):
    print("\n--------------------------------------------------")
    print(f"Prompt: {prompt}")
    print(f"Response: {response}")
    print("--------------------------------------------------\n")

# Interactive mode function
def interactive_mode():
    print("Interactive Mode: Enter 'quit' to exit.")
    logging.info("Entered interactive mode.")
    while True:
        user_input = input("\nEnter your prompt: ")
        if user_input.lower() == 'quit':
            logging.info("Exiting interactive mode.")
            break
        response = generate_response(user_input)
        print_response(user_input, response)

# Function to handle command-line arguments
def get_args():
    parser = argparse.ArgumentParser(description="Generate responses using GPT-2 model")
    parser.add_argument("-p", "--prompt", type=str, help="Provide a prompt for the model to generate a response")
    return parser.parse_args()

# Main function to execute based on CLI input
def main():
    args = get_args()
    if args.prompt:
        logging.info(f"Received command-line prompt: {args.prompt}")
        response = generate_response(args.prompt)
        print_response(args.prompt, response)
    else:
        interactive_mode()

if __name__ == "__main__":
    main()
