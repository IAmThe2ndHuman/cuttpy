# Cuttpy

Wrapper for the [Cuttly](https://cutt.ly/) URL shortener API.

## Installation

`pip install cuttpy` or `python -m pip install cuttpy`

**Make sure to generate an API key by signing up at [cutt.ly](https://cutt.ly/register) and
by going to the edit account page, https://cutt.ly/edit.**

## Documentation

This README **is** the documentation :smile:

## Examples

Basic shortener
```python
from cuttpy import Cuttpy

# define shortener
shortener = Cuttpy("YOUR API KEY")

# shorten URL
response = shortener.shorten("https://www.google.com")

# print shortened url
print(response.shortened_url)
```
Shortener with basic error handling
```python
from cuttpy import Cuttpy

# define shortener
shortener = Cuttpy("YOUR API KEY")

# shorten URL
response = shortener.shorten("https://www.google.com")

try:
    # print shortened url
    print(response.shortened_url)
# handle AttributeError because the attribute shortened_url does not return if there was an issue shortening the URL
except AttributeError:
    print("An error occurred.")
```
Shortener with advanced error handling
```python
from cuttpy import Cuttpy

# define shortener
shortener = Cuttpy("YOUR API KEY")

# shorten URL
response = shortener.shorten("https://www.google.com")

# check response code and act accordingly
# you can learn what codes there are later in the README
if response.code == 0:
    # a response code of 0 means there was a serverside error. 
    # it is a good idea to also print the http code in this case.
    # print the builtin description for the error
    print(f"{response.description}\n{response.http}")
elif not response.code == 7:
    # print the builtin description for the error
    print(response.description)
elif response.code == 7:
    # a response code of 7 means there was no error.
    # print shortened url
    print(response.shortened_url)
```

# Classes

## `Cuttpy()`
The only class worth your time in this library.

***Methods:***

`shorten(url)` - Returns a `CuttpyResponse()` object with everything you need.

## `CuttpyResponse()`
The return type of method `Cuttpy().shorten()` with various attributes.

***Attributes:***

**Attributes that always return**

These attributes always return even if the API fails. 

| Name | Description                                                  |
|------|--------------------------------------------------------------|
| http | The HTTP status code returned by the API.                    |
| code | The code that the wrapper returns. View what they mean below.|
| description | A hardcoded description for each wrapper code. View what they mean below.|

```
Wrapper Codes and descriptions


0 - Unknown serverside error

1 - URL has already been shortened

2 - Entered URL is not a URL

3 - Preferred URL name is already taken

4 - Invalid API key.

5 - URL did not pass the validation. Includes invalid characters

6 - URL provided is from a blocked domain

7 - URL has been shortened successfully
```

**Attributes that return only if the URL was shortened.**

Title speaks for itself. 

| Name          | Description                                      |
|---------------|--------------------------------------------------|
| original_url  | The original URL which was shortened by the API. |
| shortened_url | The shortened version of the original URL.       |

# Exceptions
This API wrapper uses a system of error codes. View what they mean in the attributes section of the `CuttpyResponse()` class.