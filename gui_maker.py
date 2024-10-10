import charvariables as cv

def settings_confirm(btn, app):
	charisma = app.getOptionBox("Charisma: ")
	
	app.setLabelFg("settings", "green")
	cv.character_charisma = charisma
	cv.dupe = app.getCheckBox('tourist')
	char_settings = "Charisma: %s, Dupe: %s" % (cv.character_charisma, cv.dupe)
	app.setLabel("settings", char_settings)

class create_ui:
    def __init__(self, app):
        self.app = app
        self.create_settings()

    def create_settings(self):
        self.app.startTab("Settings")
        self.app.setStretch("none")

        self.app.addLabelOptionBox("Charisma: ", itemlists.charisma_modifiers.keys() , 0, 0, 2)

        self.app.addLabel("dunce", "Are you a dupe?", 1, 0)
        self.app.setLabelPadding("dunce", 5, 2)
        self.app.setLabelAnchor("dunce", "w")
        self.app.setLabelWidth("dunce", 20)
        self.app.addNamedCheckBox("Yes!", "tourist", 1, 1)
        self.app.setCheckBoxAnchor("tourist", "e")

        self.app.addNamedButton("Save", "settings_confirm", settings_confirm(app=self.app), 2, 0)
        self.app.setButtonSticky("settings_confirm", "nw")

        self.app.stopTab()

