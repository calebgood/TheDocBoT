Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
================= RESTART: G:\TheDocBoT\trial 2\complete.py =================
{
    "extras": {},
    "items": [
        {
            "choices": [
                {
                    "id": "present",
                    "label": "Yes"
                },
                {
                    "id": "absent",
                    "label": "No"
                },
                {
                    "id": "unknown",
                    "label": "Don't know"
                }
            ],
            "id": "s_99",
            "name": "Between 98.6 and 100.4 \u00b0F (37 and 38 \u00b0C)"
        },
        {
            "choices": [
                {
                    "id": "present",
                    "label": "Yes"
                },
                {
                    "id": "absent",
                    "label": "No"
                },
                {
                    "id": "unknown",
                    "label": "Don't know"
                }
            ],
            "id": "s_100",
            "name": "Between 100.4 and 104 \u00b0F (38 and 40 \u00b0C)"
        },
        {
            "choices": [
                {
                    "id": "present",
                    "label": "Yes"
                },
                {
                    "id": "absent",
                    "label": "No"
                },
                {
                    "id": "unknown",
                    "label": "Don't know"
                }
            ],
            "id": "s_2000",
            "name": "Greater than 104 \u00b0F (40 \u00b0C)"
        },
        {
            "choices": [
                {
                    "id": "present",
                    "label": "Yes"
                },
                {
                    "id": "absent",
                    "label": "No"
                },
                {
                    "id": "unknown",
                    "label": "Don't know"
                }
            ],
            "id": "s_1820",
            "name": "I haven\u2019t checked my temperature"
        }
    ],
    "text": "What is your body temperature?",
    "type": "group_single"
}
What is your body temperature?
[{'id': 's_99', 'name': 'Between 98.6 and 100.4 °F (37 and 38 °C)', 'choices': [{'id': 'present', 'label': 'Yes'}, {'id': 'absent', 'label': 'No'}, {'id': 'unknown', 'label': "Don't know"}]}, {'id': 's_100', 'name': 'Between 100.4 and 104 °F (38 and 40 °C)', 'choices': [{'id': 'present', 'label': 'Yes'}, {'id': 'absent', 'label': 'No'}, {'id': 'unknown', 'label': "Don't know"}]}, {'id': 's_2000', 'name': 'Greater than 104 °F (40 °C)', 'choices': [{'id': 'present', 'label': 'Yes'}, {'id': 'absent', 'label': 'No'}, {'id': 'unknown', 'label': "Don't know"}]}, {'id': 's_1820', 'name': 'I haven’t checked my temperature', 'choices': [{'id': 'present', 'label': 'Yes'}, {'id': 'absent', 'label': 'No'}, {'id': 'unknown', 'label': "Don't know"}]}]
s_99
Between 98.6 and 100.4 °F (37 and 38 °C)
[{'id': 'present', 'label': 'Yes'}, {'id': 'absent', 'label': 'No'}, {'id': 'unknown', 'label': "Don't know"}]
present
Yes
[
    {
        "common_name": "Common cold",
        "id": "c_87",
        "name": "Common cold",
        "probability": 0.0258
    },
    {
        "common_name": "Gastroenteritis",
        "id": "c_10",
        "name": "Gastroenteritis",
        "probability": 0.0235
    },
    {
        "common_name": "Stress headache",
        "id": "c_55",
        "name": "Tension-type headaches",
        "probability": 0.0196
    },
    {
        "common_name": "Food poisoning",
        "id": "c_138",
        "name": "Food poisoning",
        "probability": 0.0195
    },
    {
        "common_name": "Acute viral tonsillopharyngitis",
        "id": "c_121",
        "name": "Acute viral tonsillopharyngitis",
        "probability": 0.017
    },
    {
        "common_name": "Strep throat",
        "id": "c_249",
        "name": "Acute streptococcal tonsillopharyngitis",
        "probability": 0.0149
    },
    {
        "common_name": "Flu",
        "id": "c_33",
        "name": "Influenza",
        "probability": 0.0129
    },
    {
        "common_name": "Inflammation of the gallbladder",
        "id": "c_215",
        "name": "Cholecystitis",
        "probability": 0.0112
    },
    {
        "common_name": "Appendicitis",
        "id": "c_132",
        "name": "Appendicitis",
        "probability": 0.0098
    },
    {
        "common_name": "Migraine",
        "id": "c_49",
        "name": "Migraine",
        "probability": 0.0096
    },
    {
        "common_name": "Dehydration",
        "id": "c_298",
        "name": "Dehydration",
        "probability": 0.0094
    }
]
c_87
Common cold
0.0258

