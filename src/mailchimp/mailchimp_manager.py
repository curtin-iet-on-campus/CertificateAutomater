"""
Module that handles the Mailchimp functionality.

Can connect to Mailchimp account, upload certificates, and update attendees.
However, does not have ability to authorise itself. Must get keys elsewhere.

TODO:
    * Implement methods
    * Implement datalogging
"""
import json

import base64

import mailchimp_marketing as MailchimpMarketing

from mailchimp_marketing.api_client import ApiClientError

from __future__ import annotations
from typing import *

from requests import *

from src.attendees.attendee_manager import Attendee, AttendeeManager

from mailchimp_marketing import Client

BatchStatusFunc = Callable[[str, int, int], None]
"""Type alias for batch status update callback.

Args:
    status (str): The status of the batch request.
    successful (int): Number of successful requests.
    failed (int): Number of failed requests.
"""

class MailchimpManager:
    """
    Abstract Mailchimp manager without authorisation.

    Attributes:
        TODO: detail public attributes
    """
	
    def __init__(self):
     	self.client = MailchimpMarketing.Client()
  	
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
        if type(keys) != dict:
		    raise TypeError
    	if "server" not in keys:
	    	raise ValueError
	    if "api_key" or "access_token" not in keys:
		    raise ValueError
	    if len(keys) != 2:
            raise ValueError
        for value in keys.values():
		    if type(value) != str:
			    raise TypeError
	    	elif value == "":
		    	raise ValueError
        self.keys = keys
        health_status = {"health_status": "Everything's Chimpy!"}
        if ping() == health_status:
            authorisation = True
        else:
            authorisation = False
        return authorisation
  
    def ping(self) -> dict:
        """
        Ping Mailchimp server to check for connection and authroisation.

        Returns:
            The response from the Mailchimp server.

        Raises:
            TODO: Detail potential errors
        """
        self._client.set_config(self.keys)
        response = client.ping.get()
        return response
 
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
        if type(foldername) != str:
            raise ValueError
        elif foldername = "":
            raise ValueError
        elif len(foldername) <= 4:
            raise ValueError
        self.client.set_config(self.keys)
        response = client.fileManager.create_folder({"name": foldername})
        return response["id"]
    
    def upload_certificates(self, attendees: AttendeeManager,
                            folder_id: int = None,
                            status_func: BatchStatusFunc = None
                            ) -> str:
        """
        Upload certificates to Mailchimp.

        Blocking function that waits until the batch request completes.

        Args:
            attendees (AttendeeManager): The collection of attendees. Will be updated to include file URLs.
            folder_id (int): The ID of the folder to upload certificates to. If left as ``None``, will not put in a folder.
            status_func (BatchStatusFunc): Status update callback to inform caller of what certificates have been processed. Must take in status (string), then number of successes, followed by number failed. If left as ``None``, does nothing.
        
        Returns:
            str: The response_body_url to download the responses.
        
        Raises:
            TODO: Document potential errors.
        """
        mailchimp = Client()
        mailchimp.set_config(self.keys)
        operations = []
        for attendee in attendees:
            pdf_file = attendee.file_path()
            with open(pdf_file, "rb") as pdf_file:
                base64_file = base64.b64encode(pdf_file.read())
            operation = {
                "method": "POST",
                "path": f"/file-manager/files",
                "operation_id": str(attendee.get_id()),  #if there is an attribute to the attendee object for an id or else a name
                "body":({
                    "name"  : attendee.get_Fname() + '.pdf',
                    "file_data": base64_file
                    "folder_id": folder_id
                        })
                    }
            operations.append(operation)

        payload = {
                "operations": operations
                    }
        response = mailchimp.batches.start(payload)
        batch_id = response['id']
        response_batch = mailchimp.batches.status(batch_id)
        print(response_batch['response_body_url'])
        
    def update_contact_files(self, attendees: AttendeeManager,
                             status_func: BatchStatusFunc = None) -> str:
        """
        Updates the attendee contact file field.

        Blocking function that waits for batch request to complete.

        Args:
            attendees (AttendeeManager): The collection of attendees with file URLs.
            status_func (BatchStatusFunc): Callback to inform caller of progress, must take in status (string), then number of successes, then number failed. If ``None``, does nothing.

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
