import hashlib

def sha256_file(filename):
    sha = hashlib.sha256()

    with open(filename, "rb") as f:
        while True:
            chunk = f.read(4096)
            if not chunk:
                break
            sha.update(chunk)

    return sha.hexdigest()

ledger_hash = sha256_file("ledger.json")

with open("ledger.sha256", "r") as f:
    expected_hash = f.read().strip()

print("Calculated:", ledger_hash)
print("Expected :", expected_hash)

if ledger_hash == expected_hash:
    print("✓ VERIFIED: integrity preserved")
else:
    print("✗ FAILED: file modified")
