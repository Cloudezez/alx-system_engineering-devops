Reddit API Project
Overview
This project consists of several Python scripts that interact with the Reddit API to retrieve information about various subreddits. The tasks involve querying the Reddit API to get subscriber counts, fetching hot posts, and recursively gathering all hot article titles for a given subreddit.

Requirements
Operating System: Ubuntu 20.04 LTS
Python Version: Python 3.4.3 or higher
Editor: Files should be created using vi, vim, or emacs.
PEP 8: All code should adhere to the PEP 8 style guide.
Executable Files: All Python scripts must be executable.
Project Structure
Files
0-subs.py: Contains the function number_of_subscribers(subreddit) which returns the number of subscribers for a given subreddit.
1-top_ten.py: Contains the function top_ten(subreddit) which prints the titles of the first 10 hot posts for a given subreddit.
2-recurse.py: Contains the function recurse(subreddit, hot_list=[]) which recursively returns a list of titles for all hot articles in a given subreddit.
0-main.py, 1-main.py, 2-main.py: Test files to demonstrate the usage of the above functions.
Usage
Clone the Repository:

bash
Copy code
git clone https://github.com/cloudezez/alx-system_engineering-devops.git
cd alx-system_engineering-devops/0x16-api_advanced
Make Files Executable:

bash
Copy code
chmod +x 0-subs.py 1-top_ten.py 2-recurse.py
Run Test Files:
To test each script, you can use the provided main.py files:

Functions
0-subs.py
Function: number_of_subscribers(subreddit)
Description: Queries the Reddit API and returns the total number of subscribers for a given subreddit. If the subreddit is invalid, it returns 0.
1-top_ten.py
Function: top_ten(subreddit)
Description: Queries the Reddit API and prints the titles of the first 10 hot posts for a given subreddit. If the subreddit is invalid, it prints None.
2-recurse.py
Function: recurse(subreddit, hot_list=[])
Description: Recursively queries the Reddit API to return a list of titles for all hot articles in a given subreddit. If the subreddit is invalid, it returns None.
Error Handling
All scripts are designed to handle invalid subreddits by checking for HTTP status codes.
Scripts do not follow redirects to avoid retrieving incorrect data.
Coding Standards
PEP 8 Compliance: All Python code follows the PEP 8 style guide.
Module Documentation: Each module is documented and can be checked using python3 -c 'print(__import__("module_name").__doc__)'.
Libraries: All imported libraries are listed in alphabetical order.
Known Issues
Be mindful of Reddit’s rate limits when making multiple requests in a short period.
Ensure your User-Agent is unique to avoid Too Many Requests errors.
Future Improvements
Implement caching to reduce the number of API calls.
Add support for other types of Reddit content (e.g., new posts, top posts).
Author








