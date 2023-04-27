import requests, bs4
import os, uuid

def getHtml(url):
    response = requests.get(url)
    response.raise_for_status()
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    return soup

def downloadImage(htmlContent, directoryToSave):
    imageElement = htmlContent.select('#comic img')
    imageUrl = 'https:' + imageElement[0].get('src')

    print('Downloading %s' % imageUrl)

    imageResponse = requests.get(imageUrl)
    imageResponse.raise_for_status()

    imageFile = open(os.path.join(directoryToSave,  os.path.basename(imageUrl)), 'wb')
    for chunk in imageResponse.iter_content(100000):
        imageFile.write(chunk)

    imageFile.close()


seacrhSiteBaseUrl = 'https://xkcd.com'
maxQuantityRecentResult = 5

print('Searching...')

downloadedImagesPath = 'downloaded_images%s' % uuid.uuid4()
os.makedirs(downloadedImagesPath)

htmlContent = getHtml(seacrhSiteBaseUrl)
downloadImage(htmlContent, downloadedImagesPath)

for i in range(maxQuantityRecentResult - 1):
    previousLink = htmlContent.select('a[rel="prev"]')[0]
    previousPageUrl = seacrhSiteBaseUrl + previousLink.get('href')
    htmlContent = getHtml(previousPageUrl)

    downloadImage(htmlContent, downloadedImagesPath)

print('Files downloaded to folder: %s' % downloadedImagesPath)