def order_effects(items):
	effects_ordered = []
	for tier in items:
		for effect in tier:
			effects_ordered.append(effect)
	return effects_ordered

charisma_modifiers = {'<=5': 2, '6-7': 3/2, '8-10': 4/3, '11-15': 1, '16-17': 3/4, '18': 2/3, '>= 19': 1/2 }
scroll_names = [
	'-Scroll Names-', 'ABRA KA DABRA', 'ACHAT SHTAYIM SHALOSH', 'ANDOVA BEGARIN', 'AQUE BRAGH', 'ASHPD SODALG', 'DAIYEN FOOELS',
	'DUAM XNAHT', 'EIRIS SAZUN IDISI', 'ELAM EBOW', 'ELBIB YLOH', 'ETAOIN SHRDLU', 'FNORD',
	'FOOBIE BLETCH', 'GARVEN DEH', 'GHOTI', 'GNEK SISI VLE', 'HACKEM MUCHE', 'HAPAX LEGOMENON',
	'HZLRC KSTSBD MPFNG', 'JUYED AWK YACC', 'KERNOD WEL', 'KIRJE', 'KO BATE', 'LEP GEX VEN ZEA', 'LOREM IPSUM',
	'MAPIRO MAHAM DIROMAT', 'NR 9', 'PHOL ENDE WODAN', 'PRATYAVAYAH', 'PRIRUTSENIE', 'READ ME', 'SODALG', 'STRC PRST SKRZ KRK', 'TEMOV',
	'THARR', 'VAS CORP BET MANI', 'VE FORBRYDERNE', 'VELOX NEB', 'VENZAR BORGAVVE', 'VERR YED HORRE',
	'XIXAXA XOXAXA XUXAXA', 'XOR OTA', 'YUM YUM', 'ZELGO MER', 'ZLORFIK'
]
scrolls_by_tier = [
		['identify'],
		['light'],
		['enchant weapon'],
		['enchant armor', 'remove curse'],
		['confuse monster', 'destroy armor', 'fire', 'food detection', 'gold detection', 'magic mapping', 'scare monster', 'teleportation'],
		['amnesia', 'create monster', 'earth', 'taming'],
		['charging', 'genocide', 'punishment', 'stinking cloud']
]
scroll_effects_ordered = order_effects(scrolls_by_tier)
scroll_effects = scroll_effects_ordered.copy()
scroll_effects.sort()
scroll_effects.insert(0, '-Scroll Effects-')
scroll_spent_names = ['-Used Names-']
scroll_spent_effects = ['-Used Effects-']

scroll_bases = [20, 50, 60, 80, 100, 200, 300]

potion_names = [
	'amber', 'black', 'brilliant blue', 'brown', 'bubbly', 'cloudy', 'cyan', 'dark', 'dark green', 'effervescent', 'emerald',
	'fizzy', 'golden', 'gooey', 'icy', 'indigo', 'luminescent', 'magenta', 'milky', 'muddy', 'murky', 'ochre', 'orange',
	'pink', 'puce', 'purple-red', 'ruby', 'silver', 'slimy', 'sky blue', 'smoky', 'sparkling', 'squishy', 'steamy', 'swirly',
	'white', 'yellow', 'viscous'
]

potion_names.insert(0, '-Potion Names-')
potions_by_tier = [
	['booze', 'fruit juice', 'see invisible', 'sickness'],
	['confusion', 'extra healing', 'hallucination', 'healing', 'restore ability', 'sleeping'],
	['blindness', 'gain energy', 'invisibility', 'monster detection', 'object detection'],
	['enlightenment', 'full healing', 'levitation', 'polymorph', 'speed'],
	['acid', 'oil'],
	['gain ability', 'gain level', 'paralysis']
]
potion_effects_ordered = order_effects(potions_by_tier)

potion_effects = potion_effects_ordered.copy()
potion_effects.sort()
potion_effects.insert(0, '-Potion Effects-')
potion_spent_names = ['-Used Names-']
potion_spent_effects = ['-Used Effects-']
potion_bases = [50, 100, 150, 200, 250, 300]

ring_names = [
	'agate', 'amber', 'black onyx', 'brass', 'bronze', 'ceramic', 'citrine', 'chrysoberyl', 'clay', 'copper', 'coral',
	'diamond', 'emerald', 'engagement', 'gold', 'granite', 'iron', 'ivory', 'jade',
	'jet', 'mithril', 'moonstone', 'opal', 'pearl', 'plain', 'plastic', 'platinum', 'quartz', 'porcelain', 'ridged',
	'ruby', 'sapphire', 'shiny', 'silver', 'steel', 'tiger eye', 'topaz', 'twisted', 'wire', 'wooden'
]
ring_names.insert(0, '-Ring Names-')
rings_by_tier = [
	['adornment', 'hunger', 'protection', 'protection from shape changers', 'stealth', 'sustain ability', 'warning'],
	['aggravate monster', 'cold resistance', 'gain constitution', 'gain strength', 'increase accuracy', 'increase damage', 'invisibility (ring)', 'poison resistance', 'see invisible (ring)', 'shock resistance'],
	['fire resistance', 'free action', 'levitation (ring)', 'regeneration', 'searching', 'slow digestion', 'teleportation (ring)'],
	['conflict', 'polymorph (ring)', 'polymorph control', 'teleport control']
]
ring_effects_ordered = order_effects(rings_by_tier)
ring_effects = ring_effects_ordered.copy()
ring_effects.sort()
ring_effects.insert(0, '-Ring Effects-')
ring_spent_names = ['-Used Names-']
ring_spent_effects = ['-Used Effects-']
ring_bases = [100, 150, 200, 300]

wand_names = [
	'alabaster', 'aluminum', 'balsa', 'bamboo', 'bent', 'brass', 'bronze', 'cedar', 'copper', 'crystal', 'curved',
	'ebony', 'electrum', 'forked', 'glass', 'hexagonal', 'iridium', 'iron', 'jeweled', 'long',
	'maple', 'marble', 'octagonal', 'oak', 'pine', 'platinum', 'quartz', 'runed', 'short', 'silver', 'spiked', 'steel',
	'tin', 'titanium', 'uranium', 'zinc'
]
wand_names.insert(0, '-Wand Names-')
wands_by_tier = [
	['light (wand)'],
	['digging', 'enlightenment (wand)', 'locking', 'magic missile', 'make invisible', 'opening', 'probing', 'secret door detection', 'slow monster', 'speed monster', 'striking', 'undead turning'],
	['cold', 'fire (wand)', 'lightning', 'sleep'],
	['cancellation', 'create monster (wand)', 'polymorph (wand)', 'teleportation (wand)'],
	['death', 'wishing']
]
wand_effects_ordered = order_effects(wands_by_tier)
wand_effects = wand_effects_ordered.copy()
wand_effects.sort()
wand_effects.insert(0, '-Wand Effects-')
wand_spent_names = ['-Used Names-']
wand_spent_effects = ['-Used Effects-']
wand_bases = [100, 150, 175, 200, 500]

spellbook_names = [
	'parchment', 'vellum', 'ragged', 'dog eared', 'mottled', 'stained', 'cloth', 'leather', 'white', 'pink',
	'red', 'orange', 'yellow', 'velvet', 'light green', 'dark green', 'turquoise', 'cyan', 'light blue', 'dark blue',
	'indigo', 'magenta', 'purple', 'violet', 'tan', 'plaid', 'light brown', 'dark brown', 'gray', 'wrinkled',
	'dusty', 'bronze', 'copper', 'silver', 'gold', 'glittering', 'shining', 'dull', 'thin', 'thick'
]
spellbook_names.sort()
spellbook_names.insert(0, '-Book Names-')
spellbooks_by_tier = [
	['force bolt', 'protection (book)', 'detect monsters', 'light (book)', 'sleep (book)', 'jumping', 'healing (book)', 'knock'],
	['magic missle', 'drain life', 'create monster (book)', 'detect food (book)', 'confuse monster (book)', 'slow monster (book)', 'cure blindness', 'wizard lock'],
	['remove curse (book)', 'clairvoyance', 'detect unseen', 'identify (book)', 'cause fear', 'charm monster', 'haste self', 'cure sickness', 'extra healing (book)', 'stone to flesh'],
	['cone of cold', 'fireball', 'detect treasure', 'invisibility (book)', 'levitation (book)', 'restore ability (book)'],
	['magic mapping (book)', 'dig'],
	['create familiar', 'turn undead', 'teleport away', 'polymorph (book)'],
	['finger of death', 'cancellation (book)']
]
spellbook_effects_ordered = order_effects(spellbooks_by_tier)
spellbook_effects = spellbook_effects_ordered.copy()
spellbook_effects.sort()
spellbook_effects.insert(0, "-Spell Effects-")
spellbook_spent_names = ['-Used Names-']
spellbook_spent_effects = ['-Used Effects-']
spellbook_bases = [100, 200, 300, 400, 500, 600, 700]



cloak_names = ['tattered cape', 'ornamental cope', 'opera cloak', 'piece of cloth']
cloak_names.insert(0, '-Cloak Names-')
cloaks_by_tier = [
	['displacement', 'protection (cloak)'],
	['invisibility (cloak)', 'magic resistance']
]
cloak_effects_ordered = order_effects(cloaks_by_tier)
cloak_effects = cloak_effects_ordered.copy()
cloak_effects.sort()
cloak_effects.insert(0, "-Cloak Effects-")
cloak_spent_names = ['-Used Names-']
cloak_spent_effects = ['-Used Effects-']
cloak_bases = [50, 60]

boot_names = [
	'mud boots', 'snow boots', 'riding boots', 'buckled boots', 'hiking boots',
	'combat boots', 'jungle boots'
]
boot_names.insert(0, '-Boot Names-')
boots_by_tier = [
	['elven', 'kicking'],
	['fumble', 'levitation (boot)'],
	['jumping (boot)', 'speed (boot)', 'water walking']
]
boot_effects_ordered = order_effects(boots_by_tier)
boot_effects = boot_effects_ordered.copy()
boot_effects.sort()
boot_effects.insert(0, "-Boot Effects-")
boot_spent_names = ['-Used Names-']
boot_spent_effects = ['-Used Effects-']
boot_bases = [8, 30, 50]