import requests
from bs4 import BeautifulSoup

class OPGG:
    BASE_URL = "https://www.op.gg/summoners"

    def __init__(self, region, summoner_name):
        self.region = region
        self.summoner_name = summoner_name
        self.soup = None

    def get_summoner_page(self):
        url = f"{self.BASE_URL}/{self.region}/{self.summoner_name}"
        response = requests.get(url)

        if response.status_code == 200:
            self.soup = BeautifulSoup(response.text, 'html.parser')
        else:
            print(f"Failed to retrieve the webpage: {response.status_code}")
            self.soup = None

    def get_most_played_champions(self):
        if self.soup is None:
            print("Soup is not initialized, call get_summoner_page() first.")
            return

        champions_data = []
        most_played_champions = self.soup.find_all("div", class_="champion-box")

        for champion in most_played_champions:
            name = champion.find("div", class_="name").text.strip()
            played_div = champion.find("div", class_="played")
            total_games = played_div.find("div", class_="count").text.strip()
            winrate = played_div.find("div", class_="").text.strip()
            kda = champion.find("div", class_="detail").text.strip()

            champions_data.append({
                'name': name,
                'total_games': total_games,
                'winrate': winrate,
                'kda': kda
            })

        return champions_data

    def print_most_played_champions(self):
        champions_data = self.get_most_played_champions()
        if champions_data:
            for data in champions_data:
                print(f"{data['name']} {data['total_games']} {data['winrate']} {data['kda']}")
        else:
            print("No champion data found.")

# Usage
if __name__ == "__main__":
    region = "euw"
    summoner_name = "ClockBomb-lol"

    opgg = OPGG(region, summoner_name)
    opgg.get_summoner_page()

    opgg.print_most_played_champions()


   
