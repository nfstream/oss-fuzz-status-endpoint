"""
------------------------------------------------------------------------------------------------------------------------
status_update.py
Copyright (C) 2019-22 - NFStream Developers
This file is part of NFStream, a Flexible Network Data Analysis Framework (https://www.nfstream.org/).
NFStream is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later
version.
NFStream is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty
of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more details.
You should have received a copy of the GNU Lesser General Public License along with NFStream.
If not, see <http://www.gnu.org/licenses/>.
------------------------------------------------------------------------------------------------------------------------
"""

import urllib.request
import json

OSS_FUZZ_STATUS_URL = "https://oss-fuzz-build-logs.storage.googleapis.com/status.json"
NFSTREAM_PROJECT_ID = 492
STATUS_RESPONSE = {
    "schemaVersion": 1,
    "label": "oss-fuzz",
    "message": "",
    "color": "",
    "isError": ""
}

with urllib.request.urlopen(OSS_FUZZ_STATUS_URL) as status_url:
    status_data = json.load(status_url)["projects"][NFSTREAM_PROJECT_ID]
    if status_data["name"] == "nfstream":
        if str(status_data["history"][0]["success"]) == 'True':
            with open('status.json', 'w') as status_file:
                STATUS_RESPONSE["message"] = "fuzzing"
                STATUS_RESPONSE["color"] = "brightgreen"
                STATUS_RESPONSE["isError"] = "false"
                json.dump(STATUS_RESPONSE, status_file)
        else:
            with open('status.json', 'w') as status_file:
                STATUS_RESPONSE["message"] = "failing"
                STATUS_RESPONSE["color"] = "red"
                STATUS_RESPONSE["isError"] = "true"
                json.dump(STATUS_RESPONSE, status_file)