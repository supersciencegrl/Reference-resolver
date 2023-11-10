import urllib.parse
import sys

import pyperclip

def generate_search_url(input_string):
    """
    Generate a URL for chemical search based on the input.

    The input should be a string containing chemical codes separated by commas.

    Parameters:
        input_string (str): A string containing chemical codes separated by commas.

    Returns:
        str: The generated URL with URL-encoded parameters. The URL is also copied
            to the clipboard. 

    Example:
        >>> generate_search_url("OL 2015, 17, 5728")
        'https://chemsearch.kovsky.net/index.php?q=OL%202015,%2017,%205728'
    """
    base_url = "https://chemsearch.kovsky.net/index.php?q="
    encoded_reference = urllib.parse.quote(input_string)
    result = f"{base_url}{encoded_reference}"
    
    return result

def run(input_string = "OL 2015, 17, 5728"):
    """
    Runs the Kovsky reference resolver script.

    If no kwarg or CLI arg is provided, a default test reference string is used.
    Otherwise, the provided reference string is used.

    Prints the generated search URL and copies it to the clipboard, unless '-nopaste' is in the command-line arguments.
    """
    if len(sys.argv) > 1:
        input_string = sys.argv[1]

    # Generate the result url
    result_url = generate_search_url(input_string)
    print(result_url)

    # Copy the result url to clipboard
    if '-nopaste' not in sys.argv:
        pyperclip.copy(result_url)

if __name__ == '__main__':
    run()
