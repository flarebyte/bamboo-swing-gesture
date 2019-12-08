def header(id):
    return map(lambda x : x.strip(), """id-urn: company7/examples/{0}
    license,en: Attribution 4.0 International
    license-url,html,en: https://creativecommons.org/licenses/by/4.0/legalcode
    attribution-name,en-gb: Crafted by olih assisted by code generator
    attribution-url,html,en: https://github.com/olih
    title,en: Random valid example {0}
    description,en: Single line description for {0}
    metadata-url,rdf,en: http://website.com/meta
    homepage-url,markdown,en: https://github.com/owner/project#readme
    """.format(id).split("\n"))

def formatAsEnumValue(str):
    return "".join(map(lambda s: s.capitalize(), str.split())) + "_"

# Examples from https://github.com/dariusk/corpora/blob/master/data/mythology/monsters.json
# License CC0 license
def enumerationExamples():
        return map(formatAsEnumValue,[
		"angel",
		"brownie",
		"bugbear",
		"centaur",
		"chimera",
		"chupacabra",
		"cockatrice",
		"cyclops",
		"demon",
		"djinn",
		"dragon",
		"draugr",
		"dryad",
		"dwarf",
		"elemental",
		"elf",
		"fairy",
		"faun",
		"frost giant",
		"gargoyle",
		"genie",
		"ghast",
		"ghost",
		"ghoul",
		"giant",
		"gnome",
		"goblin",
		"golem",
		"gorgon",
		"gremlin",
		"griffon",
		"hag",
		"harpy",
		"hippogriff",
		"hobgoblin",
		"homonculus",
		"hydra",
		"imp",
		"incubus",
		"kappa",
		"kobold",
		"kraken",
		"lamassu",
		"leprechaun",
		"lich",
		"manticore",
		"mermaid",
		"merman",
		"minotaur",
		"mummy",
		"naga",
		"nix",
		"nymph",
		"ogre",
		"oni",
		"orc",
		"pegasus",
		"phoenix",
		"pixie",
		"poltergeist",
		"roc",
		"sasquatch",
		"satyr",
		"selkie",
		"siren",
		"spectre",
		"sphinx",
		"sprite",
		"succubus",
		"sylph",
		"thunderbird",
		"troll",
		"unicorn",
		"vampire",
		"valkyrie",
		"warg",
		"wendigo",
		"werewolf",
		"wight",
		"witch",
		"wraith",
		"wyvern",
		"yeti",
		"zombie"
	])