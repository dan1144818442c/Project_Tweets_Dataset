"# Project_Tweest_Dataset" 

There are several CLASS:
LOADER- Loads the DATA into a file (CSV or JSON, depending on the requirement)
CLEANER - Cleans the DATA according to the exercise requirements.
Data_investigation - Using the previous CLASS, receives DF and returns JSON with data after investigating the DATA.

main.py - Using all the previous CLASS, loads the DB into the DF, sends it to the CLASS that interrogates and exports the JSON with the interrogation data into an appropriate file, and also uses the CLEANER to load the clean DF into an appropriate file.
