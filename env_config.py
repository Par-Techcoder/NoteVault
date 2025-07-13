import environ

# Initialize environment variables

env = environ.Env(
    DEBUG=(bool, False), # Default to False, can be overridden by .env file
    
    SECRET_KEY=(str, ''), # Default to empty string, should be set in .env file

    # Database configuration    
    DATABASE_NAME=(str, ''),
)

# Read the .env file
environ.Env.read_env('.env')