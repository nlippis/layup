import random

def team_name_generator():
    """
    Generates random team name by randomly chosing
    a adjective, verb and noun from three seperate
    lists, making ~one million possible names
    """
    adjs = ['tall', 'skinny', 'fat', 'old', 'young',
            'short', 'lively', 'youthful', 'boisterous',
            'red', 'orange', 'yellow', 'green', 'blue',
            'purple', 'gray', 'black', 'white', 'long',
            'magnificent', 'plain', 'fancy', 'old-fashioned',
            'clever', 'gifted', 'odd', 'rich', 'shy', 'tender',
            'angry', 'clumsy', 'fierce', 'grumpy', 'helpless',
            'itchy', 'lazy', 'mysterious', 'nervous', 'repulsive',
            'scary', 'worried', 'uptight', 'brave', 'calm', 'eager',
            'faithful', 'gentle', 'happy', 'jolly', 'kind', 'proud',
            'silly', 'victorious', 'witty', 'zealous', 'chubby', 
            'deep', 'flat', 'high', 'hollow', 'narrow', 'shallow',
            'steep', 'wide', 'great', 'immense', 'little', 
            'mammoth', 'massive', 'petite', 'puny', 'scrawny',
            'teeny', 'hissing', 'loud', 'melodic', 'noisy', 'quiet',
            'screeching', 'thundering', 'whispering', 'ancient',
            'fast', 'modern', 'rapid', 'bitter', 'delicious',
            'fresh', 'greasy', 'juicy', 'hot', 'icy', 'loose',
            'prickly', 'rotten', 'weak', 'wet', 'boiling',
            'bumpy', 'chilly', 'creepy', 'curly', 'dirty', 'hot',
            'wet', 'empty', 'heavy', 'freezing', 'woozy'
        ]

    verbs = ['abandoning', 'biting', 'blabbing', 'blaring', 'berthing',
            'telling', 'speaking', 'walking', 'running', 'faking', 
            'pulling', 'pushing', 'bluffing', 'lying', 'working',
            'relaxing', 'dreaming', 'sitting', 'standing', 'beating',
            'playing', 'jogging', 'dancing', 'swimming', 'driving', 
            'riding', 'cycling', 'hopping', 'drinking', 'eating', 
            'shaking', 'raking', 'piling', 'piercing', 'penetrating',
            'squeezing', 'mashing', 'rolling', 'spinning', 'wearing',
            'removing', 'adding', 'distributing', 'begging', 'gifting',
            'praying', 'cursing', 'laughing', 'crying', 'smiling',
            'texting', 'typing', 'printing', 'calling', 'receiving',
            'ignoring', 'opening', 'closing', 'gardening', 'watering',
            'planting', 'cooking', 'strolling', 'chatting', 'connecting',
            'showing', 'revealing' 'seeing', 'proposing', 'rejecting',
            'worrying', 'going', 'coming', 'swinging', 'recalling',
            'dialing', 'fighting', 'flying', 'jubilating', 'hunting',
            'feinting', 'dancing', 'building', 'learning', 'meditating',
            'moving', 'swallowing', 'kicking', 'chilling', 'dropping',
            'celebrating', 'climbing', 'stomping', 'floating', 'laying',
            'sleeping', 'daydreaming', 'studying', 'judging', 'boring',
            'dining', 'betraying', 'paniking', 'frolicking', 'robbing'
        ]

    nouns = ['ducks', 'whales', 'donkeys', 'eggs', 'cherries', 'actors',
            'ants', 'tigers', 'lions', 'giraffes', 'apes', 'antelopes',
            'bears', 'bats', 'beavers', 'badgers', 'baboons',
            'barracudas', 'bees', 'bison', 'boar', 'buffalo', 'butterfly',
            'camel', 'caribou', 'cats', 'caterpillars', 'chettahs'
            'chickens', 'chimpanzees', 'clams', 'cockroaches', 'cod',
            'crabs', 'crocodiles', 'crows', 'deer', 'dogs', 'dolphin',
            'dove', 'dragonfly', 'eagles', 'eels', 'elephants', 'emus',
            'falcons', 'fish', 'foxes', 'frogs', 'gazelles', 'goats', 
            'geese', 'goldfish', 'gorillas', 'hawks', 'herring',
            'hippopotamuses', 'hornets', 'humminbirds', 'jaguars',
            'jellyfish', 'kangaroos', 'koalas', 'leopards', 
            'lobsters', 'magpies', 'mallards', 'mongooses', 'moose',
            'mice', 'mules', 'ostriches', 'otters', 'owls', 'oxes',
            'panthers', 'pelicans', 'penguins', 'pigs', 'rabbits', 
            'rats', 'raccoons', 'salamanders', 'scorpions', 'seals',
            'sharks', 'sheep', 'skunks', 'snakes', 'sparrows',
            'stingrays', 'swallows', 'swans', 'toads', 'turkeys',
            'vipers', 'vultures', 'walruses', 'wolfs', 
            'woodpeckers', 'worms', 'zebras', 'wasps', 'turtles',
            'beetles', 'witches', 'children', 'men', 'wommen',
        ]

    return (random.choice(adjs) + " " +
            random.choice(verbs) + " " +
            random.choice(nouns)
        )



