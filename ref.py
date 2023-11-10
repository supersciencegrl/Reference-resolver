import urllib.parse

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
    pyperclip.copy(result)
    
    return result

# Test the function
# input_string = "OL 2015, 17, 5728"
result_url = generate_search_url(input_string)
print(result_url)
