import opendota

client = opendota.OpenDota()

response = client.get_schema()

for x in response:
    print(f"{x}: {client.get_schema(x)} \n\n")

def competitive_data(id):
    data = client.get_player(id, 'competitive_rank')['mmr_estimate']
    print(data)

