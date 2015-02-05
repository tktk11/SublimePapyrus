import sublime, sublime_plugin, sys
PYTHON_VERSION = sys.version_info
if PYTHON_VERSION[0] == 3:
    from SublimePapyrus import SublimePapyrus

    class PapyrusSkyrimActorValueSuggestionsCommand(SublimePapyrus.PapyrusShowSuggestionsCommand):
        def get_items(self, **args):
            items = {
            "Health": "Health",
			"Magicka": "Magicka",
			"Stamina": "Stamina",
			"OneHanded": "One-handed",
			"TwoHanded": "Two-handed",
			"Marksman": "Marksman",
			"Block": "Block",
			"Smithing": "Smithing",
			"HeavyArmor": "Heavy armor",
			"LightArmor": "Light armor",
			"Pickpocket": "Pickpocket",
			"Lockpicking": "Lockpicking",
			"Sneak": "Sneak",
			"Alchemy": "Alchemy",
			"Speechcraft": "Speech",
			"Alteration": "Alteration",
			"Conjuration": "Conjuration",
			"Destruction": "Destruction",
			"Illusion": "Illusion",
			"Restoration": "Restoration",
			"Enchanting": "Enchanting",
			"Aggression": "Aggression",
			"Confidence": "Confidence",
			"Energy": "Energy",
			"Morality": "Morality",
			"Mood": "Mood",
			"Assistance": "Assistance",
			"WaitingForPlayer": "Waiting for player",
			"HealRate": "Heal rate",
			"MagickaRate": "Magicka rate",
			"StaminaRate": "Stamina rate",
			"AttackDamageMult": "Attack damage multiplier",
			"SpeedMult": "Speed multiplier",
			"ShoutRecoveryMult": "Shout recovery multiplier",
			"WeaponSpeedMult": "Weapon speed multiplier",
			"DestructionMod": "Destruction modifier",
			"DestructionPowerMod": "Destruction power modifier",
			"AlterationMod": "Alteration modifier",
			"AlterationPowerMod": "Alteration power modifier",
			"IllusionMod": "Illusion modifier",
			"IllusionPowerMod": "Illusion power modifier",
			"RestorationMod": "Restoration modifier",
			"RestorationPowerMod": "Restoration power modifier",
			"ConjurationMod": "Conjuration modifier",
			"ConjurationPowerMod": "Conjuration power modifier",
			"InventoryWeight": "Inventory weight",
			"CarryWeight": "Carry weight",
			"CritChance": "Critical chance",
			"MeleeDamage": "Melee damage",
			"UnarmedDamage": "Unarmed damage",
			"Mass": "Mass",
			"VoicePoints": "Voice points",
			"VoiceRate": "Voice rate",
			"DamageResist": "Damage resistance",
			"DiseaseResist": "Disease resistance",
			"PoisonResist": "Poison resistance",
			"FireResist": "Fire resistance",
			"ElectricResist": "Shock resistance",
			"FrostResist": "Frost resistance",
			"MagicResist": "Magic resistance",
			"Paralysis": "Paralysis",
			"Invisibility": "Invisibility",
			"NightEye": "Night eye",
			"DetectLifeRange": "Detect life range",
			"WaterBreathing": "Water breating",
			"WaterWalking": "Water walking",
			"JumpingBonus": "Jumping bonus",
			"WardPower": "Ward power",
			"WardDeflection": "Ward deflection",
			"EquippedItemCharge": "Equipped item charge",
			"EquippedStaffCharge": "Equipped staff charge",
			"ArmorPerks": "Armor perks",
			"ShieldPerks": "Shield perks",
			"BowSpeedBonus": "Bow speed bonus",
			"DragonSouls": "Dragon souls",
			"Variable01": "Variable 01",
			"Variable02": "Variable 02",
			"Variable03": "Variable 03",
			"Variable04": "Variable 04",
			"Variable05": "Variable 05",
			"Variable06": "Variable 06",
			"Variable07": "Variable 07",
			"Variable08": "Variable 08",
			"Variable09": "Variable 09",
			"Variable10": "Variable 10",
			"CombatHealthRegenMultMod": "Combat health regeneration multiplier modifier",
			"CombatHealthRegenMultPowerMod": "Combat health regeneration multiplier power modifier",
			"PerceptionCondition": "Perception condition",
			"EnduranceCondition": "Endurance condition",
			"LeftAttackCondition": "Left attack condition",
			"RightAttackCondition": "Right attack condition",
			"LeftMobilityCondition": "Left mobility condition",
			"RightMobilityCondition": "Right mobility condition",
			"BrainCondition": "Brain condition",
			"IgnoreCrippledLimbs": "Ignore crippled limbs",
			"Fame": "Fame",
			"Infamy": "Infamy",
			"FavorActive": "Favor active",
			"FavorPointsBonus": "Favor points bonus",
			"FavorsPerDay": "Favors per day",
			"FavorsPerDayTimer": "Favors per day timer",
			"BypassVendorStolenCheck": "Bypass vendor stolen check",
			"BypassVendorKeywordCheck": "Bypass vendor keyword check",
			"LastBribedIntimidated": "Last bribed or intimidated",
			"LastFlattered": "Last flattered"
            }
            return items
