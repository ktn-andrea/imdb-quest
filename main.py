from scraper import ImdbScraper


def main():

    Imdb_scraper = ImdbScraper()
    uri_top_250 = "https://www.imdb.com/chart/top/"
    Imdb_Top_20 = Imdb_scraper.get_top_20(uri_top_250)

    for i in Imdb_Top_20:
        print(i.title)
        print(i.num_of_oscar_wins)
        print(i.rating)
        print(i.num_of_ratings)
    

main()