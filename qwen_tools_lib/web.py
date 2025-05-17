import os
import requests
import json

def brave_web_search(query, count=10):
    """
    Search the web using Brave Search API.
    
    Args:
        query (str): The search query.
        count (int, optional): The number of results to return. Defaults to 10.
        
    Returns:
        dict: A dictionary containing the search results or an error message.
    """
    try:
        # Get API key from environment variables
        api_key = os.environ.get('BRAVE_API_KEY')
        if not api_key:
            return {"error": "BRAVE_API_KEY environment variable not found"}
        
        # Prepare the API request
        url = "https://api.search.brave.com/res/v1/web/search"
        headers = {
            "Accept": "application/json",
            "Accept-Encoding": "gzip",
            "X-Subscription-Token": api_key
        }
        params = {
            "q": query,
            "count": count
        }
        
        # Make the API request
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        # Return the JSON response
        return response.json()
    
    except requests.exceptions.RequestException as e:
        return {"error": f"API request failed: {str(e)}"}
    except json.JSONDecodeError:
        return {"error": "Failed to decode JSON response"}
    except Exception as e:
        return {"error": f"An unexpected error occurred: {str(e)}"}


def fetch_web_page(url, headers=None, timeout=30, clean=True):
    """
    Fetch content from a specified URL and extract the main content.
    
    Args:
        url (str): The URL to fetch content from.
        headers (dict, optional): Custom headers to include in the request. Defaults to None.
        timeout (int, optional): Request timeout in seconds. Defaults to 30.
        clean (bool, optional): Whether to clean and extract main content. Defaults to True.
        
    Returns:
        str or dict: The cleaned web page content as text, or a dictionary with an error message if the request fails.
    """
    try:
        # Set default headers if none provided
        if headers is None:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
            }
        
        # Make the request
        response = requests.get(url, headers=headers, timeout=timeout)
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        if not clean:
            return response.text
        
        # Clean and extract main content using BeautifulSoup
        try:
            from bs4 import BeautifulSoup
            import re

            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Remove script, style, and other non-content elements
            for element in soup(["script", "style", "header", "footer", "nav", "aside", "form", "iframe", "noscript"]):
                element.decompose()
                
            # Remove elements likely to be ads, banners, etc.
            for element in soup.find_all(class_=re.compile('(ad|banner|menu|sidebar|footer|header|nav|comment|popup|cookie)', re.IGNORECASE)):
                element.decompose()
                
            
            clean_text = soup.get_text(separator=' ', strip=True)
                
            # Clean up extra whitespace
            clean_text = re.sub(r'\s+', ' ', clean_text).strip()
            
            return clean_text
            
        except ImportError:
            # If BeautifulSoup is not available, return the raw text
            return {"error": "BeautifulSoup is required for content cleaning but not installed. Install with: pip install beautifulsoup4"}
            
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}
    except Exception as e:
        return {"error": f"An unexpected error occurred: {str(e)}"}