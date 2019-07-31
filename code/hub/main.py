import sys


def main():
    print("Hello World!")
    args = sys.argv
    if len(args) < 2:
        print("Specify desired I2C bus!")
        print("Usage : i2c-scanner.py <bus>")
        sys.exit()
    bus = int(args[1])


if __name__ == "__main__":
    main()
