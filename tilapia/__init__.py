"""
Copyright (c) 2013, Sam Dodrill
All rights reserved.

This software is provided 'as-is', without any express or implied
warranty. In no event will the authors be held liable for any damages
arising from the use of this software.

Permission is granted to anyone to use this software for any purpose,
including commercial applications, and to alter it and redistribute it
freely, subject to the following restrictions:

    1. The origin of this software must not be misrepresented; you must not
    claim that you wrote the original software. If you use this software
    in a product, an acknowledgment in the product documentation would be
    appreciated but is not required.

    2. Altered source versions must be plainly marked as such, and must not be
    misrepresented as being the original software.

    3. This notice may not be removed or altered from any source
    distribution.
"""

import requests

class TilapiaAPI(object):
    def __init__(self, username, apikey):
        self.username = username
        self.apikey = apikey

    def list_VPS(self):
        pass

    def list_signup_VPS(self):
        pass

    def signup_VPS(self):
        pass

    def get_VPS_by_id(self, id):
        pass

    def get_VPS_templates(self):
        pass

    def deploy_VPS_template(self, id, imagename, rootpass, arch):
        pass

    def set_VPS_nickname(self, id):
        pass

    def enable_VPS_monitoring(self, id):
        pass

    def disable_VPS_monitoring(self, id):
        pass

    def get_HVM_iso(self, id):
        pass

    def set_HVM_iso(self, id):
        pass

    def set_HVM_bootorder(self, id):
        pass

    def set_HVM_nictype(self, id):
        pass

    def startup(self, id):
        pass

    def shutdown(self, id):
        pass

    def getstatus(self, id):
        pass

    def getjobs(seld, id):
        pass

