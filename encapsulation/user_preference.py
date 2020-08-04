import json

# UserPreference class to work on data fields stored (or to be stored) in JSON file
class UserPreference:
    # constructor to initialize fields in case no parameter is passed while instantiating object
    def __init__(self):
        self.__user_name = None
        self.__user_country = None
        self.__user_language = None

    # constructor to initialize fields in case atleast one parameter is passed while instantiating object
    def __init__(self, user_name, user_country = None, user_language = None):
        self.__user_name = user_name
        self.__user_country = user_country
        self.__user_language = user_language

    # validating the fields that are requested to be updated in the file...
    # if validation is successful, user language is updated in the file
    def update_user_language(self):
        if ((self.__user_country == 'COUNTRY_USA'
             and (self.__user_language == 'LANGUAGE_SPANISH' or self.__user_language == 'LANGUAGE_ENGLISH'))
                or (self.__user_country == 'COUNTRY_INDIA'
                    and (self.__user_language == 'LANGUAGE_HINDI' or self.__user_language == 'LANGUAGE_ENGLISH'))):
            self.__user_country = None        
            self._update_user_preference_in_file()

        else:
            raise Exception('Invalid country/language combination')

    # updates user country in the file
    def update_user_country(self):
        self._update_user_preference_in_file()

    # interacts(to read and write) with the user preferences file
    def _update_user_preference_in_file(self):
        user_preference = {}

        user_preferences = self._read_preferences_from_file()

        if user_preferences is None:
            user_preferences = []

        user_found = False    
        for temp_user_preference in user_preferences:
            if temp_user_preference['user_name'] == self.__user_name:
                print('User preference exists for ' + self.__user_name)
                user_found = True
                user_preference = temp_user_preference
                break

        if user_found is False:
            user_preferences.append(user_preference)

        user_preference['user_name'] = self.__user_name

        if(self.__user_country is not None):
            user_preference['user_country'] = self.__user_country

        if(self.__user_language is not None):
            user_preference['user_language'] = self.__user_language

        with open('user_preferences.json', 'w') as outfile:
            json.dump(user_preferences, outfile)
            outfile.write('\n')

    # loads the file into memory to be updated
    def _read_preferences_from_file(self):
        with open('user_preferences.json') as inputfile:
            try:
                user_preferences = json.load(inputfile)
                return user_preferences
            
            except:
                print('The file is empty! Not a problem.')