def min_time_required(machines, goal):
    l, r = 1, max(machines)*goal

    def num_of_items_produced(day):
        items = 0
        for machine in machines:
            items += day // machine
        return items

    while l < r:
        m = (l+r)//2
        if num_of_items_produced(m) < goal:
            l = m+1
        else:
            r = m

    return l
