import socket

def whois_lookup(domain: str):
    """
    Perform a WHOIS lookup for the specified domain.

    Parameters:
    domain (str): The domain for which to perform the WHOIS lookup.

    Returns:
    str: The WHOIS information for the specified domain.

    Raises:
    Exception: If there is an error during the WHOIS lookup.

    Example:
    Case 1: Valid Domain
    Enter a domain: (google.com)
    WHOIS information for google.com:
    [WHOIS response here]

    Case 2: Invalid Domain
    Enter a domain: (f4ked0main.com)
    WHOIS information for f4ke_d0main.com:
    Error: Invalid query f4ke_d0main.com
    """

    # Create a socket for the WHOIS lookup. Socket uses IPv4 (AF_INET) and TCP (SOCK_STREAM)
    whois_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to the WHOIS server via port 43 
        whois_socket.connect(("whois.iana.org", 43))

        # Send the WHOIS query for the specified domain and encode it
        whois_socket.send(f"{domain}\r\n".encode())

        # Receive and decode the WHOIS response
        response = whois_socket.recv(4096).decode()

        return response

    except Exception as e:
        #Error Handling for invalid queries
        print(f"Error: {e}")

    finally:
        # Close the socket connection after done with query
        whois_socket.close()

def main():
    input_domain = input("Enter a domain: ")
    print(whois_lookup(input_domain))

if __name__ == "__main__":
    main()
