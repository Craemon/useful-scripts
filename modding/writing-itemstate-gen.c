#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    // Array for placeholder entries
    const char *placeholders[] = {
        "green_chroma_block",
        "blue_chroma_block",
        "red_chroma_block",
        "black_chroma_block",
        "white_chroma_block",
        "yellow_chroma_block",
        "light_blue_chroma_block",
        "magenta_chroma_block",
        "replace_me_block",
        "green_chroma_lamp",
        "blue_chroma_lamp",
        "red_chroma_lamp",
        "black_chroma_lamp",
        "white_chroma_lamp",
        "yellow_chroma_lamp",
        "light_blue_chroma_lamp",
        "magenta_chroma_lamp",
        "replace_me_lamp"
    };
    // Number of placeholders
    size_t num_placeholders = sizeof(placeholders) / sizeof(placeholders[0]);

    // Generate JSON files for each placeholder
    for (size_t i = 0; i < num_placeholders; ++i) {
        // Construct the file name
        char file_name[64];
        snprintf(file_name, sizeof(file_name), "%s.json", placeholders[i]);

        // Open the file for writing
        FILE *file = fopen(file_name, "w");
        if (file == NULL) {
            perror("Error creating file");
            exit(EXIT_FAILURE);
        }

        // Write the JSON content
        fprintf(file, "{\n");
        fprintf(file, "  \"model\": {\n");
        fprintf(file, "    \"type\": \"minecraft:model\",\n");
        fprintf(file, "    \"model\": \"betterchromakey:item/%s\"\n", placeholders[i]);
        fprintf(file, "  }\n");
        fprintf(file, "}\n");

        // Close the file
        fclose(file);

        printf("Created file: %s\n", file_name);
    }

    printf("All JSON files created in the project directory.\n");
    return 0;
}
