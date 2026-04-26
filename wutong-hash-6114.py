import hashlib
import argparse
import json

def get_hash(file_path, algorithm):
    hasher = hashlib.new(algorithm)
    with open(file_path, 'rb') as file:
        while data := file.read(4096):
            hasher.update(data)
    return hasher.hexdigest()

def check_file_integrity(file_path, expected_hash, algorithm):
    computed_hash = get_hash(file_path, algorithm)
    if computed_hash == expected_hash:
        print(f"File '{file_path}' is intact with hash: {computed_hash}")
    else:
        print(f"Hash mismatch for file '{file_path}'. Expected: {expected_hash}, got: {computed_hash}")

def main():
    parser = argparse.ArgumentParser(description="Check the integrity of a file using SHA256, MD5, or SHA1.")
    parser.add_argument('file', type=str, help='Path to the file.')
    parser.add_argument('--json', action='store_true', help='Output in JSON format.')
    parser.add_argument('--output', type=str, help='Specify the output filename.')
    args = parser.parse_args()

    if not args.json:
        print(f"File integrity for '{args.file}' using {args.algorithm}:")
        computed_hash = get_hash(args.file, args.algorithm)
        print(computed_hash)

    else:
        data = {
            'file': args.file,
            'algorithm': args.algorithm,
            'computed_hash': get_hash(args.file, args.algorithm)
        }
        if args.output:
            with open(args.output, 'w') as f:
                json.dump(data, f, indent=4)
            print(f"File integrity data saved to '{args.output}'")
        else:
            print(json.dumps(data, indent=4))

if __name__ == "__main__":
    main()