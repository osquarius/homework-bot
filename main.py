import homeworkbot.credentials
from homeworkbot.bot import HomeworkBot

def main():
    token = credentials.read_token("token.txt")
    hwbot = HomeworkBot()
    hwbot.run(token)

if __name__ == "__main__":
    main()
