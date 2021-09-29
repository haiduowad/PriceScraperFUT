from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
import json
import time
from datetime import datetime

# Adding all players names to an array
playerNameArray = []
playerNameArray.append("georginioWijnaldum")
playerNameArray.append("lionelMessi")
playerNameArray.append("raphaelVarane")
playerNameArray.append("denisZakaria")
playerNameArray.append("denisZakariaIF")
playerNameArray.append("kevinMbabu")
playerNameArray.append("maxenceLacriox")
playerNameArray.append("jesusNavasIF")
playerNameArray.append("nicoloBarellaIF")
playerNameArray.append("felipeAndersonIF")
playerNameArray.append("manuelAkanji")

# Adding all players URLs to an array
playerUrlArray = []
playerUrlArray.append("https://www.futbin.com/22/playerPrices?player=181291&rids=50512939")
playerUrlArray.append("https://www.futbin.com/22/playerPrices?player=158023&rids=50489671")
playerUrlArray.append("https://www.futbin.com/22/playerPrices?player=201535&rids=")
playerUrlArray.append("https://www.futbin.com/22/playerPrices?player=229261&rids=50560909")
playerUrlArray.append("https://www.futbin.com/22/playerPrices?player=50560909&rids=229261")
playerUrlArray.append("https://www.futbin.com/22/playerPrices?player=210625&rids=")
playerUrlArray.append("https://www.futbin.com/22/playerPrices?player=244067&rids=")
playerUrlArray.append("https://www.futbin.com/22/playerPrices?player=50478184&rids=146536")
playerUrlArray.append("https://www.futbin.com/22/playerPrices?player=50555880&rids=224232")
playerUrlArray.append("https://www.futbin.com/22/playerPrices?player=50533643&rids=201995")
playerUrlArray.append("https://www.futbin.com/22/playerPrices?player=229237&rids=")

# Arrays to store the player prices
georginioWijnaldumPrices    = []
lionelMessiPrices           = []
raphaelVaranePrices         = []
denisZakariaPrices          = []
denisZakariaIFPrices        = []
kevinMbabuPrices            = []
maxenceLacrioxPrices        = []
jesusNavasIFPrices          = []
nicoloBarellaIFPrices       = []
felipeAndersonIFPrices      = []
manuelAkanjiPrices          = []

# Adding all players price arrays to an array to pass to main function
playerPriceArray = []
playerPriceArray.append(georginioWijnaldumPrices)
playerPriceArray.append(lionelMessiPrices)
playerPriceArray.append(raphaelVaranePrices)
playerPriceArray.append(denisZakariaPrices)
playerPriceArray.append(denisZakariaIFPrices)
playerPriceArray.append(kevinMbabuPrices)
playerPriceArray.append(maxenceLacrioxPrices)
playerPriceArray.append(jesusNavasIFPrices)
playerPriceArray.append(nicoloBarellaIFPrices)
playerPriceArray.append(felipeAndersonIFPrices)
playerPriceArray.append(manuelAkanjiPrices)

# Function that takes in the player URL page and returns the player's cheapest price
# Input:    String of player price URL page
# Output:   String of lowest player price
def getPlayerPrice(playerUrlPage):
    # Opening the URLs, downloading the HTML pages, and closing the connection
    uClient = Request(playerUrlPage, headers={'User-Agent': 'Mozilla/5.0'})
    pageHtml = urlopen(uClient).read()
    pageSoup = soup(pageHtml, "html.parser")
    jsonPage=json.loads(pageSoup.text)

    keyValues = list(jsonPage.keys())
    return jsonPage[keyValues[0]]["prices"]["ps"]["LCPrice"]

def arrayFiller(value, playerName):
    playerName.append(value)

def textFileCreator(priceArray, playerName):
    playerName = playerName+".txt"
    with open(playerName, "w") as txt_file:
        for line in priceArray:
            txt_file.write(line + "\n")

def main():
    timeout = time.time() + 60 * 10
    while not (time.time() > timeout):
        for i in range(len(playerUrlArray)):
            value = getPlayerPrice(playerUrlArray[i]).replace(" ", "")+"  "+ datetime.now().strftime("%H:%M:%S")
            arrayFiller(value, playerPriceArray[i])
        time.sleep(5)

    for i in range(len(playerNameArray)):
        textFileCreator(playerPriceArray[i], playerNameArray[i])

    return

if __name__ == '__main__':
    main()