
var fs = require('fs');

var file = fs.readFileSync('xml_parts.xml');

var in_sha1 = false;

for(var i = 0; i < file.length; ++ i)
{
    var b = file.readUInt8(i);

    if((b < 0x20 || b > 0x7E) && b != 0x0D && b != 0x0A && b != ' '.charCodeAt(0) && b != '\t'.charCodeAt(0)) {
        file.write('?', i);
    }
}

fs.writeFileSync('xml_parts_nohash.xml', file);




