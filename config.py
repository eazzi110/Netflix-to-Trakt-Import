import logging

LOG_FILENAME = "Netflix2TraktImportLog.log"
LOG_LEVEL = logging.INFO
VIEWING_HISTORY_FILENAME = "NetflixViewingHistory.csv"

# Set the datetime format of the csv file (default: %d.%m.%y for 05.02.21)
# Use %Y-%m-%d for 2021-02-05 (Canada, ...)
CSV_DATETIME_FORMAT = "%Y-%m-%d"

TMDB_API_KEY = "e50086d62fbb72d2a3858e91b8c6d405"
TMDB_LANGUAGE = "en"
TMDB_DEBUG = False
TMDB_SYNC_STRICT = True
TMDB_EPISODE_LANGUAGE_SEARCH = False # more api calls, longer waiting time, 
                                     # only useful if the tmdb language differs from en 
                                     # and episodes cannot be found in the season overview Api calls

TRAKT_API_CLIENT_ID = "c4859fdea8cb358425c3131856689eda4df0ace0cf8af43ed94f9e9f1ac93d75"
TRAKT_API_CLIENT_SECRET = "ac87de97f58ba7a7efff966d9c444dfc915f25c0ca1fb782b21b2af16a6521d1"
TRAKT_API_DRY_RUN = False
TRAKT_API_SYNC_PAGE_SIZE = 1000
