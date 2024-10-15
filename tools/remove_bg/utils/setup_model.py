import os

def setup_u2net_model():
    # Create the 'models' directory if it doesn't exist
    os.makedirs('models', exist_ok=True)

    # Set the environment variable to the 'models' folder in the current directory
    os.environ['U2NET_HOME'] = os.path.join(os.getcwd(), 'models')
