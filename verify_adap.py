import hashlib

def sha256_file(filename):
    sha = hashlib.sha256()

    with open(filename,"rb") as f:
        while True:
            chunk=f.read(4096)
            if not chunk:
                break
            sha.update(chunk)

    return sha.hexdigest()


files=[
    "ledger.json",
    "tampered_ledger.json"
]

with open("ledger.sha256","r") as f:
    expected=f.read().strip()


for file in files:

    calculated=sha256_file(file)

    print("\nFILE:",file)
    print("Calculated:",calculated)
    print("Expected :",expected)

    if calculated==expected:
        print("✓ VERIFIED")
    else:
        print("✗ FAILED")
