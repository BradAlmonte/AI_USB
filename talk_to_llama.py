import os
import requests
OLLAMA_ENDPOINT = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3:instruct"
USB_PATH = r"C:\AI_USB"
def list_files_and_sizes(directory):
   file_info = []
   for root, _, files in os.walk(directory):
       for file in files:
           full_path = os.path.join(root, file)
           try:
               size = os.path.getsize(full_path)
               file_info.append(f"{full_path} (Size: {size} bytes)")
           except Exception as e:
               file_info.append(f"{full_path} (Error: {str(e)})")
   return "\n".join(file_info) or "No files found."
def query_ollama(user_input, file_data, model=MODEL_NAME):
   prompt = f"""
You are an AI assistant helping analyze files on a USB drive.
User's request: {user_input}
Below is the list of files found in the directory {USB_PATH}:
{file_data}
Based on the user's request and the file list, provide a helpful response.
"""
   response = requests.post(
       OLLAMA_ENDPOINT,
       json={"model": model, "prompt": prompt, "stream": False}
   )
   response.raise_for_status()
   return response.json()["response"]
if __name__ == "__main__":
   print("Welcome to AI USB Inspector.")
   user_request = input("What do you want me to do with the USB files? (e.g., 'Summarize them', 'Check for malware', etc.): ")
   print("\nScanning USB contents...\n")
   file_summary = list_files_and_sizes(USB_PATH)
   print("Asking Ollama for analysis...\n")
   result = query_ollama(user_request, file_summary)
   print("Ollama's Response:\n")
   print(result)