from mycroft import MycroftSkill, intent_file_handler


class RecordThat(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('that.record.intent')
    def handle_that_record(self, message):
        self.speak_dialog('that.record')


def create_skill():
    return RecordThat()

