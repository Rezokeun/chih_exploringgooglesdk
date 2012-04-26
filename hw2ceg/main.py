#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
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
#
import webapp2
import string

form="""
<form method="post">
    <label>Input the ROT13 text here: <br><input type="text" name="text" value="%(text)s"></label>
    <br><br>
    <input type="submit">
</form>
"""

class MainHandler(webapp2.RequestHandler):
    def write_form(self,text=""):
	self.response.out.write(form % {"text":text})   

    def get(self):
        self.write_form()

    def post(self):
	form_input = self.request.get('text')
	rot_output = rot_13(form_input)
	self.write_form()
	
	
def rot_13(self):
    rot13_trans = string.maketrans("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
   	   		           "nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM")
    return self.translate(rot13_trans)

app = webapp2.WSGIApplication([('/', MainHandler)],
                              debug=True)



