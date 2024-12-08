class BandNameGenerator:

        def __init__(self):
            print('Welcome to the Band Name Generator.')

        def name_generation(self):
            city_name = input('What\'s the name of the city you grew up in?\n')
            pet_name = input('What\'s your pet\'s name?\n')
            return f'Your band name could be {city_name} {pet_name}'


def main():
    band_name_generator = BandNameGenerator()
    print(band_name_generator.name_generation())

if __name__ == '__main__':
    main()