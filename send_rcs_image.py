import os
from dotenv import load_dotenv
from vonage import Auth, Vonage
from vonage_messages import RcsImage, RcsResource

# Load environment variables
load_dotenv()

# Initialize Vonage Auth and client
auth = Auth(
    application_id=os.getenv("VONAGE_APPLICATION_ID"),
    private_key=os.getenv("VONAGE_PRIVATE_KEY_PATH"),
)
vonage_client = Vonage(auth)

# Define the recipient's phone number and image URL
to_number = "###########"  # Your recipient's phone number
image_url = "https://a.storyblok.com/f/270183/667x500/dcc490aba1/vonage_team_codemotion.jpg/m/fit-in"

# Construct the RCS Image message
message = RcsImage(
    from_=os.getenv("RCS_SENDER_ID"),
    to=to_number,
    image=RcsResource(url=image_url),
)

# Send the message
response = vonage_client.messages.send(message)
print(response)
