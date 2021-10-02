"""
Module for handling command line interface.

TODO:
    1. Plan CLI as series of screens
    2. Plan CLI screens as functions
    3. Implement CLI
"""

import curses
from typing import Dict, Any

from src.attendees.attendee_manager import Attendee, AttendeeManager
from src.attendees.attendee_fileio import *
from src.attendees.attendee_converter import *
from src.certificate_creator.certificate_maker import createCertificate
from src.mailchimp.mailchimp_manager import MailchimpManager

def run_cli(argv: Dict[str, str]):
    """
    Runs the CLI.

    Args:
        argv (Dict[str, str]): The processed command line arguments.
    """
    raise NotImplementedError

# TODO: Decide on needed CLI public functions

def load_attendees(path: str) -> AttendeeManager:
    """
    Checks the status of the loading of attendees and returns an AttendeeManager.

    Args:
        path(str): The path to the attendees CSV.

    Return:
        AttendeeManager: the CSV file of attendees converted to an AttendeeManager.

    Raise:
        OSError: if there is an error with loading attendees.
    """
    raise NotImplementedError



# Hidden functions go here


