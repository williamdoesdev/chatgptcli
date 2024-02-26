from src.cli import clear, title_bar

def main():
    while True:
        try:
            clear()
            print(title_bar())
            input()
        except KeyboardInterrupt:
            clear()
            break

if __name__ == '__main__':
    main()