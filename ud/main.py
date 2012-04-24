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

form="""
<form method="post">
    What is your birthday?
    <br>
    <label>
	Month
	<input type="Text" name="Month">
    </label>

    <label>
	Day
	<input type="Text" name="Date">
    </label>
    
    <label>
	Year
	<input type="Text" name="Year">
    </label>
    <br>
    <br>
    <input type="submit">
</form>
"""

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write(form)

    def post(self):
	user_day = valid_day(self.request.get("Date"))
	user_year = valid_year(self.request.get("Year"))

	if not (user_day and user_year):
	    self.response.out(form)
	else:
	    self.response.out.write("Thanks! Good to go!")

app = webapp2.WSGIApplication([('/', MainHandler),],
                              debug=True)

def valid_day(day):
    if day and day.isdigit():
	day_int = int(day)
	if day_int > 0 and day_int <32:
	    return day_int

def valid_year(year):
    if year and year.isdigit():
	year_int = int(year)
	if year_int <2020 and year_int >1900:
	    return year_int
