# Email Client with Gemini AI

A Python-based email client that uses Google's Gemini AI model to send emails through a client-server architecture.

## Features

- Server-client architecture using FastMCP
- Email sending capability using Gmail SMTP
- Integration with Google's Gemini 1.5 Flash AI model
- Asynchronous operation using asyncio

## Prerequisites

- Python 3.10 or higher
- Gmail account with App Password enabled
- Google API key for Gemini AI

## Setup

1. Clone the repository
2. Create a virtual environment and activate it:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: .\env\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install python-dotenv google-generativeai mcp
   ```
4. Create a `.env` file in the root directory with the following:
   ```
   GOOGLE_API_KEY=your_google_api_key
   SENDER_EMAIL=your_gmail_address
   SENDER_PASSWORD=your_gmail_app_password
   ```

## Gmail App Password Setup

1. Go to your Google Account settings
2. Enable 2-Step Verification if not already enabled
3. Go to Security → App Passwords
4. Generate a new app password for "Mail"
5. Use this generated password in your `.env` file

## Usage

1. Start the email server:
   ```bash
   python email_server.py
   ```

2. In a separate terminal, run the client:
   ```bash
   python talk2email.py
   ```

## Files

- `email_server.py`: Server component that handles email sending
- `talk2email.py`: Client component that interfaces with Gemini AI
- `.env`: Configuration file for API keys and credentials (not included in repository)
- `.gitignore`: Specifies which files Git should ignore

## Note

Make sure to keep your `.env` file secure and never commit it to version control. The included `.gitignore` file will help prevent accidental commits of sensitive information. 


#-------------------------------------------------------#

# Paint Automation with Gemini AI

A Python-based automation system that uses Google's Gemini AI model to control Microsoft Paint through a client-server architecture.

## Features

- Server-client architecture using FastMCP
- Microsoft Paint automation using pywinauto
- Integration with Google's Gemini 1.5 Flash AI model
- Automated drawing capabilities:
  - Rectangle drawing with precise coordinates
  - Text addition at specified locations
  - Graceful application closure without saving
- Asynchronous operation using asyncio

## Prerequisites

- Python 3.10 or higher
- Windows operating system with Microsoft Paint installed
- Google API key for Gemini AI
- Single monitor setup (coordinates are calibrated for single display)

## Setup

1. Clone the repository
2. Create a virtual environment and activate it:
   ```bash
   python -m venv env
   .\env\Scripts\activate  # Windows specific
   ```
3. Install dependencies:
   ```bash
   pip install python-dotenv google-generativeai mcp pywinauto
   ```
4. Create a `.env` file in the root directory with:
   ```
   GOOGLE_API_KEY=your_google_api_key
   ```

## Coordinate System

The application uses specific screen coordinates for Paint operations:
- Rectangle Tool: (542, 81)
- Drawing Area Start: (555, 342)
- Drawing Area End: (1155, 742)
- Text Tool: (351, 87)
- "Don't Save" Button: (961, 569)

Note: These coordinates are calibrated for a standard Windows display. Adjustments may be needed for different screen resolutions.

## Usage

1. Start the Paint server:
   ```bash
   python example2-3.py
   ```

2. In a separate terminal, run the client:
   ```bash
   python talk2mcp-2.py
   ```

The application will:
1. Open Microsoft Paint
2. Draw a rectangle using specified coordinates
3. Add text inside the rectangle
4. Close Paint without saving changes

## Files

- `example2-3.py`: Server component that handles Paint automation
- `talk2mcp-2.py`: Client component that interfaces with Gemini AI
- `.env`: Configuration file for API key (not included in repository)
- `.gitignore`: Specifies which files Git should ignore

## Available Tools

The server provides several mathematical and Paint automation tools:

### Mathematical Functions
- `add(a, b)`: Add two numbers
- `subtract(a, b)`: Subtract two numbers
- `multiply(a, b)`: Multiply two numbers
- `divide(a, b)`: Divide two numbers
- `power(a, b)`: Calculate power
- `sqrt(a)`: Calculate square root
- `factorial(a)`: Calculate factorial

### Paint Automation Functions
- `open_paint()`: Opens and maximizes MS Paint
- `draw_rectangle(x1, y1, x2, y2)`: Draws rectangle with specified coordinates
- `add_text_in_paint(text)`: Adds text at specified location
- `close_paint()`: Closes Paint without saving

### String Processing
- `strings_to_chars_to_int(string)`: Converts string to ASCII values
- `int_list_to_exponential_sum(int_list)`: Calculates sum of exponentials

## Troubleshooting

1. Coordinate Issues:
   - If rectangle or text placement is incorrect, verify your screen resolution
   - Adjust coordinates in the code if needed

2. Paint Access:
   - Ensure Paint is installed in the default Windows location
   - Run the application with appropriate permissions

3. Common Errors:
   - "Window not found": Make sure Paint is properly installed
   - "Coordinate out of bounds": Check screen resolution compatibility

## Note

This application is designed for Windows systems and requires specific screen coordinates. Testing on your specific setup may be needed before deployment. 