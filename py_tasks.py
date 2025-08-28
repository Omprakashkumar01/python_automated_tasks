import smtplib
from email.mime.text import MIMEText
from twilio.rest import Client
import requests
import tweepy


# ---------------- EMAIL ----------------
def send_email():
    sender = "your_email@gmail.com"
    receiver = "receiver_email@gmail.com"
    password = "your_app_password"

    msg = MIMEText("Hello! This is a test email sent from Python.")
    msg["Subject"] = "Python Email"
    msg["From"] = sender
    msg["To"] = receiver

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender, password)
            server.sendmail(sender, receiver, msg.as_string())
        print(" Email sent successfully!")
    except Exception as e:
        print(" Error:", e)


# ---------------- SMS ----------------
def send_sms():
    account_sid = "your_twilio_sid"
    auth_token = "your_twilio_auth_token"
    client = Client(account_sid, auth_token)

    try:
        message = client.messages.create(
            body="Hello! This is a test SMS from Python.",
            from_="+1234567890",  # Twilio number
            to="+919876543210"
        )
        print(" SMS sent successfully:", message.sid)
    except Exception as e:
        print(" Error:", e)


# ---------------- PHONE CALL ----------------
def make_call():
    account_sid = "your_twilio_sid"
    auth_token = "your_twilio_auth_token"
    client = Client(account_sid, auth_token)

    try:
        call = client.calls.create(
            url="http://demo.twilio.com/docs/voice.xml",
            to="+919876543210",
            from_="+1234567890"
        )
        print(" Call initiated:", call.sid)
    except Exception as e:
        print(" Error:", e)


# ---------------- LINKEDIN ----------------
def post_linkedin():
    access_token = "your_linkedin_access_token"
    api_url = "https://api.linkedin.com/v2/ugcPosts"

    headers = {
        "Authorization": f"Bearer {access_token}",
        "X-Restli-Protocol-Version": "2.0.0",
        "Content-Type": "application/json"
    }

    post_data = {
        "author": "urn:li:person:your_linkedin_id",
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {
                    "text": "Hello, posting on LinkedIn via Python!"
                },
                "shareMediaCategory": "NONE"
            }
        },
        "visibility": {"com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"}
    }

    try:
        response = requests.post(api_url, headers=headers, json=post_data)
        print(" LinkedIn Post response:", response.json())
    except Exception as e:
        print(" Error:", e)


# ---------------- TWITTER ----------------
def post_twitter():
    api_key = "your_api_key"
    api_secret = "your_api_secret"
    access_token = "your_access_token"
    access_secret = "your_access_secret"

    try:
        auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_secret)
        api = tweepy.API(auth)
        api.update_status("Hello from Python! #Python #TwitterAPI")
        print(" Tweet posted successfully!")
    except Exception as e:
        print(" Error:", e)


# ---------------- FACEBOOK ----------------
def post_facebook():
    page_access_token = "your_page_access_token"
    page_id = "your_page_id"
    message = "Hello! Posting on Facebook using Python."

    url = f"https://graph.facebook.com/{page_id}/feed"
    payload = {"message": message, "access_token": page_access_token}

    try:
        response = requests.post(url, data=payload)
        print(" Facebook Post response:", response.json())
    except Exception as e:
        print(" Error:", e)


# ---------------- INSTAGRAM ----------------
def post_instagram():
    access_token = "your_access_token"
    instagram_account_id = "your_ig_account_id"
    caption = "Hello Instagram! Posted via Python. #Python #Instagram"
    image_url = "https://picsum.photos/200/300"

    try:
        # Step 1: Create container
        url = f"https://graph.facebook.com/v19.0/{instagram_account_id}/media"
        params = {"image_url": image_url, "caption": caption, "access_token": access_token}
        r = requests.post(url, params=params)
        container_id = r.json()["id"]

        # Step 2: Publish container
        publish_url = f"https://graph.facebook.com/v19.0/{instagram_account_id}/media_publish"
        publish_params = {"creation_id": container_id, "access_token": access_token}
        r = requests.post(publish_url, params=publish_params)
        print(" Instagram Post response:", r.json())
    except Exception as e:
        print(" Error:", e)


# ---------------- WHATSAPP ----------------
def send_whatsapp():
    account_sid = "your_twilio_sid"
    auth_token = "your_twilio_auth_token"
    client = Client(account_sid, auth_token)

    try:
        message = client.messages.create(
            from_="whatsapp:+14155238886",  # Twilio sandbox
            body="Hello! This is a WhatsApp message sent using Python.",
            to="whatsapp:+919876543210"
        )
        print(" WhatsApp message sent:", message.sid)
    except Exception as e:
        print(" Error:", e)


# ---------------- MENU ----------------
def menu():
    while True:
        print("\n--- Python Automation Menu ---")
        print("1. Send Email")
        print("2. Send SMS")
        print("3. Make Phone Call")
        print("4. Post on LinkedIn")
        print("5. Post on Twitter")
        print("6. Post on Facebook")
        print("7. Post on Instagram")
        print("8. Send WhatsApp Message")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            send_email()
        elif choice == "2":
            send_sms()
        elif choice == "3":
            make_call()
        elif choice == "4":
            post_linkedin()
        elif choice == "5":
            post_twitter()
        elif choice == "6":
            post_facebook()
        elif choice == "7":
            post_instagram()
        elif choice == "8":
            send_whatsapp()
        elif choice == "9":
            print("Exiting... ")
            break
        else:
            print(" Invalid choice, try again.")


# Run the menu
if __name__ == "__main__":
    menu()
