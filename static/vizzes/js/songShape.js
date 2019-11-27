function btoaUTF16 (sString) {

	var aUTF16CodeUnits = new Uint16Array(sString.length);
	Array.prototype.forEach.call(aUTF16CodeUnits, function (el, idx, arr) { arr[idx] = sString.charCodeAt(idx); });
	return btoa(String.fromCharCode.apply(null, new Uint8Array(aUTF16CodeUnits.buffer)));

}
function readFile(file)
{
    var rawFile = new XMLHttpRequest();
    rawFile.open("GET", file);
    rawFile.onreadystatechange = function ()
    {
        if(rawFile.readyState === 4)
        {
            if(rawFile.status === 200 || rawFile.status == 0)
            {
                var midiArray = MidiParser.parse(btoaUTF16(rawFile.responseText))
                console.log(midiArray);
            }
        }
    }
    rawFile.send(null);
}

readFile("/static/audio/Slayer_-_Expendable_youth.midi")
// how to encode as base64??????