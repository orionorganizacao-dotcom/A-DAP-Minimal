# A-DAP-Minimal

Minimal executable implementation of A-DAP principles.

## Objective

Demonstrate independent preservation and verification of decisions before outcomes become observable.

## Components

1. Decision Record
2. SHA-256 Integrity Hash
3. Verification Script
4. Reconstruction Evidence

## Minimal Flow

Decision
↓
Hash generation
↓
Ledger registration
↓
Independent verification
↓
Reconstruction

## Files

- example_decision.json
- ledger.json
- ledger.sha256
- verify_adap.py

## Scope

This implementation demonstrates verifiability only.

It does not:

- prove correctness
- guarantee truth
- create institutional accountability
