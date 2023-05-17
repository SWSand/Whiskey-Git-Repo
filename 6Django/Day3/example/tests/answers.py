all_pokemon = [
    {
        "model": "pokemon_app.pokemon",
        "pk": 3,
        "fields": {
            "name": "Blastoise",
            "level": 37,
            "date_encountered": "2008-01-01",
            "date_captured": "2023-04-14T05:26:47Z",
            "description": "A water type pokemon with two hydro cannons sticking out of it's shell",
            "captured": False,
            "moves": [
                {
                    "model": "move_app.move",
                    "pk": 3,
                    "fields": {
                        "name": "Water Pulse",
                        "accuracy": 70,
                        "maxPP": 20,
                        "pp": 20,
                        "power": 80,
                    },
                },
                {
                    "model": "move_app.move",
                    "pk": 9,
                    "fields": {
                        "name": "Pound",
                        "accuracy": 70,
                        "maxPP": 20,
                        "pp": 20,
                        "power": 70,
                    },
                },
                {
                    "model": "move_app.move",
                    "pk": 11,
                    "fields": {
                        "name": "Blizzard",
                        "accuracy": 60,
                        "maxPP": 10,
                        "pp": 7,
                        "power": 120,
                    },
                },
            ],
        },
    },
    {
        "model": "pokemon_app.pokemon",
        "pk": 2,
        "fields": {
            "name": "Charizard",
            "level": 25,
            "date_encountered": "2007-04-07",
            "date_captured": "2023-04-14T05:17:16Z",
            "description": "A fire type pokemon with Dragon like features and capabilities.",
            "captured": True,
            "moves": [
                {
                    "model": "move_app.move",
                    "pk": 2,
                    "fields": {
                        "name": "Wing Attack",
                        "accuracy": 70,
                        "maxPP": 20,
                        "pp": 20,
                        "power": 70,
                    },
                },
                {
                    "model": "move_app.move",
                    "pk": 5,
                    "fields": {
                        "name": "Dragon Pulse",
                        "accuracy": 70,
                        "maxPP": 10,
                        "pp": 5,
                        "power": 120,
                    },
                },
                {
                    "model": "move_app.move",
                    "pk": 6,
                    "fields": {
                        "name": "Fly",
                        "accuracy": 70,
                        "maxPP": 20,
                        "pp": 20,
                        "power": 80,
                    },
                },
                {
                    "model": "move_app.move",
                    "pk": 7,
                    "fields": {
                        "name": "Cut",
                        "accuracy": 70,
                        "maxPP": 20,
                        "pp": 20,
                        "power": 80,
                    },
                },
            ],
        },
    },
    {
        "model": "pokemon_app.pokemon",
        "pk": 1,
        "fields": {
            "name": "Pikachu",
            "level": 25,
            "date_encountered": "2008-01-01",
            "date_captured": "2023-04-14T05:16:41Z",
            "description": "Pikachu is an electric type pokemon who needs a thrunder stone to evolve into Raichu.",
            "captured": True,
            "moves": [
                {
                    "model": "move_app.move",
                    "pk": 4,
                    "fields": {
                        "name": "Shock Wave",
                        "accuracy": 100,
                        "maxPP": 20,
                        "pp": 20,
                        "power": 80,
                    },
                },
                {
                    "model": "move_app.move",
                    "pk": 6,
                    "fields": {
                        "name": "Fly",
                        "accuracy": 70,
                        "maxPP": 20,
                        "pp": 20,
                        "power": 80,
                    },
                },
                {
                    "model": "move_app.move",
                    "pk": 12,
                    "fields": {
                        "name": "Thunder Bolt",
                        "accuracy": 70,
                        "maxPP": 20,
                        "pp": 20,
                        "power": 100,
                    },
                },
                {
                    "model": "move_app.move",
                    "pk": 13,
                    "fields": {
                        "name": "Lightning",
                        "accuracy": 70,
                        "maxPP": 20,
                        "pp": 20,
                        "power": 120,
                    },
                },
            ],
        },
    },
]
a_pokemon = {
    "model": "pokemon_app.pokemon",
    "pk": 1,
    "fields": {
        "name": "Pikachu",
        "level": 25,
        "date_encountered": "2008-01-01",
        "date_captured": "2023-04-14T05:16:41Z",
        "description": "Pikachu is an electric type pokemon who needs a thrunder stone to evolve into Raichu.",
        "captured": True,
        "moves": [
            {
                "model": "move_app.move",
                "pk": 4,
                "fields": {
                    "name": "Shock Wave",
                    "accuracy": 100,
                    "maxPP": 20,
                    "pp": 20,
                    "power": 80,
                },
            },
            {
                "model": "move_app.move",
                "pk": 6,
                "fields": {
                    "name": "Fly",
                    "accuracy": 70,
                    "maxPP": 20,
                    "pp": 20,
                    "power": 80,
                },
            },
            {
                "model": "move_app.move",
                "pk": 12,
                "fields": {
                    "name": "Thunder Bolt",
                    "accuracy": 70,
                    "maxPP": 20,
                    "pp": 20,
                    "power": 100,
                },
            },
            {
                "model": "move_app.move",
                "pk": 13,
                "fields": {
                    "name": "Lightning",
                    "accuracy": 70,
                    "maxPP": 20,
                    "pp": 20,
                    "power": 120,
                },
            },
        ],
    },
}

all_moves = [
    {
        "model": "move_app.move",
        "pk": 11,
        "fields": {
            "name": "Blizzard",
            "accuracy": 60,
            "maxPP": 10,
            "pp": 7,
            "power": 120
        }
    },
    {
        "model": "move_app.move",
        "pk": 7,
        "fields": {
            "name": "Cut",
            "accuracy": 70,
            "maxPP": 20,
            "pp": 20,
            "power": 80
        }
    },
    {
        "model": "move_app.move",
        "pk": 5,
        "fields": {
            "name": "Dragon Pulse",
            "accuracy": 70,
            "maxPP": 10,
            "pp": 5,
            "power": 120
        }
    },
    {
        "model": "move_app.move",
        "pk": 6,
        "fields": {
            "name": "Fly",
            "accuracy": 70,
            "maxPP": 20,
            "pp": 20,
            "power": 80
        }
    },
    {
        "model": "move_app.move",
        "pk": 13,
        "fields": {
            "name": "Lightning",
            "accuracy": 70,
            "maxPP": 20,
            "pp": 20,
            "power": 120
        }
    },
    {
        "model": "move_app.move",
        "pk": 9,
        "fields": {
            "name": "Pound",
            "accuracy": 70,
            "maxPP": 20,
            "pp": 20,
            "power": 70
        }
    },
    {
        "model": "move_app.move",
        "pk": 10,
        "fields": {
            "name": "Psybeam",
            "accuracy": 70,
            "maxPP": 20,
            "pp": 20,
            "power": 80
        }
    },
    {
        "model": "move_app.move",
        "pk": 1,
        "fields": {
            "name": "Psychic",
            "accuracy": 70,
            "maxPP": 20,
            "pp": 20,
            "power": 80
        }
    },
    {
        "model": "move_app.move",
        "pk": 8,
        "fields": {
            "name": "Rock Throw",
            "accuracy": 70,
            "maxPP": 20,
            "pp": 20,
            "power": 80
        }
    },
    {
        "model": "move_app.move",
        "pk": 4,
        "fields": {
            "name": "Shock Wave",
            "accuracy": 100,
            "maxPP": 20,
            "pp": 20,
            "power": 80
        }
    },
    {
        "model": "move_app.move",
        "pk": 12,
        "fields": {
            "name": "Thunder Bolt",
            "accuracy": 70,
            "maxPP": 20,
            "pp": 20,
            "power": 100
        }
    },
    {
        "model": "move_app.move",
        "pk": 3,
        "fields": {
            "name": "Water Pulse",
            "accuracy": 70,
            "maxPP": 20,
            "pp": 20,
            "power": 80
        }
    },
    {
        "model": "move_app.move",
        "pk": 2,
        "fields": {
            "name": "Wing Attack",
            "accuracy": 70,
            "maxPP": 20,
            "pp": 20,
            "power": 70
        }
    }
]

a_move = {
    "model": "move_app.move",
    "pk": 1,
    "fields": {
        "name": "Psychic",
        "accuracy": 70,
        "maxPP": 20,
        "pp": 20,
        "power": 80,
    },
}
