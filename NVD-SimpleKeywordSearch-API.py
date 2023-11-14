import requests
import json
import os

def prettifyJSON(outResponse):
    try:
        parsedJSON = json.loads(outResponse)
        prettifiedJSON = json.dumps(parsedJSON, indent=4, sort_keys=True)
        return prettifiedJSON
    except ValueError as ValErr:
        return "Invalid JSON: " + str(ValErr)

Example: ('Keyword: "Microsoft Onedrive"\n Results: "20"\n Starting: "1"\n CVSS2: "LOW/MEDIUM/HIGH"\n CVSS3: "LOW/MEDIUM/HIGH/CRITICAL"\n')
inputKeywords = input("Enter the Keyword: ")
inputResultsPerPage = input("Enter Number of Results: ")
inputStartingPage = input("Enter Starting Page: ")
# inputSeverityCVSS2 = input("Enter Severity V2: ")
inputSeverityCVSS3 = input("Enter Severity V3: ")

API_KEY = os.environ.get('API_KEY')

# searchedKeywordResult = str(inputKeywords)
url = f"https://services.nvd.nist.gov/rest/json/cves/1.0?keywordSearch={inputKeywords}&resultsPerPage={inputResultsPerPage}&startIndex={inputStartingPage}&cvssV3Severity={inputSeverityCVSS3}"
payload = {}
headers = {
    'apiKey': API_KEY
}
response = requests.get(url, headers=headers)  # Use get() to retrieve the response text
JSONResponse = response.json()
textResponse = response.text
# print(response) # Response Status
# print(JSONResponse) # Response in JSON
# print(textResponse) # Response in Text
# print(prettifyJSON(str(JSONResponse))) # Response in JSON Prettified
print(prettifyJSON(textResponse)) # Response in Text Prettified

# Save the response to a text file
with open("response.txt", "w") as file:
    file.write(prettifyJSON(textResponse))

print("Response saved to 'response.txt'")