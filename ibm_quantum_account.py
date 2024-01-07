from qiskit_ibm_provider import IBMProvider

# https://quantum.ibm.com/account -> copy API token
# Save your credentials on disk.
IBMProvider.save_account(token='<IBM Quantum API token>', overwrite=True)

provider = IBMProvider(instance='ibm-q/open/main')