#Connor Golden, 2020

CHANNEL = 15

##RED BOX Control
# GRIDSIZE = [3,3] ##the red box grid size(does not have to be square)

# LAUNCH_BUTTONS =[[57,58,59],
# 				[54,55,56],
# 				[51,52,53]]
# 				##these are the midi note values that correspond to the scene launch
# 				#buttons withing the SessionGrid. You will need to add more values or
# 				#delete values coressponding to the size of the Grid you set.

# SCENE_BUTTONS = [72,73,74,75]

# ##NAV Controls, move the red box in live
# DOWN_BUTTON =28
# UP_BUTTON = 29
# LEFT_BUTTON =30
# RIGHT_BUTTON = 31


# ##MIXER Controls
# #The below mixer controls correspond to the RedBox in Live. Again, if you
# #change the grid size you will need to update these lists accordingly.


# MUTE_BUTTONS = [66,67,68]
# ARM_BUTTONS = [60,61,62]
# SOLO_BUTTONS = [63,64,65]

# MIX_FADERS = [12,13,14] ##these correspond to the CC message number for each fader
# PAN_CONTROLS = [16,17,18]
# MASTER_VOLUME = [15]
# PREHEAR = [19]


# TRACK_SELECTS = [69,70,71]
# TRACK_STOPS = [48,49,50]

##DEVICE Controls
#use these in combination with the track select buttons to quickly navigate to
#and control devices

NEXT_DEVICE = 77
PREVIOUS_DEVICE = 76

DEVICE_ON = 79
DEVICE_LOCK = 78 #Locks your macro controls to current device regardless of where
				 #you are in your session

#MACRO Controls
#these correspond to the knobs and Sliders you want to use to for the first 8
#controls in any ableton device (these also correspond to the 8 macro knobs in
#an instrument or effects rack)


MACRO_CONTROLS = [116,117,118]

#TRANSPORT Controls
#channels may be different from the channel you specify above

# PLAY_BUTTON = 118
# STOP_BUTTON = 117
# RECORD_BUTTON = 119
# SEEK_LEFT = 116
# SEEK_RIGHT = 115
