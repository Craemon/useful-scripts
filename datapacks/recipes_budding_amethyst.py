import os
from itertools import permutations

output_dir = "recipes_budding_amethyst"
os.makedirs(output_dir, exist_ok=True)

key_block = '''"key": {
        "B": { "item": "minecraft:amethyst_block" },
        "C": { "item": "minecraft:small_amethyst_bud" },
        "D": { "item": "minecraft:medium_amethyst_bud" },
        "E": { "item": "minecraft:large_amethyst_bud" },
        "F": { "item": "minecraft:amethyst_cluster" }
    }'''

for i, (top, bottom, left, right) in enumerate(permutations("CDEF"), 1):
    pattern = f'''[
        " {top} ",
        "{left}B{right}",
        " {bottom} "
    ]'''

    content = f'''{{
    "type": "minecraft:crafting_shaped",
    "group": "budding_amethyst",
    "pattern": {pattern},
    {key_block},
    "result": {{
        "item": "minecraft:budding_amethyst",
        "count": 1
    }}
}}'''

    with open(f"{output_dir}/budding_amethyst_{i:02d}.json", "w") as f:
        f.write(content)

print(f"✅ Wrote 24 files to '{output_dir}'")
