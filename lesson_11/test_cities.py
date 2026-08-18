from city_functions import get_formatted_city_country

def test_city_country(): 
    """Do cities and countries like 'santiago' and 'chile' work?"""
    formatted_city_country = get_formatted_city_country(
        'santiago', 'chile')

    assert formatted_city_country == 'Santiago, Chile'

def test_city_country_population(): 
    """Do cities, countries, and population like 'santiago', 'chile', and '10,000' work?"""
    formatted_city_country_pop = get_formatted_city_country(
        'santiago', 'chile', '10,000')

    assert formatted_city_country_pop == 'Santiago, Chile - Population 10,000.'
