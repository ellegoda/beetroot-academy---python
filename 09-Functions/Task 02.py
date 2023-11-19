country_dict = {}


def make_country(name, capital):
    country_dict["Country"] = name
    country_dict["Capital city"] = capital

country_name = input("Enter the country name : ")
capital_city = input("Enter the capital city name : ")

make_country(country_name, capital_city)
print(country_dict)
