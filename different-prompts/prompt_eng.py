import os
import json
from prompt_gemini import prompt_llm


def list_text_files_in_directory(directory):
    text_files = []
    for filename in os.listdir(directory):
        if filename.startswith('_'):
            continue
        if filename.endswith(".json"):
            text_files.append(filename)
    return text_files

       
def load_and_parse_json_file(file_path):
    data = []
    with open(file_path, 'r', encoding='utf-8') as file:
        json_text = ""
        for line in file:
            line = line.strip()
            json_text += line
            if line == "]":
                try:
                    json_data = json.loads(json_text)
                    data.append(json_data)
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON: {json_text}")
                    print(e)
                json_text = ""    
    return data


def main():
    directory = "prompts"
    text_files = list_text_files_in_directory(directory)

    if not text_files:
        print("No text files found in the directory.")
        return
    
    def print_available():
        print("Available prompt tactics:")
        for i, filename in enumerate(text_files, start=1):
            print(f"{i}. {filename}")

    while True:
        try:
            print_available()
            choice = int(input("Enter the number of the prompt tactic to run (or 0 to exit): "))
            if choice == 0:
                break
            elif 1 <= choice <= len(text_files):
                selected_file = text_files[choice - 1]
                file_path = os.path.join(directory, selected_file)
                prompts = load_and_parse_json_file(file_path)
                print(f"Running prompts for {selected_file}")                
                for i, prompt in enumerate(prompts):
                    print(f"PROMPT {i+1} -------------------------------------------------")
                    print(prompt)
                    print(f"REPLY -------------------------------------------------")
                    #using OpenAI
                    print(prompt_llm(prompt))
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()