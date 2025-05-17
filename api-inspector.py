#!/usr/bin/env python3
import requests
import json
import argparse
from rich.console import Console
from rich.syntax import Syntax

console = Console()

def inspect_streaming_response(url):
    """Inspect the raw streaming response from the API"""
    console.print("[bold]Sending a basic test message to inspect streaming format...[/bold]")
    
    # Create a simple test message
    payload = {
        "messages": [{"role": "user", "content": "Hello, what's your name?"}],
        "temperature": 0.4,
        "max_output_tokens": 100
    }
    
    try:
        # Set up streaming request
        response = requests.post(url, json=payload, stream=True, headers={'Accept': 'text/event-stream'})
        
        console.print(f"[green]Response status code: {response.status_code}[/green]")
        console.print(f"[green]Response headers: {dict(response.headers)}[/green]")
        console.print("\n[bold]Raw response chunks:[/bold]")
        
        # Process raw chunks
        count = 0
        for chunk in response.iter_lines(decode_unicode=True):
            count += 1
            if not chunk:
                console.print("\n[dim]-- Empty line --[/dim]")
                continue
                
            # Try to parse JSON if it starts with data:
            if chunk.startswith("data: "):
                data_str = chunk[6:]
                console.print(f"\n[yellow]Chunk #{count}:[/yellow] {chunk}")
                
                try:
                    data = json.loads(data_str)
                    # Pretty print the parsed JSON
                    syntax = Syntax(json.dumps(data, indent=2), "json", theme="monokai")
                    console.print(syntax)
                except json.JSONDecodeError as e:
                    console.print(f"[red]Not valid JSON: {e}[/red]")
            else:
                console.print(f"\n[yellow]Chunk #{count}:[/yellow] {chunk}")
            
            # Stop after a reasonable number of chunks
            if count >= 20:
                console.print("\n[yellow]Reached 20 chunks, stopping for brevity...[/yellow]")
                break
                
        console.print("\n[bold green]Response inspection complete![/bold green]")
        
    except requests.RequestException as e:
        console.print(f"[bold red]Network error: {str(e)}[/bold red]")
    except Exception as e:
        console.print(f"[bold red]Error: {str(e)}[/bold red]")
        import traceback
        console.print(traceback.format_exc())

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Inspect API streaming response")
    parser.add_argument("--url", default="http://localhost:5001/api/chat",
                      help="API endpoint URL (default: http://localhost:5001/api/chat)")
    args = parser.parse_args()
    
    inspect_streaming_response(args.url)
