from android_client_handler import change_user_language_android, change_user_country_android
from ios_client_handler import change_user_language_ios, change_user_country_ios

if __name__== "__main__":

    # simulating the requests sent by android and ios clients for updating country and language
    change_user_country_android('dev_monk', 'COUNTRY_USA')
    change_user_country_ios('Rahul', 'COUNTRY_INDIA')

    change_user_language_android('dev_monk', 'COUNTRY_USA', 'LANGUAGE_SPANISH')
    change_user_language_ios('Rahul', 'COUNTRY_INDIA', 'LANGUAGE_HINDI')
    change_user_language_android('Shikhhar', 'COUNTRY_INDIA', 'LANGUAGE_ENGLISH')
