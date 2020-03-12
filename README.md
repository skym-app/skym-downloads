# Floatation

### Connection Instructions

Connect your ios device to your mac with a usb cable
Open "Audio MIDI Setup" on your mac
click enable on your device
Open the Float app (if it was already open, you may have to restart the app to gain proper connectivity)

### Ableton Instructions

Right-click on your Ableton Live application and select “Show Package Contents”. 
Place the FloatationScript folder from the Ableton Folder in this package into Contents/App-Resources/MIDI Remote Scripts

Open the Preferences window
Select the MIDI tab
Select your "FloatationScript" in the Control Surface menu

Define your ios device "iPhone" or "iPad" as the input and output of "FloatationScript"

### Bitwig Instructions

Place the FloatationScript folder from the Bitwig Folder in this package into Bitwig Studio/Controller Scripts
Open Bitwig preferences / settings and go to the "Controllers" tab 
Select "+ add controller" at the bottom of the window
Choose "Connor" ad the hardware vendor and "Float" as the model
Choose your ios device as both the input and output (it will be called iphone or ipad)

### Soft Synth Instructions

Wether you are working in Ableton, Bitwig, or any other DAW. The synth control CC's can be midi learned to macros or parameters. This method has been tested with Massive and Serum, but should apply to any other soft synth. 

Right click on the macro or parameter you wish to map
Click on MIDI Learn
On the float app, in settings, tap the label of the synth CC you wish to map, this will send a singular message to learn to the parameter

Some synths allow you to save the midi mapping, so it is avalible in every instance of the synth.

To use the provided presets for Massive and Serum, map Synth X, Y, and Z to Macros 1, 2, and 3 respectively.