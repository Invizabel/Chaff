let math = require("math");
let storage = require("storage");
print("CREATING CHAFF");
let data = ""; for (let i = 0; i < 2048; i++) data += "0";
let file = storage.openFile("/ext/CHAFF", "w", "create_always");
while (true)
{
    file.write(data);
}
file.close();
print("REMOVING CHAFF");
storage.remove("/ext/CHAFF");
print("DONE!");
