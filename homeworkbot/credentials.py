def read_token(token_path):
    with open(token_path, "r") as token_file:
        lines = token_file.readlines()
        return lines[0].strip()