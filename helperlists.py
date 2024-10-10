import itemlists

scroll_tier_1_slots = []
scroll_tier_2_slots = []
scroll_tier_3_slots = []
scroll_tier_34_slots = []
scroll_tier_4_slots = []
scroll_tier_5_slots = []
scroll_tier_6_slots = []
scroll_tier_7_slots = []
scroll_all_slots_list = []
for x in range(24):
	name = "scroll_slot_%s" % str(x + 1)
	if x + 1 == 1:
		scroll_tier_1_slots.append(name)
	elif x + 1 == 2:
		scroll_tier_2_slots.append(name)
	elif x + 1 == 3:
		scroll_tier_3_slots.append(name)
	elif x + 1 <= 6:
		scroll_tier_34_slots.append(name)
	elif x + 1 <= 8:
		scroll_tier_4_slots.append(name)
	elif x + 1 <= 16:
		scroll_tier_5_slots.append(name)
	elif x + 1 <= 20:
		scroll_tier_6_slots.append(name)
	elif x + 1 <= 24:
		scroll_tier_7_slots.append(name)
	scroll_all_slots_list.append(name)
scroll_slot_names = [
	scroll_tier_1_slots,
	scroll_tier_2_slots,
	scroll_tier_3_slots,
	scroll_tier_34_slots,
	scroll_tier_4_slots,
	scroll_tier_5_slots,
	scroll_tier_6_slots,
	scroll_tier_7_slots
]
potion_tier_1_slots = []
potion_tier_2_slots = []
potion_tier_3_slots = []
potion_tier_34_slots = []
potion_tier_4_slots = []
potion_tier_5_slots = []
potion_tier_6_slots = []
potion_all_slots_list = []
for x in range(35):
	name = "potion_slot_%s" % str(x + 1)
	if x + 1 <= 4:
		potion_tier_1_slots.append(name)
	elif x + 1 <= 10:
		potion_tier_2_slots.append(name)
	elif x + 1 <= 15:
		potion_tier_3_slots.append(name)
	elif x + 1 <= 25:
		potion_tier_34_slots.append(name)
	elif x + 1 <= 30:
		potion_tier_4_slots.append(name)
	elif x + 1 <= 32:
		potion_tier_5_slots.append(name)
	elif x + 1 <= 35:
		potion_tier_6_slots.append(name)
	potion_all_slots_list.append(name)
potion_slot_names = [
	potion_tier_1_slots,
	potion_tier_2_slots,
	potion_tier_3_slots,
	potion_tier_34_slots,
	potion_tier_4_slots,
	potion_tier_5_slots,
	potion_tier_6_slots
]
wand_tier_1_slots = []
wand_tier_2_slots = []
wand_tier_3_slots = []
wand_tier_24_slots = []
wand_tier_4_slots = []
wand_tier_5_slots = []
wand_all_slots_list = []
for x in range(40):
	name = "wand_slot_%s" % str(x + 1)
	if x + 1 <= 2:
		wand_tier_1_slots.append(name)
	elif x + 1 <= 14:
		wand_tier_2_slots.append(name)
	elif x + 1 <= 18:
		wand_tier_3_slots.append(name)
	elif x + 1 <= 34:
		wand_tier_24_slots.append(name)
	elif x + 1 <= 38:
		wand_tier_4_slots.append(name)
	elif x + 1 <= 40:
		wand_tier_5_slots.append(name)
	wand_all_slots_list.append(name)
wand_slot_names = [
	wand_tier_1_slots,
	wand_tier_2_slots,
	wand_tier_3_slots,
	wand_tier_24_slots,
	wand_tier_4_slots,
	wand_tier_5_slots
]
ring_tier_1_slots = []
ring_tier_2_slots = []
ring_tier_23_slots = []
ring_tier_3_slots = []
ring_tier_4_slots = []
ring_all_slots_list = []
for x in range(45):
	name = "ring_slot_%s" % str(x + 1)
	if x + 1 <= 7:
		ring_tier_1_slots.append(name)
	elif x + 1 <= 17:
		ring_tier_2_slots.append(name)
	elif x + 1 <= 34:
		ring_tier_23_slots.append(name)
	elif x + 1 <= 41:
		ring_tier_3_slots.append(name)
	elif x + 1 <= 45:
		ring_tier_4_slots.append(name)

	ring_all_slots_list.append(name)
ring_slot_names = [
	ring_tier_1_slots,
	ring_tier_2_slots,
	ring_tier_23_slots,
	ring_tier_3_slots,
	ring_tier_4_slots
]
spellbook_tier_1_slots = []
spellbook_tier_2_slots = []
spellbook_tier_3_slots = []
spellbook_tier_34_slots = []
spellbook_tier_4_slots = []
spellbook_tier_5_slots = []
spellbook_tier_6_slots = []
spellbook_tier_7_slots = []
spellbook_all_slots_list = []
for x in range(56):
	name = "spellbook_slot_%s" % str(x + 1)
	if x + 1 <= 8:
		spellbook_tier_1_slots.append(name)
	elif x + 1 <= 16:
		spellbook_tier_2_slots.append(name)
	elif x + 1 <= 26:
		spellbook_tier_3_slots.append(name)
	elif x + 1 <= 42:
		spellbook_tier_34_slots.append(name)
	elif x + 1 <= 48:
		spellbook_tier_4_slots.append(name)
	elif x + 1 <= 50:
		spellbook_tier_5_slots.append(name)
	elif x + 1 <= 54:
		spellbook_tier_6_slots.append(name)
	elif x + 1 <= 56:
		spellbook_tier_7_slots.append(name)
	spellbook_all_slots_list.append(name)
spellbook_slot_names = [
	spellbook_tier_1_slots,
	spellbook_tier_2_slots,
	spellbook_tier_3_slots,
	spellbook_tier_34_slots,
	spellbook_tier_4_slots,
	spellbook_tier_5_slots,
	spellbook_tier_6_slots,
	spellbook_tier_7_slots
]
cloak_tier_1_slots = []
cloak_tier_2_slots = []
cloak_all_slots_list = []
for x in range(4):
	name = "cloak_slot_%s" % str(x + 1)
	if x + 1 <= 2:
		cloak_tier_1_slots.append(name)
	elif x + 1 <= 4:
		cloak_tier_2_slots.append(name)
	cloak_all_slots_list.append(name)
cloak_slot_names = [
	cloak_tier_1_slots,
	cloak_tier_2_slots
]
boot_tier_1_slots = []
boot_tier_2_slots = []
boot_tier_3_slots = []
boot_all_slots_list = []
for x in range(7):
	name = "boot_slot_%s" % str(x + 1)
	if x + 1 <= 2:
		boot_tier_1_slots.append(name)
	elif x + 1 <= 4:
		boot_tier_2_slots.append(name)
	elif x + 1 <= 7:
		boot_tier_3_slots.append(name)
	boot_all_slots_list.append(name)
boot_slot_names = [
	boot_tier_1_slots,
	boot_tier_2_slots,
	boot_tier_3_slots
]
character_settings_list = [
	'settings_scrolls',
	'settings_potions',
	'settings_wands',
	'settings_rings',
	'settings_spellbooks',
	'settings_cloaks',
	'settings_boots'
]
switch_to_selling_buttons = [
	'switch_to_selling_scrolls',
	'switch_to_selling_potions',
	'switch_to_selling_wands',
	'switch_to_selling_rings',
	'switch_to_selling_spellbooks',
	'switch_to_selling_cloaks',
	'switch_to_selling_boots'
]
switch_to_buying_buttons = [
	'switch_to_buying_scrolls',
	'switch_to_buying_potions',
	'switch_to_buying_wands',
	'switch_to_buying_rings',
	'switch_to_buying_spellbooks',
	'switch_to_buying_cloaks',
	'switch_to_buying_boots'
]
switch_to_dubious_buttons = [
	'switch_to_dubious_scrolls',
	'switch_to_dubious_potions',
	'switch_to_dubious_wands',
	'switch_to_dubious_rings',
	'switch_to_dubious_spellbooks',
	'switch_to_dubious_cloaks',
	'switch_to_dubious_boots'
]
switch_to_greedy_buttons = [
	'switch_to_greedy_scrolls',
	'switch_to_greedy_potions',
	'switch_to_greedy_wands',
	'switch_to_greedy_rings',
	'switch_to_greedy_spellbooks',
	'switch_to_greedy_cloaks',
	'switch_to_greedy_boots'
]
switch_to_nice_buttons = [
	'switch_to_nice_scrolls',
	'switch_to_nice_potions',
	'switch_to_nice_wands',
	'switch_to_nice_rings',
	'switch_to_nice_spellbooks',
	'switch_to_nice_cloaks',
	'switch_to_nice_boots'
]