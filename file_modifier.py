# Python program to read a file, modify its content (e.g., convert to uppercase),
# and write the modified version to a new file. It asks the user for a filename
# and handles errors if the file doesn't exist or can't be read.

def main():
    try:
        # Ask user for the input filename
        input_filename = input("Enter the filename to read: ").strip()
        
        # Open and read the file
        with open(input_filename, 'r') as input_file:
            content = input_file.read()
        
        # Modify the content (example: convert to uppercase)
        modified_content = content.upper()
        
        # Create output filename
        output_filename = f"modified_{input_filename}"
        
        # Write the modified content to the new file
        with open(output_filename, 'w') as output_file:
            output_file.write(modified_content)
        
        print(f"File successfully read and modified. Output written to: {output_filename}")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    
    except PermissionError:
        print(f"Error: Permission denied when trying to read '{input_filename}'.")
    
    except IOError as e:
        print(f"Error: An I/O error occurred while reading the file: {e}")
    
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()