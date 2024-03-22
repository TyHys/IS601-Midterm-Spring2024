import os 

def loadEnv() -> None:
    """
    Loads environment variables from a file named '.env' in the current directory.

    The function reads the '.env' file line by line. Each line should contain
    a key-value pair separated by '='. Empty lines and lines starting with '#'
    (comments) are ignored. The function then sets the environment variables
    accordingly.

    Returns:
    - None

    Example:
    Suppose the '.env' file contains the following:
    ```
    DB_HOST=localhost
    DB_PORT=5432
    SECRET_KEY=my_secret_key
    ```

    Calling `loadEnv()` will set the environment variables as follows:
    - `os.environ['DB_HOST'] = 'localhost'`
    - `os.environ['DB_PORT'] = '5432'`
    - `os.environ['SECRET_KEY'] = 'my_secret_key'`
    """
    env_file_path = ".env"
    if os.path.exists(env_file_path):
        with open(env_file_path, "r") as file:
            for line in file:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                key, value = line.split("=", 1)
                os.environ[key.strip()] = value.strip()
    return None