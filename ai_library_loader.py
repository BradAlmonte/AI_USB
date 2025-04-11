import os

def load_text_files_from_library(base_path="./libraries"):
    content = ""
    for root, dirs, files in os.walk(base_path):
        for file in files:
            if file.endswith((".txt", ".md", ".py", ".sh", ".yaml", ".yml", ".log", ".json")):
                try:
                    with open(os.path.join(root, file), 'r', encoding='utf-8', errors='ignore') as f:
                        content += f"\n\n# === {file} ===\n" + f.read()
                except Exception as e:
                    print(f"Could not read {file}: {e}")
    return content

if __name__ == "__main__":
    print("Reading hacking library content...")
    data = load_text_files_from_library()
    print("\n--- START OF LIBRARY DUMP ---\n")
    print(data[:10000])
    print("\n--- END OF PARTIAL DUMP ---\n")

