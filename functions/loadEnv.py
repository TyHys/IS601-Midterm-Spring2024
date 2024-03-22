import os 

def loadEnv():
    env_file_path = ".env"
    if os.path.exists(env_file_path):
        with open(env_file_path, "r") as file:
            for line in file:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                key, value = line.split("=", 1)
                os.environ[key.strip()] = value.strip()