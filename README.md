# NethackPriceIdentification
A python made graphical interface for price identifying items in NetHack

## Intro
After playing NetHack for quite a few years I decided to make something similar to this that used tkinter I believe.
A couple of years ago I decided to remake it for different reasons and ended up using appJar instead as a way to test out that library, and I enjoyed it.
So I decided to share it here, I'm by no means a decent programmer, but I dabble in it for fun. This means there will likely be quite a few areas that could be rewritten more cleanly, and be made to conform with the style of python more closely.
This is something I might do in the future, I'm not certain. There are a few changes that I would like to make when I have time, for example the price of "Potion of Healing" have been altered in NetHack as of 3.7, but since that isn't even released yet I haven't implemented it here. It's also quite easy to figure out, since the new price will be between a potion of water and a tier 1 potion.

## Running the program
The program uses math, shelve, os and appJar modules at this time, and the current version of python I use myself is 3.12.6.

I use linux and have not tested it on windows.

If these requirements are met, it should start up with a simple "python identify.py" right now.
First it takes some time to generate the different price dictionaries.

## Using the program
The first tab is settings, where you can enter your charisma range, and let the program know if you're a sucker or not. This will be any character that uses a hawaian shirt without any other body armour, or a Tourist of less than 15 experience levels I believe.
It also allows you to store a set of identifed items, load a set or scrap a saved file (for when you die and want to tell the program that all your work was for nothing).
I guess one can also use the scrap function after a successful run.

The program has different tabs for Scrolls, Potions, Wands, Rings, Spellbooks, Cloaks and Boots.

The two buttons at the top change between buying/selling and if the shopkeeper is greedy or nice. If you're not sure, there is a dubious setting which will show both the nice price and the greedy one.

Please note that it is the text that is currently showing on the button that is active. So clicking a button that says "I'm buying". will change FROM buying TO selling.

Some items can be one of two different Tiers if the setting is Dubious and if so a Duplicate? button can be pushed to place the item in a separate category.

Otherwise just push the price and it will be placed in the middle list which stores the names for unknown items in tier categories.

The back arrow can be pressed if you've made a mistake or for whatever other reason you want to undo. This places the item name back in the available list.

The lightbulb lets you choose an effect from a list of available effects and thus marking it as identified.

To the right is a list of all the possible effects, when you have identified an item in the program, the effect will be enclosed by == signs to let you know it's identified.

If you've identified something wrongly, you can use the Restore drop down to restore both the item name and the effect name as unused.
