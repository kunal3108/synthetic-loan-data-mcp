from datetime import datetime, timedelta

def excel_serial_to_iso(serial_number: float) -> str:
    """
    Convert Excel serial date number to ISO 8601 format
    Excel epoch starts at 1899-12-30.
    """
    base_date = datetime(1899, 12, 30)
    delta = timedelta(days=serial_number)
    return (base_date + delta).isoformat()

# Example usage
if __name__ == "__main__":
    print(excel_serial_to_iso(45828.5724874078))  # → 2025-07-14T13:44:23
