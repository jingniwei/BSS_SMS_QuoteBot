'''
Configuration Settings

Includes keys for Twilio, etc.  Second stanza intended for Heroku deployment.
'''

# Uncomment to configure in file.
# ACCOUNT_SID = "AC9e7b5d8e36fbea0aa07e0f2fe00d1f32" 
# AUTH_TOKEN = "86383dca940b42715254ccd7f1e3ae89"
# BSSSPAM_APP_SID = "AP2eb78506a1a86e572137393307af3964"
# BSS_SPAM_ID = "+13393092550"


# Begin Heroku configuration - configured through environment variables.
import os
ACCOUNT_SID = os.environ['ACCOUNT_SID']
AUTH_TOKEN = os.environ['AUTH_TOKEN']
BSSSPAM_APP_SID = os.environ['BSSSPAM_APP_SID']
BSS_SPAM_ID = os.environ['BSS_SPAM_ID']
