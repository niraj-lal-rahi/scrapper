# import requests
# api_key = "364d902ab388957"
# payload = {'apikey':api_key , "OCREngine": 2}
# f_path = "screenshot.png"
# with open(f_path, 'rb') as f:
#     j = requests.post('https://api.ocr.space/parse/image', files={f_path: f}, data=payload).json()
#     if j['ParsedResults']:
#         print(j['ParsedResults'][0]['ParsedText'])


# print("end")

# import requests

# api_key = "364d902ab388957"
# img_url = "https://i.stack.imgur.com/022oK.jpg"
# url = f"https://api.ocr.space/parse/imageurl?apikey={api_key}&url={img_url}&OCREngine=2"

# j = requests.get(url).json()
# if j['ParsedResults']:
#     print(j['ParsedResults'][0]['ParsedText'])


from bs4 import BeautifulSoup
import requests

# lists
urls=[]

# function created
def scrape(site):

    # getting the request from url
    r = requests.get(site)

    # converting the text
    s = BeautifulSoup(r.text,"html.parser")

    for i in s.find_all("a"):

        href = i.attrs['href']

        if href.startswith("/"):
            site = site+href

            if site not in  urls:
                urls.append(site)
                print(site)
                # calling it self
                scrape(site)

# main function
if __name__ =="__main__":

    # website to be scrape
    site="http://example.webscraping.com//"

    # calling function
    scrape(site)
