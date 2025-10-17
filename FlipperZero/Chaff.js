let math = require("math");
let storage = require("storage");
let free = storage.fsInfo("/ext")["freeSpace"];
print("CREATING CHAFF");
let data = ""; for (let i = 0; i < math.pow(2,8); i++) data += "0";
let file = storage.openFile("/ext/CHAFF", "w", "create_always");
for (let i = 0; i < math.floor(free / math.pow(2,8)); i += 1)
{
    file.write(data);
}
file.close();
print("REMOVING CHAFF");
storage.remove("/ext/CHAFF");
print("DONE!");
