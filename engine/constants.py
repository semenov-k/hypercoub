import enum


class CoubCategories(enum.Enum):

    ALL = ''
    ANIMALS = 'animals-pets'
    MASHUP = 'mashup'
    ANIME = 'anime'
    MOVIES = 'movies'
    GAMING = 'gaming'
    CARTOONS = 'cartoons'
    ART = 'art'
    MUSIC = 'music'
    NEWS = 'news'
    SPORTS = 'sports'
    SCIENCE = 'science-technology'
    CELEBRITY = 'celebrity'
    NATURE = 'nature-travel'
    FASHION = 'fashion'
    DANCE = 'dance'
    CARS = 'cars'
    ADULT = 'nsfw'


class Periods(enum.Enum):

    DAILY = 'daily'
    WEEKLY = 'weekly'
    MONTHLY = 'monthly'
    QUARTER = 'quarter'
    HALF = 'half'
