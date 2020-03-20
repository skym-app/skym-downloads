// TODO: Clean up code

loadAPI(1);

host.defineController("Skym", "Skym", "1.0", "132aff60-dda8-11e9-aaef-0800200c9a66");

host.defineMidiPorts(1, 1);

load("Skym_functions.js")

var paramValues =  initArray(0, 8);
var currentDisplay = "n/a";

function init()
{
    // set MIDI callbacks/port
    host.getMidiInPort(0).setMidiCallback(onMidiPort1);

    //sends notes to Bitwig, with no input filters
    noteIn = host.getMidiInPort(0).createNoteInput("Notes", "?0????");
    noteIn.setShouldConsumeEvents(false);

    // creates a view on tp the selected device
    cursorDevice = host.createEditorCursorDevice(2);
    parameters.update();

}


function onMidiPort1(status, data1, data2)
{
    // IS MIDI DATA A CC?
    if (isChannelController(status))
    {
        if (status == 0xBF)
        {
 
            // parameters.pageScroll(data1, data2)
            // parameters.deviceScroll(data1, data2)
            //parameters.output();
            parameters.control(data1,data2)
    
        }
    }
}

function exit()
{
    println("exit.");
}