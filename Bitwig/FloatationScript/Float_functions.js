

var parameters = {
    offset: 116, // ofset of first midi CC(of 8) from 0
    control: function(data1, data2)
    {
        if (data1 >= this.offset && data1 < this.offset + 7)
        {
            cursorDevice.getParameter(data1 - this.offset).set(data2,128);
        }
    },

    pageScroll: function(data1, data2)
    {
        // if midi CCs 17 or 18 are recieved, the page will scroll (FROM LOOP BLOCK)
        if(data1 == 17 && data2 != 0){
            cursorDevice.previousParameterPage();
        }else if(data1 == 18 && data2 != 0){
            cursorDevice.nextParameterPage();
        }
    },

    deviceScroll: function(data1, data2) 
    {
        if (data1 == 19 && data2 != 0)
        {
            cursorDevice.selectPrevious();
        }
        else if (data1 == 20 && data2 != 0)
        {
            cursorDevice.selectNext();
        }
    },

    update: function()
    {
        for (var p = 0; p<8; p ++)
        {
            cursorDevice.getParameter(p).setIndication(true)
            
        }
    },

}

function paramLED(index, value)
{
	sendMidi(176, index+4, value)					
}

