# -*- coding: utf-8 -*-
import scrapy
import re
from unidecode import unidecode

class ToScrapeSpider(scrapy.Spider):
    name = 'players'
    start_urls = [
        'https://www.basketball-reference.com/leagues/NBA_2022_per_game.html',
        'https://www.basketball-reference.com/leagues/NBA_2021_per_game.html',
        'https://www.basketball-reference.com/leagues/NBA_2020_per_game.html',
        'https://www.basketball-reference.com/leagues/NBA_2019_per_game.html',
        'https://www.basketball-reference.com/leagues/NBA_2018_per_game.html',
        'https://www.basketball-reference.com/leagues/NBA_2017_per_game.html',
        'https://www.basketball-reference.com/leagues/NBA_2016_per_game.html',
        'https://www.basketball-reference.com/leagues/NBA_2015_per_game.html',
    ]

    def parse(self, response):
        year = re.findall(r"(?<=NBA_).{4}", str(response))[0]
        for row in response.css("tr"):
            if row.css('td[data-stat="player"] a::text'):
                yield{
                    "name": unidecode(row.css('td[data-stat="player"] a::text').get()).replace("'",""),
                    "year": year,
                    "team": row.css('td[data-stat="team_id"] a::text').get() if row.css('td[data-stat="team_id"] a::text') else row.css('td[data-stat="team_id"]::text').get(),
                    "position": row.css('td[data-stat="pos"]::text').get(),
                    "age": row.css('td[data-stat="age"]::text').get(),
                    "games played": row.css('td[data-stat="g"]::text').get(),
                    "games started": row.css('td[data-stat="gs"]::text').get(),
                    "minutes played per game": row.css('td[data-stat="mp_per_g"]::text').get(),
                    "field goals per game": row.css('td[data-stat="fg_per_g"]::text').get(),
                    "field goals attempted per game": row.css('td[data-stat="fga_per_g"]::text').get(),
                    "field goals percentage": row.css('td[data-stat="fg_pct"]::text').get(),
                    "3-point field goal per game": row.css('td[data-stat="fg3_per_g"]::text').get(),
                    "3-point field goal attempted per game": row.css('td[data-stat="fg3a_per_g"]::text').get(),
                    "3-point field goal percentage": row.css('td[data-stat="fg3_pct"]::text').get(),
                    "2-point field goal per game": row.css('td[data-stat="fg2_per_g"]::text').get(),
                    "2-point field goal attempted per game": row.css('td[data-stat="fg2a_per_g"]::text').get(),
                    "2-point field goal percentage": row.css('td[data-stat="fg2_pct"]::text').get(),
                    "Effective field goal percentage": row.css('td[data-stat="efg_pct"]::text').get(),
                    "Free throws Per Game": row.css('td[data-stat="ft_per_g"]::text').get(),
                    "Free throws percentage": row.css('td[data-stat="ft_pct"]::text').get(),
                    "Offensive rebounds per game": row.css('td[data-stat="orb_per_g"]::text').get(),
                    "Defensive rebounds per game": row.css('td[data-stat="drb_per_g"]::text').get(),
                    "Total rebounds per game": row.css('td[data-stt="trb_per_g"]::text').get(),
                    "Assists per game": row.css('td[data-stat="ast_per_g"]::text').get(),
                    "Steals per game": row.css('td[data-stat="stl_per_g"]::text').get(),
                    "Blocks per game": row.css('td[data-stat="blk_per_g"]::text').get(),
                    "Turnovers per game": row.css('td[data-stat="tov_per_g"]::text').get(),
                    "Personal fouls per game": row.css('td[data-stat="pf_per_g"]::text').get(),
                    "Points per game": row.css('td[data-stat="pts_per_g"]::text').get()
                }

class ExampleSpider(scrapy.Spider):
    name = 'salaries'
    allowed_domains = ['www.espn.com']
    """ start_urls = ['http://www.espn.com/'] """
    start_urls = ['http://www.espn.com/nba/salaries/_/year/2022',
                  'http://www.espn.com/nba/salaries/_/year/2021',
                  'http://www.espn.com/nba/salaries/_/year/2020',
                  'http://www.espn.com/nba/salaries/_/year/2019',
                  'http://www.espn.com/nba/salaries/_/year/2018',
                  'http://www.espn.com/nba/salaries/_/year/2017',
                  'http://www.espn.com/nba/salaries/_/year/2016',
                  'http://www.espn.com/nba/salaries/_/year/2015']
    def parse(self, response):
        pagination_links = response.xpath("//div[@class='jcarousel-next']/../@href")
        year = re.findall(r"(?<=year/).{4}", str(response))[0]
        yield from response.follow_all(pagination_links, self.parse)
        for row in response.css("table tr.oddrow") + response.css("table tr.evenrow"):
            yield {
                "name": row.css("td a::text")[0].get().replace("'",""),
                "salary": row.css("td::text")[-1].get(),
                "year": year
            }