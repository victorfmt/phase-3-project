import pygame
import sys

gods = [
        {
        "id": 1,
        "name": "Absu",
        "image": "assets/absu.png",
        "description": "The primordial goddess, mother of all that exists in the universe. She calls of calm and destruction of chaos. Access her by deep meditation and closing your eyes. She calls for innaction. 'Not doing' is her verb."
        },
        {
        "id": 2,
        "name": "Xon",
        "image": "assets/xon.png",
        "description": "The first son of Absu. He represents the first self, the first child. His birth resulted in the first disturbance in the universe. He represents the desire to look for another and the desire to bond. He is the god of guidence, plentitude, and ideas."
        },
        {"id": 3,
        "name": "Esrhea",
        "image": "assets/hisra.png",
        "description": "Goddess of love and physics (prayers include: bathing, planting, watching plants, masturbating, cleaning, caring for something or someone, feeding something or someone, forgiving, accepting, etc)."
        },
        {"id": 4,
        "name": "Alinima",
        "image": "assets/alinima.png",
        "description": "Alinima is the first creature to inhabit Earth. Alinima like Esrhea, is one of the three gods of self and signifies bodily desires and needs. An imbalance of Alinima is, for example, eating too much, or sleeping too little, etc."
        },
        {"id": 5,
        "name": "On",
        "image": "assets/on.png",
        "description": "On is the first human and represents higher-function qualities of the brain. An Onian imbalance means that the individual in question is using intelect to the detriment of themsleves. Too much work, too much analysis, or too little intelectual stibulation, brain degeneration, etc."
        },
        {"id": 6,
        "name": "Amadeadon",
        "image": "assets/amadeadon.png",
        "description": "Amadeadon is the first child of On. Amadeadon is creative inspiration. The appearance of Amadeadon can mean ease of inspiration or lack thereof. A question to ask yourself is how easily can I obtain insight? How can I improve my ability to create or have visions?"
        }

    ]

    
    # Add more god objects as needed