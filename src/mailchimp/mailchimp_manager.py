"""
Module that handles the Mailchimp functionality.

Can connect to Mailchimp account, upload certificates, and update attendees.
However, does not have ability to authorise itself. Must get keys elsewhere.

TODO:
    * Implement methods
    * Implement datalogging
"""

from typing import *

from requests import *

from src.attendees.attendee_manager import Attendee, AttendeeManager

StatusFunc = Callable[[Attendee, Exception], None]

class MailchimpManager:
    """
    Abstract Mailchimp manager without authorisation.

    Attributes:
        TODO: detail public attributes
    """

    def __init__(self, api_key, server):
        """
        Constructor
        """
   	self.server = server
	self.api_key = api_key
 
    def set_authorisation(self, keys: Dict[str, str]) -> bool:
        """
        Set keys needed to authorise self.

        Needs server key named "server", and needs either API key named
        "api_key" or OAuth token named "access_token". See Mailchimp
        API documentation for more details.

        Args:
            keys (Dict[str, str]): Collection of named keys used to authorise self.
        
        Returns:
            bool: ``True`` if authorisation passed and vice-versa.
        
        Raises:
            TODO: Document all possible errors
        """
    
    def ping(self) -> Response:
        """
        Ping Mailchimp server to check for connection and authroisation.

        Returns:
            The response from the Mailchimp server.

        Raises:
            TODO: Detail potential errors
        """
        raise NotImplementedError
    
    def create_folder(self, foldername: str) -> int:
        """
        Creates folder on user's Mailchimp account.

        Blocking function that makes HTTP request to create folder.

        Args:
            foldername (str): The name of the folder to create.
        
        Returns:
            int: the folder ID given by Mailchimp.
        
        Raises:
            TODO: Document all possible errors
        """
        raise NotImplementedError

    def upload_certificates(self, attendees: AttendeeManager,
                            folder_id: int = None,
                            status_func: StatusFunc = None
                            ) -> str:
        """
        Upload certificates to Mailchimp.

        Blocking function that waits until the batch request completes.

        Args:
            attendees (AttendeeManager): The collection of attendees. Will be updated to include file URLs.
            folder_id (int): The ID of the folder to upload certificates to. If left as ``None``, will not put in a folder.
            status_func (Callable[[Attendee, Exception], None]): Status update callback to inform caller of what certificates have been processed. Must take in ``Attendee`` object then the ``Exception``. ``Exception`` should be ``None`` if successful. If left as ``None``, does nothing.
        
        Returns:
            str: The response_body_url to download the responses.
        
        Raises:
            TODO: Document potential errors.
        """
        raise NotImplementedError

    def update_contact_files(self, attendees: AttendeeManager,
                             status_func: StatusFunc = None) -> str:
        """
        Updates the attendee contact file field.

        Blocking function that waits for batch request to complete.

        Args:
            attendees (AttendeeManager): The collection of attendees with file URLs.
            status_func (StatusFunc): Callback to inform caller of progress, must pass in ``Attendee`` object then the ``Exception`` (``None`` if no error occured), then return nothing.

        Returns:
            str: The response_body_url to download the responses.

        Raises:
            TODO: Document potential errors.
        """
        raise NotImplementedError

    def download_batch_respones(self, response_body_url: str,
                                keep_files: bool = False) -> List[str]:
        """
        Downloads batch request repsonses.

        Blocking function that will wait until file is downloaded, unzipped,
        then processed.

        Args:
            response_body_url (str): The URL to download the responses.
            keep_files (bool): Whether to keep the responses on file or delete them, defaults to ``True``.
        
        Returns:
            List[str]: The list of responses as JSON strings.
        
        Raises:
            TODO: Document potential errors.
        """
        raise NotImplementedError
