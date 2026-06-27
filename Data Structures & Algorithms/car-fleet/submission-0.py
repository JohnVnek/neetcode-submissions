class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        speeds = {}
        fleets = []

        for idx, p in enumerate(position):
            speeds[p] = speed[idx]
        position.sort(reverse=True)

        for idx, p in enumerate(position):
            if idx == 0:
                fleets.append(p)
            else:
                last_fleet_speed = speeds[fleets[-1]]
                last_fleet_pos = fleets[-1]
                last_eta = (target - last_fleet_pos) / last_fleet_speed

                curr_fleet_speed = speeds[p]
                curr_fleet_pos = p
                curr_eta = (target - curr_fleet_pos) / curr_fleet_speed

                if (curr_eta > last_eta):
                    fleets.append(p)
        return len(fleets)



