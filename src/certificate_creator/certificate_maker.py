"""
Module for creating certificates given a template and the attendees.

Currently only accepts .docx files as templates. Templates must have merge
fields or variables to substitute into. Certificates will be saved as PDF files.

TODO:
    * Implement functions
    * Use multiprocessing to speed up certificate creation.
    * Impement datalogging
    * Research other options for templates besides .docx files.
    * Research other options for certificates besides PDF files.
"""

from typing import *

from src.attendees.attendee_manager import Attendee, AttendeeManager

def createCertificate(in_path: str, out_path: str, attendees: AttendeeManager,
                     namingFunc: Callable[[Attendee], str] = None,
                     statusFunc: Callable[[Attendee, Exception], None] = None,
                     overwrite: bool = True) -> AttendeeManager:
    """
    Creates and saves certificates given template and the attendee record.

    Args:
        in_path (str): The path to the template document.
        out_dir (str): The folder to save the certificate to.
        attendees (AttendeeManager): The collection of attendees.
        namingFunc (Callable[[Attendee], str]): What to name the certificate, excluding the file extension. Defaults to ``None``, meaning certificates are automatically named.
        statusFunc (Callable[[Attendee, bool], None]): Status update function to inform caller of what certificates have been made. Must take in ``Attendee`` object and whether it was successfully created (bool). Useful for user interfaces. If left as ``None``, does nothing.
        overwrite (bool): Whether to overwrite certificate file that already exist, defaults to ``True``. Should call statusFunc with ``FileExistsError`` if False.

    Returns:
        Updated attendees with "cert_path" field. Should map to ``None`` if failed
        to create certificate.

    Raises:
        OSError: if template file IO error occurs.
        TODO: Document exact errors that can be raised.
    """
    raise NotImplementedError

mock commit
