import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Your Google API key and Custom Search Engine ID
api_key = 'AIzaSyB8w2aLAuBmtgag9vETMZKTW4sZXYyb5hs'
search_engine_id = '671bb390ee3e34193'

# Email credentials and configurations
sender_email = "adeel.hamayoun@gmail.com"
sender_password = "xlzvmubuxxzmugpn"  # Use an App Password for Gmail
recipient_email = "adeel.hamayoun@gmail.com"
smtp_server = "smtp.gmail.com"
smtp_port = 587  # For TLS


def fetch_news(query):
    """Fetch news articles using Google Custom Search API."""
    url = f"https://www.googleapis.com/customsearch/v1?q={query}&cx={search_engine_id}&key={api_key}"

    response = requests.get(url)
    if response.status_code == 200:
        search_results = response.json()
        articles = []
        for item in search_results.get('items', []):
            article = {
                'title': item['title'],
                'link': item['link'],
                'snippet': item['snippet']
            }
            articles.append(article)
        return articles
    else:
        print(f"Error fetching results: {response.status_code}")
        return []


def send_email(subject, body):
    """Send email with the given subject and body."""
    try:
        # Set up the email message
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = recipient_email
        message['Subject'] = subject

        # Add body content to the email
        message.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Start TLS encryption
            server.login(sender_email, sender_password)  # Login to the email account
            server.send_message(message)  # Send the email
            print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")


def format_news_for_email(news):
    """Format news articles for email body."""
    email_body = "Here are the latest news articles:\n\n"
    for idx, article in enumerate(news, 1):
        email_body += f"{idx}. {article['title']}\n"
        email_body += f"Link: {article['link']}\n"
        email_body += f"Snippet: {article['snippet']}\n\n"
    return email_body


# Main logic
if __name__ == "__main__":
    query = "Germany energy sector"
    news = fetch_news(query)

    if news:
        # Format the news for email
        email_body = format_news_for_email(news)

        # Send the email
        send_email("Top News on Germany's Energy Sector", email_body)
    else:
        print("No news articles found.")