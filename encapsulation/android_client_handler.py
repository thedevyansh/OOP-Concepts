from user_preference import UserPreference

def change_user_country_android(user_name, user_country):
    # Some Android specific code goes here.

    # Client code doesn't really care about UserPreference functions.
    # It just says update country.
    user_preference = UserPreference(user_name, user_country=user_country)
    user_preference.update_user_country()


def change_user_language_android(user_name, user_country, user_language):
    # Some Android specific code goes here.
  
    # Client code doesn't really care about UserPreference functions.
    # It just says update language.
    user_preference = UserPreference(user_name, user_country=user_country, user_language=user_language)
    user_preference.update_user_language()
