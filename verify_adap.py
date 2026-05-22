import hashlib
import json


def sha256_file(filename):
    sha = hashlib.sha256()

    with open(filename, "rb") as f:
        while True:
            chunk = f.read(4096)

            if not chunk:
                break

            sha.update(chunk)

    return sha.hexdigest()


# -------- STEP 1 --------
# Generate decision hash

decision_hash = sha256_file("example_decision.json")

print("\nDecision Hash:")
print(decision_hash)


# -------- STEP 2 --------
# Read ledger

with open("ledger.json", "r") as f:
    ledger = json.load(f)

stored_hash = ledger[0]["decision_hash"]

print("\nStored Hash:")
print(stored_hash)


# -------- STEP 3 --------
# Verify decision integrity

if stored_hash == "AUTO_GENERATED":
    print("\n⚠ Decision hash not yet committed")

elif decision_hash == stored_hash:
    print("\n✓ Decision VERIFIED")

else:
    print("\n✗ Decision FAILED")


# -------- STEP 4 --------
# Verify ledger integrity

with open("ledger.sha256", "r") as f:
    expected = f.read().strip()

calculated = sha256_file("ledger.json")

print("\nLedger Hash:")
print(calculated)

print("\nExpected:")
print(expected)

if calculated == expected:
    print("\n✓ Ledger VERIFIED")

else:
    print("\n✗ Ledger FAILED")


# -------- STEP 5 --------
# Tamper detection

tampered = sha256_file("tampered_ledger.json")

print("\nTampered Ledger:")
print(tampered)

if tampered == expected:
    print("\n✗ Tamper NOT detected")

else:
    print("\n✓ Tamper detected")
