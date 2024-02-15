from .Screens import Screens
from .StartScreen import StartScreen
from .PatrolScreen import PatrolScreen
from .AllegiancesScreen import AllegiancesScreen
from .CeremonyScreen import CeremonyScreen
from .ChooseAdoptiveParentScreen import ChooseAdoptiveParentScreen
from .ProfileScreen import ProfileScreen
from .RoleScreen import RoleScreen
from .SpriteInspectScreen import SpriteInspectScreen
from .MakeClanScreen import MakeClanScreen
from .MedDenScreen import MedDenScreen
from .RelationshipScreen import RelationshipScreen
from .SettingsScreen import SettingsScreen
from .SwitchClanScreen import SwitchClanScreen
from .ClanScreen import ClanScreen
from .ListScreen import ListScreen
from .EventsScreen import EventsScreen
from .ChooseMateScreen import ChooseMateScreen
from .ChooseMentorScreen import ChooseMentorScreen
from .FamilyTreeScreen import FamilyTreeScreen
from .MediationScreen import MediationScreen
from .ClanSettingsScreen import ClanSettingsScreen
from .TalkScreen import TalkScreen
from .InsultScreen import InsultScreen
from .FlirtScreen import FlirtScreen
from .ChooseRebornScreen import ChooseRebornScreen
from .AchievementScreen import AchievementScreen
from .MurderScreen import MurderScreen
from .DeputyScreen import DeputyScreen
from .NameKitsScreen import NameKitsScreen
from .LifeGenPatrolScreen import LifeGenPatrolScreen
from .DFPatrolScreen import DFPatrolScreen
from .DatePatrolScreen import DatePatrolScreen
from .AffairScreen import AffairScreen
from .ClearingScreen import ClearingScreen
from .QueenScreen import QueenScreen

# ---------------------------------------------------------------------------- #
#                                  UI RULES                                    #
# ---------------------------------------------------------------------------- #
"""
SCREEN: 700 height x 800 width

MARGINS: 25px on all sides
    ~Any new buttons or text MUST be within these margins.
    ~Buttons on the edge of the screen should butt up right against the margin. 
    (i.e. the <<Main Menu button is placed 25px x 25px on most screens) 
    
BUTTONS:
    ~Buttons are 30px in height. Width can be anything, though generally try to keep to even numbers.
    ~Square icons are 34px x 34px.
    ~Generally keep text at least 5px away from the right and left /straight/ (do not count the rounded ends) edge 
    of the button (this rule is sometimes broken. the goal is to be consistent across the entire screen or button type)
    ~Generally, the vertical gap between buttons should be 5px
"""

# SCREENS
screens = Screens()

# ---------------------------------------------------------------------------- #
#                                 cat_screens.py                               #
# ---------------------------------------------------------------------------- #

profile_screen = ProfileScreen('profile screen')
ceremony_screen = CeremonyScreen('ceremony screen')
role_screen = RoleScreen('role screen')
sprite_inspect_screen = SpriteInspectScreen("sprite inspect screen")
make_clan_screen = MakeClanScreen('make clan screen')
allegiances_screen = AllegiancesScreen('allegiances screen')
camp_screen = ClanScreen('camp screen')
catlist_screen = ListScreen('list screen')
med_den_screen = MedDenScreen('med den screen')
freshkill_pile_screen = ClearingScreen('clearing screen')
events_screen = EventsScreen('events screen')
settings_screen = SettingsScreen('settings screen')
clan_settings_screen = ClanSettingsScreen('clan settings screen')
start_screen = StartScreen('start screen')
switch_clan_screen = SwitchClanScreen('switch clan screen')
choose_mate_screen = ChooseMateScreen('choose mate screen')
choose_mentor_screen = ChooseMentorScreen('choose mentor screen')
choose_adoptive_parent_screen = ChooseAdoptiveParentScreen('choose adoptive parent screen')
relationship_screen = RelationshipScreen('relationship screen')
view_children_screen = FamilyTreeScreen('see kits screen')
mediation_screen = MediationScreen("mediation screen")

# LifeGen screens

talk_screen = TalkScreen('talk screen')
insult_screen = InsultScreen('insult screen')
flirt_screen = FlirtScreen('flirt screen')

achivement_screen = AchievementScreen('achievement screen')
murder_screen = MurderScreen("murder screen")
deputy_screen = DeputyScreen("deputy screen")
name_kits_screen = NameKitsScreen("name kits screen")
choose_reborn_screen = ChooseRebornScreen("choose reborn screen")
affair_screen = AffairScreen("affair screen")
queen_screen = QueenScreen("queen screen")

patrol_screen = PatrolScreen('patrol screen2')
patrol_screen2 = LifeGenPatrolScreen('patrol screen')
patrol_screen3 = DFPatrolScreen('patrol screen3')
patrol_screen4 = DatePatrolScreen('patrol screen4')

