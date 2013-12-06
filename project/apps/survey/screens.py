# Key principles:

# Views are responsible for rendering and handling any POST/save data.
# When they're done, they call SurveyResponse.mark_screen_complete(order),
# and redirect to next_screen.


SCREEN_DESCRIPTIONS_AND_URL_NAME = [
    {
        "id": "entrance",
        "title": "Welcome",
        "reverse_url": "survey:entrance",
        "reverse_args": None,
    },
    {
        "id": "demographics",
        "title": "Demographics",
        "reverse_url": "survey:demographics",
        "reverse_args": None,
    },
    {
        "id": "introduction",
        "title": "Introduction",
        "reverse_url": "survey:introduction",
        "reverse_args": None,
    },
]
for i in range(1, 9):
    SCREEN_DESCRIPTIONS_AND_URL_NAME.extend([
        {
            "id": "hs%s_intro" % i,
            "title": "Health State %s Intro" % i,
            "reverse_url": "survey:health_state_intro",
            "reverse_args": (i,),
            "health_state_number": i,
        },
        {
            "id": "hs%s_video" % i,
            "title": "Health State %s Video" % i,
            "reverse_url": "survey:health_state_video",
            "reverse_args": (i,),
            "health_state_number": i,
        },
        {
            "id": "hs%s_vas" % i,
            "title": "Health State %s Vertical Scale" % i,
            "reverse_url": "survey:health_state_vas",
            "reverse_args": (i,),
            "health_state_number": i,
        },
        {
            "id": "hs%s_tto" % i,
            "title": "Health State %s Time Trade-off" % i,
            "reverse_url": "survey:health_state_tto",
            "reverse_args": (i,),
            "health_state_number": i,
        },
        {
            "id": "hs%s_outro" % i,
            "title": "Health State %s Complete" % i,
            "reverse_url": "survey:health_state_outro",
            "reverse_args": (i,),
            "health_state_number": i,
        },
    ])
SCREEN_DESCRIPTIONS_AND_URL_NAME.extend([
    {
        "id": "complete",
        "title": "Survey Complete",
        "reverse_url": "survey:complete",
        "reverse_args": None,
    },
])

SCREENS = SCREEN_DESCRIPTIONS_AND_URL_NAME
counter = 0
for s in SCREEN_DESCRIPTIONS_AND_URL_NAME:
    s["order"] = counter
    counter += 1
