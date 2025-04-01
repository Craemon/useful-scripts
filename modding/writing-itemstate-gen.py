import os

# Array for placeholder entries
placeholders = [
    "green_chroma_block", "blue_chroma_block", "red_chroma_block", "black_chroma_block", "white_chroma_block", 
    "yellow_chroma_block", "light_blue_chroma_block", "magenta_chroma_block", "replace_me_block",
    "green_chroma_lamp", "blue_chroma_lamp", "red_chroma_lamp", "black_chroma_lamp", "white_chroma_lamp",
    "yellow_chroma_lamp", "light_blue_chroma_lamp", "magenta_chroma_lamp", "replace_me_lamp"
]

# Generate JSON files for each placeholder
for placeholder in placeholders:
    file_name = f"{placeholder}.json"
    
    json_content = {
        "model": {
            "type": "minecraft:model",
            "model": f"betterchromakey:item/{placeholder}"
        }
    }
    
    with open(file_name, "w") as file:
        import json
        json.dump(json_content, file, indent=2)
    
    print(f"Created file: {file_name}")

print("All JSON files created in the project directory.")

