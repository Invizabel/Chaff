#include <cmath>
#include <furi.h>
#include <storage/storage.h>

int main()
{
    Storage * storage = (Storage*)furi_record_open("storage");
    File * file = storage_file_alloc(storage);

    if (storage_file_exists(storage, "/ext/CHAFF"))
    {
        storage_common_remove(storage, "/ext/CHAFF");
    }

    uint8_t data[8192] = {0x00};

    uint64_t free, total;
    storage_common_fs_info(storage, "/ext/", &total, &free);
    uint64_t chunks = round(free / 8192);

    if(storage_file_open(file, "/ext/CHAFF", FSAM_WRITE, FSOM_OPEN_APPEND))
    {
        for (uint64_t i = 0; i < chunks; i++)
        {
            storage_file_write(file, &data, sizeof(data));
        }
    }
    
    storage_file_close(file);
    storage_file_free(file);

    if (storage_file_exists(storage, "/ext/CHAFF"))
    {
        storage_common_remove(storage, "/ext/CHAFF");
    }
    
    furi_record_close("storage");
    return 0;
}
