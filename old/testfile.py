from appJar import gui
import itemlists
import helperlists


def find_slot_tier(itemtype, slot):
    all_slot_list = []
    if itemtype == "scrolls":
        all_slot_list = helperlists.scroll_slot_names
    elif itemtype == "potions":
        all_slot_list = helperlists.potion_slot_names
    elif itemtype == "wands":
        all_slot_list = helperlists.wand_slot_names
    elif itemtype == "rings":
        all_slot_list = helperlists.ring_slot_names
    elif itemtype == "spellbooks":
        all_slot_list = helperlists.spellbook_slot_names
    elif itemtype == "cloaks":
        all_slot_list = helperlists.cloak_slot_names
    elif itemtype == "boots":
        all_slot_list = helperlists.boot_slot_names
    slot_tier = None
    for tier in all_slot_list:
        if slot in tier:
            slot_tier = tier
    tier_index = all_slot_list.index(slot_tier)
    print(tier_index)
    if itemtype == "rings":
        if tier_index < 2:
            print("Tier %s" % str(tier_index + 1))
        elif tier == 2:
            print("Tier %s or Tier %s" % (tier_index, tier_index + 1))
        else:
            print("Tier %s" % str(tier_index))
    elif itemtype == "scrolls" or itemtype == "potions":
        if tier_index < 3:
            print("Tier %s" % str(tier_index + 1))
        elif tier == 3:
            print("Tier %s or Tier %s" % (tier_index, tier_index + 1))
        else:
            print("Tier %s" % str(tier_index))

find_slot_tier("scrolls", "scroll_slot_6")