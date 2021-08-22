"""
Main file that runs the certificate automator terminal program.
"""

__version__ = "0.1.0"

import argparse
import sys
from typing import Dict

from src.cli import cli

def main():
    argv = process_cmd_line_args()
    cli.run_cli(argv)

def process_cmd_line_args() -> Dict[str, str]:
    """
    Process command line arguments.

    Will terminate program if required arguments are not found.

    Returns:
        Dict[str, str]: The processed and validated arguments.
    """
    parser = argparse.ArgumentParser("Certificate Automater")
    parser.add_argument("--attendees", required=True, help="The path to the attendee record as a CSV file")
    parser.add_argument("--server-key", required=True, help="The Mailchimp server key")
    parser.add_argument("--api-key", required=True, help="The Mailchimp API key")
    parser.add_argument("--template", required=True, help="The path to the template certificate as a .docx file")
    parser.add_argument("--event", help="The name of the event")
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    return vars(parser.parse_args(sys.argv[1:]))

if __name__ == "__main__":
    main()