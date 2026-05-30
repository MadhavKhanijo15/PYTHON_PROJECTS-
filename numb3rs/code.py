import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if not re.fullmatch(r"\d+\.\d+\.\d+\.\d+", ip):
        return False

    parts=ip.split(".")

    if len(parts)!=4:
        return False
    if re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$",ip):
        for part in parts:
            if part != str(int(part)):
                return False
            if int(part)<0 or int(part)>255:
                return False

        return True

if __name__ == "__main__":
    main()
