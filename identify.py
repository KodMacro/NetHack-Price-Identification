#Version 0.2
#TODO: Show only valid effects when identifying. (Maybe)
#TODO: Change Healing potion price when NetHack 3.7 is released

from appJar import gui

import os
import math
import shelve
import charvariables as cv
import itemlists
import helperlists

def save_the_stuff(btn):
	savefile = app.getRadioButton("savefile")
	if savefile == "Save Slot 1":
		filename = "slot1.sav"
	elif savefile == "Save Slot 2":
		filename = "slot2.sav"
	elif savefile == "Save Slot 3":
		filename = "slot3.sav"
	proceed = False
	if os.path.exists(filename):
		confirm = app.yesNoBox("Confirm", "Are you sure you want to overwrite %s" % savefile)
		if confirm:
			proceed = True
	else:
		proceed = True
	if proceed:
		db = shelve.open(filename)
		db['scroll_spent_names'] = itemlists.scroll_spent_names
		db['scroll_spent_effects'] = itemlists.scroll_spent_effects
		db['scroll_names'] = itemlists.scroll_names
		db['scroll_effects'] = itemlists.scroll_effects
		db['potion_spent_names'] = itemlists.potion_spent_names
		db['potion_spent_effects'] = itemlists.potion_spent_effects
		db['potion_names'] = itemlists.potion_names
		db['potion_effects'] = itemlists.potion_effects
		db['wand_spent_names'] = itemlists.wand_spent_names
		db['wand_spent_effects'] = itemlists.wand_spent_effects
		db['wand_names'] = itemlists.wand_names
		db['wand_effects'] = itemlists.wand_effects
		db['ring_spent_names'] = itemlists.ring_spent_names
		db['ring_spent_effects'] = itemlists.ring_spent_effects
		db['ring_names'] = itemlists.ring_names
		db['ring_effects'] = itemlists.ring_effects
		db['spellbook_spent_names'] = itemlists.spellbook_spent_names
		db['spellbook_spent_effects'] = itemlists.spellbook_spent_effects
		db['spellbook_names'] = itemlists.spellbook_names
		db['spellbook_effects'] = itemlists.spellbook_effects
		db['cloak_spent_names'] = itemlists.cloak_spent_names
		db['cloak_spent_effects'] = itemlists.cloak_spent_effects
		db['cloak_names'] = itemlists.cloak_names
		db['cloak_effects'] = itemlists.cloak_effects
		db['boot_spent_names'] = itemlists.boot_spent_names
		db['boot_spent_effects'] = itemlists.boot_spent_effects
		db['boot_names'] = itemlists.boot_names
		db['boot_effects'] = itemlists.boot_effects
		db['charisma'] = cv.character_charisma

		slots_to_save = []
		for slot in helperlists.scroll_all_slots_list:
			if not is_slot_free(slot):
				slots_to_save.append((slot, app.getLabel(slot)))
		for slot in helperlists.potion_all_slots_list:
			if not is_slot_free(slot):
				slots_to_save.append((slot, app.getLabel(slot))) 
		for slot in helperlists.wand_all_slots_list:
			if not is_slot_free(slot):
				slots_to_save.append((slot, app.getLabel(slot)))
		for slot in helperlists.ring_all_slots_list:
			if not is_slot_free(slot):
				slots_to_save.append((slot, app.getLabel(slot)))
		for slot in helperlists.spellbook_all_slots_list:
			if not is_slot_free(slot):
				slots_to_save.append((slot, app.getLabel(slot)))
		for slot in helperlists.cloak_all_slots_list:
			if not is_slot_free(slot):
				slots_to_save.append((slot, app.getLabel(slot)))
		for slot in helperlists.boot_all_slots_list:
			if not is_slot_free(slot):
				slots_to_save.append((slot, app.getLabel(slot)))
		db['slots'] = slots_to_save
		
		db.close()

def load_the_stuff(btn):
	savefile = app.getRadioButton("savefile")
	if savefile == "Save Slot 1":
		filename = "slot1.sav"
	elif savefile == "Save Slot 2":
		filename = "slot2.sav"
	elif savefile == "Save Slot 3":
		filename = "slot3.sav"
	db = shelve.open(filename)
	itemlists.scroll_spent_names = db['scroll_spent_names']
	itemlists.scroll_spent_effects = db['scroll_spent_effects']
	itemlists.scroll_names = db['scroll_names']
	itemlists.scroll_effects = db['scroll_effects']
	itemlists.potion_spent_names = db['potion_spent_names']
	itemlists.potion_spent_effects = db['potion_spent_effects']
	itemlists.potion_names = db['potion_names']
	itemlists.potion_effects = db['potion_effects']
	itemlists.wand_spent_names = db['wand_spent_names']
	itemlists.wand_spent_effects = db['wand_spent_effects']
	itemlists.wand_names = db['wand_names']
	itemlists.wand_effects = db['wand_effects']
	itemlists.ring_spent_names = db['ring_spent_names']
	itemlists.ring_spent_effects = db['ring_spent_effects']
	itemlists.ring_names = db['ring_names']
	itemlists.ring_effects = db['ring_effects']
	itemlists.spellbook_spent_names = db['spellbook_spent_names']
	itemlists.spellbook_spent_effects = db['spellbook_spent_effects']
	itemlists.spellbook_names = db['spellbook_names']
	itemlists.spellbook_effects = db['spellbook_effects']
	itemlists.cloak_spent_names = db['cloak_spent_names']
	itemlists.cloak_spent_effects = db['cloak_spent_effects']
	itemlists.cloak_names = db['cloak_names']
	itemlists.cloak_effects = db['cloak_effects']
	itemlists.boot_spent_names = db['boot_spent_names']
	itemlists.boot_spent_effects = db['boot_spent_effects']
	itemlists.boot_names = db['boot_names']
	itemlists.boot_effects = db['boot_effects']
	cv.character_charisma = db['charisma']
	for slot in db['slots']:
		app.setLabel(slot[0], slot[1])

	app.changeOptionBox("Scroll name: ", itemlists.scroll_names)
	app.changeOptionBox("Potion name: ", itemlists.potion_names)
	app.changeOptionBox("Wand name: ", itemlists.wand_names)
	app.changeOptionBox("Ring name: ", itemlists.ring_names)
	app.changeOptionBox("Spellbook name: ", itemlists.spellbook_names)
	app.changeOptionBox("Cloak name: ", itemlists.cloak_names)
	app.changeOptionBox("Boot name: ", itemlists.boot_names)
	app.changeOptionBox("restore_scroll", itemlists.scroll_spent_names)
	app.changeOptionBox("restore_potion", itemlists.potion_spent_names)
	app.changeOptionBox("restore_wand", itemlists.wand_spent_names)
	app.changeOptionBox("restore_ring", itemlists.ring_spent_names)
	app.changeOptionBox("restore_spellbook", itemlists.spellbook_spent_names)
	app.changeOptionBox("restore_cloak", itemlists.cloak_spent_names)
	app.changeOptionBox("restore_boot", itemlists.boot_spent_names)

	for effect in itemlists.scroll_spent_effects:
		if effect[0] != "-":
			app.setLabel(effect, "\t=%s=" % effect)
	for effect in itemlists.potion_spent_effects:
		if effect[0] != "-":
			app.setLabel(effect, "\t=%s=" % effect)
	for effect in itemlists.wand_spent_effects:
		if effect[0] != "-":
			app.setLabel(effect, "\t=%s=" % effect)
	for effect in itemlists.ring_spent_effects:
		if effect[0] != "-":
			app.setLabel(effect, "\t=%s=" % effect)
	for effect in itemlists.spellbook_spent_effects:
		if effect[0] != "-":
			app.setLabel(effect, "\t=%s=" % effect)
	for effect in itemlists.cloak_spent_effects:
		if effect[0] != "-":
			app.setLabel(effect, "\t=%s=" % effect)
	for effect in itemlists.boot_spent_effects:
		if effect[0] != "-":
			app.setLabel(effect, "\t=%s=" % effect)
	
	db.close()

def check_file_slot(slot):

	if os.path.exists(slot):
		return True
	else:
		return False

def clear_slot(btn):
	savefile = app.getRadioButton("savefile")
	if savefile == "Save Slot 1":
		filename = "slot1.sav"
	elif savefile == "Save Slot 2":
		filename = "slot2.sav"
	elif savefile == "Save Slot 3":
		filename = "slot3.sav"
	os.remove(filename)

def my_round(x):
    return int(x + math.copysign(0.5, x))

def shopkeeper_switch(btn):
	if "greedy" in btn:
		cv.shopkeeper_attitude = "greedy"
		for button in helperlists.switch_to_greedy_buttons:
			app.hideButton(button)
		for button in helperlists.switch_to_dubious_buttons:
			app.showButton(button)
	elif "dubious" in btn:
		cv.shopkeeper_attitude = "dubious"
		for button in helperlists.switch_to_dubious_buttons:
			app.hideButton(button)
		for button in helperlists.switch_to_nice_buttons:
			app.showButton(button)
	elif "nice" in btn:
		cv.shopkeeper_attitude = "nice"
		for button in helperlists.switch_to_nice_buttons:
			app.hideButton(button)
		for button in helperlists.switch_to_greedy_buttons:
			app.showButton(button)
	update_prices()

def change_tab():
	tab_name = app.getTabbedFrameSelectedTab("TabbedFrame")
	if  tab_name != "Settings":
		update_prices()
	action_switch_btn(cv.shop_action)
	shopkeeper_switch(cv.shopkeeper_attitude)
	

def update_prices():
	if cv.character_charisma != 0:
		string_costs = []
		itemtype = app.getTabbedFrameSelectedTab("TabbedFrame").lower()
		if itemtype != "settings":
			if cv.shop_action == "buying":				
				costs_list = price_calculation(itemtype)
				string_costs = price_stringify(costs_list)
			elif cv.shop_action == "selling":
				if itemtype == "scrolls":
					base_list = itemlists.scroll_bases
				elif itemtype == "potions":
					base_list = itemlists.potion_bases
				elif itemtype == "wands":
					base_list = itemlists.wand_bases
				elif itemtype == "rings":
					base_list = itemlists.ring_bases
				elif itemtype == "spellbooks":
					base_list = itemlists.spellbook_bases
				elif itemtype == "cloaks":
					base_list = itemlists.cloak_bases
				elif itemtype == "boots":
					base_list = itemlists.boot_bases
				for base in base_list:
					item_cost = ""
					main_mod = 0
					if cv.dupe:
						main_mod = 1/3 #Dupes get offered 1/3 base price
					else:
						main_mod = 1/2 #Non-dupes get offered half base price
					if cv.shopkeeper_attitude == "dubious":
						item_cost = "%s (%s)" % (str(my_round(base * main_mod )), str(my_round(base * (main_mod * 0.75))))
					elif cv.shopkeeper_attitude == "greedy":
						item_cost = str(my_round(base * (main_mod * 0.75)))
					elif cv.shopkeeper_attitude == "nice":
						item_cost = str(my_round(base * main_mod ))
					#str(my_round(60 * 0.5 )) + "(" + str(my_round(60 * (0.5 * 0.75))
					string_costs.append(item_cost)
			place = 0
			for cost in string_costs:
				if itemtype != "rings" and place == 3:
					place += 1
				elif itemtype == "rings" and place == 2:
					place += 1
				if itemtype == "spellbooks":
					app.setButton("%s%s" % ("m", place), cost)
				else:	
					app.setButton("%s%s" % (itemtype[0], place), cost)
				place += 1

def price_stringify(itemtype):
	cost_list = []
	for item in itemtype:
		cost = str(item[0])
		cost += "(" + str(item[1])
		if cv.dupe:
			cost += "/" + str(item[2])
		cost += ")"
		cost_list.append(cost)
	return cost_list

def price_calculation(itemtype):
	char_mod = itemlists.charisma_modifiers[cv.character_charisma]

	itemcosts = []
	bases_list = []
	if itemtype == 'scrolls':
		bases_list = itemlists.scroll_bases
	elif itemtype == 'potions':
		bases_list = itemlists.potion_bases
	elif itemtype == "wands":
		bases_list = itemlists.wand_bases
	elif itemtype == "rings":
		bases_list = itemlists.ring_bases
	elif itemtype == "spellbooks":
		bases_list = itemlists.spellbook_bases
	elif itemtype == "cloaks":
		bases_list = itemlists.cloak_bases
	elif itemtype == "boots":
		bases_list = itemlists.boot_bases
	
	for base in bases_list:
		charmodded_base = str(my_round(base * char_mod))
		singlemodded_base = str(my_round(base * (char_mod * (4/3)))) # If the shopkeeper is greedy OR character is a dupe
		doublemodded_base = str(my_round(base * (char_mod * (4/3) * (4/3)))) # If the shopkeeper is greedy AND the character is a dupe
		itemcosts.append((charmodded_base, singlemodded_base, doublemodded_base))

	return itemcosts

def settings_confirm(btn):
	charisma = app.getOptionBox("Charisma: ")
	cv.character_charisma = charisma
	cv.dupe = app.getCheckBox('tourist')
	char_settings = "Charisma: %s, Dupe: %s" % (cv.character_charisma, cv.dupe)	
	for setting in helperlists.character_settings_list:
		app.setLabelFg(setting, "green")
		app.setLabel(setting, char_settings)
	
def action_switch_btn(btn):
	if 'selling' in btn:
		cv.shop_action = "selling"	
		for button in helperlists.switch_to_selling_buttons:
			app.hideButton(button)
		for button in helperlists.switch_to_buying_buttons:
			app.showButton(button)
	elif 'buying' in btn:
		cv.shop_action = "buying"
		for button in helperlists.switch_to_selling_buttons:
			app.showButton(button)
		for button in helperlists.switch_to_buying_buttons:
			app.hideButton(button)
	update_prices()

def cost_btn(btn):
	if "s" in btn:
		if app.getOptionBox("Scroll name: ") is not None:
			slot = get_next_free_slot(int(btn[-1:]), "scrolls")
			if slot:
				entry = "\t%s" % app.getOptionBox("Scroll name: ")
				app.setLabel(slot, entry)
				itemlists.scroll_names.remove(app.getOptionBox("Scroll name: "))
				app.changeOptionBox("Scroll name: ", itemlists.scroll_names)
	if "p" in btn:
		if app.getOptionBox("Potion name: ") is not None:
			slot = get_next_free_slot(int(btn[-1:]), "potions")
			if slot:
				entry = "\t%s" % app.getOptionBox("Potion name: ")
				app.setLabel(slot, entry)
				itemlists.potion_names.remove(app.getOptionBox("Potion name: "))
				app.changeOptionBox("Potion name: ", itemlists.potion_names)
	if "w" in btn:
		if app.getOptionBox("Wand name: ") is not None:
			slot = get_next_free_slot(int(btn[-1:]), "wands")
			if slot:
				entry = "\t%s" % app.getOptionBox("Wand name: ")
				app.setLabel(slot, entry)
				itemlists.wand_names.remove(app.getOptionBox("Wand name: "))
				app.changeOptionBox("Wand name: ", itemlists.wand_names)
	if "r" in btn:
		if app.getOptionBox("Ring name: ") is not None:
			slot = get_next_free_slot(int(btn[-1:]), "rings")
			if slot:
				entry = "\t%s" % app.getOptionBox("Ring name: ")
				app.setLabel(slot, entry)
				itemlists.ring_names.remove(app.getOptionBox("Ring name: "))
				app.changeOptionBox("Ring name: ", itemlists.ring_names)
	if "m" in btn:
		if app.getOptionBox("Spellbook name: ") is not None:
			slot = get_next_free_slot(int(btn[-1:]), "spellbooks")
			if slot:
				entry = "\t%s" % app.getOptionBox("Spellbook name: ")
				app.setLabel(slot, entry)
				itemlists.spellbook_names.remove(app.getOptionBox("Spellbook name: "))
				app.changeOptionBox("Spellbook name: ", itemlists.spellbook_names)
	if "c" in btn:
		if app.getOptionBox("Cloak name: ") is not None:
			slot = get_next_free_slot(int(btn[-1:]), "cloaks")
			if slot:
				entry = "\t%s" % app.getOptionBox("Cloak name: ")
				app.setLabel(slot, entry)
				itemlists.cloak_names.remove(app.getOptionBox("Cloak name: "))
				app.changeOptionBox("Cloak name: ", itemlists.cloak_names)
	if "b" in btn:
		if app.getOptionBox("Boot name: ") is not None:
			slot = get_next_free_slot(int(btn[-1:]), "boots")
			if slot:
				entry = "\t%s" % app.getOptionBox("Boot name: ")
				app.setLabel(slot, entry)
				itemlists.boot_names.remove(app.getOptionBox("Boot name: "))
				app.changeOptionBox("Boot name: ", itemlists.boot_names)

def id_item(btn):
	slot = app.getLabel(btn[9:])
	if "scroll" in btn:
		if not is_slot_free(slot):
			identify_window("scrolls", btn[9:])
	elif "potion" in btn:
		if not is_slot_free(slot):
			identify_window("potions", btn[9:])
	elif "wand" in btn:
		if not is_slot_free(slot):
			identify_window("wands", btn[9:])
	elif "ring" in btn:
		if not is_slot_free(slot):
			identify_window("rings", btn[9:])
	elif "spellbook" in btn:
		if not is_slot_free(slot):
			identify_window("spellbooks", btn[9:])
	elif "cloak" in btn:
		if not is_slot_free(slot):
			identify_window("cloaks", btn[9:])
	elif "boot" in btn:
		if not is_slot_free(slot):
			identify_window("boots", btn[9:])

def undo_item(btn):
	slot = btn[5:]
	if not is_slot_free(app.getLabel(slot)):
		if "scroll" in btn:
			itemlists.scroll_names.append(app.getLabel(slot).strip())
			refresh_list("scrolls")
		elif "potion" in btn:
			itemlists.potion_names.append(app.getLabel(slot).strip())
			refresh_list("potions")
		elif "wand" in btn:
			itemlists.wand_names.append(app.getLabel(slot).strip())
			refresh_list("wands")
		elif "ring" in btn:
			itemlists.ring_names.append(app.getLabel(slot).strip())
			refresh_list("rings")
		elif "spellbook" in btn:
			itemlists.spellbook_names.append(app.getLabel(slot).strip())
			refresh_list("spellbooks")
		elif "cloak" in btn:
			itemlists.cloak_names.append(app.getLabel(slot).strip())
			refresh_list("cloaks")
		elif "boot" in btn:
			itemlists.boot_names.append(app.getLabel(slot).strip())
			refresh_list("boots")
		if slot[-2:] == "_1":
				app.setLabel(slot, "\t-\t\t")
		else:
			app.setLabel(slot, "\t-")

def refresh_list(itemtype):
	if itemtype == "scrolls":
		itemlists.scroll_names.remove("-Scroll Names-")
		itemlists.scroll_names.sort()
		itemlists.scroll_names.insert(0, "-Scroll Names-")
		app.changeOptionBox("Scroll name: ", itemlists.scroll_names)
	elif itemtype == "potions":
		itemlists.potion_names.remove("-Potion Names-")
		itemlists.potion_names.sort()
		itemlists.potion_names.insert(0, "-Potion Names-")
		app.changeOptionBox("Potion name: ", itemlists.potion_names)
	elif itemtype == "wands":
		itemlists.wand_names.remove("-Wand Names-")
		itemlists.wand_names.sort()
		itemlists.wand_names.insert(0, "-Wand Names-")
		app.changeOptionBox("Wand name: ", itemlists.wand_names)
	elif itemtype == "rings":
		itemlists.ring_names.remove("-Ring Names-")
		itemlists.ring_names.sort()
		itemlists.ring_names.insert(0, "-Ring Names-")
		app.changeOptionBox("Ring name: ", itemlists.ring_names)
	elif itemtype == "spellbooks":
		itemlists.spellbook_names.remove("-Book Names-")
		itemlists.spellbook_names.sort()
		itemlists.spellbook_names.insert(0, "-Book Names-")
		app.changeOptionBox("Spellbook name: ", itemlists.spellbook_names)
	elif itemtype == "cloaks":
		itemlists.cloak_names.remove("-Cloak Names-")
		itemlists.cloak_names.sort()
		itemlists.cloak_names.insert(0, "-Cloak Names-")
		app.changeOptionBox("Cloak name: ", itemlists.cloak_names)
	elif itemtype == "boots":
		itemlists.boot_names.remove("-Boot Names-")
		itemlists.boot_names.sort()
		itemlists.boot_names.insert(0, "-Boot Names-")
		app.changeOptionBox("Boot name: ", itemlists.boot_names)

def identify_window(itemtype, slot):
	effect_list = []
	if itemtype == "scrolls":
		effect_list = itemlists.scroll_effects
	elif itemtype == "potions":
		effect_list = itemlists.potion_effects
	elif itemtype == "wands":
		effect_list = itemlists.wand_effects
	elif itemtype == "rings":
		effect_list = itemlists.ring_effects
	elif itemtype == "spellbooks":
		effect_list = itemlists.spellbook_effects
	elif itemtype == "cloaks":
		effect_list = itemlists.cloak_effects
	elif itemtype == "boots":
		effect_list = itemlists.boot_effects
	try:
		app.startSubWindow("Identify")
		app.setSize(400, 150)
		app.setLocation(960 - 200, 540 - 75)
		app.setBg("white")
		app.setStopFunction(kill_windows)
	except Exception:
		app.openSubWindow("Identify")
	itemname = app.getLabel(slot).strip()
	app.addLabel("What was the %s?" % itemname, colspan=2)
	app.addOptionBox("items", effect_list, colspan=2)
	button_parameters = "%s,%s" % (itemname, slot)
	app.addNamedButton("Confirm", button_parameters, identify_item, 2, 0)
	app.addButton("Cancel", kill_windows, 2, 1)
	app.showSubWindow("Identify")
	app.stopSubWindow()

def identify_item(btn):
	parameters = btn.split(",")
	itemname = app.getOptionBox("items")
	if itemname is not None:
		if "scroll" in parameters[1]:
			itemlists.scroll_spent_names.append(parameters[0])
			app.changeOptionBox("restore_scroll", itemlists.scroll_spent_names)
			erase_left("erase_scroll_%s" % itemname)
		elif "potion" in parameters[1]:
			itemlists.potion_spent_names.append(parameters[0])
			app.changeOptionBox("restore_potion", itemlists.potion_spent_names)
			erase_left("erase_potion_%s" % itemname)
		elif "wand" in parameters[1]:
			itemlists.wand_spent_names.append(parameters[0])
			app.changeOptionBox("restore_wand", itemlists.wand_spent_names)
			erase_left("erase_wand_%s" % itemname)
		elif "ring" in parameters[1]:
			itemlists.ring_spent_names.append(parameters[0])
			app.changeOptionBox("restore_ring", itemlists.ring_spent_names)
			erase_left("erase_ring_%s" % itemname)
		elif "spellbook" in parameters[1]:
			itemlists.spellbook_spent_names.append(parameters[0])
			app.changeOptionBox("restore_spellbook", itemlists.spellbook_spent_names)
			erase_left("erase_spellbook_%s" % itemname)
		elif "cloak" in parameters[1]:
			itemlists.cloak_spent_names.append(parameters[0])
			app.changeOptionBox("restore_cloak", itemlists.cloak_spent_names)
			erase_left("erase_cloak_%s" % itemname)
		elif "boot" in parameters[1]:
			itemlists.boot_spent_names.append(parameters[0])
			app.changeOptionBox("restore_boot", itemlists.boot_spent_names)
			erase_left("erase_boot_%s" % itemname)
		if parameters[1][-2:] == "_1":
			app.setLabel(parameters[1], "\t-\t\t")
		else:
			app.setLabel(parameters[1], "\t-")

		
		kill_windows()

def kill_windows():
	app.destroyAllSubWindows()

def erase_left(btn):
	place = None
	if "potion" in btn:
		place = btn[13:]
		itemname = app.getLabel(place).strip()
		spent_list = itemlists.potion_spent_effects
		effects_list = itemlists.potion_effects
	elif "scroll" in btn:
		place = btn[13:]
		itemname = app.getLabel(place).strip()
		spent_list = itemlists.scroll_spent_effects
		effects_list = itemlists.scroll_effects
	elif "wand" in btn:
		place = btn[11:]
		itemname = app.getLabel(place).strip()
		spent_list = itemlists.wand_spent_effects
		effects_list = itemlists.wand_effects
	elif "ring" in btn:
		place = btn[11:]
		itemname = app.getLabel(place).strip()
		spent_list = itemlists.ring_spent_effects
		effects_list = itemlists.ring_effects
	elif "spellbook" in btn:
		place = btn[16:]
		itemname = app.getLabel(place).strip()
		spent_list = itemlists.spellbook_spent_effects
		effects_list = itemlists.spellbook_effects
	elif "cloak" in btn:
		place = btn[12:]
		itemname = app.getLabel(place).strip()
		spent_list = itemlists.cloak_spent_effects
		effects_list = itemlists.cloak_effects
	elif "boot" in btn:
		place = btn[11:]
		itemname = app.getLabel(place).strip()
		spent_list = itemlists.boot_spent_effects
		effects_list = itemlists.boot_effects
	if itemname[0] == "=":
		itemname = itemname.replace("=", "")
		changed_string = "\t%s" % itemname
		spent_list.remove(itemname)
		effects_list.append(itemname)
	else:
		changed_string = "\t=%s=" % itemname
		spent_list.append(itemname)
		effects_list.remove(itemname)
	spent_list.sort()
	effects_list.sort()
	app.setLabel(place, changed_string)

def restore_name(btn):
	if "scroll" in btn:
		if app.getOptionBox("restore_scroll") is not None:
			itemlists.scroll_spent_names.remove(app.getOptionBox("restore_scroll"))
			itemlists.scroll_names.append(app.getOptionBox("restore_scroll"))
			refresh_list("scrolls")
			app.changeOptionBox("restore_scroll", itemlists.scroll_spent_names)
	elif "potion" in btn:
		if app.getOptionBox("restore_potion") is not None:
			itemlists.potion_spent_names.remove(app.getOptionBox("restore_potion"))
			itemlists.potion_names.append(app.getOptionBox("restore_potion"))
			refresh_list("potions")
			app.changeOptionBox("restore_potion", itemlists.potion_spent_names)
	elif "wand" in btn:
		if app.getOptionBox("restore_wand") is not None:
			itemlists.wand_spent_names.remove(app.getOptionBox("restore_wand"))
			itemlists.wand_names.append(app.getOptionBox("restore_wand"))
			refresh_list("wands")
			app.changeOptionBox("restore_wand", itemlists.wand_spent_names)
	elif "ring" in btn:
		if app.getOptionBox("restore_ring") is not None:
			itemlists.ring_spent_names.remove(app.getOptionBox("restore_ring"))
			itemlists.ring_names.append(app.getOptionBox("restore_ring"))
			refresh_list("rings")
			app.changeOptionBox("restore_ring", itemlists.ring_spent_names)
	elif "spellbook" in btn:
		if app.getOptionBox("restore_spellbook") is not None:
			itemlists.spellbook_spent_names.remove(app.getOptionBox("restore_spellbook"))
			itemlists.spellbook_names.append(app.getOptionBox("restore_spellbook"))
			refresh_list("spellbooks")
			app.changeOptionBox("restore_spellbook", itemlists.spellbook_spent_names)
	elif "cloak" in btn:
		if app.getOptionBox("restore_cloak") is not None:
			itemlists.cloak_spent_names.remove(app.getOptionBox("restore_cloak"))
			itemlists.cloak_names.append(app.getOptionBox("restore_cloak"))
			refresh_list("cloaks")
			app.changeOptionBox("restore_cloak", itemlists.cloak_spent_names)
	elif "boot" in btn:
		if app.getOptionBox("restore_boot") is not None:
			itemlists.boot_spent_names.remove(app.getOptionBox("restore_boot"))
			itemlists.boot_names.append(app.getOptionBox("restore_boot"))
			refresh_list("boots")
			app.changeOptionBox("restore_boot", itemlists.boot_spent_names)
	


def is_slot_free(slot_text):
	if slot_text == "\t-" or slot_text == "\t-\t\t":
		return True
	else:
		return False

def get_next_free_slot(tier, itemtype):
	slot_names = []
	if itemtype == "scrolls":
		slot_names = helperlists.scroll_slot_names[tier]
	elif itemtype == "potions":
		slot_names = helperlists.potion_slot_names[tier]
	elif itemtype == "wands":
		slot_names = helperlists.wand_slot_names[tier]
	elif itemtype == "rings":
		slot_names = helperlists.ring_slot_names[tier]
	elif itemtype == "spellbooks":
		slot_names = helperlists.spellbook_slot_names[tier]
	elif itemtype == "cloaks":
		slot_names = helperlists.cloak_slot_names[tier]
	elif itemtype == "boots":
		slot_names = helperlists.boot_slot_names[tier]
	
	for slot in slot_names:
			if is_slot_free(app.getLabel(slot)):
				return slot
	return False


app = gui("Nethack Price Identification", "1020x720")
app.setLocation(960 - 500, 540 - 355)
app.setBg("white")
app.setSticky("nw")

app.startTabbedFrame("TabbedFrame")
app.setTabbedFrameSticky("TabbedFrame", "nw")
app.setTabbedFrameActiveBg("TabbedFrame", "white")
app.setTabbedFrameChangeCommand("TabbedFrame", change_tab)
print("Setting up interface. This takes a little while. Please stand by.")
print("Building settings.")
app.startTab("Settings")
app.setStretch("none")

app.addLabelOptionBox("Charisma: ", itemlists.charisma_modifiers.keys() , 0, 0, 2)

app.addLabel("dunce", "Are you a dupe?", 1, 0)
app.setLabelPadding("dunce", 5, 2)
app.setLabelAnchor("dunce", "w")
app.setLabelWidth("dunce", 20)
app.addNamedCheckBox("Yes!", "tourist", 1, 1)
app.setCheckBoxAnchor("tourist", "e")
app.addNamedButton("Save", "settings_confirm", settings_confirm, 2, 0)
app.setButtonSticky("settings_confirm", "nw")

app.addLabel("slots", "Save slots:", 4, 0)
#.addSaveEntry("savefile", 5, 0)
app.setSticky("w")
app.addRadioButton("savefile", "Save Slot 1", 6, 0)
if check_file_slot("slot1.sav"):
	app.addLabel("save1label", "*exists*", 6, 1)
	app.setLabelFg("save1label", "red")
app.addRadioButton("savefile", "Save Slot 2", 7, 0)
if check_file_slot("slot2.sav"):
	app.addLabel("save2label", "*exists*", 7, 1)
	app.setLabelFg("save2label", "red")
app.addRadioButton("savefile", "Save Slot 3", 8, 0)
if check_file_slot("slot3.sav"):
	app.addLabel("save3label", "*exists*", 8, 1)
	app.setLabelFg("save3label", "red")

app.addButton("Store", save_the_stuff)
app.addButton("Load", load_the_stuff)
app.addButton("Scrap", clear_slot)


app.stopTab()
print("Building scrolls..")
app.startTab("Scrolls")
app.setStretch("none")
app.setSticky("nw")
char_settings = "Charisma: %s, Dupe: %s" % (cv.character_charisma, cv.dupe)
app.addLabel("settings_scrolls", char_settings, 0, 0, 3)
app.setLabelTooltip("settings_scrolls", "If this is red make sure you've entered the correct charisma in settings.")
app.setLabelFg("settings_scrolls", "red")

app.addNamedButton("I'm Selling", "switch_to_buying_scrolls", action_switch_btn, 1, 0, 3)
app.setButtonBg("switch_to_buying_scrolls", "red")

app.addNamedButton("I'm Buying", "switch_to_selling_scrolls", action_switch_btn, 1, 0, 3)
app.setButtonBg("switch_to_selling_scrolls", "green")

app.addNamedButton("Greedy", "switch_to_dubious_scrolls", shopkeeper_switch, 1, 1, 3)
app.setButtonBg("switch_to_dubious_scrolls", "Black")
app.setButtonFg("switch_to_dubious_scrolls", "White")
app.hideButton("switch_to_dubious_scrolls")
app.setButtonTooltip("switch_to_dubious_scrolls", "The shopkeeper is greedy, meaning he'll offer less for unidentifed items.")

app.addNamedButton("Dubious", "switch_to_nice_scrolls", shopkeeper_switch, 1, 1, 3)
app.setButtonBg("switch_to_nice_scrolls", "Red")
app.setButtonTooltip("switch_to_nice_scrolls", "The shopkeeper is dubious, you don't know if he offers less for unidentified items")

app.addNamedButton("Nice!", "switch_to_greedy_scrolls", shopkeeper_switch, 1, 1, 3)
app.setButtonBg("switch_to_greedy_scrolls", "Green")
app.hideButton("switch_to_greedy_scrolls")
app.setButtonTooltip("switch_to_greedy_scrolls", "The shopkeeper is nice, meaning he'll offer top zorkmid for unidentified items.")

app.addLabelOptionBox("Scroll name: ", itemlists.scroll_names, 2, 0, 3)
app.addNamedButton("Tier 1", "s0", cost_btn, 3, 0)
app.addNamedButton("Tier 2", "s1", cost_btn, 3, 1)
app.addNamedButton("Tier 3", "s2", cost_btn, 4, 0)
app.addNamedButton("Tier 4", "s4", cost_btn, 4, 1)
app.addNamedButton("Duplicate?", "s3", cost_btn, 4, 2)
app.addNamedButton("Tier 5", "s5", cost_btn, 5, 0)
app.addNamedButton("Tier 6", "s6", cost_btn, 5, 1)
app.addNamedButton("Tier 7", "s7", cost_btn, 6, 0)
app.setButtonTooltip("s3", "If the price is in two buttons push here.")
app.setButtonBg("s2", "light coral")
app.setButtonBg("s4", "light coral")

app.addNamedButton("Restore", "restore_scroll_btn", restore_name, 7, 0)
app.addOptionBox("restore_scroll", itemlists.scroll_spent_names, 7, 1, colspan=2)

app.startScrollPane("scroll_display", 0, 3, rowspan=29)
app.setScrollPaneHeight("scroll_display", 690)
app.setSticky("nw")

slot_count = 0
tier_slots = []

for tier in helperlists.scroll_slot_names:
	tier_slots.append(len(tier))
for row in range(sum(tier_slots) + len(itemlists.scrolls_by_tier) + 1):
	if row == 0:
		app.addLabel("scroll_tier1", "Tier 1")
	elif row == tier_slots[0] + 1:
		app.addLabel("scroll_tier2", "Tier 2")
	elif row == sum(tier_slots[:2]) + 2:
		app.addLabel("scroll_tier3", "Tier 3")
	elif row == sum(tier_slots[:3]) + 3:
		app.addLabel("scroll_tier3/4", "Tier 3-4")
	elif row == sum(tier_slots[:4]) + 4:
		app.addLabel("scroll_tier4", "Tier 4")
	elif row == sum(tier_slots[:5]) + 5:
		app.addLabel("scroll_tier5", "Tier 5")
	elif row == sum(tier_slots[:6]) + 6:
		app.addLabel("scroll_tier6", "Tier 6")
	elif row == sum(tier_slots[:7]) + 7:
		app.addLabel("scroll_tier7", "Tier 7")

	else:
		slot = helperlists.scroll_all_slots_list[slot_count]
		if slot[-2:] == "_1":
			app.addLabel(slot, "\t-\t\t")
		else:
			app.addLabel(slot, "\t-")
		app.addImage("undo_%s" % slot, 'assets/undo.gif', row, 1)
		app.setImageSubmitFunction("undo_%s" % slot, undo_item)
		app.addImage("identify_%s" % slot, 'assets/id.gif', row, 2)
		app.setImageSubmitFunction("identify_%s" % slot, id_item)
		slot_count += 1
app.stopScrollPane()

app.startFrame("scrolls_left", 0, 4, rowspan=29)
app.setFrameHeight("scrolls_left", 700)
app.setSticky("nw")

effect_count = 0

for row in range(28):
	if row == 0:
		app.addLabel("scroll_left_tier1", "Tier 1")
	elif row == 2:
		app.addLabel("scroll_left_tier2", "Tier 2")
	elif row == 4:
		app.addLabel("scroll_left_tier3", "Tier 3")
	elif row == 6:
		app.addLabel("scroll_left_tier4", "Tier 4")
	elif row == 9:
		app.addLabel("scroll_left_tier5", "Tier 5")
	elif row == 18:
		app.addLabel("scroll_left_tier6", "Tier 6")
	elif row == 23:
		app.addLabel("scroll_left_tier7", "Tier 7")
	else:
		effect = itemlists.scroll_effects_ordered[effect_count]
		app.addLabel(effect, "\t%s" % effect)
		app.addImage("erase_scroll_%s" % effect, 'assets/change.gif', row, 1)
		app.setImageSubmitFunction("erase_scroll_%s" % effect, erase_left)
		effect_count += 1
app.stopFrame()
app.stopTab()
print("Building potions...")
app.startTab("Potions")
app.setStretch("none")
app.setSticky("nw")
char_settings = "Charisma: %s, Dupe: %s" % (cv.character_charisma, cv.dupe)
app.addLabel("settings_potions", char_settings, 0, 0, 3)
app.setLabelTooltip("settings_potions", "If this is red make sure you've entered the correct charisma in settings.")
app.setLabelFg("settings_potions", "red")

app.addNamedButton("I'm Selling", "switch_to_buying_potions", action_switch_btn, 1, 0)
app.setButtonBg("switch_to_buying_potions", "red")

app.addNamedButton("I'm Buying", "switch_to_selling_potions", action_switch_btn, 1, 0)
app.setButtonBg("switch_to_selling_potions", "green")

app.addNamedButton("Greedy", "switch_to_dubious_potions", shopkeeper_switch, 1, 1)
app.setButtonBg("switch_to_dubious_potions", "Black")
app.setButtonFg("switch_to_dubious_potions", "White")
app.hideButton("switch_to_dubious_potions")
app.setButtonTooltip("switch_to_dubious_potions", "The shopkeeper is greedy, meaning he'll offer less for unidentifed items.")

app.addNamedButton("Dubious", "switch_to_nice_potions", shopkeeper_switch, 1, 1)
app.setButtonBg("switch_to_nice_potions", "Red")
app.setButtonTooltip("switch_to_nice_potions", "The shopkeeper is dubious, you don't know if he offers less for unidentified items")

app.addNamedButton("Nice!", "switch_to_greedy_potions", shopkeeper_switch, 1, 1)
app.setButtonBg("switch_to_greedy_potions", "Green")
app.hideButton("switch_to_greedy_potions")
app.setButtonTooltip("switch_to_greedy_potions", "The shopkeeper is nice, meaning he'll offer top zorkmid for unidentified items.")

app.addLabelOptionBox("Potion name: ", itemlists.potion_names, 2, 0, 3)
app.addNamedButton("Tier 1", "p0", cost_btn, 3, 0)
app.addNamedButton("Tier 2", "p1", cost_btn, 3, 1)
app.addNamedButton("Tier 3", "p2", cost_btn, 4, 0)
app.addNamedButton("Tier 4", "p4", cost_btn, 4, 1)
app.addNamedButton("Duplicate?", "p3", cost_btn, 4, 2)
app.addNamedButton("Tier 5", "p5", cost_btn, 5, 0)
app.addNamedButton("Tier 6", "p6", cost_btn, 5, 1)
app.setButtonTooltip("p3", "If the price is in two buttons push here.")
app.setButtonBg("p2", "light coral")
app.setButtonBg("p4", "light coral")

app.addNamedButton("Restore", "restore_potion_btn", restore_name, 7, 0)
app.addOptionBox("restore_potion", itemlists.potion_spent_names, 7, 1, colspan=2)

app.startScrollPane("potion_display", 0, 3, rowspan=29)
app.setScrollPaneHeight("potion_display", 690)
app.setSticky("nw")

slot_count = 0
tier_slots = []
for tier in helperlists.potion_slot_names:
	tier_slots.append(len(tier))
for row in range(sum(tier_slots) + len(itemlists.potions_by_tier) + 1):
	if row == 0:
		app.addLabel("potion_tier1", "Tier 1")
	elif row == tier_slots[0] + 1:
		app.addLabel("potion_tier2", "Tier 2")
	elif row == sum(tier_slots[:2]) + 2:
		app.addLabel("potion_tier3", "Tier 3")
	elif row == sum(tier_slots[:3]) + 3:
		app.addLabel("potion_tier3/4", "Tier 3-4")
	elif row == sum(tier_slots[:4]) + 4:
		app.addLabel("potion_tier4", "Tier 4")
	elif row == sum(tier_slots[:5]) + 5:
		app.addLabel("potion_tier5", "Tier 5")
	elif row == sum(tier_slots[:6]) + 6:
		app.addLabel("potion_tier6", "Tier 6")

	else:
		slot = helperlists.potion_all_slots_list[slot_count]
		if slot[-2:] == "_1":
			app.addLabel(slot, "\t-\t\t")
		else:
			app.addLabel(slot, "\t-")
		app.addImage("undo_%s" % slot, 'assets/undo.gif', row, 1)
		app.setImageSubmitFunction("undo_%s" % slot, undo_item)
		app.addImage("identify_%s" % slot, 'assets/id.gif', row, 2)
		app.setImageSubmitFunction("identify_%s" % slot, id_item)
		slot_count += 1

app.stopScrollPane()

app.startFrame("potions_left", 0, 4, rowspan=29)
app.setSticky("nw")

effect_count = 0

for row in range(31):
	if row == 0:
		app.addLabel("potion_left_tier1", "Tier 1")
	elif row == 5:
		app.addLabel("potion_left_tier2", "Tier 2")
	elif row == 12:
		app.addLabel("potion_left_tier3", "Tier 3")
	elif row == 18:
		app.addLabel("potion_left_tier4", "Tier 4")
	elif row == 24:
		app.addLabel("potion_left_tier5", "Tier 5")
	elif row == 27:
		app.addLabel("potion_left_tier6", "Tier 6")
	else:
		effect = itemlists.potion_effects_ordered[effect_count]
		app.addLabel(effect, "\t%s" % effect)
		app.addImage("erase_potion_%s" % effect, 'assets/change.gif', row, 1)
		app.setImageSubmitFunction("erase_potion_%s" % effect, erase_left)
		effect_count += 1

app.stopFrame()
app.stopTab()
print("Building wands....")
app.startTab("Wands")
app.setStretch("none")
app.setSticky("nw")
char_settings = "Charisma: %s, Dupe: %s" % (cv.character_charisma, cv.dupe)
app.addLabel("settings_wands", char_settings, 0, 0, 3)
app.setLabelTooltip("settings_wands", "If this is red make sure you've entered the correct charisma in settings.")
app.setLabelFg("settings_wands", "red")

app.addNamedButton("I'm Selling", "switch_to_buying_wands", action_switch_btn, 1, 0)
app.setButtonBg("switch_to_buying_wands", "red")

app.addNamedButton("I'm Buying", "switch_to_selling_wands", action_switch_btn, 1, 0)
app.setButtonBg("switch_to_selling_wands", "green")

app.addNamedButton("Greedy", "switch_to_dubious_wands", shopkeeper_switch, 1, 1)
app.setButtonBg("switch_to_dubious_wands", "Black")
app.setButtonFg("switch_to_dubious_wands", "White")
app.hideButton("switch_to_dubious_wands")
app.setButtonTooltip("switch_to_dubious_wands", "The shopkeeper is greedy, meaning he'll offer less for unidentifed items.")

app.addNamedButton("Dubious", "switch_to_nice_wands", shopkeeper_switch, 1, 1)
app.setButtonBg("switch_to_nice_wands", "Red")
app.setButtonTooltip("switch_to_nice_wands", "The shopkeeper is dubious, you don't know if he offers less for unidentified items")

app.addNamedButton("Nice!", "switch_to_greedy_wands", shopkeeper_switch, 1, 1)
app.setButtonBg("switch_to_greedy_wands", "Green")
app.hideButton("switch_to_greedy_wands")
app.setButtonTooltip("switch_to_greedy_wands", "The shopkeeper is nice, meaning he'll offer top zorkmid for unidentified items.")

app.addLabelOptionBox("Wand name: ", itemlists.wand_names, 2, 0, 3)
app.addNamedButton("Tier 1", "w0", cost_btn, 3, 0)
app.addNamedButton("Tier 2", "w1", cost_btn, 3, 1)
app.addNamedButton("Tier 3", "w2", cost_btn, 4, 0)
app.addNamedButton("Tier 4", "w4", cost_btn, 4, 1)
app.addNamedButton("Duplicate?", "w3", cost_btn, 4, 2)
app.addNamedButton("Tier 5", "w5", cost_btn, 5, 0)
app.setButtonTooltip("w3", "If the price is in two buttons push here.")
app.setButtonBg("w1", "light coral")
app.setButtonBg("w4", "light coral")

app.addNamedButton("Restore", "restore_wand_btn", restore_name, 7, 0)
app.addOptionBox("restore_wand", itemlists.wand_spent_names, 7, 1, colspan=2)

app.startScrollPane("wand_display", 0, 3, rowspan=29)
app.setScrollPaneHeight("wand_display", 690)
app.setSticky("nw")

slot_count = 0
tier_slots = []
for tier in helperlists.wand_slot_names:
	tier_slots.append(len(tier))
for row in range(sum(tier_slots) + len(itemlists.wands_by_tier) + 1):
	if row == 0:
		app.addLabel("wand_tier1", "Tier 1")
	elif row == tier_slots[0] + 1:
		app.addLabel("wand_tier2", "Tier 2")
	elif row == sum(tier_slots[:2]) + 2:
		app.addLabel("wand_tier3", "Tier 3")
	elif row == sum(tier_slots[:3]) + 3:
		app.addLabel("wand_tier2/4", "Tier 2-4")
	elif row == sum(tier_slots[:4]) + 4:
		app.addLabel("wand_tier4", "Tier 4")
	elif row == sum(tier_slots[:5]) + 5:
		app.addLabel("wand_tier5", "Tier 5")
	else:
		slot = helperlists.wand_all_slots_list[slot_count]
		if slot[-2:] == "_1":
			app.addLabel(slot, "\t-\t\t")
		else:
			app.addLabel(slot, "\t-")
		app.addImage("undo_%s" % slot, 'assets/undo.gif', row, 1)
		app.setImageSubmitFunction("undo_%s" % slot, undo_item)
		app.addImage("identify_%s" % slot, 'assets/id.gif', row, 2)
		app.setImageSubmitFunction("identify_%s" % slot, id_item)
		slot_count += 1

app.stopScrollPane()

#app.startFrame("wands_left", 0, 4, rowspan=29)
app.startScrollPane("wands_left", 0, 4, rowspan=29)
app.setScrollPaneHeight("wands_left", 690)
app.setSticky("nw")

effect_count = 0
wands = itemlists.wands_by_tier
for row in range(len(itemlists.wand_effects_ordered) + len(itemlists.wands_by_tier)):
	if row == 0:
		app.addLabel("wand_left_tier1", "Tier 1")
	elif row == len(wands[0]) + 1:
		app.addLabel("wand_left_tier2", "Tier 2")
	elif row == len(wands[0]) + len(wands[1])  + 2:
		app.addLabel("wand_left_tier3", "Tier 3")
	elif row == len(wands[0]) + len(wands[1]) + len(wands[2])  + 3:
		app.addLabel("wand_left_tier4", "Tier 4")
	elif row == len(wands[0]) + len(wands[1]) + len(wands[2]) + len(wands[3])  + 4:
		app.addLabel("wand_left_tier5", "Tier 5")
	else:
		effect = itemlists.wand_effects_ordered[effect_count]
		app.addLabel(effect, "\t%s" % effect)
		app.addImage("erase_wand_%s" % effect, 'assets/change.gif', row, 1)
		app.setImageSubmitFunction("erase_wand_%s" % effect, erase_left)
		effect_count += 1
app.stopScrollPane()
#app.stopFrame()
app.stopTab()
print("Building rings......")
app.startTab("Rings")
app.setStretch("none")
app.setSticky("nw")
char_settings = "Charisma: %s, Dupe: %s" % (cv.character_charisma, cv.dupe)
app.addLabel("settings_rings", char_settings, 0, 0, 3)
app.setLabelTooltip("settings_rings", "If this is red make sure you've entered the correct charisma in settings.")
app.setLabelFg("settings_rings", "red")

app.addNamedButton("I'm Selling", "switch_to_buying_rings", action_switch_btn, 1, 0)
app.setButtonBg("switch_to_buying_rings", "red")

app.addNamedButton("I'm Buying", "switch_to_selling_rings", action_switch_btn, 1, 0)
app.setButtonBg("switch_to_selling_rings", "green")

app.addNamedButton("Greedy", "switch_to_dubious_rings", shopkeeper_switch, 1, 1)
app.setButtonBg("switch_to_dubious_rings", "Black")
app.setButtonFg("switch_to_dubious_rings", "White")
app.hideButton("switch_to_dubious_rings")
app.setButtonTooltip("switch_to_dubious_rings", "The shopkeeper is greedy, meaning he'll offer less for unidentifed items.")

app.addNamedButton("Dubious", "switch_to_nice_rings", shopkeeper_switch, 1, 1)
app.setButtonBg("switch_to_nice_rings", "Red")
app.setButtonTooltip("switch_to_nice_rings", "The shopkeeper is dubious, you don't know if he offers less for unidentified items")

app.addNamedButton("Nice!", "switch_to_greedy_rings", shopkeeper_switch, 1, 1)
app.setButtonBg("switch_to_greedy_rings", "Green")
app.hideButton("switch_to_greedy_rings")
app.setButtonTooltip("switch_to_greedy_rings", "The shopkeeper is nice, meaning he'll offer top zorkmid for unidentified items.")

app.addLabelOptionBox("Ring name: ", itemlists.ring_names, 2, 0, 3)
app.addNamedButton("Tier 1", "r0", cost_btn, 3, 0)
app.addNamedButton("Tier 2", "r1", cost_btn, 3, 1)
app.addNamedButton("Tier 3", "r3", cost_btn, 4, 0)
app.addNamedButton("Tier 4", "r4", cost_btn, 4, 1)
app.addNamedButton("Duplicate?", "r2", cost_btn, 4, 2)
app.setButtonTooltip("r3", "If the price is in two buttons push here.")
app.setButtonBg("r1", "light coral")
app.setButtonBg("r3", "light coral")

app.addNamedButton("Restore", "restore_ring_btn", restore_name, 7, 0)
app.addOptionBox("restore_ring", itemlists.ring_spent_names, 7, 1, colspan=2)

app.startScrollPane("ring_display", 0, 3, rowspan=29)
app.setScrollPaneHeight("ring_display", 690)
app.setSticky("nw")

slot_count = 0
tier_slots = []
for tier in helperlists.ring_slot_names:
	tier_slots.append(len(tier))
for row in range(sum(tier_slots) + len(itemlists.rings_by_tier) + 1):
	if row == 0:
		app.addLabel("ring_tier1", "Tier 1")
	elif row == tier_slots[0] + 1:
		app.addLabel("ring_tier2", "Tier 2")
	elif row == sum(tier_slots[:2]) + 2:
		app.addLabel("ring_tier2/3", "Tier 2-3")
	elif row == sum(tier_slots[:3]) + 3:
		app.addLabel("ring_tier3", "Tier 3")
	elif row == sum(tier_slots[:4]) + 4:
		app.addLabel("ring_tier4", "Tier 4")
	else:
		slot = helperlists.ring_all_slots_list[slot_count]
		if slot[-2:] == "_1":
			app.addLabel(slot, "\t-\t\t")
		else:
			app.addLabel(slot, "\t-")
		app.addImage("undo_%s" % slot, 'assets/undo.gif', row, 1)
		app.setImageSubmitFunction("undo_%s" % slot, undo_item)
		app.addImage("identify_%s" % slot, 'assets/id.gif', row, 2)
		app.setImageSubmitFunction("identify_%s" % slot, id_item)
		slot_count += 1

app.stopScrollPane()

app.startScrollPane("rings_left", 0, 4, rowspan=29)
app.setSticky("nw")

effect_count = 0
rings = itemlists.rings_by_tier
for row in range(len(itemlists.ring_effects_ordered) + len(itemlists.rings_by_tier)):
	if row == 0:
		app.addLabel("ring_left_tier1", "Tier 1")
	elif row == len(rings[0]) + 1:
		app.addLabel("ring_left_tier2", "Tier 2")
	elif row == len(rings[0]) + len(rings[1]) + 2:
		app.addLabel("ring_left_tier3", "Tier 3")
	elif row == len(rings[0]) + len(rings[1]) + len(rings[2]) + 3:
		app.addLabel("ring_left_tier4", "Tier 4")
	else:
		effect = itemlists.ring_effects_ordered[effect_count]
		app.addLabel(effect, "\t%s" % effect)
		app.addImage("erase_ring_%s" % effect, 'assets/change.gif', row, 1)
		app.setImageSubmitFunction("erase_ring_%s" % effect, erase_left)
		effect_count += 1

app.stopScrollPane()
app.stopTab()

print("Building spellbooks......")
app.startTab("Spellbooks")
app.setStretch("none")
app.setSticky("nw")
char_settings = "Charisma: %s, Dupe: %s" % (cv.character_charisma, cv.dupe)
app.addLabel("settings_spellbooks", char_settings, 0, 0, 3)
app.setLabelTooltip("settings_spellbooks", "If this is red make sure you've entered the correct charisma in settings.")
app.setLabelFg("settings_spellbooks", "red")

app.addNamedButton("I'm Selling", "switch_to_buying_spellbooks", action_switch_btn, 1, 0)
app.setButtonBg("switch_to_buying_spellbooks", "red")

app.addNamedButton("I'm Buying", "switch_to_selling_spellbooks", action_switch_btn, 1, 0)
app.setButtonBg("switch_to_selling_spellbooks", "green")

app.addNamedButton("Greedy", "switch_to_dubious_spellbooks", shopkeeper_switch, 1, 1)
app.setButtonBg("switch_to_dubious_spellbooks", "Black")
app.setButtonFg("switch_to_dubious_spellbooks", "White")
app.hideButton("switch_to_dubious_spellbooks")
app.setButtonTooltip("switch_to_dubious_spellbooks", "The shopkeeper is greedy, meaning he'll offer less for unidentifed items.")

app.addNamedButton("Dubious", "switch_to_nice_spellbooks", shopkeeper_switch, 1, 1)
app.setButtonBg("switch_to_nice_spellbooks", "Red")
app.setButtonTooltip("switch_to_nice_spellbooks", "The shopkeeper is dubious, you don't know if he offers less for unidentified items")

app.addNamedButton("Nice!", "switch_to_greedy_spellbooks", shopkeeper_switch, 1, 1)
app.setButtonBg("switch_to_greedy_spellbooks", "Green")
app.hideButton("switch_to_greedy_spellbooks")
app.setButtonTooltip("switch_to_greedy_spellbooks", "The shopkeeper is nice, meaning he'll offer top zorkmid for unidentified items.")

app.addLabelOptionBox("Spellbook name: ", itemlists.spellbook_names, 2, 0, 3)
app.addNamedButton("Tier 1", "m0", cost_btn, 3, 0)
app.addNamedButton("Tier 2", "m1", cost_btn, 3, 1)
app.addNamedButton("Tier 3", "m2", cost_btn, 4, 0)
app.addNamedButton("Tier 4", "m4", cost_btn, 4, 1)
app.addNamedButton("Duplicate?", "m3", cost_btn, 4, 2)
app.addNamedButton("Tier 5", "m5", cost_btn, 5, 0)
app.addNamedButton("Tier 6", "m6", cost_btn, 5, 1)
app.addNamedButton("Tier 7", "m7", cost_btn, 6, 0)
app.setButtonTooltip("m3", "If the price is in two buttons push here.")
app.setButtonBg("m2", "light coral")
app.setButtonBg("m4", "light coral")

app.addNamedButton("Restore", "restore_spellbook_btn", restore_name, 7, 0)
app.addOptionBox("restore_spellbook", itemlists.spellbook_spent_names, 7, 1, colspan=2)

app.startScrollPane("spellbook_display", 0, 3, rowspan=29)
app.setScrollPaneHeight("spellbook_display", 690)
app.setSticky("nw")

slot_count = 0
tier_slots = []
for tier in helperlists.spellbook_slot_names:
	tier_slots.append(len(tier))
for row in range(sum(tier_slots) + len(itemlists.spellbooks_by_tier) + 1):
	if row == 0:
		app.addLabel("spellbook_tier1", "Tier 1")
	elif row == tier_slots[0] + 1:
		app.addLabel("spellbook_tier2", "Tier 2")
	elif row == sum(tier_slots[:2]) + 2:
		app.addLabel("spellbook_tier3", "Tier 3")
	elif row == sum(tier_slots[:3]) + 3:
		app.addLabel("spellbook_tier3/4", "Tier 3-4")
	elif row == sum(tier_slots[:4]) + 4:
		app.addLabel("spellbook_tier4", "Tier 4")
	elif row == sum(tier_slots[:5]) + 5:
		app.addLabel("spellbook_tier5", "Tier 5")
	elif row == sum(tier_slots[:6]) + 6:
		app.addLabel("spellbook_tier6", "Tier 6")
	elif row == sum(tier_slots[:7]) + 7:
		app.addLabel("spellbook_tier7", "Tier 7")

	else:
		slot = helperlists.spellbook_all_slots_list[slot_count]
		if slot[-2:] == "_1":
			app.addLabel(slot, "\t-\t\t")
		else:
			app.addLabel(slot, "\t-")
		app.addImage("undo_%s" % slot, 'assets/undo.gif', row, 1)
		app.setImageSubmitFunction("undo_%s" % slot, undo_item)
		app.addImage("identify_%s" % slot, 'assets/id.gif', row, 2)
		app.setImageSubmitFunction("identify_%s" % slot, id_item)
		slot_count += 1

app.stopScrollPane()

app.startScrollPane("spellbooks_left", 0, 4, rowspan=29)
app.setSticky("nw")

effect_count = 0
books = itemlists.spellbooks_by_tier
for row in range(len(itemlists.spellbook_effects_ordered) + len(itemlists.spellbooks_by_tier)):
	if row == 0:
		app.addLabel("spellbook_left_tier1", "Tier 1")
	elif row == len(books[0]) + 1:
		app.addLabel("spellbook_left_tier2", "Tier 2")
	elif row == len(books[0]) + len(books[1]) + 2:
		app.addLabel("spellbook_left_tier3", "Tier 3")
	elif row == len(books[0]) + len(books[1]) + len(books[2]) + 3:
		app.addLabel("spellbook_left_tier4", "Tier 4")
	elif row == len(books[0]) + len(books[1]) + len(books[2]) + len(books[3]) + 4:
		app.addLabel("spellbook_left_tier5", "Tier 5")
	elif row == len(books[0]) + len(books[1]) + len(books[2]) + len(books[3]) + len(books[4]) + + 5:
		app.addLabel("spellbook_left_tier6", "Tier 6")
	elif row == len(books[0]) + len(books[1]) + len(books[2]) + len(books[3]) + len(books[4]) + len(books[5]) + 6:
		app.addLabel("spellbook_left_tier7", "Tier 7")
	else:
		effect = itemlists.spellbook_effects_ordered[effect_count]
		app.addLabel(effect, "\t%s" % effect)
		app.addImage("erase_spellbook_%s" % effect, 'assets/change.gif', row, 1)
		app.setImageSubmitFunction("erase_spellbook_%s" % effect, erase_left)
		effect_count += 1

app.stopScrollPane()
app.stopTab()
print("Building cloaks.......")
app.startTab("Cloaks")
app.setStretch("none")
app.setSticky("nw")
char_settings = "Charisma: %s, Dupe: %s" % (cv.character_charisma, cv.dupe)
app.addLabel("settings_cloaks", char_settings, 0, 0, 3)
app.setLabelTooltip("settings_cloaks", "If this is red make sure you've entered the correct charisma in settings.")
app.setLabelFg("settings_cloaks", "red")

app.addNamedButton("I'm Selling", "switch_to_buying_cloaks", action_switch_btn, 1, 0)
app.setButtonBg("switch_to_buying_cloaks", "red")

app.addNamedButton("I'm Buying", "switch_to_selling_cloaks", action_switch_btn, 1, 0)
app.setButtonBg("switch_to_selling_cloaks", "green")

app.addNamedButton("Greedy", "switch_to_dubious_cloaks", shopkeeper_switch, 1, 1)
app.setButtonBg("switch_to_dubious_cloaks", "Black")
app.setButtonFg("switch_to_dubious_cloaks", "White")
app.hideButton("switch_to_dubious_cloaks")
app.setButtonTooltip("switch_to_dubious_cloaks", "The shopkeeper is greedy, meaning he'll offer less for unidentifed items.")

app.addNamedButton("Dubious", "switch_to_nice_cloaks", shopkeeper_switch, 1, 1)
app.setButtonBg("switch_to_nice_cloaks", "Red")
app.setButtonTooltip("switch_to_nice_cloaks", "The shopkeeper is dubious, you don't know if he offers less for unidentified items")

app.addNamedButton("Nice!", "switch_to_greedy_cloaks", shopkeeper_switch, 1, 1)
app.setButtonBg("switch_to_greedy_cloaks", "Green")
app.hideButton("switch_to_greedy_cloaks")
app.setButtonTooltip("switch_to_greedy_cloaks", "The shopkeeper is nice, meaning he'll offer top zorkmid for unidentified items.")

app.addLabelOptionBox("Cloak name: ", itemlists.cloak_names, 2, 0, 3)
app.addNamedButton("Tier 1", "c0", cost_btn, 3, 0)
app.addNamedButton("Tier 2", "c1", cost_btn, 3, 1)


app.addNamedButton("Restore", "restore_cloak_btn", restore_name, 7, 0)
app.addOptionBox("restore_cloak", itemlists.cloak_spent_names, 7, 1, colspan=2)

app.startScrollPane("cloak_display", 0, 3, rowspan=29)
app.setScrollPaneHeight("cloak_display", 690)
app.setSticky("nw")

slot_count = 0
tier_slots = []
for tier in helperlists.cloak_slot_names:
	tier_slots.append(len(tier))
for row in range(sum(tier_slots) + len(itemlists.cloaks_by_tier)):
	if row == 0:
		app.addLabel("cloak_tier1", "Tier 1")
	elif row == tier_slots[0] + 1:
		app.addLabel("cloak_tier2", "Tier 2")
	else:
		slot = helperlists.cloak_all_slots_list[slot_count]
		if slot[-2:] == "_1":
			app.addLabel(slot, "\t-\t\t")
		else:
			app.addLabel(slot, "\t-")
		app.addImage("undo_%s" % slot, 'assets/undo.gif', row, 1)
		app.setImageSubmitFunction("undo_%s" % slot, undo_item)
		app.addImage("identify_%s" % slot, 'assets/id.gif', row, 2)
		app.setImageSubmitFunction("identify_%s" % slot, id_item)
		slot_count += 1

app.stopScrollPane()

app.startScrollPane("cloaks_left", 0, 4, rowspan=29)
app.setSticky("nw")

effect_count = 0
cloaks = itemlists.cloaks_by_tier
for row in range(len(itemlists.cloak_effects_ordered) + len(itemlists.cloaks_by_tier)):
	if row == 0:
		app.addLabel("cloak_left_tier1", "Tier 1")
	elif row == len(cloaks[0]) + 1:
		app.addLabel("cloak_left_tier2", "Tier 2")
	else:
		effect = itemlists.cloak_effects_ordered[effect_count]
		app.addLabel(effect, "\t%s" % effect)
		app.addImage("erase_cloak_%s" % effect, 'assets/change.gif', row, 1)
		app.setImageSubmitFunction("erase_cloak_%s" % effect, erase_left)
		effect_count += 1

app.stopScrollPane()
app.stopTab()
print("Building boots........")
app.startTab("Boots")
app.setStretch("none")
app.setSticky("nw")
char_settings = "Charisma: %s, Dupe: %s" % (cv.character_charisma, cv.dupe)
app.addLabel("settings_boots", char_settings, 0, 0, 3)
app.setLabelTooltip("settings_boots", "If this is red make sure you've entered the correct charisma in settings.")
app.setLabelFg("settings_boots", "red")

app.addNamedButton("I'm Selling", "switch_to_buying_boots", action_switch_btn, 1, 0)
app.setButtonBg("switch_to_buying_boots", "red")

app.addNamedButton("I'm Buying", "switch_to_selling_boots", action_switch_btn, 1, 0)
app.setButtonBg("switch_to_selling_boots", "green")

app.addNamedButton("Greedy", "switch_to_dubious_boots", shopkeeper_switch, 1, 1)
app.setButtonBg("switch_to_dubious_boots", "Black")
app.setButtonFg("switch_to_dubious_boots", "White")
app.hideButton("switch_to_dubious_boots")
app.setButtonTooltip("switch_to_dubious_boots", "The shopkeeper is greedy, meaning he'll offer less for unidentifed items.")

app.addNamedButton("Dubious", "switch_to_nice_boots", shopkeeper_switch, 1, 1)
app.setButtonBg("switch_to_nice_boots", "Red")
app.setButtonTooltip("switch_to_nice_boots", "The shopkeeper is dubious, you don't know if he offers less for unidentified items")

app.addNamedButton("Nice!", "switch_to_greedy_boots", shopkeeper_switch, 1, 1)
app.setButtonBg("switch_to_greedy_boots", "Green")
app.hideButton("switch_to_greedy_boots")
app.setButtonTooltip("switch_to_greedy_boots", "The shopkeeper is nice, meaning he'll offer top zorkmid for unidentified items.")

app.addLabelOptionBox("Boot name: ", itemlists.boot_names, 2, 0, 3)
app.addNamedButton("Tier 1", "b0", cost_btn, 3, 0)
app.addNamedButton("Tier 2", "b1", cost_btn, 3, 1)
app.addNamedButton("Tier 3", "b2", cost_btn, 4, 0)

app.addNamedButton("Restore", "restore_boot_btn", restore_name, 7, 0)
app.addOptionBox("restore_boot", itemlists.boot_spent_names, 7, 1, colspan=2)

app.startScrollPane("boot_display", 0, 3, rowspan=29)
app.setScrollPaneHeight("boot_display", 690)
app.setSticky("nw")

slot_count = 0
tier_slots = []
for tier in helperlists.boot_slot_names:
	tier_slots.append(len(tier))
for row in range(sum(tier_slots) + len(itemlists.boots_by_tier)):
	if row == 0:
		app.addLabel("boot_tier1", "Tier 1")
	elif row == tier_slots[0] + 1:
		app.addLabel("boot_tier2", "Tier 2")
	elif row == sum(tier_slots[:2]) + 2:
		app.addLabel("boot_tier3", "Tier 3")

	else:
		slot = helperlists.boot_all_slots_list[slot_count]
		if slot[-2:] == "_1":
			app.addLabel(slot, "\t-\t\t")
		else:
			app.addLabel(slot, "\t-")
		app.addImage("undo_%s" % slot, 'assets/undo.gif', row, 1)
		app.setImageSubmitFunction("undo_%s" % slot, undo_item)
		app.addImage("identify_%s" % slot, 'assets/id.gif', row, 2)
		app.setImageSubmitFunction("identify_%s" % slot, id_item)
		slot_count += 1

app.stopScrollPane()

app.startScrollPane("boots_left", 0, 4, rowspan=29)
app.setSticky("nw")

effect_count = 0
boots = itemlists.boots_by_tier
for row in range(len(itemlists.boot_effects_ordered) + len(itemlists.boots_by_tier)):
	if row == 0:
		app.addLabel("boot_left_tier1", "Tier 1")
	elif row == len(boots[0]) + 1:
		app.addLabel("boot_left_tier2", "Tier 2")
	elif row == len(boots[0]) + len(boots[1]) + 2:
		app.addLabel("boot_left_tier3", "Tier 3")
	else:
		effect = itemlists.boot_effects_ordered[effect_count]
		app.addLabel(effect, "\t%s" % effect)
		app.addImage("erase_boot_%s" % effect, 'assets/change.gif', row, 1)
		app.setImageSubmitFunction("erase_boot_%s" % effect, erase_left)
		effect_count += 1

app.stopScrollPane()
app.stopTab()
app.stopTabbedFrame()
app.go()
