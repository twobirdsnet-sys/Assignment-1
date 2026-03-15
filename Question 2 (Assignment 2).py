# Custom Exception
class IncompleteDataError(Exception):
    """Raised when the ledger contains incomplete data (empty line)."""
    pass


# Generator Function
def read_ledger(lines):
    """
    Generator that yields ledger lines.
    Raises IncompleteDataError if an empty line is encountered.
    """
    for line in lines:
        if line.strip() == "":
            raise IncompleteDataError("Empty line detected in ledger.")
        yield line


# Example Ledger Data (simulating a large ledger file)
ledger_data = [
    "2024-01-01,Deposit,500",
    "2024-01-02,Withdrawal,200",
    "",  # Incomplete data
    "2024-01-03,Deposit,1000"
]


# Calling Code
ledger_generator = read_ledger(ledger_data)

while True:
    try:
        record = next(ledger_generator)
        print("Processing record:", record)

    except IncompleteDataError as error:
        print("Error:", error)
        print("Stopping processing due to incomplete data.")
        break  # safely exit the loop

    except StopIteration:
        print("Finished processing ledger.")
        break