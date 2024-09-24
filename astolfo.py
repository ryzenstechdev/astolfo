import os
import requests
import sys

# Specifica la directory di destinazione
BASE_DIR = "C:/boxify/directory/system/packages/apps/"

def download_package(package_name):
    repo_url = f"https://github.com/ryzenstechdev/astolfo/raw/main/{package_name}"
    package_path = os.path.join(BASE_DIR, package_name)
    
    try:
        response = requests.get(repo_url)
        if response.status_code == 200:
            with open(package_path, 'wb') as f:
                f.write(response.content)
            print(f"Package '{package_name}' downloaded to {package_path}")
        else:
            print(f"Failed to download package '{package_name}'. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")

def main():
    # Controlla se il comando è stato invocato correttamente
    if len(sys.argv) != 3 or sys.argv[1] != 'get':
        print("Usage: astolfo get <package_name>")
        return
    
    package_name = sys.argv[2]
    download_package(package_name)

if __name__ == "__main__":
    main()
