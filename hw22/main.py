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
import hw22validation

form="""
<form method='post'>
    <label>SIGN UP FORM!</label>
    <br><br>
    <label>Username<input type='text' name='username'></label>
    <br>
    <label>Password<input type='password' name='password'></label>
    <br>
    <label>Verify Password<input type='password' name='verify_password'></label>
    <br>
    <label>Email<input type='text' name='email'></label>
    <br>
    <input type='submit' name='submit'>
</form>
"""

class MainHandler(webapp2.RequestHandler):
    def write_form(self):
	self.response.out.write(form)    

    def get(self):
	self.write_form()

    def post(self):
	user_n = self.request.get('username')
	
	user_validate = hw22validation.validate_username(user_n)

	if user_validate == 'False':
	    self.write_form()
	else:
	    self.redirect('/confirmed')

class ConfirmedHandler(webapp2.RequestHandler):
    def get(self):
	self.response.out.write('Looks good, thanks!')
	   

app = webapp2.WSGIApplication([('/', MainHandler), ('/confirmed', ConfirmedHandler)],
                              debug=True)




	
