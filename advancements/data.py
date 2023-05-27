import json, sys
d = {}
key = "minecraft:adventure/adventuring_time"
key2 = "criteria"
# will: 86d20ccc-3fb9-33c7-890d-4a3886ba7c7d
# kabir: ed6132c6-e71c-36c9-844b-51ccb9b506cf
# sanya: af3aa432-204e-32e0-977e-49180d302d9e
# tanisha: af902122-4fbd-39dd-9e63-78d8b5ee748c
# victor: 0fccb1b7-7d9a-3098-b232-c02da97f890d


uid_dict = {
     'will': '86d20ccc-3fb9-33c7-890d-4a3886ba7c7d',
 'kabir': 'ed6132c6-e71c-36c9-844b-51ccb9b506cf',
 'sanya': 'af3aa432-204e-32e0-977e-49180d302d9e',
 'tanisha': 'af902122-4fbd-39dd-9e63-78d8b5ee748c',
 'victor': '0fccb1b7-7d9a-3098-b232-c02da97f890d'
}
# with open("86d20ccc-3fb9-33c7-890d-4a3886ba7c7d.json", 'r') as f:
#     d = json.load(f)[key][key2]
# d2 = {}
# with open("ed6132c6-e71c-36c9-844b-51ccb9b506cf.json",'r') as f:
#     d2 = json.load(f)[key][key2]
# print(d['minecraft:adventure/adventuring_time'])
all_data = []
with open("all.json",'r') as f:
    all_data = set(json.load(f))
# s1 = set(list(map(lambda x: x.replace("minecraft:",""), d.keys())) )
# s2 = set(list(map(lambda x: x.replace("minecraft:",""), d2.keys())) )

exclusions = {'small_end_islands', 'crimson_forest', 'end_barrens', 'nether_wastes', 'end_midlands', 'warped_forest', 'end_highlands', 'the_end', 'basalt_deltas', 'soul_sand_valley', 'the_void'}

# s2 = set(d2.keys())
# print(all_data.difference(s1))
# print(list(map(lambda x: x.replace("minecraft:"), d.keys())))
# print(all_data)

# UID's

# print(sys.argv)
if '-p' in sys.argv:
    player = sys.argv[sys.argv.index('-p')+1]
    # print(inp)
    try:
        with open(f"{uid_dict[player]}.json",'r') as f:
            data = json.load(f)[key][key2]
            ex_all_data = all_data.difference(exclusions)
            processed = set(list(map(lambda x: x.replace("minecraft:",""), data.keys())))
            not_found = ex_all_data.difference(processed)
            # print(not_found)
            print("Stats for "+player)
            print(f"Total found {len(processed)}/{len(ex_all_data)}")
            print("Found: ")
            for i in processed:
                print(f"- {i}")
            print("Not found: ")
            for i in not_found:
                print(f"- {i}")
    except FileNotFoundError:
        print("Error in finding file...")
    
