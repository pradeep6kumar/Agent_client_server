import os
from dotenv import load_dotenv
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client
import asyncio
import google.generativeai as genai
import warnings
import traceback
import sys

# Suppress specific warnings
warnings.filterwarnings("ignore", message="unclosed.*", category=ResourceWarning)
warnings.filterwarnings("ignore", message="Exception ignored.*", category=RuntimeWarning)

# Load environment variables
load_dotenv()

# Configure Gemini
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

# Configure the model
print("Configuring model: gemini-1.5-flash")
model = genai.GenerativeModel('gemini-1.5-flash')

async def main():
    try:
        print("Starting email client...")
        
        # Create server connection
        server_params = StdioServerParameters(
            command="python",
            args=["email_server.py"]
        )
        
        async with stdio_client(server_params) as (read, write):
            async with ClientSession(read, write) as session:
                print("Connected to email server")
                await session.initialize()
                
                # Get available tools
                tools_result = await session.list_tools()
                tools = tools_result.tools
                print(f"Available tools: {[t.name for t in tools]}")
                
                # Send email
                result = await session.call_tool(
                    "send_email",
                    arguments={
                        "recipient": "6pradeep.k@gmail.com",
                        "subject": "hello",
                        "body": "This is a test email sent from the Gemini-powered email client."
                    }
                )
                
                print(result.content[0].text)
                
                # Add small delay before cleanup
                await asyncio.sleep(0.5)
                
    except Exception as e:
        print(f"Error in main function: {str(e)}")
        traceback.print_exc()

def cleanup_loop(loop):
    try:
        # Cancel all tasks
        pending = asyncio.all_tasks(loop)
        for task in pending:
            task.cancel()
        
        # Allow tasks to complete cancellation
        loop.run_until_complete(asyncio.gather(*pending, return_exceptions=True))
        
        # Stop and close the loop
        loop.stop()
        loop.close()
        
    except Exception as e:
        print(f"Error during cleanup: {str(e)}")

if __name__ == "__main__":
    # Set event loop policy for Windows
    if sys.platform == 'win32':
        asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())
    
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    
    try:
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        print("\nShutdown initiated by user...")
    except Exception as e:
        print(f"Error in event loop: {str(e)}")
    finally:
        cleanup_loop(loop)
        # Ensure event loop is properly reset
        asyncio.set_event_loop(None)
        print("Client closed successfully.") 