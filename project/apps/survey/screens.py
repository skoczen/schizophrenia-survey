# Key principles:

# Views are responsible for rendering and handling any POST/save data.
# When they're done, they call SurveyResponse.screen_complete(order),
# and redirect to next_page.


SCREEN_DESCRIPTIONS_AND_URL_NAME = [
    {
        "title": "Welcome",
        "reverse_url": "survey:entrance",
        "reverse_args": None,
    },
    {
        "title": "Demographics",
        "reverse_url": "survey:demographics",
        "reverse_args": None,
    },
    {
        "title": "Introduction",
        "reverse_url": "survey:introduction",
        "reverse_args": None,
    },
]
for i in range(1, 9):
    SCREEN_DESCRIPTIONS_AND_URL_NAME.extend([
        {
            "name": "Health State %s Intro" % i,
            "reverse_url": "survey:health_state_intro",
            "reverse_args": (i,),
        },
        {
            "name": "Health State %s Video" % i,
            "reverse_url": "survey:health_state_video",
            "reverse_args": (i,),
        },
        {
            "name": "Health State %s Standard Gamble" % i,
            "reverse_url": "survey:health_state_sg",
            "reverse_args": (i,),
        },
        {
            "name": "Health State %s Time Trade-off" % i,
            "reverse_url": "survey:health_state_tto",
            "reverse_args": (i,),
        },
        {
            "name": "Health State %s Complete" % i,
            "reverse_url": "survey:health_state_outro",
            "reverse_args": (i,),
        },
    ])
SCREEN_DESCRIPTIONS_AND_URL_NAME.extend([
    {
        "name": "Survey Complete",
        "reverse_url": "survey:complete",
        "reverse_args": None,
    },
])

SCREENS = SCREEN_DESCRIPTIONS_AND_URL_NAME
counter = 1
for s in SCREEN_DESCRIPTIONS_AND_URL_NAME:
    s["order"] = counter
    counter += 1

