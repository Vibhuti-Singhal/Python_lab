
import traceback
# Custom exception classes
class InvalidFileFormatError(Exception):
    pass


class FileParsingError(Exception):
    pass


def parse_file(filename):
    file = None

    try:
        # Open the file
        file = open(filename, "r")

        print("File opened successfully.")

        # Read file contents
        data = file.readlines()

        if not data:
            raise InvalidFileFormatError("File is empty.")

        records = []

        # Parse each line
        for line_number, line in enumerate(data, start=1):
            parts = line.strip().split(",")

            if len(parts) != 3:
                raise InvalidFileFormatError(
                    f"Invalid format at line {line_number}."
                )

            records.append(parts)

    except FileNotFoundError:
        print("Error: File not found.")

    except InvalidFileFormatError as error:
        print("Format Error:", error)
        traceback.print_exc()

    except Exception as error:
        print("Unexpected Error:", error)
        traceback.print_exc()

        raise FileParsingError("File parsing failed.") from error

    else:
        # Executes only when no exception occurs
        print("\nFile parsed successfully.")
        print("Parsed Records:")

        for record in records:
            print(record)

    finally:
        # Safely close the file
        if file is not None and not file.closed:
            file.close()
            print("\nFile closed successfully.")

        print("File parsing process completed.")


# Program execution
filename = input("Enter file name: ")
parse_file(filename)
