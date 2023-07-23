from mycroft import MycroftSkill, intent_file_handler
import requests
import os


class RecordThat(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)


    @intent_file_handler('that.record.intent')
    def handle_that_record(self, message):
        try:
            res = requests.get('http://192.168.1.189:8050/clip')
            if res.status_code == 404:
                self.speak_dialog("failure")
            else:
                os.system('bash /opt/mycroft/skills/record-that-skill/play-sound.sh')
        except:
            self.speak_dialog("failure")
            return


def create_skill():
    return RecordThat()
