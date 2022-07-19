days = int(input())
daily_plunder = int(input())
expected_plunder = int(input())
gathered_plunder = 0
for day in range(1,days+1):
    gathered_plunder += daily_plunder
    if day % 3 == 0:
        gathered_plunder += daily_plunder * 0.5
    if day % 5 == 0:
        gathered_plunder -= gathered_plunder * 0.3

if expected_plunder <= gathered_plunder:
    print(f"Ahoy! {gathered_plunder:.2f} plunder gained.")
else:
    print(f"Collected only {gathered_plunder/expected_plunder*100:.2f}% of the plunder.")