import zipfile
import os
import sys

def compress_file(file_path):
    if not os.path.exists(file_path):
        print("❌ File does not exist.")
        return

    zip_name = file_path + ".zip"

    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(file_path, os.path.basename(file_path))

    print(f"✅ File compressed successfully: {zip_name}")

def decompress_file(zip_path):
    if not os.path.exists(zip_path):
        print("❌ ZIP file does not exist.")
        return

    with zipfile.ZipFile(zip_path, 'r') as zipf:
        zipf.extractall(os.path.dirname(zip_path))

    print("✅ File extracted successfully.")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage:")
        print("  Compress:   python compressor.py compress <file_path>")
        print("  Decompress: python compressor.py decompress <zip_path>")
    else:
        action = sys.argv[1]
        path = sys.argv[2]

        if action == "compress":
            compress_file(path)
        elif action == "decompress":
            decompress_file(path)
        else:
            print("❌ Invalid command. Use 'compress' or 'decompress'.")