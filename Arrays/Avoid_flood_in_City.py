from sortedcontainers import SortedList

def avoidFlood(rains):
    n = len(rains)
    next_rain = {}
    
    # Step 1: Preprocess next rains for each lake
    for day, lake in enumerate(rains):
        if lake > 0:
            if lake not in next_rain:
                next_rain[lake] = []
            next_rain[lake].append(day)
    
    ans = [-1] * n
    full = {}
    dry_days = SortedList()
    
    for day, lake in enumerate(rains):
        if lake > 0:
            # Pop the current rain day from next_rain
            next_rain[lake].pop(0)
            
            if lake in full:
                # Need to dry it before it rains again
                last_rain = full[lake]
                idx = dry_days.bisect_right(last_rain)
                
                if idx == len(dry_days):
                    return []  # no dry day available, flood occurs
                
                dry_day = dry_days[idx]
                ans[dry_day] = lake  # dry this lake
                dry_days.remove(dry_day)
            
            full[lake] = day  # mark lake as full
            ans[day] = -1
        else:
            dry_days.add(day)
            ans[day] = 1  # default, will adjust later if needed
            
    return ans
