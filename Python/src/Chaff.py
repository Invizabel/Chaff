import argparse
import os

# NIST 800-88: https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-88r2.pdf
def main(filename):
    filesize = os.path.getsize(filename)

    # Overwrite with zeros (NIST 800-88)
    print(f"Overwriting: {filename}")
    with open(filename, "wb") as file:
        for i in range(filesize):
            file.seek(i)
            file.write(b"0")

    # Verify zeros (NIST 800-88)
    print(f"Verifying: {filename}")
    with open(filename, "rb") as file:
        for i in range(filesize):
            file.seek(i)
            is_valid = file.read(1)
            if is_valid != b"0":
                return False

    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog = "Chaff", description = "Secure overwrite tool utilizing NIST 800-88 Revision 2")
    parser.add_argument("--filename", required = True)
    args = parser.parse_args()

    is_success = main(args.filename)

    if is_success:
        print(f"Overwrite successful: {args.filename}")

    else:
        print(f"Overwrite failed: {args.filename}")