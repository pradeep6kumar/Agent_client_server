from mcp.server.fastmcp import FastMCP
from mcp.types import TextContent
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize FastMCP server
mcp = FastMCP("EmailServer")

# Global variables for email configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = os.getenv("SENDER_EMAIL")  # You'll need to set this in .env
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")  # You'll need to set this in .env

@mcp.tool()
async def send_email(recipient: str, subject: str, body: str) -> dict:
    """Send an email using Gmail SMTP"""
    try:
        # Create message
        message = MIMEMultipart()
        message["From"] = SENDER_EMAIL
        message["To"] = recipient
        message["Subject"] = subject

        # Add body to email
        message.attach(MIMEText(body, "plain"))

        # Create SMTP session
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            
            # Send email
            server.send_message(message)

        return {
            "content": [
                TextContent(
                    type="text",
                    text=f"Email sent successfully to {recipient}"
                )
            ]
        }
    except Exception as e:
        return {
            "content": [
                TextContent(
                    type="text",
                    text=f"Error sending email: {str(e)}"
                )
            ]
        }

if __name__ == "__main__":
    print("Email Server starting...")
    print("Make sure you have set SENDER_EMAIL and SENDER_PASSWORD in your .env file")
    print("Server initialized and waiting for connections...")
    mcp.run(transport="stdio") 