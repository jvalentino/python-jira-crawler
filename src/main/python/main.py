# main.py
from execution_handler import ExecutionHandler

def main():
    print("main.py: main()")
    handler = ExecutionHandler()
    handler.run()

if __name__ == "__main__":
    main()