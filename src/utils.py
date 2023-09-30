
# general response
workclass = {'Private': 'Private',
             'State': 'State',
             'Other': 'Other',
             'Self': 'Self'}

education = {'Xth': 'Xth',
             'School': 'School',
             'Associate': 'Associate',
             'BCMD': 'BCMD',
             'Prof-school': 'Prof-school'}

marital_status = {'Never-married': 'Never-married',
                  'Married': 'Married',
                  'Widowed': 'Widowed',
                  'Divorced/Separated': 'Divorced/Separated'}

occupation = {'Machine-op-inspct': 'Machine-op-inspct',
              'Other': 'Other',
              'Protective-serv': 'Protective-serv',
              'Craft-repair': 'Craft-repair',
              'Adm-clerical': 'Adm-clerical',
              'Exec-managerial': 'Exec-managerial',
              'Sales': 'Sales'}

relationship = {'Own-child': 'Own-child',
                'Husband': 'Husband',
                'Not-in-family': 'Not-in-family',
                'Unmarried': 'Unmarried',
                'Wife': 'Wife',
                'Other-relative': 'Other-relative'}

race = {'Black': 'Black',
        'White': 'White',
        'Asian-Pac-Islander': 'Asian-Pac-Islander',
        'Other': 'Other',
        'Amer-Indian-Eskimo': 'Amer-Indian-Eskimo'}

gender = {'Male': 'Male', 'Female': 'Female'}

native_country = {'United-States': 'United-States',
                  '?': '?',
                  'Peru': 'Peru',
                  'Guatemala': 'Guatemala',
                  'Mexico': 'Mexico',
                  'Dominican-Republic': 'Dominican-Republic',
                  'Ireland': 'Ireland',
                  'Germany': 'Germany',
                  'Philippines': 'Philippines',
                  'Thailand': 'Thailand',
                  'Haiti': 'Haiti',
                  'El-Salvador': 'El-Salvador',
                  'Puerto-Rico': 'Puerto-Rico',
                  'Vietnam': 'Vietnam',
                  'South': 'South',
                  'Columbia': 'Columbia',
                  'Japan': 'Japan',
                  'India': 'India',
                  'Cambodia': 'Cambodia',
                  'Poland': 'Poland',
                  'Laos': 'Laos',
                  'England': 'England',
                  'Cuba': 'Cuba',
                  'Taiwan': 'Taiwan',
                  'Italy': 'Italy',
                  'Canada': 'Canada',
                  'Portugal': 'Portugal',
                  'China': 'China',
                  'Nicaragua': 'Nicaragua',
                  'Honduras': 'Honduras',
                  'Iran': 'Iran',
                  'Scotland': 'Scotland',
                  'Jamaica': 'Jamaica',
                  'Ecuador': 'Ecuador',
                  'Yugoslavia': 'Yugoslavia',
                  'Hungary': 'Hungary',
                  'Hong': 'Hong',
                  'Greece': 'Greece',
                  'Trinadad&Tobago': 'Trinadad&Tobago',
                  'Outlying-US(Guam-USVI-etc)': 'Outlying-US(Guam-USVI-etc)',
                  'France': 'France',
                  'Holand-Netherlands': 'Holand-Netherlands'}

age = {"value": 25,
       "min": 16,
       "max": 65}

cap_gain = {"value": 1080,
            "min": 0,
            "max": 10000}

cap_loss = {"value": 95,
            "min": 0,
            "max": 5000}

hp_week = {"value": 40,
           "min": 8,
           "max": 48}

columns_table = ["age",
                 "workclass",
                 "education",
                 "marital-status",
                 "occupation",
                 "relationship",
                 "race",
                 "gender",
                 "capital-gain",
                 "capital-loss",
                 "hours-per-week",
                 "native-country"
                 ]