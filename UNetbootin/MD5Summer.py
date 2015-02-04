#!/usr/bin/env python
#
# Copyright 2015 ninjabong
# Copyright 2014 Timothy Sutton (original example)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""See docstring for MD5Summer class"""

import os
import hashlib

from autopkglib import Processor, ProcessorError

__all__ = ["MD5Summer"]


class MD5Summer(Processor):
    """This processor doesn't do anything useful. It is a demonstration of using
    a shared processor via a recipe repo."""
    description = __doc__
    input_variables = {
        "md5sum_path": {
            "required": True,
            "description": "The path to a file to be md5 checksummed."
        }
    }
    output_variables = {
        "md5sum_result": {
            "description": "The file's md5 checksum."
        }
    }

    def main(self):
        md5sum_result = hashlib.md5(open(self.env["md5sum_path"]).read()).hexdigest()
        
        try:
            module_file_path = os.path.abspath(__file__)
            self.output("The file's path to be checksummed is '%s'" % self.env["md5sum_path"])
            self.output("The file's md5 checksum result is %s" % md5sum_result)
            self.env["md5sum_result"] = md5sum_result
        except BaseException as err:
            # handle unexpected errors here
            raise ProcessorError(err)

if __name__ == "__main__":
    PROCESSOR = MD5Summer()
    PROCESSOR.execute_shell()
