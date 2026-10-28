#Safe File Processor with Custom Exception Hierarchy

class FileProcessingError(Exception):
    pass


class InvalidFileFormatError(FileProcessingError):
    pass


def process_file(filename):
    file = None

    try:
        file = open(filename, "r")

        if not filename.endswith(".txt"):
            raise InvalidFileFormatError(
                "Invalid file format! Only .txt files are allowed."
            )

        content = file.read()

    except FileNotFoundError:
        print("Error: File not found.")

    except PermissionError:
        print("Error: Permission denied.")

    except InvalidFileFormatError as e:
        print("Error:", e)

    except Exception as e:
        print("Unexpected error:", e)

    else:
        print("\nFile processed successfully!")
        print("File content:")
        print(content)

    finally:
        if file is not None:
            file.close()
            print("\nFile closed safely.")


filename = input("Enter file name: ")
process_file(filename)
